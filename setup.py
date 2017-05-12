from setuptools import setup
from codecs import open
from os import path

from inshore import __version__

here = path.abspath(path.dirname(__file__))


def readme():
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        return f.read()


setup(
    name='inshore',
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

    keywords='plotting matplotlib seaborn',
    url='https://github.com/scruffy-t/inshore',
    author='Tobias Schruff',
    author_email='tobias.schruff@gmail.com',
    license='BSD',
    packages=['inshore'],

    # we use "nose" for tests
    # $ python setup.py test
    # to execute the test suite
    test_suite='nose.collector',
    tests_require=['nose'],

    zip_safe=False
)
