import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": _("Coordinator"), "fieldname": "coordinator", "fieldtype": "Link", "options": "Transplant Coordinator", "width": 180},
        {"label": _("Cases Handled"), "fieldname": "cases", "fieldtype": "Int", "width": 120},
        {"label": _("Total Hours"), "fieldname": "total_hours", "fieldtype": "Float", "width": 120},
        {"label": _("Avg Response (min)"), "fieldname": "avg_response", "fieldtype": "Float", "width": 160},
    ]
    rows = frappe.db.sql("""
        SELECT coordinator, COUNT(*) as cases, SUM(hours_spent) as total_hours
        FROM `tabCoordinator Case Log`
        WHERE docstatus < 2
        GROUP BY coordinator ORDER BY cases DESC
    """, as_dict=True)
    return columns, [{"coordinator": r.coordinator, "cases": r.cases,
                       "total_hours": flt(r.total_hours), "avg_response": 0} for r in rows]
