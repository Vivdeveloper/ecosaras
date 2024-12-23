frappe.ui.form.on('Sales Order', {
    refresh: function (frm) {
        if (frm.doc.docstatus === 1) { // Ensure this condition is checked within a valid callback
            frm.add_custom_button(__('Maintenance Schedule'), function () {
                frappe.model.open_mapped_doc({
                    method: "ecosaras.override.maintenance_schedule.make_maintenance_schedule", 
                    frm: frm,
                });
            }, __("Create"));
        }
    }
});
