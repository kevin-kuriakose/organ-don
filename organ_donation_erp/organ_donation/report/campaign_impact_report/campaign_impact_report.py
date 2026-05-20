import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Campaign"), "fieldname": "campaign_name", "fieldtype": "Data", "width": 200},
        {"label": _("Type"), "fieldname": "type", "fieldtype": "Data", "width": 140},
        {"label": _("State"), "fieldname": "state", "fieldtype": "Data", "width": 120},
        {"label": _("Reach"), "fieldname": "actual_reach", "fieldtype": "Int", "width": 100},
        {"label": _("Pledges"), "fieldname": "pledges_generated", "fieldtype": "Int", "width": 100},
    ]
    rows = frappe.db.sql("""
        SELECT campaign_name, type, state, actual_reach, pledges_generated
        FROM `tabAwareness Campaign` WHERE docstatus < 2 ORDER BY pledges_generated DESC
    """, as_dict=True)
    return columns, [{"campaign_name": r.campaign_name, "type": r.type, "state": r.state,
                       "actual_reach": r.actual_reach, "pledges_generated": r.pledges_generated} for r in rows]
