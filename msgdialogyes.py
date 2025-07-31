# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from ui_msgdialog import Ui_Dialog
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from ui_msgdialogyes import Ui_msgdialogyes
class msgdialogyes(QDialog):
    dialog_signal = Signal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_msgdialogyes()
        self.ui.setupUi(self)
        self.ui.btn_yes.clicked.connect(lambda:self.close())
        self.ui.btn_no.clicked.connect(lambda:self.close())
