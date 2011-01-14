from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from zope.interface import providedBy

try:
    import json
except ImportError:
    import simplejson as json

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

    def interfaces(self):
        """ return interfaces provided by current context 
        """
        myobj = self.context
        myinterfaces = tuple(providedBy(self.context))
        result = [ ]   

        for i in myinterfaces:
            result.append({"title": i.__name__ })

        return json.dumps( result , ensure_ascii= True, indent=4) 
 
    def interfaces_not_provided(self):
        """ 
        """
        
        
    def adapts(self):
        """ 
        """
        from zope.component import getGlobalSiteManager
        sm = getGlobalSiteManager()
        aa = [i for i in sm.registeredAdapters()]
        

    def class_ancestors(self):
        """
        """
        content_tree = build_class_tree(self.context.__class__)
        return json.dumps(content_tree, ensure_ascii= True, indent=4)

def build_class_tree(elem, level = 1024):        
    if level <= 0 or elem == object:
        return None
    level -= 1

    myclass = elem
    myclassbase = myclass.__bases__
    node = {}
    children = []

    for i in myclassbase:
        result = build_class_tree(i, level)
        if result:
            children.append(result)

    node["title"] = myclass.__name__
        
    if len(children):
        node["children"] = children
        node["key"] = myclass.__name__
        node["isFolder"] = True
        #node["isLazy"] = True

    return node 


