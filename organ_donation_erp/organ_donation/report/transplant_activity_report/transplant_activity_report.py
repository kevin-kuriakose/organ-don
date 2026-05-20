import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Hospital"), "fieldname": "transplant_hospital", "fieldtype": "Link", "options": "Hospital", "width": 180},
        {"label": _("Organ"), "fieldname": "organ_type", "fieldtype": "Data", "width": 120},
        {"label": _("Surgeries"), "fieldname": "count", "fieldtype": "Int", "width": 100},
        {"label": _("Successful"), "fieldname": "successful", "fieldtype": "Int", "width": 110},
        {"label": _("Surgeon"), "fieldname": "transplant_surgeon", "fieldtype": "Data", "width": 150},
    ]
    rows = frappe.db.sql("""
        SELECT ts.transplant_hospital, orec.organ_type, ts.transplant_surgeon,
            COUNT(*) as count,
            SUM(CASE WHEN ts.outcome = 'Successful' THEN 1 ELSE 0 END) as successful
        FROM `tabTransplant Surgery` ts
        LEFT JOIN `tabOrgan Record` orec ON orec.name = ts.organ_record
        WHERE ts.docstatus < 2
        GROUP BY ts.transplant_hospital, orec.organ_type, ts.transplant_surgeon
        ORDER BY count DESC
    """, as_dict=True)
    return columns, [{"transplant_hospital": r.transplant_hospital, "organ_type": r.organ_type,
                       "count": r.count, "successful": r.successful, "transplant_surgeon": r.transplant_surgeon} for r in rows]
