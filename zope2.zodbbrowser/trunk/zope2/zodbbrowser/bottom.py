from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
import inspect 
from zope.interface import providedBy
from pprint import pformat

try:
    import json
except ImportError:
    import simplejson as json

try: 
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import HtmlFormatter
except:
    print 'no pygments'    


class Source(BrowserView):
    """
    """
    
    def get_method(self):
        """ 
        """    
        myclass = self.context.__class__

        try: 
            mymethod_name = self.request['QUERY_STRING'].split('/')[0]
        except: 
            return ''

        try:
            code = inspect.getsource(getattr( myclass, mymethod_name))
            source = highlight(code, PythonLexer(), HtmlFormatter())
        except TypeError:
            source = '<pre>' + inspect.getsource(getattr( myclass, mymethod_name)) + '</pre>'
        except NameError:
            source = inspect.getsource(getattr( myclass, mymethod_name))
        except:
            source = "" 

        status = 'Reading ' + inspect.getsourcefile(myclass) 
        result = { 'status': status,  'bottom': source}
        return json.dumps(result, ensure_ascii= True, indent=4)

    def get_class(self):
        """ XXX: if the are a monkey patch i wont know about it
        """ 
        myclass = self.context.__class__
        ancestors = {}
        get_ancestors(myclass, ancestors)

        try: 
            mysupclass_name = self.request['QUERY_STRING'].split('/')[0]
        except: 
            return ''

        mysupclass = ancestors[mysupclass_name]
         
        try:
            code = '### Reading' + inspect.getsourcefile(mysupclass) 
            code = inspect.getsource(mysupclass ) 
            source = highlight(code, PythonLexer(), HtmlFormatter())
 
        except TypeError:
            source = '<pre>' + inspect.getsource( mysupclass) + '</pre>'
        except NameError:
            source = inspect.getsource(mysupclass)
        except:
            source = "" 

        status = 'Reading ' + inspect.getsourcefile(mysupclass) 
        result = { 'status': status,  'bottom': source}
        return json.dumps(result, ensure_ascii= True, indent=4)

    def get_interface(self):
        """ 
        """ 

        try: 
            myinterface_name = self.request['QUERY_STRING'].split('/')[0]
        except: 
            return ''

        interfacesdict = {}
        get_interfaces( tuple(providedBy(self.context))  , interfacesdict)

        myiclass = interfacesdict[myinterface_name]
         
        try:
            code = inspect.getsource(myiclass) 
            source = highlight(code, PythonLexer(), HtmlFormatter())
 
        except TypeError:
            source = '<pre>' + inspect.getsource(myiclass) + '</pre>'
        except NameError:
            source = inspect.getsource(myiclass)
        except:
            source = "" 

        status = 'Reading ' + inspect.getsourcefile(myiclass) 
        result = { 'status': status,  'bottom': source}
        return json.dumps(result, ensure_ascii= True, indent=4)
        

    def get_property(self):
        """ Return property type and current value
        """
        try:
            prop = getattr(self.context, self.request['QUERY_STRING'].split('/')[0])
            status = 'Type: ' + str(type(prop)).replace(">","").replace("<","")
            code = pformat(prop)
            source = highlight(code, PythonLexer(), HtmlFormatter())
        except TypeError:
            source = '<pre>' + str(prop) + '</pre>'
        except NameError:
            source = str(prop)
        except:
            source = "" 

        result = { 'status': status,  'bottom': source}
        return json.dumps(result, ensure_ascii= True, indent=4)


def get_interfaces(c, interfaces):
    for i in c:
        interfaces[i.__name__] = i
    
def get_ancestors(c, ancestors = {}):
     ancestors[c.__name__] = c
     for i in c.__bases__:
        get_ancestors(i, ancestors)

