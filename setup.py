"""Setup."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Optimize images living on a GCP-hosted CDN.',
    version='0.0.1',
    description='Pulls individual author details & social accounts.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hackersandslackers/gcloud-image-optimization',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Google Cloud GCP Image Optimization Endpoint Serverless Pillow Webp Compression Retina',
    packages=find_packages(),
    install_requires=['Flask',
                      'Pillow',
                      'google-cloud-storage',
                      'Requests',
                      'webp-converter',
                      'python-resize-image'],
    entry_points={
        'console_scripts': [
            'run = main:__main__',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hackersandslackers/gcloud-image-optimization/issues',
        'Source': 'https://github.com/hackersandslackers/gcloud-image-optimization/',
    },
)
