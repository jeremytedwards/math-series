# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="Mail Room Madness",
    description="A Python command line application for the mail room assignment.",
    long_description="This program takes input from the command line and runs different processes depending on the choice.",
    version=0.1,
    author="Jeremy Edwards",
    author_email="jeremytedwards@gmail.com",
    maintainer="Jeremy Edwards",
    license="MIT",
    py_modules=["mrmaddness"],
    package_dir={"": "src"},
    install_requires=[],
    extras_require={'test': ['pytest', "pytest-xdist", "tox"]},
)