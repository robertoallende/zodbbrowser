import transaction
from Products.Five import BrowserView

class DoomedBrowserView(BrowserView):
    """ A browser view that calls transaction.doom() when it is initialized.
    
    This is useful for browser views that shouldn't be able to commit a transaction
    to the database no matter what.
    """
    
    def __init__(self, context, request):
        transaction.doom()
        super(DoomedBrowserView, self).__init__(context, request)
