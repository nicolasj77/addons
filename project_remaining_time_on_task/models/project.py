# -*- coding: utf-8 -*-
from openerp import api, fields, models


class Task(models.Model):
    _inherit = 'project.task'

    has_contract_hours = fields.Boolean(string="Has contract hours",
                                        compute="_compute_has_contract_hours")

    remaining_contract_hours = fields.Float(
        string="Remaining Contract Hours",
        compute='_compute_remaining_hours_contract',
        digits=(16, 2))

    # @api.multi
    # def _get_qty_invoiced(self):
    #     self.ensure_one()
    #     sale_order = self.env['sale.order'].search(
    #         [('project_id', '=', self.analytic_account_id.id)])
    #     return sum(line.qty_invoiced for line in sale_order.order_line)

    @api.multi
    def _get_qty_effective(self):
        self.ensure_one()
        tasks = self.project_id.task_ids

        return sum([task.effective_hours for task in tasks])

    # @api.multi
    # @api.depends('remaining_hours')
    # def _compute_remaining_hours_contract(self):
    #     for task in self:
    #         sale_order = self.env['sale.order'].search(
    #         [('project_id', '=', self.analytic_account_id.id)])
    #         sale_order.qty_invoiced = sale_order._get_qty_invoiced()
    #         if sale_order.qty_invoiced > 0:
    #             for task in self:
    #                 task.remaining_contract_hours = sale_order.qty_invoiced \
    #                                                 - task._get_qty_effective()

    @api.multi
    @api.depends('remaining_hours')
    def _compute_remaining_hours_contract(self):
        self.ensure_one()
        sale_order = self.env['sale.order'].search(
            [('project_id', '=', self.analytic_account_id.id)])
        qty_invoiced = sum(line.qty_invoiced for line in sale_order.order_line)
        for task in self:
            task.remaining_contract_hours = qty_invoiced \
                                            - task._get_qty_effective()

    @api.multi
    @api.depends('has_contract_hours')
    def _compute_has_contract_hours(self):
        self.ensure_one()
        sale_order = self.env['sale.order'].search(
            [('project_id', '=', self.analytic_account_id.id)])
        qty_invoiced = sum(line.qty_invoiced for line in sale_order.order_line)
        self.has_contract_hours = qty_invoiced > 0
