# Copyright 2017-2020 Forgeflow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Winprof Approval",
    "author": "Winprof",
    "version": "15.0.1.0.0",
    "website": "",
    "category": "LSBL",
    "depends": ["base", "mail", "ssi_multiple_approval_mixin"],
    "data": [
        "data/mail_template_data.xml",
        "security/ir.model.access.csv",
        "views/custom_approval_view.xml",
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": True,

}
