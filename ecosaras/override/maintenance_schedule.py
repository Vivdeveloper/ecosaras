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


    # File: apps/nirjay_customization/nirjay_customization/override/maintenance_schedule.py
@frappe.whitelist()
def send_email_on_submission(doc, method):
    # Iterate through the items in the child table to fetch the sales person
    for item in doc.items:
        if item.sales_person:
            # Get the Sales Person linked to the Maintenance Schedule Item
            sales_person = frappe.get_doc("Sales Person", item.sales_person)
            
            # Fetch the employee linked to the Sales Person
            employee = frappe.get_doc("Employee", sales_person.employee)
            
            # Get the email from the employee's user_id
            email = frappe.db.get_value("User", {"name": employee.user_id}, "email")
            
            if email:
                # Compose the email content
                email_subject = "Task Assigned: Maintenance Schedule"
                email_content = f"""
                    Hi Team,
                    <br><br>
                    I hope this message finds you well. I wanted to inform you that the task has been allocated to you. Kindly review the details and proceed with the activity as outlined.
                    <br>
                    <a href="{frappe.utils.get_url_to_form('Maintenance Schedule', doc.name)}">Click here to view the task</a>
                    <br>
                    Thanks,
                    <br><br>
                    {doc.modified_by}
                """
                
                # Send the email
                frappe.sendmail(
                    recipients=[email],
                    subject=email_subject,
                    message=email_content,
                    now=True  
                )
