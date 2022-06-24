from setuptools import setup, find_packages
import pkg_resources  # part of setuptools
setup(
    name='dataEngineerUtilities',
    packages=['dataEngineerUtilities'],
    description='DB Library for Credgenics',
    version= pkg_resources.require("dataEngineerUtilities")[0].version,
    url='',
    author='Ketan Bassi',
    author_email='ketan.bassi@credgenics.com',
   
)
