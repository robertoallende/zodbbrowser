from Products.Five.browser import BrowserView
from zope.viewlet.interfaces import IViewlet
from zope.interface import implements

class LeftbarViewlet(BrowserView):
    """ Base class with common functions for link viewlets.
    """
    implements(IViewlet)

    def __init__(self, context, request, view, manager):
        super(LeftbarViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.context = context
        self.request = request
        self.view = view
        self.manager = manager

    def list_objects(self):
        context = self.context
        return context.getChildNodes()

    def giveme_pdb(self):
        import pdb ; pdb.set_trace()

