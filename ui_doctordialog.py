# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doctordialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_doctor(object):
    def setupUi(self, doctor):
        if not doctor.objectName():
            doctor.setObjectName(u"doctor")
        doctor.resize(330, 300)
        self.frame = QFrame(doctor)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 330, 300))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 50, 201, 16))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.le_doctor_name = QLineEdit(self.frame)
        self.le_doctor_name.setObjectName(u"le_doctor_name")
        self.le_doctor_name.setGeometry(QRect(40, 80, 260, 30))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(10)
        self.le_doctor_name.setFont(font1)
        self.le_doctor_name.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(40, 120, 171, 21))
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.cmb_specialty = QComboBox(self.frame)
        self.cmb_specialty.addItem("")
        self.cmb_specialty.addItem("")
        self.cmb_specialty.addItem("")
        self.cmb_specialty.addItem("")
        self.cmb_specialty.setObjectName(u"cmb_specialty")
        self.cmb_specialty.setGeometry(QRect(40, 150, 261, 30))
        self.cmb_specialty.setFont(font1)
        self.cmb_specialty.setStyleSheet(u"QComboBox\n"
"{\n"
" background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.btn_savedoctor = QPushButton(self.frame)
        self.btn_savedoctor.setObjectName(u"btn_savedoctor")
        self.btn_savedoctor.setGeometry(QRect(40, 210, 260, 45))
        self.btn_savedoctor.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;\n"
"font: 500 11pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);\n"
"")

        self.retranslateUi(doctor)

        QMetaObject.connectSlotsByName(doctor)
    # setupUi

    def retranslateUi(self, doctor):
        doctor.setWindowTitle(QCoreApplication.translate("doctor", u"Add New Doctor", None))
        self.label_7.setText(QCoreApplication.translate("doctor", u"Doctor Name", None))
        self.le_doctor_name.setPlaceholderText(QCoreApplication.translate("doctor", u"Enter Doctor Name", None))
        self.label_12.setText(QCoreApplication.translate("doctor", u"Specialty ", None))
        self.cmb_specialty.setItemText(0, QCoreApplication.translate("doctor", u"IOL", None))
        self.cmb_specialty.setItemText(1, QCoreApplication.translate("doctor", u"Retinal", None))
        self.cmb_specialty.setItemText(2, QCoreApplication.translate("doctor", u"Cornea", None))
        self.cmb_specialty.setItemText(3, "")

        self.cmb_specialty.setPlaceholderText(QCoreApplication.translate("doctor", u"Select", None))
        self.btn_savedoctor.setText(QCoreApplication.translate("doctor", u"Submit", None))
    # retranslateUi

