#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=7.0',
    'numpy>=1.19.5',
    'pandas>=1.1.5'
]

test_requirements = ['pytest>=3', ]

setup(
    author="Nathaniel Delos Santos",
    author_email='Nathaniel.P.DelosSantos@jacobs.ucsd.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Utility functions for conversion between IUPAC nucleotide codes and one-hot-like encoded sequence matrices, with extensions for RNA.",
    entry_points={
        'console_scripts': [
            'nucleotides_to_matrices=nucleotides_to_matrices.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='nucleotides_to_matrices',
    name='nucleotides_to_matrices',
    packages=find_packages(include=['nucleotides_to_matrices', 'nucleotides_to_matrices.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/npdeloss/nucleotides_to_matrices',
    version='0.1.0',
    zip_safe=False,
)
