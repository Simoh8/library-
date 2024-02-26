// Copyright (c) 2024, simon muturi  and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Book', {
//     // Triggered before the form is saved
//     before_save: function(frm) {
//         // Your custom logic here
//         console.log("Save button pressed!");
//     }
// });
frappe.ui.form.on('Book', {
    // Triggered after the form is saved
    after_save: function(frm) {
        // Your custom logic here
        console.log("Form saved successfully!");
    }
});
