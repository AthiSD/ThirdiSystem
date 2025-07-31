# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateTimeEdit, QFrame, QGraphicsView, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import rc_myresource

class Ui_dash_screen(object):
    def setupUi(self, dash_screen):
        if not dash_screen.objectName():
            dash_screen.setObjectName(u"dash_screen")
        dash_screen.resize(1680, 1050)
        dash_screen.setStyleSheet(u" QToolTip {\n"
"        background-color: transparent;\n"
"        color: white;\n"
"        border: 1px solid black;\n"
"    }")
        self.centralwidget = QWidget(dash_screen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget_2 = QStackedWidget(self.centralwidget)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(0, 0, 1680, 1050))
        self.stackedWidget_2.setStyleSheet(u"background-color: rgb(245, 246, 245);\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.main_widget = QWidget()
        self.main_widget.setObjectName(u"main_widget")
        self.frame = QFrame(self.main_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1680, 60))
        self.frame.setStyleSheet(u"background-color: rgb(235, 238, 236);\n"
"border-color: transparent;\n"
"border-radius: 0px;\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(28, 16, 117, 28))
        self.label.setPixmap(QPixmap(u":/new/prefix_topheader/images/logo_with_text.png"))
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(169, 16, 1241, 30))
        self.frame_2.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(350, 0, 500, 30))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1460, 20, 22, 22))
        self.label_2.setPixmap(QPixmap(u":/new/prefix_topheader/images/calender.png"))
        self.lbl_datetime = QLabel(self.frame)
        self.lbl_datetime.setObjectName(u"lbl_datetime")
        self.lbl_datetime.setGeometry(QRect(1487, 20, 171, 22))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        self.lbl_datetime.setFont(font)
        self.lbl_datetime.setStyleSheet(u"color: rgb(55, 64, 71);\n"
"font: 500 11pt \"Ubuntu\";")
        self.horizontalLayoutWidget = QWidget(self.frame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(450, 20, 711, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.btn_patients = QPushButton(self.horizontalLayoutWidget)
        self.btn_patients.setObjectName(u"btn_patients")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(11)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.btn_patients.setFont(font1)
        self.btn_patients.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgb(100, 107, 116);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    border-top:1px solid #30CFC6;\n"
"    border-bottom:1px solid #30CFC6;\n"
"    border-radius:0px;	\n"
"    color:#0C6582\n"
"}\n"
"QPushButton::checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/new/prefix_topheader/images/users.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_patients.setIcon(icon)
        self.btn_patients.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_patients)

        self.btn_doctor = QPushButton(self.horizontalLayoutWidget)
        self.btn_doctor.setObjectName(u"btn_doctor")
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(11)
        self.btn_doctor.setFont(font2)
        self.btn_doctor.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgb(100, 107, 116);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	    border-top:1px solid #30CFC6;\n"
"    border-bottom:1px solid #30CFC6;\n"
"    border-radius:0px;	\n"
"    color:#0C6582\n"
"}\n"
"QPushButton::checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/new/prefix_topheader/images/doctor.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_doctor.setIcon(icon1)
        self.btn_doctor.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_doctor)

        self.btn_settings = QPushButton(self.horizontalLayoutWidget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setFont(font2)
        self.btn_settings.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgb(100, 107, 116);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	    border-top:1px solid #30CFC6;\n"
"    border-bottom:1px solid #30CFC6;\n"
"    border-radius:0px;	\n"
"    color:#0C6582\n"
"}\n"
"QPushButton::checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/new/prefix_topheader/images/settings_ 2 (2).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings.setIcon(icon2)
        self.btn_settings.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_settings)

        self.btn_aboutus = QPushButton(self.horizontalLayoutWidget)
        self.btn_aboutus.setObjectName(u"btn_aboutus")
        self.btn_aboutus.setFont(font2)
        self.btn_aboutus.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgb(100, 107, 116);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	    border-top:1px solid #30CFC6;\n"
"    border-bottom:1px solid #30CFC6;\n"
"    border-radius:0px;	\n"
"    color:#0C6582\n"
"}\n"
"QPushButton::checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/new/prefix_topheader/images/aboutus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_aboutus.setIcon(icon3)
        self.btn_aboutus.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_aboutus)

        self.btn_shutdown = QPushButton(self.horizontalLayoutWidget)
        self.btn_shutdown.setObjectName(u"btn_shutdown")
        self.btn_shutdown.setFont(font2)
        self.btn_shutdown.setStyleSheet(u"QPushButton\n"
"{\n"
"	color: rgb(100, 107, 116);\n"
"}\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	    border-top:1px solid #30CFC6;\n"
"    border-bottom:1px solid #30CFC6;\n"
"    border-radius:0px;	\n"
"    color:#0C6582\n"
"}\n"
"QPushButton::checked\n"
"{\n"
"	background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(74, 74, 74, 255),stop:1 rgba(49, 49, 49, 255));\n"
"	border: 1px solid #222;\n"
"\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/new/prefix_stack/images/power 1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_shutdown.setIcon(icon4)
        self.btn_shutdown.setFlat(True)

        self.horizontalLayout.addWidget(self.btn_shutdown)

        self.stackedWidget = QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 60, 1680, 1000))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(223, 228, 225);")
        self.patientpage = QWidget()
        self.patientpage.setObjectName(u"patientpage")
        self.frame_7 = QFrame(self.patientpage)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 0, 1680, 990))
        self.frame_7.setStyleSheet(u"background-color: rgb(245, 246, 245);\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(590, 50, 500, 600))
        self.frame_8.setStyleSheet(u"background-color: rgb(200, 211, 204);")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 20, 501, 20))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(10, 20, 30);")
        self.lbl_patient = QLabel(self.frame_8)
        self.lbl_patient.setObjectName(u"lbl_patient")
        self.lbl_patient.setGeometry(QRect(125, 60, 71, 16))
        font3 = QFont()
        font3.setFamilies([u"Ubuntu"])
        font3.setPointSize(10)
        self.lbl_patient.setFont(font3)
        self.lineEdit = QLineEdit(self.frame_8)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(125, 80, 260, 30))
        self.lineEdit.setFont(font3)
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.lbl_patientfname = QLabel(self.frame_8)
        self.lbl_patientfname.setObjectName(u"lbl_patientfname")
        self.lbl_patientfname.setGeometry(QRect(125, 130, 191, 16))
        self.lbl_patientfname.setFont(font3)
        self.lineEdit_2 = QLineEdit(self.frame_8)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(125, 150, 125, 30))
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.lbl_gender = QLabel(self.frame_8)
        self.lbl_gender.setObjectName(u"lbl_gender")
        self.lbl_gender.setGeometry(QRect(125, 200, 71, 16))
        self.lbl_gender.setFont(font3)
        self.lbl_age = QLabel(self.frame_8)
        self.lbl_age.setObjectName(u"lbl_age")
        self.lbl_age.setGeometry(QRect(125, 270, 71, 16))
        self.lbl_age.setFont(font3)
        self.lineEdit_4 = QLineEdit(self.frame_8)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(125, 290, 260, 30))
        self.lineEdit_4.setFont(font3)
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.lbl_mobile = QLabel(self.frame_8)
        self.lbl_mobile.setObjectName(u"lbl_mobile")
        self.lbl_mobile.setGeometry(QRect(125, 340, 121, 16))
        self.lbl_mobile.setFont(font3)
        self.lineEdit_5 = QLineEdit(self.frame_8)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(125, 360, 260, 30))
        self.lineEdit_5.setFont(font3)
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.lbl_doctor = QLabel(self.frame_8)
        self.lbl_doctor.setObjectName(u"lbl_doctor")
        self.lbl_doctor.setGeometry(QRect(125, 410, 71, 16))
        self.lbl_doctor.setFont(font3)
        self.comboBox = QComboBox(self.frame_8)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(125, 430, 261, 30))
        self.comboBox.setFont(font3)
        self.comboBox.setStyleSheet(u"QComboBox\n"
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
        self.radioButton = QRadioButton(self.frame_8)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(125, 220, 125, 31))
        self.radioButton.setFont(font3)
        self.radioButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.radioButton_2 = QRadioButton(self.frame_8)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(259, 220, 125, 31))
        self.radioButton_2.setFont(font3)
        self.radioButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.lineEdit_3 = QLineEdit(self.frame_8)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(259, 150, 125, 30))
        self.lineEdit_3.setFont(font3)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.pushButton = QPushButton(self.frame_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(125, 500, 260, 45))
        self.pushButton.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;\n"
