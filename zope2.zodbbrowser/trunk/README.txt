============
        Introduction
        ============

        Zope2.ZodbBrowser is a web application to browse, inspect and introspect Zope's zodb objects. It is inspired on smalltalk's class browser and zodbbrowsers for zope3. 

        There is a demo video available at `YouTube's menttes channel
        <http://www.youtube.com/watch?v=GkOpdnC5zvs/>`_. 

        ====================================
        Using ZodbBrowser with your buildout
        ====================================

        If you already have a buildout for Zope2.13 or Plone4 running, edit 
        buildout.cfg to add zope2.zodbbrowser to eggs and zcml sections at buildout
        and instance parts respectively. 

        ::

          [buildout]
          ...
          eggs = zope2.zodbbrowser
          ...
          [instance]
          ...
          zcml = zope2.zodbbrowser

        Then run bin/buildout to make the changes effective.



        ================
        Buildout Install
        ================

        ::

          $ svn co http://zodbbrowser.googlecode.com/svn/buildout/ zodbbrowser
          $ python2.6 bootstrap.py
          $ bin/buildout -v
          $ bin/instance fg

        ==================
        Use of zodbbrowser
        ==================

        To access zodbbrowser add /zodbbrowser in your zope instance url, for example:
        http://localhost:8080/zodbbrowser

        =========
        Changelog
        =========


        0.2 experimental version 
        ------------------------

        - Added ui.layout for better layout and resizable panels. Thanks to Quimera.
        - Updated jquery from 1.4.2 to 1.4.4. 
        - Added Pretty printing format to show propertie's values. Thanks to Laurence Rowe and Emanuel Sartor. 
        - Added support for older pythons 2.4 , 2.5. Thanks to Laurence Rowe.
        - Included module and file path for source code. Thanks to davidjb.
        - Added z3c.autoinclude.plugin support to remove the zcml entry on buildout. Thanks to aclark. 

        0.1 experimental version 
        ------------------------

        - Initial release includes: Class and Ancestors, Properties, Callables and 
          Interfaces provided.
        - Support for Zope 2.13.x and Plone 4.0. Not tested with older or newer versions of Zope although it should work.
        - Support for Firefox 3.6 and Chrome 5.0. No support Internet Explorer yet.        
        
