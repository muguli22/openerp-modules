from osv import fields, osv
from tools.translate import _
from openerp import netsvc

class stock_location(osv.osv):
    _name = "stock.location"
    _inherit = "stock.location"

    def name_get(self, cr, uid, ids, context=None):
        context = context or {}
        if(context.get('short_name', False)):
            return self._short_name(cr, uid, ids, context=context)
        return self._complete_name(cr, uid, ids, 'complete_name', None, context=context).items()

    def _short_name(self, cr, uid, ids, context=None):
        return [(location.id, location.name) for location in self.browse(cr, uid, ids, context=context)]
