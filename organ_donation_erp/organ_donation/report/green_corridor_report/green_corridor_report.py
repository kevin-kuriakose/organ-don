import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Origin"), "fieldname": "origin_city", "fieldtype": "Data", "width": 130},
        {"label": _("Destination"), "fieldname": "destination_city", "fieldtype": "Data", "width": 130},
        {"label": _("Count"), "fieldname": "count", "fieldtype": "Int", "width": 80},
        {"label": _("Avg Time Saved (min)"), "fieldname": "avg_time_saved", "fieldtype": "Float", "width": 170},
    ]
    rows = frappe.db.sql("""
        SELECT origin_city, destination_city,
            COUNT(*) as count, AVG(total_time_saved_minutes) as avg_time_saved
        FROM `tabGreen Corridor Request`
        WHERE docstatus < 2 AND `status` = 'Completed'
        GROUP BY origin_city, destination_city ORDER BY count DESC
    """, as_dict=True)
    return columns, [{"origin_city": r.origin_city, "destination_city": r.destination_city,
                       "count": r.count, "avg_time_saved": r.avg_time_saved} for r in rows]
