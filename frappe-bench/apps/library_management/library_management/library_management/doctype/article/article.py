# # Copyright (c) 2024, sam and contributors
# # For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class Article(WebsiteGenerator):
	pass


# class Article(WebsiteGenerator):
#     def before_save(self):
#         if not self.route:
#             self.route = f"/articles/{self.title.replace(' ', '-')}"
