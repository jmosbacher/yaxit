
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='yaxit',
    version='0.1.0',
    description='Top-level package for yaxit.',
    python_requires='>=3.7.1',
    project_urls={"homepage": "https://github.com/jmosbacher/yaxit"},
    author='Yossi Mosbacher',
    author_email='joe.mosbacher@gmail.com',
    license='MIT',
    classifiers=['Development Status :: 2 - Pre-Alpha', 'Intended Audience :: Developers', 'License :: OSI Approved :: MIT License', 'Natural Language :: English', 'Programming Language :: Python :: 3.7', 'Programming Language :: Python :: 3.8'],
    entry_points={"console_scripts": ["yaxit = yaxit.cli:main"]},
    packages=['yaxit'],
    package_dir={"": "."},
    package_data={},
    install_requires=['aiohttp==3.*,>=3.7.4', 'bokeh==2.*,>=2.3.1', 'click', 'h5py==3.*,>=3.2.1', 'matplotlib==3.*,>=3.4.1', 'numpy==1.*,>=1.20.2', 'pandas==1.*,>=1.2.4', 'pathlib==1.*,>=1.0.1', 'requests==2.*,>=2.25.1', 'tables==3.*,>=3.6.1', 'xarray==0.*,>=0.17.0', 'xpublish==0.*,>=0.1.0', 'xrviz==0.*,>=0.1.4'],
    extras_require={"dev": ["bumpversion", "coverage", "dephell", "flake8", "isort", "nbsphinx", "pylint", "pytest", "sphinx", "sphinx-material", "tox", "yapf"]},
)
