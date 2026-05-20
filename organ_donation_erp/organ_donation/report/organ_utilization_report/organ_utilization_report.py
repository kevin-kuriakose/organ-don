import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Organ Type"), "fieldname": "organ_type", "fieldtype": "Data", "width": 130},
        {"label": _("Procured"), "fieldname": "procured", "fieldtype": "Int", "width": 100},
        {"label": _("Transplanted"), "fieldname": "transplanted", "fieldtype": "Int", "width": 120},
        {"label": _("Discarded"), "fieldname": "discarded", "fieldtype": "Int", "width": 110},
        {"label": _("Utilization %"), "fieldname": "utilization_pct", "fieldtype": "Percent", "width": 120},
    ]
    rows = frappe.db.sql("""
        SELECT organ_type,
            COUNT(*) as procured,
            SUM(CASE WHEN outcome = 'Transplanted' THEN 1 ELSE 0 END) as transplanted,
            SUM(CASE WHEN outcome = 'Discarded' THEN 1 ELSE 0 END) as discarded
        FROM `tabOrgan Record`
        WHERE docstatus < 2
        GROUP BY organ_type ORDER BY procured DESC
    """, as_dict=True)
    result = []
    for r in rows:
        pct = (r.transplanted / r.procured * 100) if r.procured else 0
        result.append({"organ_type": r.organ_type, "procured": r.procured,
                        "transplanted": r.transplanted, "discarded": r.discarded, "utilization_pct": pct})
    return columns, result
