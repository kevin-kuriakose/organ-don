import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Report Type"), "fieldname": "report_type", "fieldtype": "Data", "width": 180},
        {"label": _("Period"), "fieldname": "report_period", "fieldtype": "Data", "width": 120},
        {"label": _("Submitted Date"), "fieldname": "submitted_date", "fieldtype": "Date", "width": 130},
        {"label": _("Reference"), "fieldname": "submission_reference", "fieldtype": "Data", "width": 150},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 110},
    ]
    rows = frappe.db.sql("""
        SELECT report_type, report_period, submitted_date, submission_reference, `status`
        FROM `tabNOTTO Report` WHERE docstatus < 2 ORDER BY submitted_date DESC
    """, as_dict=True)
    return columns, [{"report_type": r.report_type, "report_period": r.report_period,
                       "submitted_date": r.submitted_date, "submission_reference": r.submission_reference,
                       "status": r.status} for r in rows]
