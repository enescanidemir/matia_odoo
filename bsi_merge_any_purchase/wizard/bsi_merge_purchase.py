# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2023-today Botspot Infoware Pvt. Ltd. <www.botspotinfoware.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from odoo import api, fields, models, _
from datetime import date


class BsiMergePurchase(models.TransientModel):
    _name = "bsi.merge.purchase"
    _description = "Bsi Merge Purchase"

    customer = fields.Many2one("res.partner", string="Customer")
    purchase_date = fields.Date(string="Purchase Date")
    purchase_order_line = fields.Many2many(
        "purchase.order.line", string="Purchase")

    def merge_purchase(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['purchase.order'].browse(selected_ids)
            self.purchase_order_line = selected_records.order_line.ids

            move_line_vals = []
            for lines in self.purchase_order_line:
                line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                        'product_qty': lines.product_qty, 'price_unit': lines.price_unit})
                move_line_vals.append(line)
            purchase = {'partner_id': record.customer.id, 'date_planned': record.purchase_date,
                        'order_line': move_line_vals}
            purchase_ids = self.env['purchase.order'].create(purchase)

    def merge_andnew(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['purchase.order'].browse(selected_ids)
            if not self.purchase_order_line:
                self.purchase_order_line = selected_records.order_line.ids

                move_line_vals = []
                for lines in self.purchase_order_line:
                    line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                            'product_qty': lines.product_qty, 'price_unit': lines.price_unit})
                    move_line_vals.append(line)
                purchase = {'partner_id': record.customer.id, 'date_planned': record.purchase_date,
                            'order_line': move_line_vals}
                purchase_ids = self.env['purchase.order'].create(purchase)

            else:
                move_line_vals = []
                for lines in self.purchase_order_line:
                    line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                            'product_qty': lines.product_qty, 'price_unit': lines.price_unit})
                    move_line_vals.append(line)
                purchase = {'partner_id': record.customer.id, 'date_planned': record.purchase_date,
                            'order_line': move_line_vals}
                purchase_ids = self.env['purchase.order'].create(purchase)

        return {
            'name': "Merge Purchase",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'bsi.merge.purchase',
            'target': 'new',
            'context': {
                    'default_purchase_order_line': self.purchase_order_line.ids,
            }
        }

    def merge_andview(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['purchase.order'].browse(selected_ids)
            self.purchase_order_line = selected_records.order_line.ids

            move_line_vals = []
            for lines in self.purchase_order_line:
                line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name,
                        'product_qty': lines.product_qty, 'price_unit': lines.price_unit})
                move_line_vals.append(line)
            purchase = {'partner_id': record.customer.id, 'date_planned': record.purchase_date,
                        'order_line': move_line_vals}
            purchase_ids = self.env['purchase.order'].create(purchase)
            ir_model_data = self.env['ir.model.data']
            view_id = ir_model_data._xmlid_lookup(
                'purchase.purchase_order_form')[2]
            record_id = self.env['purchase.order'].search(
                [('partner_id', '=', record.customer.id)])

            return {
                'name': record_id.partner_id,
                'view_mode': 'form',
                'view_type': 'form',
                'views': [(view_id, 'form')],
                'view_id': view_id,
                'type': 'ir.actions.act_window',
                'res_model': 'purchase.order',
                'res_id': purchase_ids.id
            }
