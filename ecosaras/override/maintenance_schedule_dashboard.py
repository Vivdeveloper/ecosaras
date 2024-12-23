from frappe import _
#connection Shipment in sales order
def get_dashboard_data(data):
    data["non_standard_fieldnames"]["Sales Order"] = "maintenance_schedule"
    
   
    for transaction in data.get("transactions", []):
        if transaction.get("label") == _("Fulfillment"):
            transaction["items"].append("Maintenance Schedule")
            break
    else:
        data["transactions"].append({
            "label": _("Fulfillment"),
            "items": ["Maintenance Schedule"],
        })
    
    return data