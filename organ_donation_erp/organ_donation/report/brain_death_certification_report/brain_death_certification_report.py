import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Hospital"), "fieldname": "hospital", "fieldtype": "Link", "options": "Hospital", "width": 180},
        {"label": _("Total BD Cases"), "fieldname": "total", "fieldtype": "Int", "width": 130},
        {"label": _("Consent Obtained"), "fieldname": "consented", "fieldtype": "Int", "width": 140},
        {"label": _("Consent Rate %"), "fieldname": "consent_rate", "fieldtype": "Percent", "width": 130},
    ]
    rows = frappe.db.sql("""
        SELECT bdc.hospital,
            COUNT(*) as total,
            SUM(CASE WHEN dd.next_of_kin_consent_obtained = 1 THEN 1 ELSE 0 END) as consented
        FROM `tabBrain Death Certificate` bdc
        LEFT JOIN `tabDeceased Donor` dd ON dd.name = bdc.deceased_donor
        WHERE bdc.docstatus < 2
        GROUP BY bdc.hospital ORDER BY total DESC
    """, as_dict=True)
    result = []
    for r in rows:
        rate = (r.consented / r.total * 100) if r.total else 0
        result.append({"hospital": r.hospital, "total": r.total, "consented": r.consented, "consent_rate": rate})
    return columns, result
