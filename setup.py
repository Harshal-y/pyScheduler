#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

with open('Version', 'rb') as f:
    version = next(f).strip().decode('utf-8')

with open('README.rst') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = [r for r in f]
try:
    with open('requirements_test.txt') as f:
        requirements_test = [r for r in f]
except IOError:
    requirements_test = None


__doc__ = readme

setup(
    name='TaskScheduler',
    version=version,
    url='https://github.com/Richard-Mathie/pyScheduler',
    license='MIT',
    author='Richard Mathie',
    author_email='richard.mathie@cantab.net',
    description='Scheduler schedules python tasks to run at some delay time later',
    long_description=__doc__,
    py_modules=['scheduler'],
    install_requires=requirements,
    tests_require=requirements_test,
    test_suite='nose2.collector.collector',
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)
