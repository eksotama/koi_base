# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from openerp.osv import fields, osv


class family_relationship_type(osv.osv):
    _name = 'base.family_relationship_type'
    _description = 'Family Relationship Type'

    def _default_active(self, cr, uid, context={}):
        return True

    _columns = {
        'name': fields.char(
            string='Family Relationship Type',
            size=126,
            required=True,
            ),
        'active': fields.boolean(
            string='Active',
            ),
        'description': fields.text(
            string='Description',
            ),
        }

    _defaults = {
        'active': _default_active,
        }

family_relationship_type()
