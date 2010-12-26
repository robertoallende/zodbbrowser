from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
import json

error = "ERROR "

class Elements(BrowserView):
    """For every object we clasify its kind of properties.
    """

    def lista(self, is_call = 1):
        """ 1: callable, 2: not callable, 3: both
        """
        elems = dir(self.context)
        result = []
        for i in elems:
            try:
                elem = getattr(self.context, i)
                if callable(elem) and is_call == 1:
                    result.append({"title": i})
                if not callable(elem) and is_call == 2:
                    result.append({"title": i})
                if is_call == 3:
                    result.append({"title": i})
            except:
                result.append(error + i)

        return result

    def properties_and_callables(self):
        """ returns callables of the current context
        """
        return json.dumps( self.lista(3) , ensure_ascii= True, indent=4)

    def properties(self):
        """ returns properties of the current context 
        """
        return json.dumps( self.lista(2) , ensure_ascii= True, indent=4)

    def callables(self):
        """ returns callables of the current context
        """
        return json.dumps( self.lista(1) , ensure_ascii= True, indent=4)

    def interfaces_provided(self):
        """ 
        """

    def interfaces_not_provided(self):
        """ 
        """

    def adapts(self):
        """ 
        """
