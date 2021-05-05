#!/usr/bin/env python3

import os, re
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

if __name__ == "__main__":
    setup(
        name = 'jasmin-statusboard',
        description = 'Django application for managing services, roles and access',
        long_description = README,
        classifiers = [
            "Programming Language :: Python",
            "Framework :: Django",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
        author = 'Matt Pritchard',
        author_email = 'matt.pritchard@stfc.ac.uk',
        url = 'https://github.com/cedadev/jasmin-statusboard',
        keywords = 'web django jasmin services',
        packages = find_packages(),
        include_package_data = True,
        zip_safe = False,
        install_requires = [
            'django',
            'django-statusboard'
        ],
    )
