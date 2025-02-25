# This file is part of copy_on_write.
# Copyright (c) 2023, Bas Terwijn.
# SPDX-License-Identifier: BSD-2-Clause

from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description_from_readme = (this_directory / "README.md").read_text()

setup(
    name = 'copy_on_write',
    version = '0.0.1',
    description = 'Copy-on-Write alternatives for common Python collection types',
    long_description = long_description_from_readme,
    long_description_content_type = 'text/markdown',
    readme = 'README.md',
    url = 'https://github.com/bterwijn/copy_on_write',
    author = 'Bas Terwijn',
    author_email = 'bterwijn@gmail.com',
    license = 'BSD 2-clause',
    packages = ['copy_on_write'],

    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  
        'Programming Language :: Python :: 3',
    ],
)
