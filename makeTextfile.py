#!/usr/bin/env python

"make flie and write someting"

import os

ls = os.linesep

#get filename

while True:
    fname = raw_input("please input the file name:\n")

    if os.path.exists(fname):
        print "ERROR: '%s' already exists" %fname
    else:
        break

#get file content (text) lines

all = []

print "\nEnter lines ('.'by itself to quit).\n"

#loop until user terminates input 

while True:
    entry = raw_input("> ")
    if entry == ".":
        break
    else:
        all.append(entry)


fobj = open(fname ,"w")
fobj.writelines(['%s%s' % (x , ls) for x in all])
fobj.close()

print "DONE"


