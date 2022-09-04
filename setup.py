#!/usr/bin/env python
"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = []

test_requirements = []

setup(
    author="Vikash Bajaj",
    author_email='esq@vikashbajaj.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description=
    "A python package that provides GraphQL API for Elasticsearch and makes it easier to query data without writing complex queries.",
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='esq',
    name='esq',
    packages=find_packages(include=['esq', 'esq.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/scottydelta/esq',
    version='1.0.2',
    zip_safe=False,
)
