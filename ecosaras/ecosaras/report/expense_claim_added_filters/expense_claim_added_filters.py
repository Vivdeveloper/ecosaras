import frappe
from frappe import _

def execute(filters=None):
    columns, data = [], []
    
    columns = [
        {"label": _("ID"), "fieldname": "name", "fieldtype": "Link", "options": "Expense Claim", "width": 100},
        {"label": _("From Employee"), "fieldname": "employee", "fieldtype": "Link", "options": "Employee", "width": 150},
        {"label": _("Employee Name"), "fieldname": "employee_name", "fieldtype": "Data", "width": 150},
        {"label": _("Company"), "fieldname": "company", "fieldtype": "Link", "options": "Company", "width": 150},
        {"label": _("Expense Date"), "fieldname": "expense_date", "fieldtype": "Date", "width": 120},
        {"label": _("Expense Type"), "fieldname": "expense_type", "fieldtype": "Data", "width": 150},
        {"label": _("Description"), "fieldname": "description", "fieldtype": "Data", "width": 250},
        {"label": _("Amount"), "fieldname": "amount", "fieldtype": "Currency", "width": 150},  
        {"label": _("Total Claimed Amount"), "fieldname": "total_claimed_amount", "fieldtype": "Currency", "width": 150},
        {"label": _("Total Sanctioned Amount"), "fieldname": "total_sanctioned_amount", "fieldtype": "Currency", "width": 150},
        {"label": _("Posting Date"), "fieldname": "posting_date", "fieldtype": "Date", "width": 120},
        {"label": _("Approval Status"), "fieldname": "approval_status", "fieldtype": "Data", "width": 120}
    ]

    conditions = ""
    if filters.get("from_date") and filters.get("to_date"):
        conditions += "AND ec.posting_date BETWEEN %(from_date)s AND %(to_date)s"
    if filters.get("from_employee"):
        conditions += " AND ec.employee = %(from_employee)s"
    if filters.get("employee_name"):
        conditions += " AND ec.employee_name LIKE %(employee_name)s"
    if filters.get("company"):
        conditions += " AND ec.company = %(company)s"
    if filters.get("approval_status"):
        conditions += " AND ec.approval_status = %(approval_status)s"

    data = frappe.db.sql(f"""
        SELECT
            ec.name, ec.employee, ec.employee_name, ec.company, 
            ecd.description, ecd.expense_type, ecd.expense_date, ecd.amount,
            ec.total_claimed_amount, ec.total_sanctioned_amount, ec.posting_date, ec.approval_status
        FROM
            `tabExpense Claim` ec
        LEFT JOIN
            `tabExpense Claim Detail` ecd ON ecd.parent = ec.name
        WHERE
            ec.docstatus < 2
            {conditions}
        ORDER BY
            ec.posting_date DESC
    """, filters, as_dict=1)


    total_claimed_amount = sum(row['total_claimed_amount'] for row in data)
    total_sanctioned_amount = sum(row['total_sanctioned_amount'] for row in data)
    total_amount= sum(row['amount'] for row in data)

    total_row = {
        "name": _("Total"),
        "total_claimed_amount": total_claimed_amount,
        "total_sanctioned_amount": total_sanctioned_amount,
        "amount": total_amount
    }
    data.append(total_row)

    return columns, data
