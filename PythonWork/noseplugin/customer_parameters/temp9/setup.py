#! /usr/bin/python
# -*- coding: utf-8 -*-

try:
    import ez_setup
    ez_setup.use_setuptools()
except ImportError:
    pass

from setuptools import setup, find_packages

setup(
    name='Command Arguments',
    version='0.1',
    author='Frank Zhu',
    author_email = 'fzhurd@gmail.com',
    description = 'nose plugin for command line parsed parameters',
    license = 'GNU LGPL',
    py_modules = ['test_plugin'],
    zip_safe=True,
    packages=find_packages(),
    install_requires=['nose'],
    entry_points = {
        'nose.plugins.0.10': [       
            'with-command_arguments=test_plugin:CommandArguments',
            ]
        }

    )
