import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": _("Organ Type"), "fieldname": "organ_type", "fieldtype": "Data", "width": 130},
        {"label": _("Avg Cold Ischemia (hrs)"), "fieldname": "avg_cia", "fieldtype": "Float", "width": 180},
        {"label": _("Max Cold Ischemia (hrs)"), "fieldname": "max_cia", "fieldtype": "Float", "width": 180},
        {"label": _("Count"), "fieldname": "count", "fieldtype": "Int", "width": 80},
    ]
    rows = frappe.db.sql("""
        SELECT organ_type,
            AVG(total_cold_ischemia_time) as avg_cia,
            MAX(total_cold_ischemia_time) as max_cia,
            COUNT(*) as count
        FROM `tabOrgan Record`
        WHERE total_cold_ischemia_time > 0 AND docstatus < 2
        GROUP BY organ_type ORDER BY avg_cia DESC
    """, as_dict=True)
    return columns, [{"organ_type": r.organ_type, "avg_cia": flt(r.avg_cia, 2),
                       "max_cia": flt(r.max_cia, 2), "count": r.count} for r in rows]
