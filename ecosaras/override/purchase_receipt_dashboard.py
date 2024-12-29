from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate, nowtime, flt


def get_quality_inspection_counts(purchase_receipt_no, filters=None):
    if not filters:
        filters = {}

    filters.update({
        "reference_name": ["=", purchase_receipt_no],
        "docstatus": ["in", [0, 1, 2]]  # Draft, Submitted, Cancelled
    })

    return frappe.get_all('Quality Inspection', filters=filters, fields=['name'], as_list=True)
