#!/usr/bin/env python
import sys

from setuptools import find_packages, setup


install_requires = [
    'cssselect',
    'cssutils',
    'lxml',
]

tests_require = [
    'exam',
    'pytest',
]

setup(
    name='toronado',
    version='0.0.2',
    author='ted kaemming, disqus',
    author_email='ted@disqus.com',
    packages=find_packages(exclude=('tests',)),
    install_requires=install_requires,
    tests_require=tests_require,
    zip_safe=False,
    license='Apache License 2.0',
)
