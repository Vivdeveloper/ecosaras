frappe.ui.form.on('Purchase Receipt', {
    refresh: function(frm) {
        frm.add_custom_button(__('Quality Inspection'), function() {
            frappe.route_options = {
                reference_name: frm.doc.name,  
                docstatus: ['in', [0, 1, 2]]  
            };
            frappe.set_route('List', 'Quality Inspection');  
        });
    }
});
