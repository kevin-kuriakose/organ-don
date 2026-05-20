import frappe
from frappe import _
from frappe.utils import flt

def execute(filters=None):
    columns = [
        {"label": _("Type"), "fieldname": "donor_type", "fieldtype": "Data", "width": 130},
        {"label": _("Count"), "fieldname": "count", "fieldtype": "Int", "width": 100},
        {"label": _("Blood Group"), "fieldname": "blood_group", "fieldtype": "Data", "width": 120},
        {"label": _("State"), "fieldname": "state", "fieldtype": "Data", "width": 130},
    ]
    pledges = frappe.db.sql("SELECT blood_group, COUNT(*) as cnt FROM `tabDonor Pledge` WHERE docstatus < 2 GROUP BY blood_group", as_dict=True)
    deceased = frappe.db.sql("SELECT COUNT(*) as cnt FROM `tabDeceased Donor` WHERE docstatus < 2", as_dict=True)
    living = frappe.db.sql("SELECT COUNT(*) as cnt FROM `tabLiving Donor` WHERE docstatus < 2", as_dict=True)
    data = [{"donor_type": "Total Pledges", "count": sum(r.cnt for r in pledges), "blood_group": "", "state": ""}]
    data.append({"donor_type": "Deceased Donors", "count": deceased[0].cnt if deceased else 0, "blood_group": "", "state": ""})
    data.append({"donor_type": "Living Donors", "count": living[0].cnt if living else 0, "blood_group": "", "state": ""})
    for r in pledges:
        data.append({"donor_type": "Pledge by Blood Group", "count": r.cnt, "blood_group": r.blood_group, "state": ""})
    return columns, data
