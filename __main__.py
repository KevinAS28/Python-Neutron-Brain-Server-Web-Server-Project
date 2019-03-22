import os
import sys
import time
import imp
from threading import Thread
import NeutronBrain_Files

parent_dir = os.getcwd()

printt = NeutronBrain_Files.Load_Module("printt", "NeutronBrain_API")
conf = NeutronBrain_Files.Load_Module("conf", "NeutronBrain_API")
logg = NeutronBrain_Files.Load_Module("logg", "NeutronBrain_API")
all_server = NeutronBrain_Files.Module_Lister("NeutronBrain_Servers")
all_gui = NeutronBrain_Files.Module_Lister("NeutronBrain_GUIs")
all_protocol = NeutronBrain_Files.Module_Lister("NeutronBrain_Protocols")

def Debug():
        while True:
            try:
                order = (input("order: "))
                if (order=="exit"):
                    break
                exec(order)
            except KeyboardInterrupt:
                break
            except Exception as err:
                printt.Error(str(err))

def Dev_Mode():
    Thread(target=Debug).start()

GUI0 = NeutronBrain_Files.Load_Module("NeutronBrain_MAIN_GUI", "NeutronBrain_GUIs", asname="GUI0")

def Start_NeutronBrain_GUI():
    Thread(target=GUI0.Start_GUI()).start()
    
def main():
    printt.Add_Function(logg.Logg)
    printt.Info("Starting OWS...")
    Dev_Mode()
    printt.Info("Opening GUI...")
    Start_NeutronBrain_GUI()
    def addlog():
        while (True):
            try:
                if (GUI0.window!=None):
                    printt.Add_Function(GUI0.window.Write_Log)
                    break
            except:
                pass
            time.sleep(2)
    Thread(target=addlog).start()


if __name__ == "__main__":
    main()