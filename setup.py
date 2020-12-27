#!/usr/bin/env python3
from setuptools import setup, find_packages


setup(
	name="Zgoubi metadata",
	version="0.1",
	packages=find_packages(),
	include_package_data=True,
	install_requires=["PyYAML>=5.3"],
)
