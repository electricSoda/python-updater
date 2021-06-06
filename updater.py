print("Hi")

import requests
import re

class Updater:
    def __init__(self, target_link):
        self.target_link = target_link

        r = requests.get(self.target_link, allow_redirects=True)
        filename = self.getFileName(self.target_link)
        open(filename, "wb").write(r.content)

    def getFileName(self, url):
        fname = url.split("/")
        fname = fname[len(fname)-1]
        return fname


Updater("https://github.com/electricSoda/python-updater/blob/main/updater.py")
