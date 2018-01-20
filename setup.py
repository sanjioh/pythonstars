# coding: utf-8
from setuptools import find_packages, setup

setup(
    name='pythonstars_app',
    version='0.0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    zip_safe=False,
)
