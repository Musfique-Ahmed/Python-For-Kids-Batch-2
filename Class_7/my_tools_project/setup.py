# This file is the build script for your package. It contains metadata and tells
# setuptools how to package your code.

from setuptools import setup, find_packages
import os

setup(
    name='my_tools',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A collection of useful math and string functions.',
    long_description=open('README.md', 'r').read() if 'README.md' in os.listdir('.') else '',
    long_description_content_type='text/markdown',
    url='https://github.com/your_username/my_tools',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

