#!/usr/bin/env python
#This file is part of emailvalid. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

import os
from setuptools import setup, find_packages
import emailvalid


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='emailvalid',
        version=emailvalid.__version__,
        author='Zikzakmedia SL',
        author_email='zikzak@zikzakmedia.com',
        url="http://www.zikzakmedia.com/",
        description="Python module to validate eMail",
        long_description=read('README'),
        download_url="https://bitbucket.org/zikzakmedia/python-emailvalid",
        packages=find_packages(),
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Office/Business :: Financial :: Accounting',
            'Topic :: Software Development :: Internationalization',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
        license='GPL-3',
        extras_require={
        },
        test_suite="emailvalid.tests",
    )
