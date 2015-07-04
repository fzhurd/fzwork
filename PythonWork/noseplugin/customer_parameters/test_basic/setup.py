# usr/bin/python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='mypackage',
    ...
    install_requires=['nose==1.3.0'],
    py_modules=['myplugin'],
    entry_points={
      'nose.plugins.0.10': [
        'myplugin = myplugin:MyCustomPlugin'
      ]
    }
)