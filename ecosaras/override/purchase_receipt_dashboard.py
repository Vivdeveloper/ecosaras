from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate, nowtime, flt

@frappe.whitelist()
def get_quality_inspection_counts(filters=None):
    filters = frappe.parse_json(filters) if filters else {}
    purchase_receipt_no = filters.get('purchase_receipt_no')
    docstatus = filters.get('docstatus', [0, 1, 2])  # Default to [0, 1, 2] if not provided
    
    count = frappe.db.count('Quality Inspection', {
        'reference_name': purchase_receipt_no,
        'docstatus': ['in', docstatus]  # Apply the filters
    })
    
    return count
