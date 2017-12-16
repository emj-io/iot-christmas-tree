# -*- coding: utf-8 -*-
# Format from https://github.com/kennethreitz/samplemod/

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('VERSION') as f:
    version = f.read()

setup(
    name='iot-christmas-tree',
    version=version,
    description='IOT Christmas tree light controller',
    long_description=readme,
    author='Anthony Agresta and Eric M. Johnson',
    author_email='ejohnson.pub@gmail.com',
    url='https://github.com/emj-io/iot-christmas-tree',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
