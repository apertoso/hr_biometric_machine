{
    "name" : "Biometric Device Integration",
    "version" : "10.0.1.0.0",
    "author" : "Gaurav Sahu",
    "category" : "Custom",
    "website" : "gauravsahu.odoo.com",
    "description": "A Module for Biometric Device Integration",
    "depends" : ["base","hr"],
    "init_xml" : [],
    "data" : [
        "biometric_machine_view.xml",
        "report/daily_attendance_view.xml",
        "schedule.xml",
        "wizard/schedule_wizard.xml",
    ],
    "external_dependencies": {'python': ['zklib']},
    "active": False,
    "installable": True
}
