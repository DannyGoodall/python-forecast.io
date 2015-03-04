import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8') as f:
        contents = f.read()

    return contents


setup(
    name="python-forecastio",
    version="1.3.1",
    author="Ze'ev Gilovitz",
    author_email="zeev.gil@gmail.com",
    description=("A thin Python Wrapper for the Forecast.io weather API"),
    license="BSD 2-clause",
    keywords="weather API wrapper forecast.io location",
    url="http://zeevgilovitz.com/python-forecast.io/",
    packages=['forecastio'],
    package_data={'forecastio': ['LICENSE.txt', 'README.rst']},
    long_description=read('README.rst'),
    install_requires=['requests>=1.6'],
)
