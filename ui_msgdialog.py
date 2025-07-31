# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'msgdialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)
import rc_myresource

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog.resize(350, 200)
        Dialog.setStyleSheet(u"background-color:transparent;")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 350, 200))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"border: 1px solid #C8D3CC;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 61, 201, 51))
        self.frame.setStyleSheet(u"background-color: rgb(245, 246, 245);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 181, 31))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"color:#0A141E;\n"
"\n"
"")
        self.label_3.setTextFormat(Qt.TextFormat.RichText)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 110, 231, 51))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(10)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"")
        self.label_2.setTextFormat(Qt.TextFormat.RichText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(152, 10, 48, 48))
        self.label.setStyleSheet(u"border: 2px solid #18B1A8;\n"
"border-radius:16px;")
        self.label.setPixmap(QPixmap(u":/new/prefix_msgdialogok/image/check.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_ok = QPushButton(self.frame_2)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setGeometry(QRect(65, 160, 231, 31))
        self.btn_ok.setStyleSheet(u"border-radius:6px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(24, 177, 168);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Dr.Smith Jhon", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Are you sure you want to delete this patient?", None))
        self.label.setText("")
        self.btn_ok.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

