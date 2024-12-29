from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate, nowdate, nowtime, flt

@frappe.whitelist()
def get_quality_inspection_counts(purchase_receipt_no, filters=None):
   pass