"font: 500 11pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_newdoctor_patient = QPushButton(self.frame_8)
        self.btn_newdoctor_patient.setObjectName(u"btn_newdoctor_patient")
        self.btn_newdoctor_patient.setGeometry(QRect(169, 408, 91, 20))
        self.btn_newdoctor_patient.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(24, 177, 168);")
        icon5 = QIcon()
        icon5.addFile(u":/new/prefix_topheader/image/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/new/prefix_topheader/image/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_newdoctor_patient.setIcon(icon5)
        self.frame_16 = QFrame(self.frame_8)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 0, 500, 600))
        self.frame_16.setStyleSheet(u"background-color:#EBEEEC;")
        self.frame_16.setFrameShape(QFrame.NoFrame)
        self.label_26 = QLabel(self.frame_16)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(0, 20, 501, 20))
        font4 = QFont()
        font4.setFamilies([u"Ubuntu"])
        font4.setPointSize(16)
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"color: rgb(10, 20, 30);")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_27 = QLabel(self.frame_16)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(125, 60, 71, 16))
        self.label_27.setFont(font3)
        self.txt_patientid = QLineEdit(self.frame_16)
        self.txt_patientid.setObjectName(u"txt_patientid")
        self.txt_patientid.setGeometry(QRect(125, 80, 260, 30))
        self.txt_patientid.setFont(font3)
        self.txt_patientid.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_28 = QLabel(self.frame_16)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(125, 130, 191, 16))
        self.label_28.setFont(font3)
        self.txt_firstname = QLineEdit(self.frame_16)
        self.txt_firstname.setObjectName(u"txt_firstname")
        self.txt_firstname.setGeometry(QRect(125, 150, 125, 30))
        self.txt_firstname.setFont(font3)
        self.txt_firstname.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_29 = QLabel(self.frame_16)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(125, 200, 71, 16))
        self.label_29.setFont(font3)
        self.label_30 = QLabel(self.frame_16)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(125, 270, 71, 16))
        self.label_30.setFont(font3)
        self.txt_age = QLineEdit(self.frame_16)
        self.txt_age.setObjectName(u"txt_age")
        self.txt_age.setGeometry(QRect(125, 290, 260, 30))
        self.txt_age.setFont(font3)
        self.txt_age.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_31 = QLabel(self.frame_16)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(125, 340, 121, 16))
        self.label_31.setFont(font3)
        self.txt_mobile = QLineEdit(self.frame_16)
        self.txt_mobile.setObjectName(u"txt_mobile")
        self.txt_mobile.setGeometry(QRect(125, 360, 260, 30))
        self.txt_mobile.setFont(font3)
        self.txt_mobile.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_32 = QLabel(self.frame_16)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(125, 410, 71, 16))
        self.label_32.setFont(font3)
        self.cmb_doctor_patient = QComboBox(self.frame_16)
        self.cmb_doctor_patient.setObjectName(u"cmb_doctor_patient")
        self.cmb_doctor_patient.setGeometry(QRect(125, 430, 261, 30))
        self.cmb_doctor_patient.setFont(font3)
        self.cmb_doctor_patient.setStyleSheet(u"QComboBox\n"
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
        self.rbt_male = QRadioButton(self.frame_16)
        self.rbt_male.setObjectName(u"rbt_male")
        self.rbt_male.setGeometry(QRect(125, 220, 125, 31))
        self.rbt_male.setFont(font3)
        self.rbt_male.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.rbt_female = QRadioButton(self.frame_16)
        self.rbt_female.setObjectName(u"rbt_female")
        self.rbt_female.setGeometry(QRect(259, 220, 125, 31))
        self.rbt_female.setFont(font3)
        self.rbt_female.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.txt_lastname = QLineEdit(self.frame_16)
        self.txt_lastname.setObjectName(u"txt_lastname")
        self.txt_lastname.setGeometry(QRect(259, 150, 125, 30))
        self.txt_lastname.setFont(font3)
        self.txt_lastname.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.btn_patient_save = QPushButton(self.frame_16)
        self.btn_patient_save.setObjectName(u"btn_patient_save")
        self.btn_patient_save.setGeometry(QRect(125, 500, 260, 45))
        self.btn_patient_save.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;\n"
"font: 500 11pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_adddoctor = QPushButton(self.frame_16)
        self.btn_adddoctor.setObjectName(u"btn_adddoctor")
        self.btn_adddoctor.setGeometry(QRect(169, 408, 91, 20))
        self.btn_adddoctor.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(24, 177, 168);")
        icon6 = QIcon()
        icon6.addFile(u":/new/prefix_topheader/images/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_adddoctor.setIcon(icon6)
        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(15, 50, 111, 30))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.btn_back_patient = QPushButton(self.frame_9)
        self.btn_back_patient.setObjectName(u"btn_back_patient")
        self.btn_back_patient.setGeometry(QRect(32, 3, 75, 24))
        self.btn_back_patient.setFont(font3)
        self.btn_back_patient.setFlat(False)
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(4, 3, 24, 24))
        self.label_13.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 1px solid #18B1A8;")
        self.label_13.setPixmap(QPixmap(u":/new/prefix_stack/images/chevron-left.png"))
        self.label_13.setScaledContents(False)
        self.label_13.setMargin(2)
        self.stackedWidget.addWidget(self.patientpage)
        self.settingpage = QWidget()
        self.settingpage.setObjectName(u"settingpage")
        self.frame_15 = QFrame(self.settingpage)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 0, 1680, 990))
        self.frame_15.setStyleSheet(u"background-color: rgb(245, 246, 245);\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(494, 50, 691, 671))
        self.frame_19.setStyleSheet(u"background-color:#EBEEEC;\n"
"border-radius: 6px;\n"
"border: 1px solid #ffff;")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.stackedWidget_setting = QStackedWidget(self.frame_19)
        self.stackedWidget_setting.setObjectName(u"stackedWidget_setting")
        self.stackedWidget_setting.setGeometry(QRect(10, 60, 671, 611))
        self.stackedWidget_setting.setStyleSheet(u"background-color:#EBEEEC;\n"
"border-radius: 6px;\n"
"border: 1px solid #ffff;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_17 = QFrame(self.page)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setGeometry(QRect(10, -30, 650, 581))
        self.frame_17.setStyleSheet(u"background-color:#EBEEEC;\n"
"border-radius: 6px;\n"
"border: 1px solid #ffff;")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.label_34 = QLabel(self.frame_17)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(280, 140, 141, 16))
        self.label_34.setFont(font3)
        self.txt_hospitalName = QLineEdit(self.frame_17)
        self.txt_hospitalName.setObjectName(u"txt_hospitalName")
        self.txt_hospitalName.setGeometry(QRect(280, 160, 311, 30))
        self.txt_hospitalName.setFont(font3)
        self.txt_hospitalName.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_35 = QLabel(self.frame_17)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(280, 200, 191, 16))
        self.label_35.setFont(font3)
        self.txt_doctor_fname = QLineEdit(self.frame_17)
        self.txt_doctor_fname.setObjectName(u"txt_doctor_fname")
        self.txt_doctor_fname.setGeometry(QRect(280, 220, 150, 30))
        self.txt_doctor_fname.setFont(font3)
        self.txt_doctor_fname.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_36 = QLabel(self.frame_17)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(280, 80, 221, 16))
        self.label_36.setFont(font3)
        self.label_37 = QLabel(self.frame_17)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(280, 260, 71, 16))
        self.label_37.setFont(font3)
        self.txt_address1 = QLineEdit(self.frame_17)
        self.txt_address1.setObjectName(u"txt_address1")
        self.txt_address1.setGeometry(QRect(280, 280, 150, 30))
        self.txt_address1.setFont(font3)
        self.txt_address1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_38 = QLabel(self.frame_17)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(280, 320, 121, 16))
        self.label_38.setFont(font3)
        self.txt_city = QLineEdit(self.frame_17)
        self.txt_city.setObjectName(u"txt_city")
        self.txt_city.setGeometry(QRect(280, 340, 150, 30))
        self.txt_city.setFont(font3)
        self.txt_city.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_39 = QLabel(self.frame_17)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(280, 380, 71, 16))
        self.label_39.setFont(font3)
        self.cmb_country = QComboBox(self.frame_17)
        self.cmb_country.addItem("")
        self.cmb_country.addItem("")
        self.cmb_country.addItem("")
        self.cmb_country.addItem("")
        self.cmb_country.setObjectName(u"cmb_country")
        self.cmb_country.setGeometry(QRect(280, 400, 150, 30))
        self.cmb_country.setFont(font3)
        self.cmb_country.setStyleSheet(u"QComboBox\n"
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
        self.radio_btn_header = QRadioButton(self.frame_17)
        self.radio_btn_header.setObjectName(u"radio_btn_header")
        self.radio_btn_header.setGeometry(QRect(280, 100, 150, 31))
        self.radio_btn_header.setFont(font3)
        self.radio_btn_header.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.radio_btn_Noheader = QRadioButton(self.frame_17)
        self.radio_btn_Noheader.setObjectName(u"radio_btn_Noheader")
        self.radio_btn_Noheader.setGeometry(QRect(440, 100, 150, 31))
        self.radio_btn_Noheader.setFont(font3)
        self.radio_btn_Noheader.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.txt_doctor_lname = QLineEdit(self.frame_17)
        self.txt_doctor_lname.setObjectName(u"txt_doctor_lname")
        self.txt_doctor_lname.setGeometry(QRect(440, 220, 150, 30))
        self.txt_doctor_lname.setFont(font3)
        self.txt_doctor_lname.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.btn_report_save = QPushButton(self.frame_17)
        self.btn_report_save.setObjectName(u"btn_report_save")
        self.btn_report_save.setGeometry(QRect(280, 500, 311, 45))
        self.btn_report_save.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;\n"
"font: 500 11pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.line_3 = QFrame(self.frame_17)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(230, 70, 2, 461))
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_3 = QLabel(self.frame_17)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 80, 111, 21))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ")
        self.label_33 = QLabel(self.frame_17)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(30, 110, 161, 171))
        self.label_33.setStyleSheet(u"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_33.setPixmap(QPixmap(u":/new/prefix_stack/images/cloud-upload_1.png"))
        self.label_33.setScaledContents(False)
        self.label_33.setAlignment(Qt.AlignCenter)
        self.btn_browser = QPushButton(self.frame_17)
        self.btn_browser.setObjectName(u"btn_browser")
        self.btn_browser.setGeometry(QRect(30, 290, 161, 30))
        font5 = QFont()
        font5.setFamilies([u"Ubuntu"])
        font5.setPointSize(9)
        self.btn_browser.setFont(font5)
        self.btn_browser.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(100, 107, 116);\n"
"border-radius: 6px;\n"
"border: 1px solid #30CFC6;")
        icon7 = QIcon()
        icon7.addFile(u":/new/prefix_stack/images/cloud-upload_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_browser.setIcon(icon7)
        self.btn_browser.setFlat(True)
        self.txt_address2 = QLineEdit(self.frame_17)
        self.txt_address2.setObjectName(u"txt_address2")
        self.txt_address2.setGeometry(QRect(440, 280, 150, 30))
        self.txt_address2.setFont(font3)
        self.txt_address2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_40 = QLabel(self.frame_17)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(440, 260, 71, 16))
        self.label_40.setFont(font3)
        self.txt_state = QLineEdit(self.frame_17)
        self.txt_state.setObjectName(u"txt_state")
        self.txt_state.setGeometry(QRect(440, 340, 150, 30))
        self.txt_state.setFont(font3)
        self.txt_state.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_41 = QLabel(self.frame_17)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(440, 320, 121, 16))
        self.label_41.setFont(font3)
        self.label_42 = QLabel(self.frame_17)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(440, 380, 121, 16))
        self.label_42.setFont(font3)
        self.txt_pincode = QLineEdit(self.frame_17)
        self.txt_pincode.setObjectName(u"txt_pincode")
        self.txt_pincode.setGeometry(QRect(440, 400, 150, 30))
        self.txt_pincode.setFont(font3)
        self.txt_pincode.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_43 = QLabel(self.frame_17)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(280, 440, 121, 16))
        self.label_43.setFont(font3)
        self.txt_emailid = QLineEdit(self.frame_17)
        self.txt_emailid.setObjectName(u"txt_emailid")
        self.txt_emailid.setGeometry(QRect(280, 460, 150, 30))
        self.txt_emailid.setFont(font3)
        self.txt_emailid.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.label_44 = QLabel(self.frame_17)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(440, 440, 121, 16))
        self.label_44.setFont(font3)
        self.txt_mobile_no = QLineEdit(self.frame_17)
        self.txt_mobile_no.setObjectName(u"txt_mobile_no")
        self.txt_mobile_no.setGeometry(QRect(440, 460, 150, 30))
        self.txt_mobile_no.setFont(font3)
        self.txt_mobile_no.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.stackedWidget_setting.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_45 = QLabel(self.page_2)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(50, 60, 161, 16))
        self.label_45.setFont(font3)
        self.label_46 = QLabel(self.page_2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(50, 110, 161, 16))
        self.label_46.setFont(font3)
        self.label_47 = QLabel(self.page_2)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(50, 160, 161, 16))
        self.label_47.setFont(font3)
        self.dateTimeEdit = QDateTimeEdit(self.page_2)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(220, 50, 301, 35))
        font6 = QFont()
        font6.setFamilies([u"Ubuntu"])
        font6.setPointSize(10)
        font6.setBold(False)
        self.dateTimeEdit.setFont(font6)
        self.dateTimeEdit.setStyleSheet(u"QDateTimeEdit \n"
"{\n"
"   color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"border: 1px solid #30CFC6;\n"
"\n"
"}\n"
"\n"
"\n"
"QDateTimeEdit::down-arrow\n"
"{\n"
"    image: url(:/new/prefix_stack/images/calendar 1.png);\n"
"    width: 16px;\n"
"    height: 16px;\n"
"\n"
"}\n"
"")
        self.dateTimeEdit.setFrame(True)
        self.dateTimeEdit.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit_2 = QDateTimeEdit(self.page_2)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setGeometry(QRect(220, 100, 301, 35))
        self.dateTimeEdit_2.setFont(font6)
        self.dateTimeEdit_2.setStyleSheet(u"QDateTimeEdit \n"
"{\n"
"   color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"border: 1px solid #30CFC6;\n"
"\n"
"}\n"
"")
        self.dateTimeEdit_2.setFrame(True)
        self.dateTimeEdit_2.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.radioButton_7 = QRadioButton(self.page_2)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(220, 150, 141, 31))
        self.radioButton_7.setFont(font3)
        self.radioButton_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.radioButton_8 = QRadioButton(self.page_2)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(379, 150, 141, 31))
        self.radioButton_8.setFont(font3)
        self.radioButton_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(55, 64, 71);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;")
        self.btn_set = QPushButton(self.page_2)
        self.btn_set.setObjectName(u"btn_set")
        self.btn_set.setGeometry(QRect(220, 200, 301, 45))
        self.btn_set.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;\n"
"font: 500 11pt \"Ubuntu\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.stackedWidget_setting.addWidget(self.page_2)
        self.frame_18 = QFrame(self.frame_19)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(180, 10, 321, 45))
        self.frame_18.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border: 1px solid rgb(200, 211, 204);\n"
"")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.btn_report_set = QPushButton(self.frame_18)
        self.btn_report_set.setObjectName(u"btn_report_set")
        self.btn_report_set.setGeometry(QRect(5, 5, 150, 35))
        self.btn_report_set.setFont(font3)
        self.btn_report_set.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: #30CFC6;\n"
