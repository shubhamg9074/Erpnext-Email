import frappe
from frappe.utils import get_url_to_form

@frappe.whitelist()
def send_item_email(item_code):
    # Fetch last 5 sales invoices for the item
    invoices = frappe.db.sql("""
        SELECT si.name, si.posting_date
        FROM `tabSales Invoice Item` sii
        INNER JOIN `tabSales Invoice` si ON sii.parent = si.name
        WHERE sii.item_code = %s
        ORDER BY si.creation DESC
        LIMIT 5
    """, (item_code,), as_dict=True)

    if not invoices:
        frappe.throw("No Sales Invoices found for this Item.")

    # Prepare context for Jinja template
    context = {
        "item_code": item_code,
        "invoices": invoices
    }

    # Render custom email template
    message = frappe.render_template("templates/emails/item_invoice_email.html", context)

    # Attach PDFs of invoices
    attachments = []
    for inv in invoices:
        pdf = frappe.get_print("Sales Invoice", inv.name, print_format="Standard", as_pdf=True)
        attachments.append({
            "fname": f"{inv.name}.pdf",
            "fcontent": pdf
        })

    # Send email
    frappe.sendmail(
        recipients=["laxmivermahv1998@gmail.com"],   # put your email here
        subject=f"Latest 5 Sales Invoices for Item {item_code}",
        message=message,
        attachments=attachments
    )

    return "Email sent successfully"
