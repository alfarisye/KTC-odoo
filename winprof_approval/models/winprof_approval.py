# Copyright 2017-2020 Forgeflow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval

_logger = logging.getLogger(__name__)

class Winprof_approval(models.Model):
    _inherit = "approval.template"

    computation_method = fields.Selection(
        string="Computation Method",
        selection=[
            ("use_domain", "Domain"),
            ("use_python", "Python Code"),
        ],
        default="use_domain",
        required=True,
    )

class Winprof_approval_detail(models.Model):
    _inherit = "approval.template_detail"

    model = fields.Char(
        string="Related Document Model",
        index=True,
        related="template_id.model"
    )

    domain = fields.Char(
        string="Domain",
    )

    approver_selection_method = fields.Selection(
        string="Approval Method",
        selection=[
            ("use_user", "Users"),
            ("use_group", "Groups"),
            ("use_both", "Both specific user and group."),
            ("use_python", "Python Code"),
        ],
        default="use_user",
        required=True,
    )

class Winprof_purchase_request_release_strategy(models.Model):
    _name = 'approval.release.strategy'
    _order = "sequence asc"
    _description = 'Approval'

    name = fields.Char('Object Approval No')
    sequence = fields.Integer('Sequence')
    obj_id = fields.Integer('Obj Id')
    model_id = fields.Many2one(
        string="Referenced Model",
        comodel_name="ir.model",
        index=True,
        required=True,
        ondelete="cascade",
    )
    model = fields.Char(
        related="model_id.model",
        index=True,
        store=True,
    )
    user_id = fields.Many2one('res.users', 'User')
    state = fields.Selection(
        string="Status",
        selection=[
            ("draft", "Draft"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
    )
    note = fields.Char('Catatan')
    email_to = fields.Char('Email To')

    def get_show_button(self, model_id, obj_id, state):
        result = False
        obj = self.env[model_id].sudo().browse(obj_id)
        if obj:
            if self.env.context.get('uid', False):
                if self.env.context.get('uid', False) == obj.current_assigned_to.id and obj.state == state:
                    result = True

        return result

    def send_mail_to_approve(self, params):
        rel_strat_id = params['release_strategy_id']
        user_id_to_approve = params['user_id_to_approve']
        model_name = params['model_name']
        no_dokumen = params['no_dokumen']
        subject = '<No Reply> Approval ' + model_name + ' ' + no_dokumen
        email_to = ''
        employee_val = self.env['hr.employee'].sudo().search([('user_id', '=', user_id_to_approve)])
        if employee_val:
            email_to = employee_val[0].work_email if employee_val[0] else ""
        
        template = self.env.ref('winprof_approval.winprof_approval_email_template').with_context(
            email_to=email_to,
            model_name=model_name,
            subject=subject
        )
        template.sudo().send_mail(rel_strat_id, email_layout_xmlid='mail.mail_notification_light', force_send=True)

    def send_mail_full_approved(self, params):
        rel_strat_id = params['release_strategy_id']
        user_id_approve = self.env.user
        who_approve = ''
        employee_val = self.env['hr.employee'].sudo().search([('user_id', '=', user_id_approve.id)])
        if employee_val:
            who_approve = employee_val.name
        else:
            user_id = self.env['res.users'].sudo().browse(user_id_approve.id)
            if user_id.partner_id:
                who_approve = user_id.partner_id.name
            else:
                who_approve = user_id.login

        model_name = params['model_name']
        no_dokumen = params['no_dokumen']
        subject = '<No Reply> Full Approved ' + model_name + ' ' + no_dokumen
        email_to = ''
        rel_strat_obj = self.env["approval.release.strategy"]
        rel_strat_val = rel_strat_obj.sudo().browse(rel_strat_id)
        if rel_strat_val:
            domain = [("model_id","=",rel_strat_val.model_id.id),("obj_id","=",rel_strat_val.obj_id)]
            rel_strat_ids = rel_strat_obj.sudo().search(domain)
            for dtl in rel_strat_ids: 
                user_id_to_approve = dtl.user_id.id
                employee_val = self.env['hr.employee'].sudo().search([('user_id', '=', user_id_to_approve)])
                if employee_val:
                    email_to = (employee_val[0].work_email if employee_val[0] else "") + ',' + email_to 
        template = self.env.ref('winprof_approval.winprof_full_approved_email_template').with_context(
            email_to=email_to,
            model_name=model_name,
            subject=subject,
            who_approve=who_approve
        )
        template.sudo().send_mail(rel_strat_id, email_layout_xmlid='mail.mail_notification_light', force_send=True)

    def send_mail_rejected(self, params):
        rel_strat_id = params['release_strategy_id']
        user_id_reject = self.env.user
        who_reject = ''
        employee_val = self.env['hr.employee'].sudo().search([('user_id', '=', user_id_reject.id)])
        if employee_val:
            who_reject = employee_val.name
        else:
            user_id = self.env['res.users'].sudo().browse(user_id_reject.id)
            if user_id.partner_id:
                who_reject = user_id.partner_id.name
            else:
                who_reject = user_id.login

        model_name = params['model_name']
        no_dokumen = params['no_dokumen']
        subject = '<No Reply> Approval Rejected ' + model_name + ' ' + no_dokumen
        email_to = ''

        rel_strat_obj = self.env["approval.release.strategy"]
        rel_strat_val = rel_strat_obj.sudo().browse(rel_strat_id)
        if rel_strat_val:
            domain = [("model_id","=",rel_strat_val.model_id.id),("obj_id","=",rel_strat_val.obj_id)]
            rel_strat_ids = rel_strat_obj.sudo().search(domain)
            for dtl in rel_strat_ids:
                user_id_to_approve = dtl.user_id.id
                employee_val = self.env['hr.employee'].sudo().search([('user_id', '=', user_id_to_approve)])
                if employee_val:
                    email_to = (employee_val[0].work_email if employee_val[0] else "") + ',' + email_to 
            
            template = self.env.ref('winprof_approval.winprof_rejected_email_template').with_context(
                email_to=email_to,
                model_name=model_name,
                subject=subject,
                who_reject=who_reject
            )
            template.sudo().send_mail(rel_strat_id, email_layout_xmlid='mail.mail_notification_light', force_send=True)

    def generate_release_strategy(self, model_id, obj_id, function_to_approve, no_dokumen):
        domain_releases = [("model","=",model_id)]
        domain_model = [("model","=",model_id)]

        model_obj = self.env["ir.model"]
        model_ids = model_obj.sudo().search(domain_model)
        
        release_obj = self.env["approval.template"]
        releases = release_obj.search(domain_releases)
        
        request_obj = self.env[model_id]
        request_id = request_obj.sudo().browse(obj_id)

        # reset release strategy
        for rel in request_id.release_strategy_ids:
            rel.unlink()

        for rel in releases:
            obj = self.env[model_id]
            if rel.domain:
                dom = [("id", "=", obj_id)] + safe_eval(rel.domain, {})
            else:
                dom = [("id", "=", obj_id)]
            count_result = obj.search_count(dom)
            email_to = ''
            if count_result > 0:
                for rel_dtl in rel.detail_ids:
                    employee_val = self.env['hr.employee'].sudo().search([('user_id', '=', rel_dtl.approver_user_ids[0].id)])
                    if employee_val:
                        email_to = employee_val[0].work_email if employee_val[0] else ""
                        
                    values = {
                        "name" : no_dokumen,
                        "email_to" : email_to,
                        "sequence" : rel_dtl.sequence,
                        "obj_id" : obj_id,
                        "model_id" : model_ids[0].id,
                        "user_id" : rel_dtl.approver_user_ids[0].id,
                        "state" : "draft"
                    }
                    rel_strat_obj = self.env["approval.release.strategy"]
                    rel_strat = rel_strat_obj.sudo().create(values)
                    if rel_dtl.sequence == 1 :
                        request_id.current_assigned_to = rel_dtl.approver_user_ids[0].id

                        model_name = request_id._description
                        params = {
                            'user_id_to_approve' : rel_dtl.approver_user_ids[0].id,
                            'model_name' : model_name,
                            'release_strategy_id' : rel_strat.id,
                            'no_dokumen' : rel_strat.name 
                        }
                        self.send_mail_to_approve(params)
                        
                func = getattr(request_id, function_to_approve)
                res = func()

    def button_approve(self, model_id, obj_id, function_to_approve, function_approve):
        request_obj = self.env[model_id]
        request_id = request_obj.sudo().browse(obj_id)

        for rel in request_id.release_strategy_ids:
            if rel.user_id == self.env.user and request_id.current_assigned_to == self.env.user:
                rel.state = 'approved'
                body = self.env.user.name + " " + rel.state
                request_id.message_post(body=body)
                
                domain = [("model","=",model_id),("obj_id","=",request_id.id),("sequence","=", rel.sequence+1)]
                rel_strat_obj = self.env["approval.release.strategy"]
                rel_strat_ids = rel_strat_obj.sudo().search(domain)
                if rel_strat_ids:
                    rel_strat_id = rel_strat_ids[0]
                    request_id.current_assigned_to = rel_strat_id.user_id.id
                    
                    model_name = request_id._description
                    params = {
                        'user_id_to_approve' : rel_strat_id.user_id.id,  
                        'model_name' : model_name,
                        'release_strategy_id' : rel_strat_id.id,
                        'no_dokumen' : rel_strat_id.name 
                    }
                    self.send_mail_to_approve(params)

                    if rel.sequence == 1:
                        func = getattr(request_id, function_to_approve)
                        res = func()
                else:
                    func = getattr(request_id, function_approve)
                    res = func()
                    
                    domain = [("model","=",model_id),("obj_id","=",request_id.id)]
                    rel_strat_obj = self.env["approval.release.strategy"]
                    rel_strat_ids = rel_strat_obj.sudo().search(domain)
                    if rel_strat_ids:
                        rel_strat_id = rel_strat_ids[0]
                    
                    model_name = request_id._description
                    params = {
                        'model_name' : model_name,
                        'release_strategy_id' : rel_strat_id.id,
                        'no_dokumen' : rel_strat_id.name 
                    }
                    self.send_mail_full_approved(params)

    def button_reject(self, model_id, obj_id, function_reject):
        request_obj = self.env[model_id]
        request_id = request_obj.sudo().browse(obj_id)

        for rel in request_id.release_strategy_ids:
            if rel.user_id == self.env.user and request_id.current_assigned_to == self.env.user:
                rel.state = 'rejected'
                body = self.env.user.name + " " + rel.state
                request_id.message_post(body=body)
                
                domain = [("model","=",model_id),("obj_id","=",request_id.id),("sequence","=", 1)]
                rel_strat_obj = self.env["approval.release.strategy"]
                rel_strat_ids = rel_strat_obj.sudo().search(domain)
                if rel_strat_ids:
                    rel_strat_id = rel_strat_ids[0]
                    request_id.current_assigned_to = rel_strat_id.user_id.id
                    func = getattr(request_id, function_reject)
                    res = func()

                    model_name = request_id._description
                    params = {
                        'model_name' : model_name,
                        'release_strategy_id' : rel_strat_id.id,
                        'no_dokumen' : rel_strat_id.name 
                    }
                    self.send_mail_rejected(params)

    def button_draft(self, model_id, obj_id, function_draft):
        request_obj = self.env[model_id]
        request_id = request_obj.sudo().browse(obj_id)

        for rel in request_id.release_strategy_ids:
            rel.state = 'draft'

        domain = [("model","=",model_id),("obj_id","=",request_id.id),("sequence","=", 1)]
        rel_strat_obj = self.env["approval.release.strategy"]
        rel_strat_ids = rel_strat_obj.sudo().search(domain)
        if rel_strat_ids:
            rel_strat_id = rel_strat_ids[0]
            request_id.current_assigned_to = rel_strat_id.user_id.id
        func = getattr(request_id, function_draft)
        res = func()

    def button_to_approve(self, model_id, obj_id, function_to_approve):
        request_obj = self.env[model_id]
        request_id = request_obj.sudo().browse(obj_id)
        func = getattr(request_id, function_to_approve)
        res = func()