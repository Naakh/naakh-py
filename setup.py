# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "naakh"
VERSION = "0.0.1"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Naakh Translations",
    author_email="rohitsalim@gmail.com",
    url="",
    keywords=["Swagger", "Naakh Translations"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This is the python library that developers can use to query the Naakh API
    """
)


