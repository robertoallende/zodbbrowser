from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
import json
import inspect 
from zope.interface import providedBy

try: 
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import HtmlFormatter
except:
    print 'no pygments'    


class Source(BrowserView):
    """
    """

    def get_source(self):
        try:
            code = inspect.getsource(self.context.__class__) 
            source = highlight(code, PythonLexer(), HtmlFormatter())
 
        except TypeError:
            source = '<pre>' + inspect.getsource(self.context.__class__) + '</pre>'
        except NameError:
            source = inspect.getsource(self.context.__class__)
        except:
            source = "Error"

        # XXX: if the are a monkey patch i wont know about it
        return source

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

        return source

    def get_class(self):
        """ 
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
            code = inspect.getsource(mysupclass ) 
            source = highlight(code, PythonLexer(), HtmlFormatter())
 
        except TypeError:
            source = '<pre>' + inspect.getsource( mysupclass) + '</pre>'
        except NameError:
            source = inspect.getsource(mysupclass)
        except:
            source = "" 

        # XXX: if the are a monkey patch i wont know about it
        return source
    
def get_ancestors(c, ancestors = {}):
     ancestors[c.__name__] = c
     for i in c.__bases__:
        get_ancestors(i, ancestors)
