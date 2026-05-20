app_name = "organ_donation_erp"
app_title = "LifeEdge"
app_publisher = "Kevin K"
app_description = "Full-suite ERP for Organ Donation and Transplantation Organizations"
app_email = "kevinkbiju04@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "organ_donation_erp",
# 		"logo": "/assets/organ_donation_erp/logo.png",
# 		"title": "LifeEdge",
# 		"route": "/organ_donation_erp",
# 		"has_permission": "organ_donation_erp.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/organ_donation_erp/css/organ_donation_erp.css"
# app_include_js = "/assets/organ_donation_erp/js/organ_donation_erp.js"

# include js, css files in header of web template
# web_include_css = "/assets/organ_donation_erp/css/organ_donation_erp.css"
# web_include_js = "/assets/organ_donation_erp/js/organ_donation_erp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "organ_donation_erp/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "organ_donation_erp/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "organ_donation_erp.utils.jinja_methods",
# 	"filters": "organ_donation_erp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "organ_donation_erp.install.before_install"
# after_install = "organ_donation_erp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "organ_donation_erp.uninstall.before_uninstall"
# after_uninstall = "organ_donation_erp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "organ_donation_erp.utils.before_app_install"
# after_app_install = "organ_donation_erp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "organ_donation_erp.utils.before_app_uninstall"
# after_app_uninstall = "organ_donation_erp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "organ_donation_erp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"organ_donation_erp.tasks.all"
# 	],
# 	"daily": [
# 		"organ_donation_erp.tasks.daily"
# 	],
# 	"hourly": [
# 		"organ_donation_erp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"organ_donation_erp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"organ_donation_erp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "organ_donation_erp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "organ_donation_erp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "organ_donation_erp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["organ_donation_erp.utils.before_request"]
# after_request = ["organ_donation_erp.utils.after_request"]

# Job Events
# ----------
# before_job = ["organ_donation_erp.utils.before_job"]
# after_job = ["organ_donation_erp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"organ_donation_erp.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []


