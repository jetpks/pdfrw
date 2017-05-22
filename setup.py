#!/usr/bin/env python

from setuptools import setup
from pdfrw import __version__ as version
from pdfrw.py23_diffs import convert_load

setup(
    name='pdfrw-unsafe',
    version=version,
    description='PDF file reader/writer library',
    long_description=convert_load(open("README.rst", 'rb').read()),
    author='Eric Jacobs',
    author_email='eric@slush.systems',
    platforms='Independent',
    url='https://github.com/pmaupin/pdfrw',
    packages=['pdfrw-unsafe', 'pdfrw-unsafe.objects'],
    license='MIT',
    classifiers=[
    ]
)
