import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "NeutronBrain.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.start_server.clicked.connect(self.ada)
        self.stop_server.clicked.connect(self.daa)
    def ada(self):
        print("ADA")
    def daa(self):
        print("YAY")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
sys.exit(app.exec_())