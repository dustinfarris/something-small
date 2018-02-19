#!/usr/bin/env python


from setuptools import setup, find_packages


install_requires = [
]


tests_require = [
  "ipython",
  "ipdb",
  "pytest",
  "pytest-watch",
]


setup(
  name="something-small",
  packages=find_packages(),
  version="0.0.1",
  description="An example python package",
  url="https://github.com/dustinfarris/something-small",
  maintainer="Dustin Farris",
  maintainer_email="dustin.farris@colorado.edu",
  extras_require={
    "tests": tests_require,
  },
  install_requires=install_requires,
)
