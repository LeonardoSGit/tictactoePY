#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Leonardo Ferrer",
    author_email='leoferrersilva@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Tic Tac Toe in Python vs AI",
    entry_points={
        'console_scripts': [
            'tictactoe=tictactoe.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tictactoe',
    name='tictactoe',
    packages=find_packages(include=['tictactoe', 'tictactoe.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/LeonardoSGit/tictactoe',
    version='0.1.0',
    zip_safe=False,
)