"border-radius: 12px;\n"
"border: 4px solid #30CFC6;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_report_set.setCheckable(True)
        self.btn_report_set.setFlat(True)
        self.btn_dtime_set = QPushButton(self.frame_18)
        self.btn_dtime_set.setObjectName(u"btn_dtime_set")
        self.btn_dtime_set.setGeometry(QRect(165, 5, 150, 35))
        self.btn_dtime_set.setFont(font3)
        self.btn_dtime_set.setStyleSheet(u"background-color: #30CFC6;\n"
"border-radius: 12px;\n"
"border: 4px solid #30CFC6;")
        self.btn_dtime_set.setCheckable(True)
        self.btn_dtime_set.setFlat(True)
        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(15, 50, 111, 30))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.btn_back_setting = QPushButton(self.frame_21)
        self.btn_back_setting.setObjectName(u"btn_back_setting")
        self.btn_back_setting.setGeometry(QRect(32, 3, 75, 24))
        self.btn_back_setting.setFont(font3)
        self.btn_back_setting.setFlat(False)
        self.label_61 = QLabel(self.frame_21)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(4, 3, 24, 24))
        self.label_61.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 1px solid #18B1A8;")
        self.label_61.setPixmap(QPixmap(u":/new/prefix_stack/images/chevron-left.png"))
        self.label_61.setScaledContents(False)
        self.label_61.setMargin(2)
        self.stackedWidget.addWidget(self.settingpage)
        self.doctorpage = QWidget()
        self.doctorpage.setObjectName(u"doctorpage")
        self.tableWidget_2 = QTableWidget(self.doctorpage)
        if (self.tableWidget_2.columnCount() < 7):
            self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(0, 0, 1280, 749))
        self.tableWidget_2.setStyleSheet(u"/*-----QTableView-----*/\n"
"QTableView, \n"
"QHeaderView, \n"
"QTableView::item \n"
"{\n"
"	background-color: #FFF;\n"
"	color: #000;\n"
"	border: 1px solid #C8D3CC;\n"
"   \n"
"   \n"
"}\n"
"\n"
"QTableView::item:selected \n"
"{ \n"
"    background-color: #C8D3CC;\n"
"    color: #000;\n"
"\n"
"}\n"
"\n"
"QHeaderView::section:horizontal \n"
"{\n"
"    background-color: #EBEEEC;\n"
"	border: 0px solid #37384d;\n"
"	padding: 2px;\n"
" \n"
"}\n"
"\n"
"QTableView::indicator{\n"
"	background-color: #212121;\n"
"	border: 1px solid #37384d;\n"
"\n"
"}\n"
"\n"
"QTableView::indicator:checked{\n"
"	image:url(\"./ressources/check.png\"); /*To replace*/\n"
"	background-color: #212121;\n"
"\n"
"}")
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget_2.setGridStyle(Qt.NoPen)
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(182)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.frame_10 = QFrame(self.doctorpage)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(0, 0, 1680, 990))
        self.frame_10.setStyleSheet(u"background-color: rgb(245, 246, 245);\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.lbl_doctor_count = QLabel(self.frame_10)
        self.lbl_doctor_count.setObjectName(u"lbl_doctor_count")
        self.lbl_doctor_count.setGeometry(QRect(20, 10, 111, 16))
        self.lbl_doctor_count.setFont(font2)
        self.lbl_doctor_count.setStyleSheet(u"color: rgb(10, 20, 30);")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(20, 30, 252, 35))
        self.frame_11.setStyleSheet(u"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #C8D3CC;")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setLineWidth(1)
        self.txt_searchbox_doctor = QLineEdit(self.frame_11)
        self.txt_searchbox_doctor.setObjectName(u"txt_searchbox_doctor")
        self.txt_searchbox_doctor.setGeometry(QRect(7, 2, 211, 30))
        self.txt_searchbox_doctor.setFont(font3)
        self.txt_searchbox_doctor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 0px solid #C8D3CC;\n"
"\n"
"")
        self.btn_searchbox_doctor = QPushButton(self.frame_11)
        self.btn_searchbox_doctor.setObjectName(u"btn_searchbox_doctor")
        self.btn_searchbox_doctor.setGeometry(QRect(219, 2, 30, 30))
        self.btn_searchbox_doctor.setStyleSheet(u"border-radius: 6px;\n"
"font: 500 13pt \"Ubuntu\";\n"
"background: #18B1A8;\n"
"color: rgb(255, 255, 255);\n"
"")
        icon8 = QIcon()
        icon8.addFile(u":/new/prefix_topheader/images/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_searchbox_doctor.setIcon(icon8)
        self.btn_newdoctor = QPushButton(self.frame_10)
        self.btn_newdoctor.setObjectName(u"btn_newdoctor")
        self.btn_newdoctor.setGeometry(QRect(1290, 20, 142, 45))
        self.btn_newdoctor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;\n"
"font: 500 11pt \"Ubuntu\";\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/new/prefix_topheader/image/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_newdoctor.setIcon(icon9)
        self.btn_newdoctor.setIconSize(QSize(24, 24))
        self.btn_refresh_doctor = QPushButton(self.frame_10)
        self.btn_refresh_doctor.setObjectName(u"btn_refresh_doctor")
        self.btn_refresh_doctor.setGeometry(QRect(278, 31, 32, 32))
        self.btn_refresh_doctor.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;\n"
"font: 500 11pt \"Ubuntu\";\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/new/prefix_topheader/images/refresh-cw.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_refresh_doctor.setIcon(icon10)
        self.btn_refresh_doctor.setIconSize(QSize(14, 14))
        self.btn_refresh_doctor.setFlat(False)
        self.tableWidget_3 = QTableWidget(self.frame_10)
        if (self.tableWidget_3.columnCount() < 2):
            self.tableWidget_3.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(20, 90, 1634, 900))
        self.tableWidget_3.setStyleSheet(u"\n"
"/*-----QTableView-----*/\n"
"QTableView:item\n"
"{\n"
"	background-color: rgb(245, 246, 245);\n"
"	color: #000;\n"
"	border: 0px solid #C8D3CC;\n"
"   \n"
"   \n"
"}\n"
"QTableView::item:alternate \n"
"{\n"
"background-color: rgb(235, 238, 236);\n"
"}\n"
"QTableView::item:selected \n"
"{ \n"
"    background-color: #C8D3CC;\n"
"    color: #000;\n"
"background-color: #18B1A8;\n"
"}\n"
"QTableView::item:focus{\n"
"    border: 1px solid rgb(242, 128, 133);\n"
"    \n"
"}\n"
"QHeaderView::section:horizontal \n"
"{\n"
"    background-color: #EBEEEC;\n"
"	border: 0px solid #37384d;\n"
"	padding: 2px;\n"
"   font-weight:200;\n"
"}\n"
"\n"
"QTableView::indicator{\n"
"	background-color: #212121;\n"
"	border: 0px solid #37384d;\n"
"\n"
"}\n"
"\n"
"QTableView::indicator:checked{\n"
"	image:url(\"./ressources/check.png\"); /*To replace*/\n"
"	background-color: #212121;\n"
"}\n"
"")
        self.tableWidget_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setAlternatingRowColors(True)
        self.tableWidget_3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget_3.setGridStyle(Qt.NoPen)
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(182)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(1450, 26, 111, 30))
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.btn_back_doctor = QPushButton(self.frame_12)
        self.btn_back_doctor.setObjectName(u"btn_back_doctor")
        self.btn_back_doctor.setGeometry(QRect(32, 3, 75, 24))
        self.btn_back_doctor.setFont(font3)
        self.btn_back_doctor.setFlat(False)
        self.label_16 = QLabel(self.frame_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(4, 3, 24, 24))
        self.label_16.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 1px solid #18B1A8;")
        self.label_16.setPixmap(QPixmap(u":/new/prefix_stack/images/chevron-left.png"))
        self.label_16.setScaledContents(False)
        self.label_16.setMargin(2)
        self.stackedWidget.addWidget(self.doctorpage)
        self.mainpage = QWidget()
        self.mainpage.setObjectName(u"mainpage")
        self.frame_4 = QFrame(self.mainpage)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 0, 1380, 990))
        self.frame_4.setStyleSheet(u"background-color: rgb(245, 246, 245);\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.lbl_patient_count = QLabel(self.frame_4)
        self.lbl_patient_count.setObjectName(u"lbl_patient_count")
        self.lbl_patient_count.setGeometry(QRect(20, 10, 111, 16))
        self.lbl_patient_count.setFont(font2)
        self.lbl_patient_count.setStyleSheet(u"color: rgb(10, 20, 30);")
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(20, 30, 252, 35))
        self.frame_6.setStyleSheet(u"border-radius: 6px;\n"
"background-color: rgb(255, 255, 255);\n"
"border: 1px solid #C8D3CC;")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setLineWidth(1)
        self.txt_searchbox = QLineEdit(self.frame_6)
        self.txt_searchbox.setObjectName(u"txt_searchbox")
        self.txt_searchbox.setGeometry(QRect(10, 2, 211, 30))
        self.txt_searchbox.setFont(font3)
        self.txt_searchbox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 0px solid #C8D3CC;\n"
"\n"
"")
        self.btn_searchbox = QPushButton(self.frame_6)
        self.btn_searchbox.setObjectName(u"btn_searchbox")
        self.btn_searchbox.setGeometry(QRect(220, 2, 30, 30))
        self.btn_searchbox.setStyleSheet(u"border-radius: 6px;\n"
"font: 500 13pt \"Ubuntu\";\n"
"background: #18B1A8;\n"
"color: rgb(255, 255, 255);\n"
"")
        self.btn_searchbox.setIcon(icon8)
        self.btn_newpatient = QPushButton(self.frame_4)
        self.btn_newpatient.setObjectName(u"btn_newpatient")
        self.btn_newpatient.setGeometry(QRect(1067, 20, 142, 45))
        self.btn_newpatient.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;\n"
"font: 500 11pt \"Ubuntu\";\n"
"")
        self.btn_newpatient.setIcon(icon6)
        self.btn_newpatient.setIconSize(QSize(24, 24))
        self.btn_live = QPushButton(self.frame_4)
        self.btn_live.setObjectName(u"btn_live")
        self.btn_live.setGeometry(QRect(1223, 20, 142, 45))
        font7 = QFont()
        font7.setFamilies([u"Ubuntu"])
        font7.setPointSize(13)
        font7.setBold(False)
        font7.setItalic(False)
        self.btn_live.setFont(font7)
        self.btn_live.setAutoFillBackground(False)
        self.btn_live.setStyleSheet(u"border-radius: 6px;\n"
"font: 500 13pt \"Ubuntu\";\n"
"background: #18B1A8;\n"
"color: rgb(255, 255, 255);\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/new/prefix_topheader/images/live.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_live.setIcon(icon11)
        self.btn_live.setIconSize(QSize(20, 20))
        self.btn_live.setFlat(False)
        self.btn_refresh = QPushButton(self.frame_4)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(276, 31, 32, 32))
        self.btn_refresh.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 6px;\n"
