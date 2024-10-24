// Copyright (c) 2024, Prathamesh Jadhav and contributors
// For license information, please see license.txt

frappe.query_reports["KRA"] = {
	"filters": [
		{
            'fieldname': 'kra',
            'label': 'KRA',
            'fieldtype': 'Link',
            'options':"KRA"
        },
		{
            'fieldname': 'from_date',
            'label': 'From Date',
            'fieldtype': 'Date',
            'reqd':0
        },
		{
            'fieldname': 'to_date',
            'label': 'To Date',
            'fieldtype': 'Date',
            'reqd':0
        },
		
	]
};
