#!/usr/bin/env python

from setuptools import setup, find_packages
from trein import __version__


setup(name='Distutils',
      version=__version__,
      description='Containerized Data Reduction Pipelines',
      author='Gijs Molenaar',
      author_email='gijsmolenaar@gmail.com',
      url='hhttps://github.com/gijzelaerr/trein',
      packages=find_packages(),
      install_requires=['luigi', 'docker-py'],
     )