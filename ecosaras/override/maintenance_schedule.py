import frappe
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def make_maintenance_schedule(source_name, target_doc=None):
    def set_missing_values(source, target, source_parent=None):
        target.company = source.company
        target.customer = source.customer
    doc = get_mapped_doc(
        "Sales Order",  
        source_name,
        {
            "Sales Order": {  
                "doctype": "Maintenance Schedule", 
                "field_map": {
                    "name": "sales_order", 
                    "customer": "customer",
                    "company": "company",
                },
                "postprocess": set_missing_values,  
            },
        },
        target_doc,
    )

    return doc
