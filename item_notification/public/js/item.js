frappe.ui.form.on("Item", {
    refresh: function(frm) {
        if (!frm.is_new()) {
            frm.add_custom_button(__('Send Email'), function() {
                frappe.call({
                    method: "item_notification.api.send_item_email",
                    args: {
                        item_code: frm.doc.name
                    },
                    callback: function(r) {
                        if (!r.exc) {
                            frappe.msgprint("Email sent successfully!");
                        }
                    }
                });
            }, ("Actions"));
        }
    }
});
