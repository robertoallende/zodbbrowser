from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
try:
    import json
except ImportError:
    import simplejson as json


class Tree(BrowserView):
    """Contents tree
    """

    def context_tree(self):
        if self.context.__name__ == 'Zope' and self.context.__class__.__name__ == 'Application':
            content_tree  =  build_tree(self.context, 2) 
        else:
            content_tree  =  build_tree(self.context, 2, 1)
    
        if type(content_tree) == dict:
            content_tree  =  [ content_tree ] 
        return json.dumps(content_tree, ensure_ascii= True, indent=4)

"""Helpers methods"""
def build_tree(elem, level = 1024, remove_root = 0):
        """Levels represents how deep is the tree
        """
        if level <= 0:
            return None
        level -= 1

        lista = elem.objectValues()
        node = {}
        children = []

        for i in lista:
            result = (build_tree(i, level))
            if result:
                children.append(result)

        if remove_root:
            return children
        else:
            node["title"] = get_id(elem)
            node["children"] = []

            if len(lista):
                node["key"] = get_id(elem)
                node["isFolder"] = True

                if not len(node["children"]):
                    node["isLazy"] = True

            node["children"] = children

        return node 

def get_id(elem):
        if callable(elem.id):
            result = elem.id()
        else:
            result =  elem.id 

        if not result:
            result = "Application"

        return result