"border: 1px solid #18B1A8;\n"
"font: 500 11pt \"Ubuntu\";\n"
"")
        self.btn_refresh.setIcon(icon10)
        self.btn_refresh.setIconSize(QSize(14, 14))
        self.btn_refresh.setFlat(False)
        self.tableWidget = QTableWidget(self.mainpage)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem9)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 80, 1359, 909))
        font8 = QFont()
        font8.setPointSize(11)
        self.tableWidget.setFont(font8)
        self.tableWidget.setStyleSheet(u"\n"
"/*-----QTableView-----*/\n"
"QTableView:item\n"
"{\n"
"	background-color: rgb(245, 246, 245);\n"
"	color: #000;\n"
"	border: 0px solid #C8D3CC;\n"
"   \n"
"   \n"
"}\n"
"QTableView::item:alternate \n"
"{\n"
"background-color: rgb(235, 238, 236);\n"
"}\n"
"QTableView::item:selected \n"
"{ \n"
"    background-color: #C8D3CC;\n"
"    color: #000;\n"
"background-color: #18B1A8;\n"
"}\n"
"QTableView::item:focus{\n"
"    border: 1px solid rgb(242, 128, 133);\n"
"    \n"
"}\n"
"QHeaderView::section:horizontal \n"
"{\n"
"    background-color: #EBEEEC;\n"
"	border: 0px solid #37384d;\n"
"	padding: 2px;\n"
"   font-weight:200;\n"
"}\n"
"\n"
"QTableView::indicator{\n"
"	background-color: #212121;\n"
"	border: 0px solid #37384d;\n"
"\n"
"}\n"
"\n"
"QTableView::indicator:checked{\n"
"	image:url(\"./ressources/check.png\"); /*To replace*/\n"
"	background-color: #212121;\n"
"}\n"
"")
        self.tableWidget.setLineWidth(0)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setTextElideMode(Qt.ElideMiddle)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setGridStyle(Qt.NoPen)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(182)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.patient_detail_frame = QFrame(self.mainpage)
        self.patient_detail_frame.setObjectName(u"patient_detail_frame")
        self.patient_detail_frame.setGeometry(QRect(1380, 0, 300, 990))
        font9 = QFont()
        font9.setFamilies([u"Ubuntu"])
        font9.setPointSize(12)
        self.patient_detail_frame.setFont(font9)
        self.patient_detail_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 0px;")
        self.patient_detail_frame.setFrameShape(QFrame.NoFrame)
        self.frame_20 = QFrame(self.patient_detail_frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(9, 15, 284, 90))
        self.frame_20.setStyleSheet(u"background-color:#F5F6F5;\n"
"border-radius: 6px;\n"
"border: 1px solid #C8D3CC;")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.label_48 = QLabel(self.frame_20)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(10, 20, 38, 38))
        self.label_48.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.label_48.setPixmap(QPixmap(u":/new/prefix_stack/images/user_.png"))
        self.label_48.setScaledContents(True)
        self.label_49 = QLabel(self.frame_20)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(50, 7, 71, 16))
        self.label_49.setFont(font5)
        self.label_49.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_patient_delete = QPushButton(self.frame_20)
        self.btn_patient_delete.setObjectName(u"btn_patient_delete")
        self.btn_patient_delete.setGeometry(QRect(250, 6, 20, 20))
        self.btn_patient_delete.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        icon12 = QIcon()
        icon12.addFile(u":/new/prefix_stack/images/delete_2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_patient_delete.setIcon(icon12)
        self.btn_patient_delete.setIconSize(QSize(20, 20))
        self.btn_patient_edit = QPushButton(self.frame_20)
        self.btn_patient_edit.setObjectName(u"btn_patient_edit")
        self.btn_patient_edit.setGeometry(QRect(220, 6, 20, 20))
        self.btn_patient_edit.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        icon13 = QIcon()
        icon13.addFile(u":/new/prefix_stack/images/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_patient_edit.setIcon(icon13)
        self.btn_patient_edit.setIconSize(QSize(20, 20))
        self.label_50 = QLabel(self.frame_20)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(115, 5, 101, 20))
        self.label_50.setFont(font3)
        self.label_50.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.label_51 = QLabel(self.frame_20)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(50, 32, 227, 31))
        font10 = QFont()
        font10.setFamilies([u"Ubuntu"])
        font10.setPointSize(14)
        self.label_51.setFont(font10)
        self.label_51.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.label_52 = QLabel(self.frame_20)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(50, 68, 91, 16))
        self.label_52.setFont(font5)
        self.label_52.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.label_53 = QLabel(self.frame_20)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(134, 68, 61, 16))
        self.label_53.setFont(font5)
        self.label_53.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_capture = QPushButton(self.patient_detail_frame)
        self.btn_capture.setObjectName(u"btn_capture")
        self.btn_capture.setGeometry(QRect(9, 120, 80, 80))
        self.btn_capture.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(241, 245, 251, 255),stop:1 rgba(204, 214, 227, 255) );\n"
"border: 1px solid #18B1A8;\n"
"border-radius: 6px;\n"
"")
        icon14 = QIcon()
        icon14.addFile(u":/new/prefix_stack/images/capture.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_capture.setIcon(icon14)
        self.btn_capture.setIconSize(QSize(24, 24))
        self.btn_capture.setFlat(True)
        self.btn_compare = QPushButton(self.patient_detail_frame)
        self.btn_compare.setObjectName(u"btn_compare")
        self.btn_compare.setGeometry(QRect(110, 120, 80, 80))
        self.btn_compare.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(241, 245, 251, 255),stop:1 rgba(204, 214, 227, 255) );\n"
