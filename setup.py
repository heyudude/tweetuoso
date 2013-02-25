#!/usr/bin/env python
#coding: utf-8

from distutils.core import setup

setup(
    name = 'tweetuoso',
    version = "1.0.2",
    url = "http://c0ding.github.com/tweetuoso/",
    download_url = "https://github.com/c0ding/tweetuoso/archive/master.zip",
    author = 'c0ding',
    author_email='c0ding@nowhere.net',
    license = "WTFPL",
    packages = ['tweetuoso'],
    scripts = ['bin/tweetuoso'],
    description = 'Tweetuoso is a very light Twitter Command-line client developed in Python.',
    long_description=open('README.md').read(),
    keywords = 'twitter tweepy python command-line',
    requires=[
        'colorama (==0.2.5)',
        'requests (==1.1.0)',
        'tweepy (==2.0)',
    ],
)
