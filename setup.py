from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in libraryapp/__init__.py
from libraryapp import __version__ as version

setup(
	name="libraryapp",
	version=version,
	description="a library test app",
	author="simon muturi ",
	author_email="simomutu8@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
