import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Organ Type"), "fieldname": "organ_type", "fieldtype": "Data", "width": 130},
        {"label": _("Total Offers"), "fieldname": "total", "fieldtype": "Int", "width": 110},
        {"label": _("Accepted"), "fieldname": "accepted", "fieldtype": "Int", "width": 100},
        {"label": _("Declined"), "fieldname": "declined", "fieldtype": "Int", "width": 100},
        {"label": _("Acceptance Rate %"), "fieldname": "accept_rate", "fieldtype": "Percent", "width": 140},
    ]
    rows = frappe.db.sql("""
        SELECT organ_type, COUNT(*) as total,
            SUM(CASE WHEN response = 'Accepted' THEN 1 ELSE 0 END) as accepted,
            SUM(CASE WHEN response = 'Declined' THEN 1 ELSE 0 END) as declined
        FROM `tabOrgan Offer`
        WHERE docstatus < 2
        GROUP BY organ_type ORDER BY total DESC
    """, as_dict=True)
    result = []
    for r in rows:
        rate = (r.accepted / r.total * 100) if r.total else 0
        result.append({"organ_type": r.organ_type, "total": r.total, "accepted": r.accepted,
                        "declined": r.declined, "accept_rate": rate})
    return columns, result
