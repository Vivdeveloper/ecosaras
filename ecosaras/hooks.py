from . import __version__ as app_version

app_name = "ecosaras"
app_title = "ecosaras"
app_publisher = "sushant"
app_description = "ecosaras"
app_email = "sushantmanjare33@gmail.com"
app_license = "MIT"



# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ecosaras/css/ecosaras.css"
# app_include_js = "/assets/ecosaras/js/ecosaras.js"

# include js, css files in header of web template
# web_include_css = "/assets/ecosaras/css/ecosaras.css"
# web_include_js = "/assets/ecosaras/js/ecosaras.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ecosaras/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ecosaras.utils.jinja_methods",
#	"filters": "ecosaras.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ecosaras.install.before_install"
# after_install = "ecosaras.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ecosaras.uninstall.before_uninstall"
# after_uninstall = "ecosaras.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ecosaras.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Production Plan": "ecosaras.override.production_plan.override_material"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ecosaras.tasks.all"
#	],
#	"daily": [
#		"ecosaras.tasks.daily"
#	],
#	"hourly": [
#		"ecosaras.tasks.hourly"
#	],
#	"weekly": [
#		"ecosaras.tasks.weekly"
#	],
#	"monthly": [
#		"ecosaras.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "ecosaras.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"erpnext.manufacturing.doctype.production_plan.production_plan.make_material_request": "ecosaras.override.make_material_request"
# }
#apps/erpnext/erpnext/manufacturing/doctype/production_plan/production_plan.py
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ecosaras.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ecosaras.utils.before_request"]
# after_request = ["ecosaras.utils.after_request"]

# Job Events
# ----------
# before_job = ["ecosaras.utils.before_job"]
# after_job = ["ecosaras.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ecosaras.auth.validate"
# ]
# doc_events = {
#     "*": {
#         "validate": "ecosaras.override.filter_print.validate_custom_default_print_format"
#     }
# }


override_doctype_dashboards = {
    "Sales Order": "ecosaras.override.maintenance_schedule_dashboard.get_dashboard_data"
}


doctype_js = {
    "Sales Order": "public/js/sales_order.js",
    "Purchase Receipt": "public/js/purchase_receipt.js"
    }


doc_events = {
    "Maintenance Schedule": {
        "on_submit": "ecosaras.override.maintenance_schedule.send_email_on_submission"
    }
}
