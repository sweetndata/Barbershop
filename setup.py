#!/usr/bin/env python

import pathlib

import pkg_resources
import setuptools

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]
setuptools.setup(
    name='barbershop',
    version='0.1',
    description='Barbershop',
    author='Dave Choi',
    author_email='dave.dev@icloud.com',
    packages=setuptools.find_packages(include=['*']),
    install_requires=install_requires
)
