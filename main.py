from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QWidget, QDialog
from plot import plot
from PyQt5.QtWidgets import*
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtWidgets import QMessageBox

def PopUpMessage(self, error_message):
    QMessageBox.critical(self, "Error", error_message)

class UI(QDialog):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('plloter.ui', self)
        self.button1.clicked.connect(self.sketch)


    def sketch(self):
        try:
            o=plot(self.lineEdit_3.text(), self.lineEdit.text(), self.lineEdit_2.text())
            o.plotFunction()
        except ValueError as ve:
            err_message = ve.args[0]
            PopUpMessage(self, err_message)
            self.emptyEntries()
            return

    def emptyEntries(self):
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")

if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    currWindow = UI()
    currWindow.show()
    sys.exit(application.exec_())
