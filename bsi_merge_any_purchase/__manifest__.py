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
{
    "name": "Combine/Merge any RFQ/Purchase Order",
    'author': 'Botspot Infoware Pvt. Ltd.',
    'category': 'Purchase',
    'company': 'Botspot Infoware Pvt. Ltd.',
    'maintainer': 'Botspot Infoware Pvt. Ltd.',
    "version": "15.0.1.0",
    'summary': """Select multiple RFQ/Purchase and create single RFQ/Purchase Orders. Create and open new RFQ/Purchase Orders.""",
    'website': 'https://www.botspotinfoware.com',
    "depends": ['base', 'purchase'],
    'description': """Select multiple RFQ/Purchase and create single RFQ/Purchase Orders. Create and open new RFQ/Purchase Orders.""",
    "data": [
        "security/ir.model.access.csv",
        "wizard/bsi_merge_purchase.xml",
    ],
    "images":  ['static/description/Banner.gif'],
    "qweb":  [],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
