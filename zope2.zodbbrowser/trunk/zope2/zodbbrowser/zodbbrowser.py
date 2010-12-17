from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView

import json

class Tree(BrowserView):
    """Default view of a task 
    """
    __call__ = ViewPageTemplateFile('templates/tree.zpt')

    # XXX: This should be used as a zope3view
    #      It should show just 2 levels, not more.

    def context_tree(self):
        content_tree  =  [ build_tree(self.context) ] 
        return json.dumps(content_tree, ensure_ascii= True, indent=4)

"""Helpers methods"""
def build_tree(elem):
        lista = elem.listDAVObjects() #objectValues()
        node = {}

        node["data"] = get_id(elem)
        node["children"] = []

        for i in lista:
            node["children"].append(build_tree(i))

        return node 

def get_id(elem):
        if callable(elem.id):
            result = elem.id()
        else:
            result =  elem.id 

        if not result:
            result = "Root"

        return result