"border: 1px solid #18B1A8;\n"
"border-radius: 6px;\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/new/prefix_stack/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_compare.setIcon(icon15)
        self.btn_compare.setIconSize(QSize(24, 24))
        self.btn_report = QPushButton(self.patient_detail_frame)
        self.btn_report.setObjectName(u"btn_report")
        self.btn_report.setGeometry(QRect(212, 120, 80, 80))
        self.btn_report.setStyleSheet(u"background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:0, stop:0 rgba(241, 245, 251, 255),stop:1 rgba(204, 214, 227, 255) );\n"
"border: 1px solid #18B1A8;\n"
"border-radius: 6px;\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/new/prefix_stack/images/report_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_report.setIcon(icon16)
        self.btn_report.setIconSize(QSize(24, 24))
        self.label_54 = QLabel(self.patient_detail_frame)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(11, 175, 75, 21))
        self.label_54.setFont(font2)
        self.label_54.setStyleSheet(u"background-color:  transparent;")
        self.label_54.setAlignment(Qt.AlignCenter)
        self.label_55 = QLabel(self.patient_detail_frame)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(113, 175, 75, 21))
        self.label_55.setFont(font2)
        self.label_55.setStyleSheet(u"background-color:transparent;")
        self.label_55.setAlignment(Qt.AlignCenter)
        self.label_56 = QLabel(self.patient_detail_frame)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(214, 175, 76, 21))
        font11 = QFont()
        font11.setFamilies([u"Ubuntu"])
        font11.setPointSize(11)
        font11.setBold(False)
        self.label_56.setFont(font11)
        self.label_56.setStyleSheet(u"background-color:transparent;")
        self.label_56.setAlignment(Qt.AlignCenter)
        self.lbl_visit_show = QLabel(self.patient_detail_frame)
        self.lbl_visit_show.setObjectName(u"lbl_visit_show")
        self.lbl_visit_show.setGeometry(QRect(10, 220, 41, 21))
        self.lbl_visit_show.setFont(font2)
        self.lbl_visit_show.setStyleSheet(u"color: rgb(55, 64, 71);")
        self.line_4 = QFrame(self.patient_detail_frame)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 250, 280, 2))
        self.line_4.setStyleSheet(u"background-color: rgb(200, 211, 204);")
        self.line_4.setFrameShape(QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_5 = QFrame(self.patient_detail_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(10, 260, 281, 61))
        self.frame_5.setStyleSheet(u"background-color: rgb(227, 246, 245);\n"
"border-radius: 6px;\n"
"border: 1px solid #30CFC6;")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.label_58 = QLabel(self.frame_5)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setGeometry(QRect(5, 11, 61, 20))
        self.label_58.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.label_59 = QLabel(self.frame_5)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setGeometry(QRect(60, 10, 41, 21))
        self.label_59.setFont(font3)
        self.label_59.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.line_5 = QFrame(self.frame_5)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(100, 10, 2, 20))
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_60 = QLabel(self.frame_5)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(110, 10, 131, 20))
        self.label_60.setFont(font3)
        self.label_60.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.label_68 = QLabel(self.frame_5)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setGeometry(QRect(5, 37, 41, 16))
        self.label_68.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.label_69 = QLabel(self.frame_5)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(50, 37, 51, 16))
        self.label_69.setFont(font3)
        self.label_69.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.line_8 = QFrame(self.frame_5)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(100, 30, 2, 20))
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.label_75 = QLabel(self.frame_5)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setGeometry(QRect(110, 37, 31, 16))
        self.label_75.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.label_76 = QLabel(self.frame_5)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setGeometry(QRect(140, 35, 121, 20))
        self.label_76.setFont(font3)
        self.label_76.setStyleSheet(u"border-color: transparent;\n"
"border-radius: 0px;")
        self.listView = QListView(self.patient_detail_frame)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 330, 281, 491))
        self.listView.setStyleSheet(u"border-radius: 6px;\n"
"border: 1px solid #30CFC6;")
        self.lbl_visit_count = QLabel(self.patient_detail_frame)
        self.lbl_visit_count.setObjectName(u"lbl_visit_count")
        self.lbl_visit_count.setGeometry(QRect(54, 220, 61, 21))
        self.lbl_visit_count.setFont(font2)
        self.lbl_visit_count.setStyleSheet(u"color: rgb(55, 64, 71);")
        self.btn_visit_next = QPushButton(self.patient_detail_frame)
        self.btn_visit_next.setObjectName(u"btn_visit_next")
        self.btn_visit_next.setGeometry(QRect(255, 220, 24, 24))
        self.btn_visit_next.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 2px solid rgb(24, 177, 168);")
        icon17 = QIcon()
        icon17.addFile(u":/new/prefix_stack/images/chevron-right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_visit_next.setIcon(icon17)
        self.btn_visit_back = QPushButton(self.patient_detail_frame)
        self.btn_visit_back.setObjectName(u"btn_visit_back")
        self.btn_visit_back.setGeometry(QRect(223, 220, 24, 24))
        self.btn_visit_back.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 2px solid rgb(24, 177, 168);")
        icon18 = QIcon()
        icon18.addFile(u":/new/prefix_stack/images/chevron-left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_visit_back.setIcon(icon18)
        self.stackedWidget.addWidget(self.mainpage)
        self.reportpdf = QWidget()
        self.reportpdf.setObjectName(u"reportpdf")
        self.frame_36 = QFrame(self.reportpdf)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(12, 50, 111, 30))
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_36)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(4, 3, 24, 24))
        self.label_4.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 1px solid #18B1A8;")
        self.label_4.setPixmap(QPixmap(u":/new/prefix_stack/images/chevron-left.png"))
        self.label_4.setMargin(2)
        self.btn_back_report = QPushButton(self.frame_36)
        self.btn_back_report.setObjectName(u"btn_back_report")
        self.btn_back_report.setGeometry(QRect(32, 3, 75, 24))
        font12 = QFont()
        font12.setPointSize(10)
        self.btn_back_report.setFont(font12)
        self.widget = QWidget(self.reportpdf)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(450, 50, 840, 920))
        self.label_5 = QLabel(self.reportpdf)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(770, 10, 141, 20))
        self.stackedWidget.addWidget(self.reportpdf)
        self.stackedWidget_2.addWidget(self.main_widget)
        self.mplayer_widget = QWidget()
        self.mplayer_widget.setObjectName(u"mplayer_widget")
        self.mplayer_widget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.mediaframe = QFrame(self.mplayer_widget)
        self.mediaframe.setObjectName(u"mediaframe")
        self.mediaframe.setGeometry(QRect(0, 0, 1680, 981))
        self.mediaframe.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.mediaframe.setFrameShape(QFrame.StyledPanel)
        self.mediaframe.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.mediaframe)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1681, 981))
        self.medialayout = QVBoxLayout(self.verticalLayoutWidget)
        self.medialayout.setObjectName(u"medialayout")
        self.medialayout.setContentsMargins(0, 0, 0, 0)
        self.frame_34 = QFrame(self.mplayer_widget)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(795, 1000, 141, 43))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.btn_mplay = QPushButton(self.frame_34)
        self.btn_mplay.setObjectName(u"btn_mplay")
        self.btn_mplay.setGeometry(QRect(0, 4, 40, 37))
        icon19 = QIcon()
        iconThemeName = u"media-playback-start"
        if QIcon.hasThemeIcon(iconThemeName):
            icon19 = QIcon.fromTheme(iconThemeName)
        else:
            icon19.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.btn_mplay.setIcon(icon19)
        self.btn_mplay.setIconSize(QSize(28, 28))
        self.btn_mstop = QPushButton(self.frame_34)
        self.btn_mstop.setObjectName(u"btn_mstop")
        self.btn_mstop.setGeometry(QRect(50, 4, 40, 37))
        icon20 = QIcon()
        iconThemeName = u"media-playback-pause"
        if QIcon.hasThemeIcon(iconThemeName):
            icon20 = QIcon.fromTheme(iconThemeName)
        else:
            icon20.addFile(u".", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        self.btn_mstop.setIcon(icon20)
        self.btn_mstop.setIconSize(QSize(28, 28))
        self.btn_mclose = QPushButton(self.frame_34)
        self.btn_mclose.setObjectName(u"btn_mclose")
        self.btn_mclose.setGeometry(QRect(100, 4, 40, 37))
        icon21 = QIcon()
        icon21.addFile(u":/new/prefix_stack/images/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_mclose.setIcon(icon21)
        self.btn_mclose.setIconSize(QSize(28, 28))
        self.lbl_status_mplayer = QLabel(self.mplayer_widget)
        self.lbl_status_mplayer.setObjectName(u"lbl_status_mplayer")
        self.lbl_status_mplayer.setGeometry(QRect(790, 980, 141, 18))
        self.lbl_status_mplayer.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_status_mplayer.setAlignment(Qt.AlignCenter)
        self.stackedWidget_2.addWidget(self.mplayer_widget)
        self.splash_widget = QWidget()
        self.splash_widget.setObjectName(u"splash_widget")
        self.label_65 = QLabel(self.splash_widget)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setGeometry(QRect(660, 420, 372, 98))
        self.label_65.setPixmap(QPixmap(u":/new/prefix_topheader/images/logo_with_text_splash.png"))
        self.label_65.setScaledContents(True)
        self.progressBar = QProgressBar(self.splash_widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(660, 550, 371, 15))
        self.progressBar.setStyleSheet(u"QProgressBar\n"
"{\n"
"	border: 1px solid #fffff;\n"
"     text-align: center;\n"
"	border-radius: 5px;\n"
"	color: #374047;\n"
"	font-weight: bold;	\n"
"	background-color: rgb(227, 216, 217);\n"
"    \n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #30CFC6;\n"
"	border-radius: 5px;\n"
"    margin: 0.5px;\n"
"\n"
"}\n"
"\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)
        self.lbl_status = QLabel(self.splash_widget)
        self.lbl_status.setObjectName(u"lbl_status")
        self.lbl_status.setGeometry(QRect(660, 590, 371, 31))
        font13 = QFont()
        font13.setFamilies([u"Ubuntu"])
        font13.setPointSize(16)
        font13.setBold(False)
        self.lbl_status.setFont(font13)
        self.lbl_status.setAlignment(Qt.AlignCenter)
        self.stackedWidget_2.addWidget(self.splash_widget)
        self.compare_widget = QWidget()
        self.compare_widget.setObjectName(u"compare_widget")
        self.frame_22 = QFrame(self.compare_widget)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(0, 0, 1680, 60))
        self.frame_22.setStyleSheet(u"background-color: rgb(10, 20, 30);")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.btn_back_compare = QPushButton(self.frame_22)
        self.btn_back_compare.setObjectName(u"btn_back_compare")
        self.btn_back_compare.setGeometry(QRect(18, 18, 24, 24))
        self.btn_back_compare.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 2px solid rgb(24, 177, 168);")
        self.btn_back_compare.setIcon(icon18)
        self.lbl_compare_pid = QLabel(self.frame_22)
        self.lbl_compare_pid.setObjectName(u"lbl_compare_pid")
        self.lbl_compare_pid.setGeometry(QRect(63, 10, 181, 16))
        self.lbl_compare_pid.setStyleSheet(u"color: rgb(245, 246, 245);\n"
"font: 500 11pt \"Ubuntu\";")
        self.lbl_compare_pname = QLabel(self.frame_22)
        self.lbl_compare_pname.setObjectName(u"lbl_compare_pname")
        self.lbl_compare_pname.setGeometry(QRect(63, 30, 181, 25))
        font14 = QFont()
        font14.setFamilies([u"Ubuntu"])
        font14.setPointSize(15)
        font14.setBold(False)
        font14.setItalic(False)
        self.lbl_compare_pname.setFont(font14)
        self.lbl_compare_pname.setStyleSheet(u"color: rgb(245, 246, 245);\n"
"font: 500 15pt \"Ubuntu\";")
        self.label_66 = QLabel(self.frame_22)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(738, 15, 121, 31))
        font15 = QFont()
        font15.setFamilies([u"Ubuntu"])
        font15.setPointSize(16)
        font15.setBold(False)
        font15.setItalic(False)
        self.label_66.setFont(font15)
        self.label_66.setStyleSheet(u"font: 500 16pt \"Ubuntu\";\n"
"color: rgb(200, 211, 204);")
        self.label_64 = QLabel(self.frame_22)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setGeometry(QRect(1472, 15, 117, 28))
        self.label_64.setPixmap(QPixmap(u":/new/prefix_topheader/image/logo_with_text.png"))
        self.frame_23 = QFrame(self.compare_widget)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(0, 60, 1680, 990))
        self.frame_23.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.line_6 = QFrame(self.frame_23)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(840, 0, 3, 1050))
        self.line_6.setStyleSheet(u"background-color: rgb(132, 137, 143);")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(0, 890, 839, 100))
        self.frame_24.setStyleSheet(u"background-color: rgb(100, 107, 116);")
        self.frame_24.setFrameShape(QFrame.NoFrame)
        self.btn_visit_back_left = QPushButton(self.frame_24)
        self.btn_visit_back_left.setObjectName(u"btn_visit_back_left")
        self.btn_visit_back_left.setGeometry(QRect(5, 38, 24, 24))
        self.btn_visit_back_left.setStyleSheet(u"background-color: #374047;\n"
"border-radius: 12px;\n"
"border: 2px solid #646B74;")
        self.btn_visit_back_left.setIcon(icon18)
        self.btn_visit_next_left = QPushButton(self.frame_24)
        self.btn_visit_next_left.setObjectName(u"btn_visit_next_left")
        self.btn_visit_next_left.setEnabled(True)
        self.btn_visit_next_left.setGeometry(QRect(809, 38, 24, 24))
        self.btn_visit_next_left.setStyleSheet(u"background-color: #374047;\n"
"border-radius: 12px;\n"
"border: 2px solid #646B74;")
        self.btn_visit_next_left.setIcon(icon17)
        self.left_thumbnail_list = QListWidget(self.frame_24)
        self.left_thumbnail_list.setObjectName(u"left_thumbnail_list")
        self.left_thumbnail_list.setGeometry(QRect(30, 10, 778, 90))
        self.left_thumbnail_list.setFlow(QListView.LeftToRight)
        self.left_thumbnail_list.setSpacing(5)
        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setGeometry(QRect(844, 890, 836, 100))
        self.frame_25.setStyleSheet(u"background-color: rgb(100, 107, 116);")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.btn_visit_next_right = QPushButton(self.frame_25)
        self.btn_visit_next_right.setObjectName(u"btn_visit_next_right")
        self.btn_visit_next_right.setGeometry(QRect(804, 38, 24, 24))
        self.btn_visit_next_right.setStyleSheet(u"background-color: #374047;\n"
"border-radius: 12px;\n"
"border: 2px solid #646B74;")
        self.btn_visit_next_right.setIcon(icon17)
        self.btn_visit_back_right = QPushButton(self.frame_25)
        self.btn_visit_back_right.setObjectName(u"btn_visit_back_right")
        self.btn_visit_back_right.setGeometry(QRect(10, 38, 24, 24))
        self.btn_visit_back_right.setStyleSheet(u"background-color: #374047;\n"
"border-radius: 12px;\n"
"border: 2px solid #646B74;")
        self.btn_visit_back_right.setIcon(icon18)
        self.right_thumbnail_list = QListWidget(self.frame_25)
        self.right_thumbnail_list.setObjectName(u"right_thumbnail_list")
        self.right_thumbnail_list.setGeometry(QRect(34, 10, 769, 90))
        self.cmb_left_vid = QComboBox(self.frame_23)
        self.cmb_left_vid.setObjectName(u"cmb_left_vid")
        self.cmb_left_vid.setGeometry(QRect(10, 10, 100, 28))
        self.cmb_left_vid.setFont(font3)
        self.cmb_left_vid.setStyleSheet(u"background-color: rgb(55, 64, 71);\n"
"color: rgb(255, 255, 255);")
        self.frame_26 = QFrame(self.frame_23)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(690, 10, 140, 31))
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.btn_compare_left_zoomout = QPushButton(self.frame_26)
        self.btn_compare_left_zoomout.setObjectName(u"btn_compare_left_zoomout")
        self.btn_compare_left_zoomout.setGeometry(QRect(10, 0, 26, 26))
        self.btn_compare_left_zoomout.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        icon22 = QIcon()
        icon22.addFile(u":/new/prefix_stack/images/zoom_out.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_compare_left_zoomout.setIcon(icon22)
        self.btn_compare_left_zoomout.setIconSize(QSize(20, 20))
        self.btn_compare_left_zoomin = QPushButton(self.frame_26)
        self.btn_compare_left_zoomin.setObjectName(u"btn_compare_left_zoomin")
        self.btn_compare_left_zoomin.setGeometry(QRect(40, 0, 26, 26))
        self.btn_compare_left_zoomin.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        icon23 = QIcon()
        icon23.addFile(u":/new/prefix_stack/images/zoom_in.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_compare_left_zoomin.setIcon(icon23)
        self.btn_compare_left_zoomin.setIconSize(QSize(20, 20))
        self.btn_compare_fit = QPushButton(self.frame_26)
        self.btn_compare_fit.setObjectName(u"btn_compare_fit")
        self.btn_compare_fit.setGeometry(QRect(75, 0, 26, 26))
        self.btn_compare_fit.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        icon24 = QIcon()
        icon24.addFile(u":/new/prefix_stack/images/zoom_to_fit_3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_compare_fit.setIcon(icon24)
        self.btn_compare_fit.setIconSize(QSize(24, 24))
        self.btn_compare_single_wnd_left = QPushButton(self.frame_26)
        self.btn_compare_single_wnd_left.setObjectName(u"btn_compare_single_wnd_left")
        self.btn_compare_single_wnd_left.setGeometry(QRect(105, 0, 26, 26))
        self.btn_compare_single_wnd_left.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        icon25 = QIcon()
        icon25.addFile(u":/new/prefix_stack/images/full_screen.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_compare_single_wnd_left.setIcon(icon25)
        self.btn_compare_single_wnd_left.setIconSize(QSize(24, 24))
        self.cmb_right_vid = QComboBox(self.frame_23)
        self.cmb_right_vid.setObjectName(u"cmb_right_vid")
        self.cmb_right_vid.setGeometry(QRect(860, 10, 100, 28))
        self.cmb_right_vid.setFont(font3)
        self.cmb_right_vid.setStyleSheet(u"background-color: rgb(55, 64, 71);\n"
"color: rgb(255, 255, 255);")
        self.frame_29 = QFrame(self.frame_23)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(1530, 10, 140, 31))
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.btn_compare_right_zoomout = QPushButton(self.frame_29)
        self.btn_compare_right_zoomout.setObjectName(u"btn_compare_right_zoomout")
        self.btn_compare_right_zoomout.setGeometry(QRect(10, 0, 26, 26))
        self.btn_compare_right_zoomout.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_compare_right_zoomout.setIcon(icon22)
        self.btn_compare_right_zoomout.setIconSize(QSize(20, 20))
        self.btn_compare_right_zoomin = QPushButton(self.frame_29)
        self.btn_compare_right_zoomin.setObjectName(u"btn_compare_right_zoomin")
        self.btn_compare_right_zoomin.setGeometry(QRect(40, 0, 26, 26))
        self.btn_compare_right_zoomin.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_compare_right_zoomin.setIcon(icon23)
        self.btn_compare_right_zoomin.setIconSize(QSize(20, 20))
        self.btn_compare_fit_2 = QPushButton(self.frame_29)
        self.btn_compare_fit_2.setObjectName(u"btn_compare_fit_2")
        self.btn_compare_fit_2.setGeometry(QRect(75, 0, 26, 26))
        self.btn_compare_fit_2.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_compare_fit_2.setIcon(icon24)
        self.btn_compare_fit_2.setIconSize(QSize(24, 24))
        self.btn_compare_single_wnd_right = QPushButton(self.frame_29)
        self.btn_compare_single_wnd_right.setObjectName(u"btn_compare_single_wnd_right")
        self.btn_compare_single_wnd_right.setGeometry(QRect(105, 0, 26, 26))
        self.btn_compare_single_wnd_right.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_compare_single_wnd_right.setIcon(icon25)
        self.btn_compare_single_wnd_right.setIconSize(QSize(24, 24))
        self.lbl_compare_left_image = QGraphicsView(self.frame_23)
        self.lbl_compare_left_image.setObjectName(u"lbl_compare_left_image")
        self.lbl_compare_left_image.setGeometry(QRect(18, 50, 801, 821))
        self.lbl_compare_right_image = QGraphicsView(self.frame_23)
        self.lbl_compare_right_image.setObjectName(u"lbl_compare_right_image")
        self.lbl_compare_right_image.setGeometry(QRect(860, 50, 801, 821))
        self.stackedWidget_2.addWidget(self.compare_widget)
        self.preview_widget = QWidget()
        self.preview_widget.setObjectName(u"preview_widget")
        self.frame_27 = QFrame(self.preview_widget)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(0, 0, 1680, 60))
        self.frame_27.setStyleSheet(u"background-color: rgb(10, 20, 30);")
        self.frame_27.setFrameShape(QFrame.NoFrame)
        self.btn_back_scn_preview = QPushButton(self.frame_27)
        self.btn_back_scn_preview.setObjectName(u"btn_back_scn_preview")
        self.btn_back_scn_preview.setGeometry(QRect(18, 18, 24, 24))
        self.btn_back_scn_preview.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 2px solid rgb(24, 177, 168);")
        self.btn_back_scn_preview.setIcon(icon18)
        self.lbl_pre_pid = QLabel(self.frame_27)
        self.lbl_pre_pid.setObjectName(u"lbl_pre_pid")
        self.lbl_pre_pid.setGeometry(QRect(63, 10, 181, 16))
        self.lbl_pre_pid.setStyleSheet(u"color: rgb(245, 246, 245);\n"
"font: 500 11pt \"Ubuntu\";")
        self.lbl_pre_pname = QLabel(self.frame_27)
        self.lbl_pre_pname.setObjectName(u"lbl_pre_pname")
        self.lbl_pre_pname.setGeometry(QRect(63, 30, 181, 25))
        self.lbl_pre_pname.setFont(font14)
        self.lbl_pre_pname.setStyleSheet(u"color: rgb(245, 246, 245);\n"
"font: 500 15pt \"Ubuntu\";")
        self.line_7 = QFrame(self.frame_27)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(250, 5, 1, 51))
        self.line_7.setStyleSheet(u"background-color: rgb(100, 107, 116);")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.lbl_pre_vid = QLabel(self.frame_27)
        self.lbl_pre_vid.setObjectName(u"lbl_pre_vid")
        self.lbl_pre_vid.setGeometry(QRect(260, 10, 200, 16))
        self.lbl_pre_vid.setStyleSheet(u"color: rgb(245, 246, 245);\n"
"font: 500 11pt \"Ubuntu\";")
        self.lbl_pre_visitdate = QLabel(self.frame_27)
        self.lbl_pre_visitdate.setObjectName(u"lbl_pre_visitdate")
        self.lbl_pre_visitdate.setGeometry(QRect(260, 35, 251, 16))
        self.lbl_pre_visitdate.setStyleSheet(u"color: rgb(245, 246, 245);\n"
"font: 500 11pt \"Ubuntu\";")
        self.lbl_pre_img_name = QLabel(self.frame_27)
        self.lbl_pre_img_name.setObjectName(u"lbl_pre_img_name")
        self.lbl_pre_img_name.setGeometry(QRect(738, 15, 81, 31))
        self.lbl_pre_img_name.setFont(font15)
        self.lbl_pre_img_name.setStyleSheet(u"font: 500 16pt \"Ubuntu\";\n"
"color: rgb(200, 211, 204);")
        self.label_86 = QLabel(self.frame_27)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(1472, 15, 117, 28))
        self.label_86.setPixmap(QPixmap(u":/new/prefix_topheader/image/logo_with_text.png"))
        self.frame_28 = QFrame(self.preview_widget)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(0, 60, 1680, 860))
        self.frame_28.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.lbl_pre_img = QGraphicsView(self.frame_28)
        self.lbl_pre_img.setObjectName(u"lbl_pre_img")
        self.lbl_pre_img.setGeometry(QRect(40, 2, 1600, 827))
        self.frame_30 = QFrame(self.preview_widget)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setGeometry(QRect(0, 920, 1680, 100))
        self.frame_30.setStyleSheet(u"background-color: rgb(100, 107, 116);")
        self.frame_30.setFrameShape(QFrame.NoFrame)
        self.btn_visit_next_5 = QPushButton(self.frame_30)
        self.btn_visit_next_5.setObjectName(u"btn_visit_next_5")
        self.btn_visit_next_5.setGeometry(QRect(1648, 38, 24, 24))
        self.btn_visit_next_5.setStyleSheet(u"background-color: #374047;\n"
"border-radius: 12px;\n"
"border: 2px solid #646B74;")
        self.btn_visit_next_5.setIcon(icon17)
        self.btn_visit_back_5 = QPushButton(self.frame_30)
        self.btn_visit_back_5.setObjectName(u"btn_visit_back_5")
        self.btn_visit_back_5.setGeometry(QRect(0, 38, 24, 24))
        self.btn_visit_back_5.setStyleSheet(u"background-color: #374047;\n"
"border-radius: 12px;\n"
"border: 2px solid #646B74;")
        self.btn_visit_back_5.setIcon(icon18)
        self.pre_list = QListWidget(self.frame_30)
        self.pre_list.setObjectName(u"pre_list")
        self.pre_list.setGeometry(QRect(26, 6, 1614, 90))
        self.frame_31 = QFrame(self.preview_widget)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(0, 1020, 1680, 30))
        self.frame_31.setStyleSheet(u"background-color: rgb(10, 20, 30);")
        self.frame_31.setFrameShape(QFrame.NoFrame)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(1504, 2, 181, 26))
        self.frame_32.setFrameShape(QFrame.NoFrame)
        self.btn_preview_zoomout = QPushButton(self.frame_32)
        self.btn_preview_zoomout.setObjectName(u"btn_preview_zoomout")
        self.btn_preview_zoomout.setGeometry(QRect(96, 0, 26, 26))
        self.btn_preview_zoomout.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_preview_zoomout.setIcon(icon22)
        self.btn_preview_zoomout.setIconSize(QSize(20, 20))
        self.btn_preview_zoomin = QPushButton(self.frame_32)
        self.btn_preview_zoomin.setObjectName(u"btn_preview_zoomin")
        self.btn_preview_zoomin.setGeometry(QRect(56, 0, 26, 26))
        self.btn_preview_zoomin.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_preview_zoomin.setIcon(icon23)
        self.btn_preview_zoomin.setIconSize(QSize(20, 20))
        self.btn_previewscn_fit = QPushButton(self.frame_32)
        self.btn_previewscn_fit.setObjectName(u"btn_previewscn_fit")
        self.btn_previewscn_fit.setGeometry(QRect(140, 0, 26, 26))
        self.btn_previewscn_fit.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_previewscn_fit.setIcon(icon24)
        self.btn_previewscn_fit.setIconSize(QSize(24, 24))
        self.stackedWidget_2.addWidget(self.preview_widget)
        self.compare_full_widget = QWidget()
        self.compare_full_widget.setObjectName(u"compare_full_widget")
        self.frame_33 = QFrame(self.compare_full_widget)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(0, 0, 1680, 1050))
        self.frame_33.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_33.setFrameShape(QFrame.NoFrame)
        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(0, 949, 1680, 100))
        self.frame_35.setStyleSheet(u"background-color: rgb(100, 107, 116);")
        self.frame_35.setFrameShape(QFrame.NoFrame)
        self.btn_visit_next_single_img = QPushButton(self.frame_35)
        self.btn_visit_next_single_img.setObjectName(u"btn_visit_next_single_img")
        self.btn_visit_next_single_img.setGeometry(QRect(1648, 40, 24, 24))
        self.btn_visit_next_single_img.setStyleSheet(u"background-color: #374047;\n"
"border-radius: 12px;\n"
"border: 2px solid #646B74;")
        self.btn_visit_next_single_img.setIcon(icon17)
        self.btn_visit_back_single_img = QPushButton(self.frame_35)
        self.btn_visit_back_single_img.setObjectName(u"btn_visit_back_single_img")
        self.btn_visit_back_single_img.setGeometry(QRect(0, 38, 24, 24))
        self.btn_visit_back_single_img.setStyleSheet(u"background-color: #374047;\n"
"border-radius: 12px;\n"
"border: 2px solid #646B74;")
        self.btn_visit_back_single_img.setIcon(icon18)
        self.cmp_single_img_list = QListWidget(self.frame_35)
        self.cmp_single_img_list.setObjectName(u"cmp_single_img_list")
        self.cmp_single_img_list.setGeometry(QRect(25, 10, 1614, 82))
        self.cmb_single_window = QComboBox(self.frame_33)
        self.cmb_single_window.setObjectName(u"cmb_single_window")
        self.cmb_single_window.setGeometry(QRect(0, 10, 100, 28))
        self.cmb_single_window.setFont(font3)
        self.cmb_single_window.setStyleSheet(u"background-color: rgb(55, 64, 71);\n"
"color: rgb(255, 255, 255);")
        self.frame_37 = QFrame(self.frame_33)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(1530, 10, 140, 31))
        self.frame_37.setFrameShape(QFrame.NoFrame)
        self.btn_compare_zoomout_single_wnd = QPushButton(self.frame_37)
        self.btn_compare_zoomout_single_wnd.setObjectName(u"btn_compare_zoomout_single_wnd")
        self.btn_compare_zoomout_single_wnd.setGeometry(QRect(10, 0, 26, 26))
        self.btn_compare_zoomout_single_wnd.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_compare_zoomout_single_wnd.setIcon(icon22)
        self.btn_compare_zoomout_single_wnd.setIconSize(QSize(20, 20))
        self.btn_compare_zoomin_single_wnd = QPushButton(self.frame_37)
        self.btn_compare_zoomin_single_wnd.setObjectName(u"btn_compare_zoomin_single_wnd")
        self.btn_compare_zoomin_single_wnd.setGeometry(QRect(40, 0, 26, 26))
        self.btn_compare_zoomin_single_wnd.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_compare_zoomin_single_wnd.setIcon(icon23)
        self.btn_compare_zoomin_single_wnd.setIconSize(QSize(20, 20))
        self.btn_compare_fit_ = QPushButton(self.frame_37)
        self.btn_compare_fit_.setObjectName(u"btn_compare_fit_")
        self.btn_compare_fit_.setGeometry(QRect(73, 0, 26, 26))
        self.btn_compare_fit_.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        self.btn_compare_fit_.setIcon(icon24)
        self.btn_compare_fit_.setIconSize(QSize(24, 24))
        self.btn_compare_full__back_single_wnd = QPushButton(self.frame_37)
        self.btn_compare_full__back_single_wnd.setObjectName(u"btn_compare_full__back_single_wnd")
        self.btn_compare_full__back_single_wnd.setGeometry(QRect(105, 0, 26, 26))
        self.btn_compare_full__back_single_wnd.setStyleSheet(u"background-color: transparent;\n"
"border-color: transparent;\n"
"border-radius: 0px;")
        icon26 = QIcon()
        icon26.addFile(u":/new/prefix_stack/images/fullscreen_exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_compare_full__back_single_wnd.setIcon(icon26)
        self.btn_compare_full__back_single_wnd.setIconSize(QSize(24, 24))
        self.lbl_com_img_single_wnd = QGraphicsView(self.frame_33)
        self.lbl_com_img_single_wnd.setObjectName(u"lbl_com_img_single_wnd")
        self.lbl_com_img_single_wnd.setGeometry(QRect(7, 50, 1651, 871))
        self.stackedWidget_2.addWidget(self.compare_full_widget)
        self.captuer_widget = QWidget()
        self.captuer_widget.setObjectName(u"captuer_widget")
        self.frame_13 = QFrame(self.captuer_widget)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(0, 0, 1680, 1050))
        self.frame_13.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(0, 0, 1679, 60))
        self.frame_14.setStyleSheet(u"background-color: rgb(10, 20, 30);")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.btn_back_captuer = QPushButton(self.frame_14)
        self.btn_back_captuer.setObjectName(u"btn_back_captuer")
        self.btn_back_captuer.setGeometry(QRect(18, 18, 24, 24))
        self.btn_back_captuer.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 2px solid rgb(24, 177, 168);")
        self.btn_back_captuer.setIcon(icon18)
        self.lbl_capture_pid = QLabel(self.frame_14)
        self.lbl_capture_pid.setObjectName(u"lbl_capture_pid")
        self.lbl_capture_pid.setGeometry(QRect(63, 10, 181, 16))
        self.lbl_capture_pid.setStyleSheet(u"color: rgb(245, 246, 245);\n"
"font: 500 11pt \"Ubuntu\";")
        self.lbl_capture_pname = QLabel(self.frame_14)
        self.lbl_capture_pname.setObjectName(u"lbl_capture_pname")
        self.lbl_capture_pname.setGeometry(QRect(63, 30, 181, 25))
        self.lbl_capture_pname.setFont(font14)
        self.lbl_capture_pname.setStyleSheet(u"color: rgb(245, 246, 245);\n"
"font: 500 15pt \"Ubuntu\";")
        self.line = QFrame(self.frame_14)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(250, 5, 1, 51))
        self.line.setStyleSheet(u"background-color: rgb(100, 107, 116);")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.lbl_capture_visitid = QLabel(self.frame_14)
        self.lbl_capture_visitid.setObjectName(u"lbl_capture_visitid")
        self.lbl_capture_visitid.setGeometry(QRect(260, 10, 200, 16))
        self.lbl_capture_visitid.setStyleSheet(u"color: rgb(245, 246, 245);\n"
"font: 500 11pt \"Ubuntu\";")
        self.label_20 = QLabel(self.frame_14)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(260, 35, 251, 16))
        self.label_20.setStyleSheet(u"color: rgb(245, 246, 245);\n"
"font: 500 11pt \"Ubuntu\";")
        self.lbl_scanpage_title = QLabel(self.frame_14)
        self.lbl_scanpage_title.setObjectName(u"lbl_scanpage_title")
        self.lbl_scanpage_title.setGeometry(QRect(738, 15, 81, 31))
        self.lbl_scanpage_title.setFont(font15)
        self.lbl_scanpage_title.setStyleSheet(u"font: 500 16pt \"Ubuntu\";\n"
"color: rgb(200, 211, 204);")
        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(1402, 20, 61, 16))
        self.label_22.setStyleSheet(u"color: rgb(200, 211, 204);\n"
"font: 400 10pt \"Ubuntu\";")
        self.label_23 = QLabel(self.frame_14)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(1467, 20, 61, 16))
        self.label_23.setStyleSheet(u"color: rgb(200, 211, 204);\n"
"font: 500 11pt \"Ubuntu\";")
        self.line_2 = QFrame(self.frame_14)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1534, 5, 1, 51))
        self.line_2.setStyleSheet(u"background-color: rgb(100, 107, 116);")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.lbl_rec = QLabel(self.frame_14)
        self.lbl_rec.setObjectName(u"lbl_rec")
        self.lbl_rec.setGeometry(QRect(1560, 20, 91, 16))
        self.lbl_rec.setStyleSheet(u"color: rgb(200, 211, 204);\n"
"font: 400 10pt \"Ubuntu\";")
        self.label_25 = QLabel(self.frame_14)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(1541, 22, 14, 14))
        self.label_25.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 5px;\n"
