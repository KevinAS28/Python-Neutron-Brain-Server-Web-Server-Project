import sys
import os
import time
from threading import Thread
from PyQt4 import QtCore, QtGui, uic

path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)

qtCreatorFile = os.path.join(dir_path, "NeutronBrain_MAIN_GUI.ui") # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class GUI(QtGui.QMainWindow, Ui_MainWindow):
    @property
    def GUI_Name(self):
        return "NeutronBrain_MAIN_GUI"

    def Start_Server(self):
        self.Write_Log("Starting server %s... "%(self.list_server[self.SERVER_NUM.value()][0]))
        def start():
            self.list_server[self.SERVER_NUM.value()][1]()
        Thread(target=start).start()
        self.Write_Log("server %s started"%(self.list_server[self.SERVER_NUM.value()][0]))

    def Stop_Server(self):
        self.Write_Log("Stopping server %s... "%(self.list_server[self.SERVER_NUM.value()][0]))
        self.list_server[self.SERVER_NUM.value()][2]()
        self.Write_Log("Server %s stopped"%(self.list_server[self.SERVER_NUM.value()][0]))

    def Restart_Server(self):
        self.Write_Log("Restarting server %s... "%(self.list_server[self.SERVER_NUM.value()][0]))
        self.list_server[self.SERVER_NUM.value()][3]()
        self.Write_Log("Server Restarted "%(self.list_server[self.SERVER_NUM.value()][0]))

    def About_Server(self):
        self.Write_Status(self.list_server[self.SERVER_NUM.value()][4])

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)        
        self.START.clicked.connect(self.Start_Server)
        self.STOP.clicked.connect(self.Stop_Server)
        self.RESTART.clicked.connect(self.Restart_Server)
        self.ABOUT.clicked.connect(self.About_Server)
        self.list_server = []
        self.txt = ""
        self.log = ""
        number = 0
        for i in NeutronBrain_Files.Module_Lister("NeutronBrain_Servers"):
            server = NeutronBrain_Files.Load_Module(i, "NeutronBrain_Servers").Server(NeutronBrain_Files.Load_Module("TCP", "NeutronBrain_Protocols"))
            self.list_server.append([i, server.Start, server.Stop, server.Restart, "IDK but for joking"])
            self.LIST_SERVER.insertPlainText(str(number)+ ". " + i)
            number+=1
    def Write_Status(self, txt=""):
            if (not (self.txt.endswith("\n"))):
                self.txt += "\n"
            self.STATUS.insertPlainText(self.txt)
    def Write_Log(self, txt=""):
            if (not (txt.endswith("\n"))):
                txt += "\n"
            self.log+=txt
            self.LOGGING.insertPlainText(self.log)


def Start_GUI():
    def sub():
        app = QtGui.QApplication(sys.argv)
        global window
        window=(GUI())
        window.show()
        sys.exit(app.exec_())
    Thread(target=sub).start()

module_name = "NeutronBrain_MAIN_GUI"