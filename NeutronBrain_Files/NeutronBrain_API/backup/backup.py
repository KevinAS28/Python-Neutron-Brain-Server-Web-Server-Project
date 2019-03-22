








###
###C++
###


#from printt import *
import sys


backup_ext = ".backup"
def backup(berkas):
    #Info("Backup %s ..." %(berkas))
    with open(berkas+backup_ext, "rb") as baca:
        baca = baca.read()
        
