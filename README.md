Collective.ZodbBrowser is a web application to browse, inspect and introspect Zope's zodb objects. 

## Watch
<a href='http://www.youtube.com/watch?feature=player_embedded&v=GkOpdnC5zvs' target='_blank'><img src='http://img.youtube.com/vi/GkOpdnC5zvs/0.jpg' width='425' height=344 /></a>

## Features 

ZodbBrowser let's you browse the whole ZODB content tree and for every object you can get:

    * Its class and ancestors source code.

    * Its attributes values and callables source code

    * Its Interface class source code


## Try and use

collective.zodbbrowser requires:

 * Zope 2.12

 * Python 2.6

## On your buildout

If you already have a buildout for Zope2.13 or Plone4 running, edit buildout.cfg to add zope2.zodbbrowser to eggs and zcml sections at buildout and instance parts respectively.

```python
[buildout]
...
eggs = zope2.zodbbrowser
...
[instance]
...
zcml = zope2.zodbbrowser
```

Then run bin/buildout to make the changes effective. Start the instance and then, from a browser open http://yourinstance-url:port/zodbbrowser


## Development Buildout Install

```bash
$ svn co http://zodbbrowser.googlecode.com/svn/buildout/ zodbbrowser
$ python2.6 bootstrap.py
$ bin/buildout -v
$ bin/instance fg
``` 
Then open in your browser:
```
http://localhost:8080/zodbbrowser
```

## Changelog 

*0.2 experimental version*

    * Added ui.layout for better layout and resizable panels. Thanks to Quimera.
    * Updated jquery from 1.4.2 to 1.4.4.
    * Added Pretty printing format to show propertie's values. Thanks to Laurence Rowe and Emanuel Sartor.
    * Added support for older pythons 2.4 , 2.5. Thanks to Laurence Rowe.
    * Included module and file path for source code. Thanks to davidjb.
    * Added z3c.autoinclude.plugin support to remove the zcml entry on buildout. Thanks to aclark.

*0.1 experimental version*

    * Initial release includes: Class and Ancestors, Properties, Callables and Interfaces provided.
    * Support for Zope 2.13.x and Plone 4.0. Not tested with older or newer versions of Zope although it should work.
    * Support for Firefox 3.6 and Chrome 5.0. No support Internet Explorer yet.

## Special Thanks

 * Steve McMahon. This project is a result of taking his JavaScript/JQuery training.

 * All the people at menttes. Special thanks to 'The Sushi Guy' aka Quimera.

##Related Projects

 * [z3c.zodbbrowser uses gtk](http://svn.zope.org/z3c.zodbbrowser/trunk/)

 * [zodbbrowser uses Zope 3.4](https://launchpad.net/zodbbrowser)
