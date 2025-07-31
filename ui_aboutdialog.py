# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QSizePolicy,
    QWidget)
import rc_myresource

class Ui_about(object):
    def setupUi(self, about):
        if not about.objectName():
            about.setObjectName(u"about")
        about.resize(453, 216)
        about.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_2 = QLabel(about)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 120, 120))
        self.label_2.setStyleSheet(u"background-color: rgb(245, 246, 245);\n"
"border-radius: 6px;\n"
"border: 1px solid #EBEEEC;")
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(about)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 60, 60, 60))
        self.label_3.setStyleSheet(u"background-color: transparent;")
        self.label_3.setPixmap(QPixmap(u":/new/prefix_stack/images/logo_A.png"))
        self.label_4 = QLabel(about)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 30, 251, 31))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_5 = QLabel(about)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(160, 70, 261, 16))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(10)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(100, 107, 116);")
        self.label_6 = QLabel(about)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 90, 261, 71))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(14)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(55, 64, 71);")
        self.label_6.setWordWrap(True)

        self.retranslateUi(about)

        QMetaObject.connectSlotsByName(about)
    # setupUi

    def retranslateUi(self, about):
        about.setWindowTitle(QCoreApplication.translate("about", u"About Us", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("about", u"Aurolab", None))
        self.label_5.setText(QCoreApplication.translate("about", u"Address :", None))
        self.label_6.setText(QCoreApplication.translate("about", u"No. 1, Veerapanjan, Sivagangai Main Road, Madurai, Tamilnadu 625020.", None))
    # retranslateUi