override_doctype_class = {
    "Hospital Transplant Facility": "organ_donation_erp.organ_donation.doctype.hospital_transplant_facility.hospital_transplant_facility.HospitalTransplantFacility",
    "Hospital": "organ_donation_erp.organ_donation.doctype.hospital.hospital.Hospital",
    "Transplant Center Organ Program": "organ_donation_erp.organ_donation.doctype.transplant_center_organ_program.transplant_center_organ_program.TransplantCenterOrganProgram",
    "Transplant Center": "organ_donation_erp.organ_donation.doctype.transplant_center.transplant_center.TransplantCenter",
    "Hospital Partnership": "organ_donation_erp.organ_donation.doctype.hospital_partnership.hospital_partnership.HospitalPartnership",
    "Coordinator Training": "organ_donation_erp.organ_donation.doctype.coordinator_training.coordinator_training.CoordinatorTraining",
    "Coordinator On Call": "organ_donation_erp.organ_donation.doctype.coordinator_on_call.coordinator_on_call.CoordinatorOnCall",
    "Transplant Coordinator": "organ_donation_erp.organ_donation.doctype.transplant_coordinator.transplant_coordinator.TransplantCoordinator",
    "Staff Training": "organ_donation_erp.organ_donation.doctype.staff_training.staff_training.StaffTraining",
    "IEC Material": "organ_donation_erp.organ_donation.doctype.iec_material.iec_material.IECMaterial",
    "Donor Pledge Organ": "organ_donation_erp.organ_donation.doctype.donor_pledge_organ.donor_pledge_organ.DonorPledgeOrgan",
    "Donor Pledge": "organ_donation_erp.organ_donation.doctype.donor_pledge.donor_pledge.DonorPledge",
    "Deceased Donor Certifying Doctor": "organ_donation_erp.organ_donation.doctype.deceased_donor_certifying_doctor.deceased_donor_certifying_doctor.DeceasedDonorCertifyingDoctor",
    "Deceased Donor Organ Consented": "organ_donation_erp.organ_donation.doctype.deceased_donor_organ_consented.deceased_donor_organ_consented.DeceasedDonorOrganConsented",
    "Deceased Donor": "organ_donation_erp.organ_donation.doctype.deceased_donor.deceased_donor.DeceasedDonor",
    "Living Donor Organ Offered": "organ_donation_erp.organ_donation.doctype.living_donor_organ_offered.living_donor_organ_offered.LivingDonorOrganOffered",
    "Living Donor": "organ_donation_erp.organ_donation.doctype.living_donor.living_donor.LivingDonor",
    "Donor Evaluation Lab Result": "organ_donation_erp.organ_donation.doctype.donor_evaluation_lab_result.donor_evaluation_lab_result.DonorEvaluationLabResult",
    "Donor Evaluation Imaging": "organ_donation_erp.organ_donation.doctype.donor_evaluation_imaging.donor_evaluation_imaging.DonorEvaluationImaging",
    "Donor Evaluation Serology": "organ_donation_erp.organ_donation.doctype.donor_evaluation_serology.donor_evaluation_serology.DonorEvaluationSerology",
    "Donor Evaluation": "organ_donation_erp.organ_donation.doctype.donor_evaluation.donor_evaluation.DonorEvaluation",
    "Brain Death Certificate Doctor": "organ_donation_erp.organ_donation.doctype.brain_death_certificate_doctor.brain_death_certificate_doctor.BrainDeathCertificateDoctor",
    "Brain Death Certificate": "organ_donation_erp.organ_donation.doctype.brain_death_certificate.brain_death_certificate.BrainDeathCertificate",
    "Family Consent Organ": "organ_donation_erp.organ_donation.doctype.family_consent_organ.family_consent_organ.FamilyConsentOrgan",
    "Family Consent Record": "organ_donation_erp.organ_donation.doctype.family_consent_record.family_consent_record.FamilyConsentRecord",
    "Recipient Comorbidity": "organ_donation_erp.organ_donation.doctype.recipient_comorbidity.recipient_comorbidity.RecipientComorbidity",
    "Recipient Previous Transplant": "organ_donation_erp.organ_donation.doctype.recipient_previous_transplant.recipient_previous_transplant.RecipientPreviousTransplant",
    "Recipient Current Medication": "organ_donation_erp.organ_donation.doctype.recipient_current_medication.recipient_current_medication.RecipientCurrentMedication",
    "Recipient Allergy": "organ_donation_erp.organ_donation.doctype.recipient_allergy.recipient_allergy.RecipientAllergy",
    "Recipient Hospitalization": "organ_donation_erp.organ_donation.doctype.recipient_hospitalization.recipient_hospitalization.RecipientHospitalization",
    "Recipient": "organ_donation_erp.organ_donation.doctype.recipient.recipient.Recipient",
    "Waitlist Entry": "organ_donation_erp.organ_donation.doctype.waitlist_entry.waitlist_entry.WaitlistEntry",
    "HLA Matching Record": "organ_donation_erp.organ_donation.doctype.hla_matching_record.hla_matching_record.HLAMatchingRecord",
    "Organ Offer": "organ_donation_erp.organ_donation.doctype.organ_offer.organ_offer.OrganOffer",
    "Recipient Medical History": "organ_donation_erp.organ_donation.doctype.recipient_medical_history.recipient_medical_history.RecipientMedicalHistory",
    "Retrieval Team Member": "organ_donation_erp.organ_donation.doctype.retrieval_team_member.retrieval_team_member.RetrievalTeamMember",
    "Organs Procured": "organ_donation_erp.organ_donation.doctype.organs_procured.organs_procured.OrgansProcured",
    "Procurement Case": "organ_donation_erp.organ_donation.doctype.procurement_case.procurement_case.ProcurementCase",
    "Organ Record": "organ_donation_erp.organ_donation.doctype.organ_record.organ_record.OrganRecord",
    "Allocation Priority List": "organ_donation_erp.organ_donation.doctype.allocation_priority_list.allocation_priority_list.AllocationPriorityList",
    "Allocation Order": "organ_donation_erp.organ_donation.doctype.allocation_order.allocation_order.AllocationOrder",
    "Transport Team Member": "organ_donation_erp.organ_donation.doctype.transport_team_member.transport_team_member.TransportTeamMember",
    "Transport Temperature Log": "organ_donation_erp.organ_donation.doctype.transport_temperature_log.transport_temperature_log.TransportTemperatureLog",
    "Transport Chain of Custody": "organ_donation_erp.organ_donation.doctype.transport_chain_of_custody.transport_chain_of_custody.TransportChainOfCustody",
    "Organ Transport": "organ_donation_erp.organ_donation.doctype.organ_transport.organ_transport.OrganTransport",
    "Green Corridor Request": "organ_donation_erp.organ_donation.doctype.green_corridor_request.green_corridor_request.GreenCorridorRequest",
    "Surgical Team Member": "organ_donation_erp.organ_donation.doctype.surgical_team_member.surgical_team_member.SurgicalTeamMember",
    "Intraoperative Complication": "organ_donation_erp.organ_donation.doctype.intraoperative_complication.intraoperative_complication.IntraoperativeComplication",
    "Transplant Surgery": "organ_donation_erp.organ_donation.doctype.transplant_surgery.transplant_surgery.TransplantSurgery",
    "Immunosuppression Regimen": "organ_donation_erp.organ_donation.doctype.immunosuppression_regimen.immunosuppression_regimen.ImmunosuppressionRegimen",
    "Followup Lab Result": "organ_donation_erp.organ_donation.doctype.followup_lab_result.followup_lab_result.FollowupLabResult",
    "Post Transplant Follow Up": "organ_donation_erp.organ_donation.doctype.post_transplant_follow_up.post_transplant_follow_up.PostTransplantFollowUp",
    "Graft Outcome": "organ_donation_erp.organ_donation.doctype.graft_outcome.graft_outcome.GraftOutcome",
    "Rejection Episode": "organ_donation_erp.organ_donation.doctype.rejection_episode.rejection_episode.RejectionEpisode",
    "Coordinator Case Activity": "organ_donation_erp.organ_donation.doctype.coordinator_case_activity.coordinator_case_activity.CoordinatorCaseActivity",
    "Coordinator Case Log": "organ_donation_erp.organ_donation.doctype.coordinator_case_log.coordinator_case_log.CoordinatorCaseLog",
    "On Call Schedule Entry": "organ_donation_erp.organ_donation.doctype.on_call_schedule_entry.on_call_schedule_entry.OnCallScheduleEntry",
    "On Call Schedule": "organ_donation_erp.organ_donation.doctype.on_call_schedule.on_call_schedule.OnCallSchedule",
    "Campaign Partner Org": "organ_donation_erp.organ_donation.doctype.campaign_partner_org.campaign_partner_org.CampaignPartnerOrg",
    "Awareness Campaign": "organ_donation_erp.organ_donation.doctype.awareness_campaign.awareness_campaign.AwarenessCampaign",
    "Pledge Drive Volunteer": "organ_donation_erp.organ_donation.doctype.pledge_drive_volunteer.pledge_drive_volunteer.PledgeDriveVolunteer",
    "Pledge Drive": "organ_donation_erp.organ_donation.doctype.pledge_drive.pledge_drive.PledgeDrive",
    "Event Speaker": "organ_donation_erp.organ_donation.doctype.event_speaker.event_speaker.EventSpeaker",
    "Public Awareness Event": "organ_donation_erp.organ_donation.doctype.public_awareness_event.public_awareness_event.PublicAwarenessEvent",
    "Referral": "organ_donation_erp.organ_donation.doctype.referral.referral.Referral",
    "THOTA Compliance Record": "organ_donation_erp.organ_donation.doctype.thota_compliance_record.thota_compliance_record.THOTAComplianceRecord",
    "Authorization Committee Member": "organ_donation_erp.organ_donation.doctype.authorization_committee_member.authorization_committee_member.AuthorizationCommitteeMember",
    "Authorization Committee Record": "organ_donation_erp.organ_donation.doctype.authorization_committee_record.authorization_committee_record.AuthorizationCommitteeRecord",
    "Medico Legal Case": "organ_donation_erp.organ_donation.doctype.medico_legal_case.medico_legal_case.MedicoLegalCase",
    "Audit Log": "organ_donation_erp.organ_donation.doctype.audit_log.audit_log.AuditLog",
    "NOTTO Report Data Summary": "organ_donation_erp.organ_donation.doctype.notto_report_data_summary.notto_report_data_summary.NottoReportDataSummary",
    "NOTTO Report": "organ_donation_erp.organ_donation.doctype.notto_report.notto_report.NOTTOReport",
    "Tissue Donor Type": "organ_donation_erp.organ_donation.doctype.tissue_donor_type.tissue_donor_type.TissueDonorType",
    "Tissue Donor": "organ_donation_erp.organ_donation.doctype.tissue_donor.tissue_donor.TissueDonor",
    "Tissue Issue": "organ_donation_erp.organ_donation.doctype.tissue_issue.tissue_issue.TissueIssue",
    "Tissue Storage Batch": "organ_donation_erp.organ_donation.doctype.tissue_storage_batch.tissue_storage_batch.TissueStorageBatch",
    "Tissue Storage": "organ_donation_erp.organ_donation.doctype.tissue_storage.tissue_storage.TissueStorage",
}

scheduled_tasks = {
    "cron": {
        "*/30 * * * *": [
            "organ_donation_erp.organ_donation.utils.alerts.check_time_critical_alerts"
        ]
    }
}
