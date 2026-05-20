import frappe
from frappe.utils import now_datetime, add_to_date
from datetime import timedelta


def check_time_critical_alerts():
    """Runs every 30 minutes. Fires time-critical alerts that Frappe
    scheduler cannot handle (sub-24-hour windows)."""
    now = now_datetime()

    # 1. Organ viability expiring — 2 hours before cold_ischemia_end_time
    organs = frappe.db.sql("""
        SELECT name, organ_type, allocated_to_recipient, cold_ischemia_end_time
        FROM `tabOrgan Record`
        WHERE status NOT IN ('Transplanted','Discarded')
          AND cold_ischemia_end_time IS NOT NULL
          AND docstatus < 2
    """, as_dict=True)
    for o in organs:
        if o.cold_ischemia_end_time:
            time_left = (o.cold_ischemia_end_time - now).total_seconds() / 3600
            if 0 < time_left <= 2:
                _send_alert(
                    subject=f"URGENT: Organ {o.organ_type} viability expiring in {round(time_left, 1)} hrs",
                    message=f"""<p>Organ <b>{o.organ_type}</b> (Record: {o.name}) cold ischemia ends at
                        <b>{o.cold_ischemia_end_time}</b>.</p>
                        <p>Recipient: {o.allocated_to_recipient or 'Not allocated'}</p>
                        <p>Immediate action required.</p>"""
                )

    # 2. Organ offer expiring — 1 hour before offer_expiry_date
    offers = frappe.db.sql("""
        SELECT name, organ_type, offered_to_recipient, offer_expiry_date
        FROM `tabOrgan Offer`
        WHERE status = 'Open' AND offer_expiry_date IS NOT NULL AND docstatus < 2
    """, as_dict=True)
    for o in offers:
        if o.offer_expiry_date:
            time_left = (o.offer_expiry_date - now).total_seconds() / 3600
            if 0 < time_left <= 1:
                _send_alert(
                    subject=f"Organ offer expiring in 1 hour: {o.organ_type}",
                    message=f"""<p>Organ offer <b>{o.name}</b> for <b>{o.organ_type}</b> to
                        recipient <b>{o.offered_to_recipient}</b> expires at {o.offer_expiry_date}.</p>
                        <p>No response received. Please contact the transplant center immediately.</p>"""
                )

    # 3. Organ offer no response — 2 hours after offer_date
    no_response = frappe.db.sql("""
        SELECT name, organ_type, offered_to_recipient, offer_date
        FROM `tabOrgan Offer`
        WHERE status = 'Open' AND response IS NULL AND offer_date IS NOT NULL AND docstatus < 2
    """, as_dict=True)
    for o in no_response:
        if o.offer_date:
            hours_elapsed = (now - o.offer_date).total_seconds() / 3600
            if 2 <= hours_elapsed < 2.5:
                _send_alert(
                    subject=f"No response to organ offer after 2 hours: {o.organ_type}",
                    message=f"""<p>Organ offer <b>{o.name}</b> for <b>{o.organ_type}</b> has received
                        no response after 2 hours.</p>
                        <p>Offered to: {o.offered_to_recipient}</p>
                        <p>Consider escalating to next recipient on waitlist.</p>"""
                )

    # 4. Donor evaluation overdue — 4 hours after brain_death_declaration_date
    donors = frappe.db.sql("""
        SELECT dd.name, dd.donor_name, dd.hospital_admitted, dd.brain_death_declaration_date
        FROM `tabDeceased Donor` dd
        WHERE dd.status = 'Brain Death Declared'
          AND dd.brain_death_declaration_date IS NOT NULL
          AND dd.docstatus < 2
    """, as_dict=True)
    for d in donors:
        if d.brain_death_declaration_date:
            hours_elapsed = (now - d.brain_death_declaration_date).total_seconds() / 3600
            if 4 <= hours_elapsed < 4.5:
                _send_alert(
                    subject=f"Donor evaluation overdue: {d.donor_name}",
                    message=f"""<p>Donor <b>{d.donor_name}</b> was declared brain dead 4+ hours ago.</p>
                        <p>Hospital: {d.hospital_admitted}</p>
                        <p>Donor evaluation must be initiated immediately.</p>"""
                )

    # 5. Brain death second declaration overdue — 6 hours after first_declaration_date
    bdcs = frappe.db.sql("""
        SELECT name, deceased_donor, first_declaration_date, second_declaration_date
        FROM `tabBrain Death Certificate`
        WHERE status = 'Draft'
          AND first_declaration_date IS NOT NULL
          AND second_declaration_date IS NULL
          AND docstatus < 2
    """, as_dict=True)
    for bdc in bdcs:
        if bdc.first_declaration_date:
            hours_elapsed = (now - bdc.first_declaration_date).total_seconds() / 3600
            if 6 <= hours_elapsed < 6.5:
                _send_alert(
                    subject=f"Second brain death declaration overdue: {bdc.deceased_donor}",
                    message=f"""<p>Brain Death Certificate <b>{bdc.name}</b> for donor
                        <b>{bdc.deceased_donor}</b> — second declaration is overdue (6+ hours since first).</p>
                        <p>Please complete the second declaration immediately per THOTA guidelines.</p>"""
                )

    # 6. Transport departure overdue — past departure_date with status Planned
    transports = frappe.db.sql("""
        SELECT name, organ_record, origin_hospital, destination_hospital, departure_date
        FROM `tabOrgan Transport`
        WHERE status = 'Planned' AND departure_date IS NOT NULL AND docstatus < 2
    """, as_dict=True)
    for t in transports:
        if t.departure_date and t.departure_date < now:
            _send_alert(
                subject=f"Transport departure overdue: {t.organ_record}",
                message=f"""<p>Organ transport <b>{t.name}</b> for organ <b>{t.organ_record}</b> was
                    scheduled to depart from <b>{t.origin_hospital}</b> at {t.departure_date}.</p>
                    <p>Departure is overdue. Please check status immediately.</p>"""
            )


def _send_alert(subject, message):
    """Send alert to System Manager users."""
    users = frappe.db.get_all("Has Role", filters={"role": "System Manager", "parenttype": "User"},
                               fields=["parent"])
    for user in users:
        frappe.sendmail(
            recipients=[user.parent],
            subject=subject,
            message=message,
            now=True
        )
