import os
import re


curdir = os.getcwd()
secdir = curdir
print(curdir)
with open("dir.txt", "r") as f:
    ll = f.readlines()
    for ls in ll:
        r = re.compile("([ ]*)(\|-)([\w]+)(.+)")
        l = list(r.match(ls).groups())

        if len(l[0]) == 0 and l[-1] == "/":
            os.chdir(curdir)
            os.mkdir(l[2])
            os.chdir(l[2])
            secdir = os.getcwd()
            print(secdir)
        elif len(l[0]) == 0:
            os.chdir(curdir)
            open(l[2] + l[3], 'w').close()
        elif len(l[0]) == 2 and l[-1] == "/":
            os.chdir(secdir)
            os.mkdir(l[2])
            os.chdir(l[2])
            print(os.getcwd())
        elif l[-1] != "/":
            open(l[2]+l[3], 'w').close()
