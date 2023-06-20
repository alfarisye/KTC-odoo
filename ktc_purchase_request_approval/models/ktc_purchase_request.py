from asyncore import write
import logging

from odoo import _, api, fields, models

_logger = logging.getLogger(__name__)

_STATES = [
    ("draft", "Draft"),
    ("to_approve", "To be approved"),
    ("approved", "Approved"),
    ("rejected", "Rejected"),
    ("on_hold", "On Hold"),
    ("done", "Done"),
]

class KTCPurchaseRequestInheritApproval(models.Model):
    _inherit = 'purchase.request'

    state = fields.Selection(
        selection=_STATES,
        string="Status",
        index=True,
        tracking=True,
        required=True,
        copy=False,
        default="draft",
    )

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

    @api.depends("state", "line_ids.product_qty", "line_ids.cancelled")
    def _compute_to_approve_allowed(self):
        for rec in self:
            rec.to_approve_allowed = any(
                not line.cancelled and line.product_qty for line in rec.line_ids
            )

    def get_show_button(self):
        self.show_button_approve = False
        if self.state == 'on_hold':
            self.show_button_approve = self.release_strategy_ids.get_show_button(self._name, self.id, 'on_hold')
        else:
            self.show_button_approve = self.release_strategy_ids.get_show_button(self._name, self.id, 'to_approve')

    def winprof_button_hold(self):
        return self.write({"state":"on_hold"})

    def winprof_button_approve(self):
        self.release_strategy_ids.button_approve(self._name, self.id, 'button_to_approve', 'button_approved')
        return True

    def winprof_button_reject(self):
        self.release_strategy_ids.button_reject(self._name, self.id, 'button_rejected')
        return True

    def winprof_button_draft(self):
        self.release_strategy_ids.button_draft(self._name, self.id, 'button_draft')
        return True

    def winprof_button_to_approve(self):
        self.release_strategy_ids.generate_release_strategy(self._name, self.id, 'button_to_approve', self.name)
        return True


