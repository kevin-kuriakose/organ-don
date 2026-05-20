import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Hospital"), "fieldname": "hospital", "fieldtype": "Link", "options": "Hospital", "width": 180},
        {"label": _("Compliance Type"), "fieldname": "compliance_type", "fieldtype": "Data", "width": 160},
        {"label": _("Due Date"), "fieldname": "due_date", "fieldtype": "Date", "width": 110},
        {"label": _("Status"), "fieldname": "compliance_status", "fieldtype": "Data", "width": 120},
        {"label": _("Penalty"), "fieldname": "penalty_amount", "fieldtype": "Currency", "width": 110},
    ]
    rows = frappe.db.sql("""
        SELECT hospital, compliance_type, due_date, compliance_status, penalty_amount
        FROM `tabTHOTA Compliance Record`
        WHERE docstatus < 2 ORDER BY due_date ASC
    """, as_dict=True)
    return columns, [{"hospital": r.hospital, "compliance_type": r.compliance_type,
                       "due_date": r.due_date, "compliance_status": r.compliance_status,
                       "penalty_amount": r.penalty_amount} for r in rows]
