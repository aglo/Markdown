# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

setup (
    name = "Markdown",
    version = "1.0.dev",
    url = "http://github.com/arkfang/Markdown",
    author = "arkfang",
    author_email = "risetofly@163.com",
    packages = find_packages(),

    install_requires = [
        "Flask==0.10.1",
        "WTForms==1.0.4",
        "misaka==1.0.2",
        "Flask-Misaka==0.1.1"
    ]
)
