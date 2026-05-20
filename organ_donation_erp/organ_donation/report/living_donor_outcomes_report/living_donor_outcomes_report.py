import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Donor"), "fieldname": "donor_name", "fieldtype": "Data", "width": 150},
        {"label": _("Organ"), "fieldname": "organ_type", "fieldtype": "Data", "width": 120},
        {"label": _("Surgery Date"), "fieldname": "surgery_date", "fieldtype": "Date", "width": 120},
        {"label": _("Medical Fitness"), "fieldname": "medical_fitness_status", "fieldtype": "Data", "width": 140},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 120},
    ]
    rows = frappe.db.sql("""
        SELECT ld.donor_name, ldo.organ_type, ld.surgery_date,
               ld.medical_fitness_status, ld.`status`
        FROM `tabLiving Donor` ld
        LEFT JOIN `tabLiving Donor Organ Offered` ldo ON ldo.parent = ld.name
        WHERE ld.docstatus < 2 AND ld.`status` = 'Completed'
        ORDER BY ld.surgery_date DESC
    """, as_dict=True)
    return columns, [{"donor_name": r.donor_name, "organ_type": r.organ_type,
                       "surgery_date": r.surgery_date, "medical_fitness_status": r.medical_fitness_status,
                       "status": r.status} for r in rows]
