# Copyright (c) 2024, Prathamesh Jadhav and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
          {"fieldname": "parent", "label": "Title", "fieldtype": "Link", "options": "KRA", "width": 100},
    {"fieldname": "week", "label": "Week", "fieldtype": "Date", "width": 150},
    {"fieldname": "particular", "label": "Particular", "fieldtype": "Data","width": 100},
    {"fieldname": "priority", "label": "Priority", "fieldtype": "Data", "width": 150},
    {"fieldname": "planned_target", "label": "Priority Target", "fieldtype": "Int", "width": 150},
    {"fieldname": "achieved_target", "label": "Achieved Target", "fieldtype": "Int", "width": 180},
    {"fieldname": "progress_in_percentage", "label": "Progress In Percentage", "fieldtype": "Int", "width": 180},
    {"fieldname": "recovery_action_plan", "label": "Recovery Action Plan", "fieldtype": "Data", "width": 150}
	]
	data = report_data(filters)
	return columns, data

def report_data(filters):
    kra = filters.get("kra")
    from_date = filters.get("from_date")
    to_date = filters.get("to_date")
    cond = []

    # Building condition for kra
    if kra:
        cond.append(f"parent = '{kra}'")
    
    # Building condition for from_date
    if from_date:
        cond.append(f"week >= '{from_date}'")
    
    # Building condition for to_date
    if to_date:
        cond.append(f"week <= '{to_date}'")

    # Combine all conditions with 'AND' and ensure there's always a valid condition
    cond = " AND ".join(cond) if cond else "1=1"

    # Query with dynamic conditions
    report_qry_data = frappe.db.sql(f"""
        SELECT parent, week, particular, priority, planned_target, 
               achieved_target, progress_in_percentage, recovery_action_plan
        FROM `tabKPI`
        WHERE {cond}
    """, as_dict=True)
    
    return report_qry_data