#!/usr/bin/env python3

'''
Name:       test_kabul_download.py
Author:     Eric Rosko
Date:       Mar 21, 2018
Python ver. 3.4.3

Usage:  py.test (this just gives one pass or fail for all tests)
        py.test -v (this gives pass/fail for individual tests)
        py.test -s (this also lets print statements appear)
        py.test -sv (this enables both switches)

Desc: This is a short script so there aren't a ton of tests.
'''

from kabul_download import KabulDownloader

kd = None


def setup_function(function):
    """
    Runs once before each function in this file.  This is the same as
    XCUnit or CPPUnit testing.
    """
    global kd
    kd = KabulDownloader()


def teardown_function(function):
    """
    Runs once before each function in this file.  This is the same as
    XCUnit or CPPUnit testing.
    """
    global kd
    kd = None


def test_hello():
    text = kd.hello()
    assert text.find("hello") != -1
    assert text == "hello"


def test_class_read():
    assert kd.pageSource == ""
    kd.readFile("gallery.txt")
    assert kd.pageSource != ""


def test_readFromUrl():
    assert kd.pageSource == ""
    kd.readUrl()
    print(kd.pageSource)
    assert kd.pageSource != ""


def test_findImages():
    kd.readFile("gallery.txt")
    kd.findImages()
    # print(kd.images)

    assert len(kd.images) != 0
