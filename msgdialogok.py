# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from ui_msgdialog import Ui_Dialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal

class msgdialogok(QDialog):
    dialog_signal = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btn_ok.clicked.connect(self.dclose)
    def dclose(self):
        self.close()


