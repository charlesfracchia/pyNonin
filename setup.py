from distutils.core import setup
import os
    
packages=[
    'pynonin',

requiredPackages=[
    'serial',
]

setup(
    name='pyNonin',
    version='0.1',
    author='Charles Fracchia',
    author_email='charlesfracchia@gmail.com',
    packages=packages,
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='Python package to collect and parse Nonin Oximeter data',
    long_description=open('README').read(),
    requires=requiredPackages,
    provides=packages,
)
