import os
import sys

print("USE C++ FOR FASTER PROCESSS!!!")

def Check_File(file):
    if (not(os.access(file, os.R_OK))):
        return False
    return True

def File_Reader(file):
    if (not(Check_File(file))):
        raise FileNotFoundError('the file %s is not exist' %(file))
    with open(file, "rb") as read:
        return read.read()


    
