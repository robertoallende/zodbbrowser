from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView

import json

class Tree(BrowserView):
    """Contents tree
    """

    def context_tree(self):
        content_tree  =  [ build_tree(self.context ) ] 
        return json.dumps(content_tree, ensure_ascii= True, indent=4)

"""Helpers methods"""
def build_tree(elem, level = 1024):
        """Levels represents how deep is the tree
        """
        if level <= 0:
            return None
        level -= 1

        lista = elem.objectValues()
        node = {}

        node["title"] = get_id(elem)
        node["children"] = []

        if len(lista):
            node["key"] = get_id(elem)
            node["isFolder"] = True

        for i in lista:
            result = (build_tree(i, level))
            if result:
                node["children"].append(result)

        return node 

def get_id(elem):
        if callable(elem.id):
            result = elem.id()
        else:
            result =  elem.id 

        if not result:
            result = "Root"

        return result
