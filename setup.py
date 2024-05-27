# -*- coding: utf-8 -*-
"""Setup for dataset-examples."""
from setuptools import setup, find_packages

requires = [
        'mrjob',
        'testify',
        'unittest2',
        ]

setup(
        name='local-lattes-python',
        description='Python microservice for local lattes',
        author='',
        url='https://github.com/Yelp/dataset-examples',
        packages=find_packages(),
        install_requires=requires,
        tests_require=requires,
        )