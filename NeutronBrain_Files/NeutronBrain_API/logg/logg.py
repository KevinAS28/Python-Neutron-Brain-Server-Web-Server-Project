log_file = ["NeutronBrain.log"]
over_write_log_file = True

import time

def Del_Space(x):
    return x.rstrip(" ").strip(" ")

def Check_Logg():
    #check file
    if (os.access(log_file[0], os.R_OK)):
        print("Log file exist")
        if over_write_log_file:
            print("Recreating...")
            os.remove(log_file[0])
            open(log_file[0], "w+")
            
def Logg(text, mode_log=0):
    with open(log_file[0], "a+") as tulis:
        tulis.write(str(time.ctime()))
        tulis.write(" ")
        tulis.write(text)
        tulis.write("\n")

module_name = "logg"
