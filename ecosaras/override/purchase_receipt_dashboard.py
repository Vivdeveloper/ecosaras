from frappe import _

def get_quality_inspection_counts(data):
    data["non_standard_fieldnames"]["Purchase Receipt"] = "quality_inspection"
    
    # Add connection for Quality Inspection in Purchase Order
    for transaction in data.get("transactions", []):
        if transaction.get("label") == _("Reference"):
            transaction["items"].append({
                    "Quality Inspection": {
                        "filters": {
                            "reference_name": ["=", "purchase_receipt_no"],  # Add filter
                            "docstatus": ["in", [0, 1, 2]]  # Draft, Submitted, Cancelled
                        }
                    }
            })

    return data

