from setuptools import setup, find_packages

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    packages=find_packages(exclude=('tests'))
)