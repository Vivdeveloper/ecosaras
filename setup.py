from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecosaras/__init__.py
from ecosaras import __version__ as version

setup(
	name="ecosaras",
	version=version,
	description="ecosaras",
	author="sushant",
	author_email="sushantmanjare33@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
