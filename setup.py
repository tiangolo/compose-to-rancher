"""compose-to-rancher
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='compose-to-rancher',
    version='0.1.0a4',

    description='Convert Docker Compose V2 to Rancher compatible Docker Compose V1',
    long_description=long_description,
    url='https://github.com/tiangolo/compose-to-rancher',
    author='Sebastian Ramirez',
    author_email='tiangolo@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Code Generators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='setuptools development docker rancher compose',
    packages=find_packages(),
    install_requires=['pyyaml'],
    entry_points={
        'console_scripts': [
            'compose-to-rancher=compose_to_rancher:main',
        ],
    },
)
