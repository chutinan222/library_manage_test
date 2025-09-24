# Copyright (c) 2025, fdg and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class person(Document):
    def before_save(salf):
        frappe.msgprint("Hello")
        doc = frappe.get_doc({
            "doctype": "Item",
            "item_code": "NEW-ITEM-002",
            "item_group": "Products",   # Replace with your item group
            "item_name": "Sample Item",
            "stock_uom": "Nos"          # Replace with your UoM
            # Add more fields as needed
        })

        doc.save(ignore_permissions=True)
