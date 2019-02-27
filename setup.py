#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-fbpageinsights",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_fbpageinsights"],
    install_requires=[
        "singer-python>=5.0.12",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-fbpageinsights=tap_fbpageinsights:main
    """,
    packages=["tap_fbpageinsights"],
    package_data = {
        "schemas": ["tap_fbpageinsights/schemas/*.json"]
    },
    include_package_data=True,
)
