from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='zope2.zodbbrowser',
      version=version,
      description="A zodb browser for Zope2",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='zope2 zope zodb python',
      author='Roberto Allende - Menttes SRL',
      author_email='rover@menttes.com',
      url='http://code.google.com/p/zodbbrowser',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['zope2'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'pygments',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
