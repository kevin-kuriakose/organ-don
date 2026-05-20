import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Organ"), "fieldname": "organ_type", "fieldtype": "Data", "width": 120},
        {"label": _("Total"), "fieldname": "total", "fieldtype": "Int", "width": 80},
        {"label": _("Alive 1M"), "fieldname": "alive_1m", "fieldtype": "Int", "width": 100},
        {"label": _("Alive 6M"), "fieldname": "alive_6m", "fieldtype": "Int", "width": 100},
        {"label": _("Alive 1Y"), "fieldname": "alive_1y", "fieldtype": "Int", "width": 100},
        {"label": _("Alive 5Y"), "fieldname": "alive_5y", "fieldtype": "Int", "width": 100},
    ]
    rows = frappe.db.sql("""
        SELECT orec.organ_type,
            COUNT(*) as total,
            SUM(CASE WHEN go.survival_1_month = 'Alive' THEN 1 ELSE 0 END) as alive_1m,
            SUM(CASE WHEN go.survival_6_months = 'Alive' THEN 1 ELSE 0 END) as alive_6m,
            SUM(CASE WHEN go.survival_1_year = 'Alive' THEN 1 ELSE 0 END) as alive_1y,
            SUM(CASE WHEN go.survival_5_years = 'Alive' THEN 1 ELSE 0 END) as alive_5y
        FROM `tabGraft Outcome` go
        LEFT JOIN `tabOrgan Record` orec ON orec.name = go.organ_record
        WHERE go.docstatus < 2
        GROUP BY orec.organ_type
    """, as_dict=True)
    return columns, [{"organ_type": r.organ_type, "total": r.total, "alive_1m": r.alive_1m,
                       "alive_6m": r.alive_6m, "alive_1y": r.alive_1y, "alive_5y": r.alive_5y} for r in rows]
