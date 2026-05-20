import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Hospital"), "fieldname": "hospital_name", "fieldtype": "Data", "width": 200},
        {"label": _("Type"), "fieldname": "type", "fieldtype": "Data", "width": 140},
        {"label": _("State"), "fieldname": "state", "fieldtype": "Data", "width": 130},
        {"label": _("NOTTO Reg"), "fieldname": "notto_registration_number", "fieldtype": "Data", "width": 120},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 100},
    ]
    rows = frappe.db.sql("""
        SELECT hospital_name, type, state, notto_registration_number, `status`
        FROM `tabHospital` WHERE docstatus < 2 ORDER BY state, hospital_name
    """, as_dict=True)
    return columns, [{"hospital_name": r.hospital_name, "type": r.type, "state": r.state,
                       "notto_registration_number": r.notto_registration_number, "status": r.status} for r in rows]
