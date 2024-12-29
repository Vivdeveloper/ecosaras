import frappe
from frappe import _
from frappe import db

@frappe.whitelist()
def get_quality_inspection_counts(data):
    data["non_standard_fieldnames"]["Purchase Receipt"] = "quality_inspection"
    
    # Add connection for Quality Inspection in Purchase Order
    for transaction in data.get("transactions", []):
        if transaction.get("label") == _("Fulfillment"):
            transaction["items"].append("Quality Inspection")
            break
    else:
        data["transactions"].append({
            "label": _("Fulfillment"),
            "items": ["Quality Inspection"],
        })

    return data
