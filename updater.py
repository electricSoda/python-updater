print("Hi THIS IS AN UPDATE")

import requests
import re
import os
import uuid

class Updater:
    def __init__(self, target_link):
        self.target_link = target_link

    def checkUpdate(self, link):
        os.chdir("C:\\teleport\\Code\\Python Updating Concept\\")
        r = requests.get(link, allow_redirects=True)
        filename = self.getFileName(link)
        open(filename, "wb").write(r.content)
        f = open(filename, "r")
        f1 = open("updatebranchLOCAL.txt", "r")

        if str(f.readline()) == str(f1.readline()):
            print(f.readline(), "Up to date")
            return False
        else:
            print(f.readline(), "Different than (local): " + f1.readline())
            return True

    def update(self):
        os.chdir("C:\\teleport\\Code\\Python Updating Concept\\updated")

        r = requests.get(self.target_link, allow_redirects=True)
        filename = self.getFileName(self.target_link)
        open(filename, "wb").write(r.content)

    def updateChanges(self):
        os.chdir("C:\\teleport\\Code\\Python Updating Concept\\")

        pathtonewfile = "updated/updater.py"
        a = open(pathtonewfile, 'r')
        newContents = a.read()
        a.close()

        with open("updater.py", "w") as f:
            f.write(newContents)
            f.close()

    def updateBranch(self):
        globalF = open("updatebranch.txt", "r")
        id = globalF.readline()

        f = open("updatebranchLOCAL.txt", "w")
        f.write(id)
        f.close()

    def getFileName(self, url):
        fname = url.split("/")
        fname = fname[len(fname)-1]
        return fname

    def uid():
        return uuid.uuid1()


u = Updater("https://raw.githubusercontent.com/electricSoda/python-updater/main/updater.py")
check = u.checkUpdate("https://raw.githubusercontent.com/electricSoda/python-updater/main/updatebranch.txt")

if check:
    u.update()
    u.updateChanges()
    u.updateBranch()
