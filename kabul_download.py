#!/usr/bin/env python3

'''
Name:       kabul_download.py
Author:     Eric Rosko
Date:       Mar 21, 2018
Python ver. 3.4.3

Usage: >python3 ./kabul_download.py http://your-website/image-folder/

Description: This downloader only supports jpg but that is easy to change
in the source or make it support multiple extensions.  It does not work
with files that have spaces in the name and stops downloading everything
when it cannot find the file to download.
'''

import os
import re
import time
import urllib.request
import sys

__author__ = 'Eric Rosko'


class KabulDownloader():
    def __init__(self,
                 url=None):
        if url is None:
            self.rootURL = 'http://www.ericrosko.com/sample-album/'
        else:
            self.rootURL = url
        self.pageSource = ""
        self.images = []

    def hello(self):
        return "hello"

    def readFile(self, name):
        with open(name, 'r') as myfile:
            self.pageSource = myfile.read().replace('\n', '')
        # print(self.pageSource)

    def findImages(self):
            # http://www.regexpal.com has a nice online checker :)
        regex = re.compile("[A-Za-z0-9@\._-]+\.jpg".format('jpg'))

        results = regex.findall(self.pageSource)

        for item in results:
            # a set would be better here
            if item not in self.images:
                # print("adding", item)
                self.images.append(item)

    def readUrl(self):
        assert self.rootURL is not None
        response = urllib.request.urlopen(self.rootURL)
        # print("response", response)
        self.pageSource = response.read().decode('utf-8')

    def downloadImage(self,
                      url=None,
                      imageName=None):

        if url is None:
            if self.rootURL is None:
                print("No url available for download file")
                return
            else:
                url = self.rootURL

        if imageName is None:
            print("image name is required.")
            return

        if os.path.isdir("files") is False:
            print("ERROR: local downloads folder does not exist")
            os.makedirs('files')
            print("Local 'files' folder successfully created.")
            return

        fullLocalPath = os.path.join('files', imageName)
        if os.path.exists(fullLocalPath):
            print("File already downloaded:", imageName)
            return

        path = os.path.join(url, imageName)
        print("remote url:", path)

        response = urllib.request.urlopen(path)
        image = response.read()

        # print("image", image)
        fullLocalPath = os.path.join('files', imageName)
        print("full local path", fullLocalPath)

        with open(fullLocalPath, 'wb') as f:
            f.write(image)
            print("Downloaded", imageName)

    def run(self):
        self.readUrl()
        self.findImages()

        for image in self.images:
            self.downloadImage(imageName=image)
            # to prevent the server from freaking out and
            # locking us out, put in a small delay
            time.sleep(1)


counter = 0
url = ""
for arg in sys.argv:
    if counter == 1:
        if arg[:7] != "http://":
            print("Error: Your URL must start with 'http://'.")
        else:
            url = arg
    else:
        counter += 1

if url != "":
    print("using URL:", url)
    test = KabulDownloader(url=url)
    test.run()
else:
    print("You must give a parameter starting with http://")
# test = KabulDownloader()
# print(test.rootURL)
# test.readUrl()
# # print(test.pageSource)
# test.findImages()

# test.run()
