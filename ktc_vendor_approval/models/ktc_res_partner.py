from odoo import _, api, fields, models
import logging

_logger = logging.getLogger(__name__)

_STATES = [
    ("draft", "Draft"),
    ("to_approve", "To be approved"),
    ("rejected", "Rejected"),
    ("on_hold", "On Hold"),
    ("done", "Done"),
]

class KTCResPartnerInheritApproval(models.Model):
    _inherit = 'res.partner'

    state = fields.Selection(
        selection=_STATES,
        string="Status",
        index=True,
        tracking=True,
        required=True,
        copy=False,
        default="draft",
    )

    remark_vendor = fields.Selection([
        ('active', 'Active'),
        ('blocked', 'Blocked'),
    ], string='Remark Vendor',
        required=True,
        copy=False,
        default="active",)

    current_assigned_to = fields.Many2one(
        comodel_name="res.users",
        string="Approver",
        tracking=True,
        index=True,
    )
    release_strategy_ids = fields.One2many(
        'approval.release.strategy', 
        'obj_id', 
        string="Releas Strategy",
        domain=lambda self: [("model", "=", self._name)]
    )
    show_button_approve = fields.Boolean(compute='get_show_button', string='Show Button Approve')

    def get_show_button(self):
        self.show_button_approve = False
        if self.state == 'on_hold':
            self.show_button_approve = self.release_strategy_ids.get_show_button(self._name, self.id, 'on_hold')
        else:
            self.show_button_approve = self.release_strategy_ids.get_show_button(self._name, self.id, 'to_approve')

    def winprof_button_hold(self):
        return self.write({"state":"on_hold"})
    
    def set_approved(self):
        return self.write({"state":"done"})

    def button_to_approve(self):
        return self.write({"state": "to_approve"})
    
    def set_canceled(self):
        return self.write({"state": "cancel"})
    
    def set_draft(self):
        return self.write({"state": "draft"})

    def winprof_button_approve(self):
        self.release_strategy_ids.button_approve(self._name, self.id, 'button_to_approve', 'set_approved')
        return True

    def winprof_button_reject(self):
        self.release_strategy_ids.button_reject(self._name, self.id, 'set_canceled')
        return True

    def winprof_button_draft(self):
        self.release_strategy_ids.button_draft(self._name, self.id, 'set_draft')
        return True

    def winprof_button_to_approve(self):
        self.release_strategy_ids.generate_release_strategy(self._name, self.id, 'button_to_approve', self.name)
        return True


