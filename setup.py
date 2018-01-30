# -*- coding: utf-8 -*-
#
# Copyright 2018 ITCase (info@itcase.pro)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path

from setuptools import find_packages, setup

AUTHOR = 'ITCase'
DESCRIPTION = 'Field with CAPTCHA for Django Forms'
EMAIL = 'info@itcase.pro'
NAME = 'supercaptcha'
URL = 'http://www.itcase.pro/'
VERSION = '0.2.1'

REQUIRED = [
    'django>=1.11,<2.0',
    'pillow',
]

here = Path(__file__).parent

with (here / 'README.md').open() as f:
    long_description = '\n' + f.read()

setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=long_description,
    version=VERSION,
    url=URL,
    author=AUTHOR,
    author_email=EMAIL,
    packages=find_packages(exclude=('tests', 'docs')),
    include_package_data=True,
    install_requires=REQUIRED,
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
    ]
)
