// Copyright (c) 2024, sushant and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Expense claim added filters"] = {
	"filters": [
		{
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_start(),
            "reqd": 1
        },
        {
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.month_end(),
            "reqd": 1
        },
        {
            "fieldname": "from_employee",
            "label": __("From Employee"),
            "fieldtype": "Link",
            "options": "Employee"
        },
        {
            "fieldname": "employee_name",
            "label": __("Employee Name"),
            "fieldtype": "Data"
        },
        {
            "fieldname": "company",
            "label": __("Company"),
            "fieldtype": "Link",
            "options": "Company",
            "default": frappe.defaults.get_user_default("Company"),
            "reqd": 1
        },
        {
            "fieldname": "approval_status",
            "label": __("Status"),
            "fieldtype": "Select",
            "default": "Approved",
			"options": [
                { "label": __("All"), "value": "" }, 
				{ "label": __("Draft"), "value": "Draft" }, 
				{ "label": __("Approved"), "value": "Approved" },
				{ "label": __("Rejected"), "value": "Rejected" }
            ]   
        }

	]
};
