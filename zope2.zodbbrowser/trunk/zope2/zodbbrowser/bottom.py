from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
import json
import inspect 


class Source(BrowserView):
    """
    """

    def get_source(self):
        try: 
            source = inspect.getsource(self.context)
        except TypeError:
            source = inspect.getsource(self.context.__class__)
        except:
            source = 'ERROR'

        # XXX: if the are a monkey patch i wont know about it
        return source
