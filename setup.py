import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


# Some initialization
here = os.path.abspath(os.path.dirname(__file__))
long_description = open(os.path.join(here, 'README.rst')).read()


data_files = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)


package_name = 'obscene_words_filter'


# this code snippet is taken from django-registration setup.py script
for dirpath, dirnames, filenames in os.walk(package_name):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if filenames:
        prefix = dirpath[len(package_name):]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name="python-obscene-words-filter",
    version="0.1.4",
    packages=find_packages(),
    author="asyncee",
    description="Obscene words filter for python, built on regexp for Russian language.",
    long_description=long_description,
    license="MIT",
    keywords="obscene swear words filter",
    url='https://github.com/asyncee/python-obscene-words-filter',
    download_url='https://pypi.python.org/pypi/python-obscene-words-filter/',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    package_dir={package_name: package_name},
    package_data={package_name: data_files},
    zip_safe=False,
)
