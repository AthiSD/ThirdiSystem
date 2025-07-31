# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'msgdialogyes.ui'
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

class Ui_msgdialogyes(object):
    def setupUi(self, msgdialogyes):
        if not msgdialogyes.objectName():
            msgdialogyes.setObjectName(u"msgdialogyes")
        msgdialogyes.resize(277, 272)
        msgdialogyes.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"border: 1px solid #C8D3CC;")
        self.frame_2 = QFrame(msgdialogyes)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 277, 272))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(40, 70, 201, 61))
        self.frame.setStyleSheet(u"background-color: rgb(245, 246, 245);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 4, 181, 31))
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
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 36, 181, 20))
        self.label_4.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;\n"
"color: rgb(100, 107, 116);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 140, 201, 61))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color: transparent;\n"
"border:0px;\n"
"color: rgb(55, 64, 71);\n"
"")
        self.label_2.setTextFormat(Qt.TextFormat.RichText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(111, 10, 48, 48))
        self.label.setStyleSheet(u"border: 2px solid #FC4349;\n"
"border-radius:24px;")
        self.label.setPixmap(QPixmap(u":/new/prefix_msgdialogok/image/delete-2.png"))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_yes = QPushButton(self.frame_2)
        self.btn_yes.setObjectName(u"btn_yes")
        self.btn_yes.setGeometry(QRect(20, 220, 101, 31))
        self.btn_yes.setStyleSheet(u"border-radius:6px;\n"
"background-color: #18B1A8;\n"
"border-color: rgb(24, 177, 168);\n"
"color: rgb(255, 255, 255);")
        self.btn_no = QPushButton(self.frame_2)
        self.btn_no.setObjectName(u"btn_no")
        self.btn_no.setGeometry(QRect(150, 220, 101, 31))
        self.btn_no.setStyleSheet(u"border-radius:6px;\n"
"background-color: red;\n"
"border-color: rgb(24, 177, 168);\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(msgdialogyes)

        QMetaObject.connectSlotsByName(msgdialogyes)
    # setupUi

    def retranslateUi(self, msgdialogyes):
        msgdialogyes.setWindowTitle(QCoreApplication.translate("msgdialogyes", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("msgdialogyes", u"Dr.Smith Jhon", None))
        self.label_4.setText(QCoreApplication.translate("msgdialogyes", u"Patient ID: 100386", None))
        self.label_2.setText(QCoreApplication.translate("msgdialogyes", u"Are you sure you want to delete this patient?", None))
        self.label.setText("")
        self.btn_yes.setText(QCoreApplication.translate("msgdialogyes", u"YES", None))
        self.btn_no.setText(QCoreApplication.translate("msgdialogyes", u"NO", None))
    # retranslateUi