"border: 1px solid red;")
        self.lbl_preview_image = QLabel(self.frame_13)
        self.lbl_preview_image.setObjectName(u"lbl_preview_image")
        self.lbl_preview_image.setGeometry(QRect(200, 60, 1200, 1000))
        self.lbl_preview_image.setScaledContents(True)
        self.frame_buttons = QFrame(self.frame_13)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setGeometry(QRect(0, 80, 0, 265))
        self.frame_buttons.setStyleSheet(u"background-color: transparent;")
        self.frame_buttons.setFrameShape(QFrame.NoFrame)
        self.btn_setting_2 = QPushButton(self.frame_buttons)
        self.btn_setting_2.setObjectName(u"btn_setting_2")
        self.btn_setting_2.setGeometry(QRect(0, 210, 50, 50))
        icon27 = QIcon()
        icon27.addFile(u":/new/prefix_topheader/images/settings_ 2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_setting_2.setIcon(icon27)
        self.btn_setting_2.setIconSize(QSize(24, 24))
        self.btn_record = QPushButton(self.frame_buttons)
        self.btn_record.setObjectName(u"btn_record")
        self.btn_record.setGeometry(QRect(0, 110, 50, 50))
        icon28 = QIcon()
        icon28.addFile(u":/new/prefix_stack/images/record_off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_record.setIcon(icon28)
        self.btn_record.setIconSize(QSize(24, 24))
        self.btn_odos = QPushButton(self.frame_buttons)
        self.btn_odos.setObjectName(u"btn_odos")
        self.btn_odos.setGeometry(QRect(0, 160, 50, 50))
        self.btn_odos.setFont(font9)
        self.btn_odos.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.btn_start_cam = QPushButton(self.frame_buttons)
        self.btn_start_cam.setObjectName(u"btn_start_cam")
        self.btn_start_cam.setGeometry(QRect(0, 10, 50, 50))
        self.btn_start_cam.setStyleSheet(u"")
        icon29 = QIcon()
        icon29.addFile(u":/new/prefix_stack/images/camera_on.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_start_cam.setIcon(icon29)
        self.btn_start_cam.setIconSize(QSize(24, 24))
        self.btn_start_cam.setFlat(False)
        self.snap_btn = QPushButton(self.frame_buttons)
        self.snap_btn.setObjectName(u"snap_btn")
        self.snap_btn.setGeometry(QRect(0, 60, 50, 50))
        icon30 = QIcon()
        icon30.addFile(u":/new/prefix_stack/images/camera.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.snap_btn.setIcon(icon30)
        self.snap_btn.setIconSize(QSize(24, 24))
        self.frame_image_list = QFrame(self.frame_13)
        self.frame_image_list.setObjectName(u"frame_image_list")
        self.frame_image_list.setGeometry(QRect(1649, 59, 282, 990))
        self.frame_image_list.setStyleSheet(u"background-color: rgb(55, 64, 71);")
        self.frame_image_list.setFrameShape(QFrame.NoFrame)
        self.btn_slider = QPushButton(self.frame_image_list)
        self.btn_slider.setObjectName(u"btn_slider")
        self.btn_slider.setGeometry(QRect(2, 400, 24, 24))
        self.btn_slider.setLayoutDirection(Qt.LeftToRight)
        self.btn_slider.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 2px solid rgb(24, 177, 168);")
        self.btn_slider.setIcon(icon18)
        self.btn_slider_2 = QPushButton(self.frame_image_list)
        self.btn_slider_2.setObjectName(u"btn_slider_2")
        self.btn_slider_2.setGeometry(QRect(2, 400, 24, 24))
        self.btn_slider_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_slider_2.setStyleSheet(u"background-color: rgb(24, 177, 168);\n"
"border-radius: 12px;\n"
"border: 2px solid rgb(24, 177, 168);")
        self.btn_slider_2.setIcon(icon17)
        self.lv_capture_image = QListView(self.frame_image_list)
        self.lv_capture_image.setObjectName(u"lv_capture_image")
        self.lv_capture_image.setGeometry(QRect(30, 0, 250, 990))
        self.stackedWidget_2.addWidget(self.captuer_widget)
        self.report_widget = QWidget()
        self.report_widget.setObjectName(u"report_widget")
        self.stackedWidget_2.addWidget(self.report_widget)
        dash_screen.setCentralWidget(self.centralwidget)

        self.retranslateUi(dash_screen)

        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_setting.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dash_screen)
    # setupUi

    def retranslateUi(self, dash_screen):
        dash_screen.setWindowTitle(QCoreApplication.translate("dash_screen", u"splashscreen", None))
        self.label.setText("")
        self.label_2.setText("")
        self.lbl_datetime.setText(QCoreApplication.translate("dash_screen", u"14-04-2025  05:33 PM", None))
        self.btn_patients.setText(QCoreApplication.translate("dash_screen", u"Patients", None))
        self.btn_doctor.setText(QCoreApplication.translate("dash_screen", u"Doctors", None))
        self.btn_settings.setText(QCoreApplication.translate("dash_screen", u"Settings", None))
        self.btn_aboutus.setText(QCoreApplication.translate("dash_screen", u"About Us", None))
        self.btn_shutdown.setText(QCoreApplication.translate("dash_screen", u"Shutdown", None))
        self.label_6.setText(QCoreApplication.translate("dash_screen", u"Add Patient", None))
        self.lbl_patient.setText(QCoreApplication.translate("dash_screen", u"Patient ID", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Patient Id", None))
        self.lbl_patientfname.setText(QCoreApplication.translate("dash_screen", u"Patient Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("dash_screen", u"First Name", None))
        self.lbl_gender.setText(QCoreApplication.translate("dash_screen", u"Gender", None))
        self.lbl_age.setText(QCoreApplication.translate("dash_screen", u"Age", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Patient Age", None))
        self.lbl_mobile.setText(QCoreApplication.translate("dash_screen", u"Mobile Number", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Patient Id", None))
        self.lbl_doctor.setText(QCoreApplication.translate("dash_screen", u"Doctor", None))
        self.radioButton.setText(QCoreApplication.translate("dash_screen", u"Male", None))
        self.radioButton_2.setText(QCoreApplication.translate("dash_screen", u"Female", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Last Name", None))
        self.pushButton.setText(QCoreApplication.translate("dash_screen", u"Submit", None))
        self.btn_newdoctor_patient.setText(QCoreApplication.translate("dash_screen", u"New Doctor", None))
        self.label_26.setText(QCoreApplication.translate("dash_screen", u"Add Patient", None))
        self.label_27.setText(QCoreApplication.translate("dash_screen", u"Patient ID*", None))
        self.txt_patientid.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Patient Id", None))
        self.label_28.setText(QCoreApplication.translate("dash_screen", u"Patient Name*", None))
        self.txt_firstname.setPlaceholderText(QCoreApplication.translate("dash_screen", u"First Name", None))
        self.label_29.setText(QCoreApplication.translate("dash_screen", u"Gender", None))
        self.label_30.setText(QCoreApplication.translate("dash_screen", u"Age", None))
        self.txt_age.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Patient Age", None))
        self.label_31.setText(QCoreApplication.translate("dash_screen", u"Mobile Number", None))
        self.txt_mobile.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Mobile No", None))
        self.label_32.setText(QCoreApplication.translate("dash_screen", u"Doctor", None))
        self.rbt_male.setText(QCoreApplication.translate("dash_screen", u"Male", None))
        self.rbt_female.setText(QCoreApplication.translate("dash_screen", u"Female", None))
        self.txt_lastname.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Last Name", None))
        self.btn_patient_save.setText(QCoreApplication.translate("dash_screen", u"Save", None))
        self.btn_adddoctor.setText(QCoreApplication.translate("dash_screen", u"New Doctor", None))
        self.btn_back_patient.setText(QCoreApplication.translate("dash_screen", u"Dashboard", None))
        self.label_13.setText("")
        self.label_34.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_34.setText(QCoreApplication.translate("dash_screen", u"Hospital Name", None))
        self.txt_hospitalName.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Hospital Name", None))
        self.label_35.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_35.setText(QCoreApplication.translate("dash_screen", u"Doctor Name", None))
        self.txt_doctor_fname.setPlaceholderText(QCoreApplication.translate("dash_screen", u"First Name", None))
        self.label_36.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_36.setText(QCoreApplication.translate("dash_screen", u"Report Type", None))
        self.label_37.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_37.setText(QCoreApplication.translate("dash_screen", u"Address 1", None))
        self.txt_address1.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Address 1", None))
        self.label_38.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_38.setText(QCoreApplication.translate("dash_screen", u"City", None))
        self.txt_city.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter City", None))
        self.label_39.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_39.setText(QCoreApplication.translate("dash_screen", u"Country", None))
        self.cmb_country.setItemText(0, QCoreApplication.translate("dash_screen", u"India", None))
        self.cmb_country.setItemText(1, QCoreApplication.translate("dash_screen", u"Europe", None))
        self.cmb_country.setItemText(2, QCoreApplication.translate("dash_screen", u"Africa", None))
        self.cmb_country.setItemText(3, QCoreApplication.translate("dash_screen", u"Indonesis", None))

        self.cmb_country.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Select Country", None))
        self.radio_btn_header.setText(QCoreApplication.translate("dash_screen", u"Header", None))
        self.radio_btn_Noheader.setText(QCoreApplication.translate("dash_screen", u"No Header", None))
        self.txt_doctor_lname.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Last Name", None))
        self.btn_report_save.setText(QCoreApplication.translate("dash_screen", u"Submit", None))
        self.label_3.setText(QCoreApplication.translate("dash_screen", u"Hospital Logo", None))
        self.label_33.setText("")
        self.btn_browser.setText(QCoreApplication.translate("dash_screen", u"Upload Image", None))
        self.txt_address2.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Address 2", None))
        self.label_40.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_40.setText(QCoreApplication.translate("dash_screen", u"Address 2", None))
        self.txt_state.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter State", None))
        self.label_41.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_41.setText(QCoreApplication.translate("dash_screen", u"State", None))
        self.label_42.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_42.setText(QCoreApplication.translate("dash_screen", u"Pincode", None))
        self.txt_pincode.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Pincode", None))
        self.label_43.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_43.setText(QCoreApplication.translate("dash_screen", u"Email id", None))
        self.txt_emailid.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter email id", None))
        self.label_44.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_44.setText(QCoreApplication.translate("dash_screen", u"Contact No", None))
        self.txt_mobile_no.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Contact Number", None))
        self.label_45.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_45.setText(QCoreApplication.translate("dash_screen", u"Set Date", None))
        self.label_46.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_46.setText(QCoreApplication.translate("dash_screen", u"Set Time", None))
        self.label_47.setStyleSheet(QCoreApplication.translate("dash_screen", u"background-color: transparent;\n"
"border-radius: 6px;\n"
"border: 0px solid ", None))
        self.label_47.setText(QCoreApplication.translate("dash_screen", u"Use 24-hour Format", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("dash_screen", u"dd-MM-yyyy", None))
        self.dateTimeEdit_2.setDisplayFormat(QCoreApplication.translate("dash_screen", u"HH:mm:ss", None))
        self.radioButton_7.setText(QCoreApplication.translate("dash_screen", u"12 Hrs", None))
        self.radioButton_8.setText(QCoreApplication.translate("dash_screen", u"24 hrs", None))
        self.btn_set.setText(QCoreApplication.translate("dash_screen", u"Set", None))
        self.btn_report_set.setText(QCoreApplication.translate("dash_screen", u"Report", None))
        self.btn_dtime_set.setText(QCoreApplication.translate("dash_screen", u"Date && Time", None))
        self.btn_back_setting.setText(QCoreApplication.translate("dash_screen", u"Dashboard", None))
        self.label_61.setText("")
        self.lbl_doctor_count.setText(QCoreApplication.translate("dash_screen", u"Doctor (000)", None))
        self.txt_searchbox_doctor.setText("")
        self.txt_searchbox_doctor.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter Name", None))
        self.btn_searchbox_doctor.setText("")
        self.btn_newdoctor.setText(QCoreApplication.translate("dash_screen", u"New Doctor", None))
        self.btn_refresh_doctor.setText("")
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("dash_screen", u"Doctor Name", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("dash_screen", u"Speciality", None));
        self.btn_back_doctor.setText(QCoreApplication.translate("dash_screen", u"Dashboard", None))
        self.label_16.setText("")
        self.lbl_patient_count.setText(QCoreApplication.translate("dash_screen", u"Patients (000)", None))
        self.txt_searchbox.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Enter PatientID", None))
        self.btn_searchbox.setText("")
        self.btn_newpatient.setText(QCoreApplication.translate("dash_screen", u"New Patient", None))
        self.btn_live.setText(QCoreApplication.translate("dash_screen", u"Live", None))
        self.btn_refresh.setText("")
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("dash_screen", u"Patient ID", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("dash_screen", u"Visitid", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("dash_screen", u"Patient Name", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("dash_screen", u"Age", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("dash_screen", u"Gender", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("dash_screen", u"Visit Date", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("dash_screen", u"Eye", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("dash_screen", u"Doctor", None));
        self.label_48.setText("")
        self.label_49.setText(QCoreApplication.translate("dash_screen", u"Patient id :", None))
        self.btn_patient_delete.setText("")
        self.btn_patient_edit.setText("")
        self.label_50.setText(QCoreApplication.translate("dash_screen", u"00000", None))
        self.label_51.setText(QCoreApplication.translate("dash_screen", u"Patient Name", None))
        self.label_52.setText(QCoreApplication.translate("dash_screen", u"000 Years old ,", None))
        self.label_53.setText(QCoreApplication.translate("dash_screen", u"Male", None))
        self.btn_capture.setText("")
        self.btn_compare.setText("")
        self.btn_report.setText("")
        self.label_54.setText(QCoreApplication.translate("dash_screen", u"Capture", None))
        self.label_55.setText(QCoreApplication.translate("dash_screen", u"Compare", None))
        self.label_56.setText(QCoreApplication.translate("dash_screen", u"Report", None))
        self.lbl_visit_show.setText(QCoreApplication.translate("dash_screen", u"Visits", None))
        self.label_58.setText(QCoreApplication.translate("dash_screen", u"Visit id:", None))
        self.label_59.setText(QCoreApplication.translate("dash_screen", u"0000", None))
        self.label_60.setText(QCoreApplication.translate("dash_screen", u"01-02-2026 01:01 AM", None))
        self.label_68.setText(QCoreApplication.translate("dash_screen", u"  Eye:", None))
        self.label_69.setText(QCoreApplication.translate("dash_screen", u"OD,OS", None))
        self.label_75.setText(QCoreApplication.translate("dash_screen", u"Dr.", None))
        self.label_76.setText(QCoreApplication.translate("dash_screen", u"Doctor Name", None))
        self.lbl_visit_count.setText(QCoreApplication.translate("dash_screen", u"(0/0)", None))
        self.btn_visit_next.setText("")
        self.btn_visit_back.setText("")
        self.label_4.setText("")
        self.btn_back_report.setText(QCoreApplication.translate("dash_screen", u"Dashboard", None))
        self.label_5.setText(QCoreApplication.translate("dash_screen", u"Report Document", None))
        self.btn_mplay.setText("")
        self.btn_mstop.setText("")
        self.btn_mclose.setText("")
        self.lbl_status_mplayer.setText(QCoreApplication.translate("dash_screen", u"NOT PLAY", None))
        self.label_65.setText("")
        self.lbl_status.setText("")
        self.btn_back_compare.setText("")
        self.lbl_compare_pid.setText(QCoreApplication.translate("dash_screen", u"Patient ID: 100386", None))
        self.lbl_compare_pname.setText(QCoreApplication.translate("dash_screen", u"Patient name", None))
        self.label_66.setText(QCoreApplication.translate("dash_screen", u"Compare", None))
        self.label_64.setText("")
        self.btn_visit_back_left.setText("")
        self.btn_visit_next_left.setText("")
        self.btn_visit_next_right.setText("")
        self.btn_visit_back_right.setText("")
        self.cmb_left_vid.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Select Visit", None))
        self.btn_compare_left_zoomout.setText("")
        self.btn_compare_left_zoomin.setText("")
        self.btn_compare_fit.setText("")
        self.btn_compare_single_wnd_left.setText("")
        self.cmb_right_vid.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Select Visit", None))
        self.btn_compare_right_zoomout.setText("")
        self.btn_compare_right_zoomin.setText("")
        self.btn_compare_fit_2.setText("")
        self.btn_compare_single_wnd_right.setText("")
        self.btn_back_scn_preview.setText("")
        self.lbl_pre_pid.setText(QCoreApplication.translate("dash_screen", u"Patient ID: 100386", None))
        self.lbl_pre_pname.setText(QCoreApplication.translate("dash_screen", u"Patient name", None))
        self.lbl_pre_vid.setText(QCoreApplication.translate("dash_screen", u"Visit ID        : 100386", None))
        self.lbl_pre_visitdate.setText(QCoreApplication.translate("dash_screen", u"Visited  On : 12-04-2025 10:30 AM", None))
        self.lbl_pre_img_name.setText(QCoreApplication.translate("dash_screen", u"OD1", None))
        self.label_86.setText("")
        self.btn_visit_next_5.setText("")
        self.btn_visit_back_5.setText("")
        self.btn_preview_zoomout.setText("")
        self.btn_preview_zoomin.setText("")
        self.btn_previewscn_fit.setText("")
        self.btn_visit_next_single_img.setText("")
        self.btn_visit_back_single_img.setText("")
        self.cmb_single_window.setPlaceholderText(QCoreApplication.translate("dash_screen", u"Select Visit", None))
        self.btn_compare_zoomout_single_wnd.setText("")
        self.btn_compare_zoomin_single_wnd.setText("")
        self.btn_compare_fit_.setText("")
        self.btn_compare_full__back_single_wnd.setText("")
        self.btn_back_captuer.setText("")
        self.lbl_capture_pid.setText(QCoreApplication.translate("dash_screen", u"Patient ID: 100386", None))
        self.lbl_capture_pname.setText(QCoreApplication.translate("dash_screen", u"Patient name", None))
        self.lbl_capture_visitid.setText(QCoreApplication.translate("dash_screen", u"Visit ID        : 100386", None))
        self.label_20.setText(QCoreApplication.translate("dash_screen", u"Visited  On : 12-04-2025 10:30 AM", None))
        self.lbl_scanpage_title.setText(QCoreApplication.translate("dash_screen", u"Capture", None))
        self.label_22.setText(QCoreApplication.translate("dash_screen", u"Status :", None))
        self.label_23.setText(QCoreApplication.translate("dash_screen", u"Off", None))
        self.lbl_rec.setText(QCoreApplication.translate("dash_screen", u"Recording Off", None))
        self.label_25.setText("")
        self.lbl_preview_image.setText("")
#if QT_CONFIG(tooltip)
        self.btn_setting_2.setToolTip(QCoreApplication.translate("dash_screen", u"Setting", None))
#endif // QT_CONFIG(tooltip)
        self.btn_setting_2.setText("")
#if QT_CONFIG(tooltip)
        self.btn_record.setToolTip(QCoreApplication.translate("dash_screen", u"Recording", None))
#endif // QT_CONFIG(tooltip)
        self.btn_record.setText("")
#if QT_CONFIG(tooltip)
        self.btn_odos.setToolTip(QCoreApplication.translate("dash_screen", u"Eye ", None))
#endif // QT_CONFIG(tooltip)
        self.btn_odos.setText(QCoreApplication.translate("dash_screen", u"OD", None))
#if QT_CONFIG(tooltip)
        self.btn_start_cam.setToolTip(QCoreApplication.translate("dash_screen", u"Start Camera", None))
#endif // QT_CONFIG(tooltip)
        self.btn_start_cam.setText("")
#if QT_CONFIG(tooltip)
        self.snap_btn.setToolTip(QCoreApplication.translate("dash_screen", u"Snap", None))
#endif // QT_CONFIG(tooltip)
        self.snap_btn.setText("")
        self.btn_slider.setText("")
        self.btn_slider_2.setText("")
    # retranslateUi

