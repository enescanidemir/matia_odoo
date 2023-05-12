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


class BsiMergeInventory(models.TransientModel):
    _name = "bsi.merge.inventory"
    _description = "Bsi Merge Inventory"

    contact = fields.Many2one("res.partner", string="Contact")
    operation_type = fields.Many2one(
        "stock.picking.type", string="Operation Type")
    scheduled_date = fields.Datetime(string="Scheduled Date")
    source_location = fields.Many2one(
        "stock.location", string="Source Location")
    destination_location = fields.Many2one(
        "stock.location", string="Destination Location")
    stock_move = fields.Many2many("stock.move", string="Stock")

    def merge_inventory(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['stock.picking'].browse(selected_ids)
            self.stock_move = selected_records.move_ids_without_package.ids

            move_line_vals = []
            for lines in self.stock_move:
                line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name, 'location_id': lines.location_id.id, 'location_dest_id': lines.location_dest_id.id,
                        'product_uom': lines.product_uom, 'product_uom_qty': lines.product_uom_qty, 'reserved_availability': lines.reserved_availability, 'quantity_done': lines.quantity_done})
                move_line_vals.append(line)
            inventory = {'partner_id': record.contact.id, 'location_id': record.source_location.id, 'location_dest_id': record.destination_location.id,
                         'picking_type_id': record.operation_type.id, 'scheduled_date': record.scheduled_date, 'move_ids_without_package': move_line_vals}
            inventory_ids = self.env['stock.picking'].create(inventory)

    def merge_andnew(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['stock.picking'].browse(selected_ids)
            if not self.stock_move:
                self.stock_move = selected_records.move_ids_without_package.ids
                move_line_vals = []
                for lines in self.stock_move:
                    line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name, 'location_id': lines.location_id.id, 'location_dest_id': lines.location_dest_id.id,
                            'product_uom': lines.product_uom, 'product_uom_qty': lines.product_uom_qty, 'reserved_availability': lines.reserved_availability, 'quantity_done': lines.quantity_done})
                    move_line_vals.append(line)
                inventory = {'partner_id': record.contact.id, 'location_id': record.source_location.id, 'location_dest_id': record.destination_location.id,
                             'picking_type_id': record.operation_type.id, 'scheduled_date': record.scheduled_date, 'move_ids_without_package': move_line_vals}
                inventory_ids = self.env['stock.picking'].create(inventory)

            else:
                move_line_vals = []
                for lines in self.stock_move:
                    line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name, 'location_id': lines.location_id.id, 'location_dest_id': lines.location_dest_id.id,
                            'product_uom': lines.product_uom, 'product_uom_qty': lines.product_uom_qty, 'reserved_availability': lines.reserved_availability, 'quantity_done': lines.quantity_done})
                    move_line_vals.append(line)
                inventory = {'partner_id': record.contact.id, 'location_id': record.source_location.id, 'location_dest_id': record.destination_location.id,
                             'picking_type_id': record.operation_type.id, 'scheduled_date': record.scheduled_date, 'move_ids_without_package': move_line_vals}
                inventory_ids = self.env['stock.picking'].create(inventory)

        return {
            'name': "Merge Inventory",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'bsi.merge.inventory',
            'target': 'new',
            'context': {
                    'default_stock_move': self.stock_move.ids,
            }
        }

    def merge_andview(self):
        for record in self:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['stock.picking'].browse(selected_ids)
            self.stock_move = selected_records.move_ids_without_package.ids

            move_line_vals = []
            for lines in self.stock_move:
                line = (0, 0, {'product_id': lines.product_id.id, 'name': lines.name, 'location_id': lines.location_id.id, 'location_dest_id': lines.location_dest_id.id,
                        'product_uom': lines.product_uom, 'product_uom_qty': lines.product_uom_qty, 'reserved_availability': lines.reserved_availability, 'quantity_done': lines.quantity_done})
                move_line_vals.append(line)
            inventory = {'partner_id': record.contact.id, 'location_id': record.source_location.id, 'location_dest_id': record.destination_location.id,
                         'picking_type_id': record.operation_type.id, 'scheduled_date': record.scheduled_date, 'move_ids_without_package': move_line_vals}
            inventory_ids = self.env['stock.picking'].create(inventory)
            ir_model_data = self.env['ir.model.data']
            view_id = ir_model_data._xmlid_lookup('stock.view_picking_form')[2]
            record_id = self.env['stock.picking'].search(
                [('partner_id', '=', record.contact.id)])

            return {
                'name': record_id.partner_id,
                'view_mode': 'form',
                'view_type': 'form',
                'views': [(view_id, 'form')],
                'view_id': view_id,
                'type': 'ir.actions.act_window',
                'res_model': 'stock.picking',
                'res_id': inventory_ids.id
            }
