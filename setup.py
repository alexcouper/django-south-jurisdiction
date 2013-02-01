#!/usr/bin/python

from distutils.core import setup
from south_jurisdiction import __version__

setup(
    name='South Jurisdiction',
    version=__version__,
    description='South Jurisdiction: South Migrations contained for Django',
    long_description=open('README.md').read(),
    author='Alex Couper',
    author_email='amcouper@gmail.com',
    url='https://github.com/alexcouper/django-south-jurisdiction/',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    packages=[
        'south_jurisdiction',
    ],
)
