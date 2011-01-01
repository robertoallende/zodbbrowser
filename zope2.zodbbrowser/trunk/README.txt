Introduction
============

Zope2.ZodbBrowser is a tool to inspect ZODB objects. Inspired on smalltalk's class browser and zodbbrowsers for zope3.

Buildout Install
================

$ svn co http://zodbbrowser.googlecode.com/svn/buildout/ zodbbrowser
$ python2.6 bootstrap.py
$ bin/buildout -v
$ bin/instance fg

Existing buildout install
=========================

If you already have a buildout for Zope2.13 or Plone4 running, edit buildout.cfg to add zope2.zodbbrowser to eggs and zcml sections at buildout and instance parts respectively. 

...
eggs = zope2.zodbbrowser

[instance]
...
zcml = zope2.zodbbrowser

Then run bin/buildout to make the changes effective.

Use of zodbbrowser
===============

To access zodbbrowser use /zodbbrowser in your zope instance, for example:
http://localhost:8080/zodbbrowser


