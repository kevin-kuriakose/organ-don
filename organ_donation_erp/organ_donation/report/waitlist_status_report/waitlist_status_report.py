import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Organ Type"), "fieldname": "organ_type", "fieldtype": "Data", "width": 130},
        {"label": _("Urgency"), "fieldname": "urgency_category", "fieldtype": "Data", "width": 130},
        {"label": _("Count"), "fieldname": "count", "fieldtype": "Int", "width": 100},
        {"label": _("Blood Group"), "fieldname": "blood_group", "fieldtype": "Data", "width": 120},
    ]
    rows = frappe.db.sql("""
        SELECT we.organ_type, r.urgency_category, r.blood_group, COUNT(*) as count
        FROM `tabWaitlist Entry` we
        LEFT JOIN `tabRecipient` r ON r.name = we.recipient
        WHERE we.`status` = 'Active' AND we.docstatus < 2
        GROUP BY we.organ_type, r.urgency_category, r.blood_group
        ORDER BY we.organ_type, r.urgency_category
    """, as_dict=True)
    return columns, [{"organ_type": r.organ_type, "urgency_category": r.urgency_category,
                      "count": r.count, "blood_group": r.blood_group} for r in rows]
