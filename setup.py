from setuptools import setup
from codecs import open
from os import path

from mpls.version import __version__

here = path.abspath(path.dirname(__file__))


def readme():
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(
    name='mpls',
    version=__version__,
    description='An open library of matplotlib styles',
    long_description=readme(),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    keywords='plotting matplotlib styles',
    url='https://github.com/scruffy-t/mpls',
    author='Tobias Schruff',
    author_email='tobias.schruff@gmail.com',
    license='BSD',
    packages=['mpls'],

    zip_safe=False
)
