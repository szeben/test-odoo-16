# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class purchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    requisition_ids = fields.Many2many('sale.order', 'sale_id', string='Requisiciones')

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    sale_id = fields.Many2one('purchase.order')