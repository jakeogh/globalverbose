# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

import fastentrypoints

dependencies = ["click"]

config = {
    "version": "0.1",
    "name": "globalverbose",
    "url": "https://github.com/jakeogh/globalverbose",
    "license": "ISC",
    "author": "Justin Keogh",
    "author_email": "github.com@v6y.net",
    "description": "minimal global state for verbose",
    "long_description": __doc__,
    "packages": find_packages(exclude=["tests"]),
    "package_data": {"globalverbose": ["py.typed"]},
    "include_package_data": True,
    "zip_safe": False,
    "platforms": "any",
    "install_requires": dependencies,
}

setup(**config)
