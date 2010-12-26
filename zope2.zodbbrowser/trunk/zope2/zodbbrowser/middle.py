from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
import json

class Kind(BrowserView):
    """For every object we clasify its kind of properties.
    """

    def list(self):
        content = []
        content.append({"title": "Properties and Callables"})
        content.append({"title": "Properties"})
        content.append({"title": "Callables"})
        content.append({"title": "Interfaces Provided"})
        content.append({"title": "Adapts"})
        return json.dumps(content, ensure_ascii= True, indent=4)
