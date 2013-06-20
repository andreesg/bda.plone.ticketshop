from zope.interface import implementer
from zope.component import adapter
from zope.annotation.interfaces import IAnnotations
from BTrees.OOBTree import OOBTree
from Acquisition import aq_parent
from bda.plone.cart.interfaces import ICartItemDataProvider
from .interfaces import (
    ITicket,
    ITicketOccurrence,
    ISharedStockData,
)


@implementer(ICartItemDataProvider)
@adapter(ITicketOccurrence)
def TicketOccurrenceCartItemDataProviderProxy(context):
    return ICartItemDataProvider(aq_parent(context))


SHARED_STOCK_DATA_KEY = 'bda.plone.ticketshop.shared_stock'


@implementer(ISharedStockData)
class SharedStockData(object):

    def __init__(self, context):
        self.context = context

    @property
    def shared_stock_context(self):
        raise NotImplementedError(u"Abstract ``SharedStockData`` does not "
                                  u"implement ``shared_stock_context``")

    @property
    def shared_stock_key(self):
        raise NotImplementedError(u"Abstract ``SharedStockData`` does not "
                                  u"implement ``shared_stock_key``")

    def stock_data(self):
        annotations = IAnnotations(self.shared_stock_context)
        data = annotations.get(SHARED_STOCK_DATA_KEY, None)
        if data is None:
            data = OOBTree()
            annotations[SHARED_STOCK_DATA_KEY] = data
        return data

    def get(self):
        return 10.0

    def set(self, value):
        pass


@adapter(ITicket)
class TicketSharedStock(SharedStockData):

    @property
    def shared_stock_context(self):
        return aq_parent(self.context)

    @property
    def shared_stock_key(self):
        return 'canonical_tickets'


@adapter(ITicketOccurrence)
class TicketOccurrenceSharedStock(SharedStockData):

    @property
    def shared_stock_context(self):
        return aq_parent(aq_parent(self.context))

    @property
    def shared_stock_key(self):
        context = self.context
        # XXX: end date as well? plone.app.event currently only
        #      uses start date
        return context.start_date_iso
