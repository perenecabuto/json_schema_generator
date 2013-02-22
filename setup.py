#!/usr/bin/env python

from distutils.core import setup


setup(
    name='json_schema_generator',
    version='0.1',
    description='A simple json schema generator based on json resource with auto validation tools',
    author='Felipe Ramos Ferreira',
    author_email='perenecabuto@gmail.com',
    maintainer='Felipe Ramos Ferreira',
    maintainer_email='perenecabuto@gmail.com',
    scripts=['bin/jsonschema_generator.py'],
    url='https://pypi.python.org/pypi/json_schema_generator/',
    include_dirs=('json_schema_generator/',),
    packages=[
        'json_schema_generator',
    ],
    keywords='json_schema, jsonschema, json, generator, api, validator',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
    ],
)
