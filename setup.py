from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Advance Recon Tool'
LONG_DESCRIPTION = 'A tool for automating recon'

# Setting up
setup(
    name="artmation",
    version=VERSION,
    author="Nakba",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['animation', 'requests', 'colorama','argparse','python-whois'],
    url='https://github.com/nerdynerd09/ART',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)