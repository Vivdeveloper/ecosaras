frappe.ui.form.on('Purchase Receipt', {
    refresh: function(frm) {
        frm.add_custom_button(__('Quality Inspection'), function() {
            frappe.route_options = {
                reference_name: frm.doc.name,  // Pass doc.name as reference_name filter
                docstatus: ['in', [0, 1, 2]]  // Filter where docstatus can be Draft, Submitted, or Cancelled
            };
            frappe.set_route('List', 'Quality Inspection');  // Redirect to Quality Inspection list
        });
    }
});
