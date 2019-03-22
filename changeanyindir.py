#!/usr/bin/python3

import os
import re
import sys

print("Change anything in dir, file name, dir name, inside text")
startdir = input("start directory: ")

if (startdir=="" or (os.access(startdir, os.W_OK)==False)):
 startdir = os.getcwd()
print("Startdir: %s"%(startdir))

dari = input("What you want to replace (Using regex)? ")
ke = input("you wish replace %s become: "%(dari))

for root, dirs, files in os.walk(top=startdir, topdown=False):
 for i in files:
  try:
    try:
      with open(os.path.join(root, i), "rb") as reader:
        baca =  reader.read()
        os.remove(os.path.join(root, i))
        with open(os.path.join(root, re.sub(dari, ke, i)), "wb") as writer:
         writer.write(re.sub(dari.encode("utf-8"), ke.encode("utf-8"), baca))
    except Exception as err:
      print(str(err))
      os.rename(os.path.join(root, i), os.path.join(root, re.sub(dari, ke, i)))
  except:
    pass
 for i in dirs:
  try:
    os.rename(os.path.join(root, i), os.path.join(root, re.sub(dari, ke, i)))
  except:
    pass
