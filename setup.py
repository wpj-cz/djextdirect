#!/usr/bin/env python

from distutils.core import setup

from djextdirect import VERSION

setup(name='djextdirect',
    version=( '%d.%d' % VERSION ),
    description='Ext.Direct serverside and clientside implementation for Django',
    author="Michael Ziegler",
    author_email='diese-addy@funzt-halt.net',
    url='http://bitbucket.org/Svedrin/djextdirect/downloads',
    download_url=('http://bitbucket.org/Svedrin/djextdirect/get/v%d.%d.tar.bz2' % VERSION),
    packages=['djextdirect'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'],
    )

