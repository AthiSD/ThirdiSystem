# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtCore import Qt,QSharedMemory,QSystemSemaphore
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtGui import QPainter
from PySide6 import QtCore
from PySide6.QtCore import QSizeF
from PySide6.QtWidgets import QApplication, QSizePolicy, QMainWindow, QFileDialog, QScrollArea
from PySide6.QtCore import QRect,QPropertyAnimation,QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QAction
from PySide6.QtGui import QImage
from PySide6.QtGui import QMouseEvent,QMovie,QPixmap
import sqlite3
import os
import cv2
import time
import fitz
from PIL import Image
from PySide6.QtGui import QPixmap, QIcon, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QListView, QFrame
from PySide6.QtCore import QSize
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication,QMenuBar, QMenu, QMessageBox,QListWidget,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QListWidgetItem,QTableWidgetItem,QFileDialog,QGraphicsPixmapItem,QGraphicsScene
from ui_form import Ui_dash_screen
from msgdialogok import msgdialogok
from doctorclass import doctorclass
from datetime import datetime, date
from datetime import timedelta
from aboutclass import aboutclass
from licenceclass import licenceclass
from msgdialogyes import msgdialogyes
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
import re
import logging
import shutil
import subprocess
import shlex
import webbrowser
from PySide6.QtPdf import QPdfDocument
from PySide6.QtPdfWidgets import QPdfView

log_file = '/home/npdslitlamp/SLTAPPNEW/LOGS/main.log'
if not os.path.exists(log_file):
    # If the file doesn't exist, create it
    with open(log_file, 'w') as f:
        pass

# Configure logging
logging.basicConfig(
    filename='/home/npdslitlamp/SLTAPPNEW/LOGS/main.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'  # Overwrites the log file each time
)

class dash_screen(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_dash_screen()
        self.ui.setupUi(self)
        self.sw_2(2)
        self.pcount=0
        self.dynamic_list = []
        self._time_format=""
        self.read_os()       
        self.DTimer()
        self.eye_visitid=0
        self.HName=''
        self.HWstate=''
        self.folder=''
        self.tempfolder=''
        self.dbfile=''
        self.reportfolder=''
        self.Marker=''
        self.flip=-1
        self.rec=0
        self.count=0
        self.spl_load_config()
        self.load_config()
        self.check_db()
        self.ListPatient()
        self.flipimage1()
        self.ui.txt_searchbox.setText("")
        self.tuple_data = None
        self.getdateformate()
        self.DTimer1()
        self.loaddoctor()
        self.livestatus=0
        self.ODOS='OD'
        self.current_visit_index = 0
        self.all_visits = []
        self.edit_check=0
        self.current_eye = "OD"  # default starting value
        self.update_eye_button_text()
        self.dash_listview_model = QStandardItemModel()
        self.ui.listView.setModel(self.dash_listview_model)
        self.ui.btn_refresh.clicked.connect(self.refresh)
        self.ui.btn_searchbox.clicked.connect(self.SearchListPatient)
        # setting context menu policy on my table, "self.ui.tableWidgetGraph"
        self.ui.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.ui.listWidget.setContextMenuPolicy(Qt.CustomContextMengeneratelicenseu)
        self.ui.tableWidget.selectionModel().selectionChanged.connect(self.get_selected_rows)
        self.ui.tableWidget.customContextMenuRequested.connect(self.on_context_menu)
        self.ui.tableWidget_3.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableWidget_3.selectionModel().selectionChanged.connect(self.get_selected_rows_doctor)
        self.ui.tableWidget_3.customContextMenuRequested.connect(self.on_context_menu2)
        self.ui.listView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.listView.customContextMenuRequested.connect(self.on_context_menu_3)
        self.ui.btn_back_scn_preview.clicked.connect(self.back_preview)
        self.ui.btn_patients.clicked.connect(self.addpatient)
        self.ui.btn_patient_save.clicked.connect(self.save_patientdata)
        self.ui.btn_back_patient.clicked.connect(self.dashboard)
        self.ui.btn_visit_back.clicked.connect(self.on_btn_visit_back_clicked)
        self.ui.btn_visit_next.clicked.connect(self.on_btn_visit_next_clicked)
        self.ui.btn_back_captuer.clicked.connect(self.back)
        #self.ui.od_btn.clicked.connect(self.ODSet)
        #self.ui.os_btn.clicked.connect(self.OSSet)
        #self.ui.btn_back_captuer.clicked.connect(lambda:self.sw_2(0))
        self.ui.btn_back_doctor.clicked.connect(self.dashboard)
        self.ui.btn_back_setting.clicked.connect(self.dashboard)
        self.ui.btn_back_compare.clicked.connect(self.cmp_back)
        #main screen Doctor
        self.ui.btn_doctor.clicked.connect(self.doctorlist)
        self.ui.btn_newdoctor.clicked.connect(self.doctordialog)
        self.ui.btn_refresh_doctor.clicked.connect(self.doc_refresh)
        self.ui.btn_searchbox_doctor.clicked.connect(self.SearchListDoctor)
        self.ui.btn_newpatient.clicked.connect(self.addpatient)
        self.ui.btn_settings.clicked.connect(self.setting_wnd)
        #self.ui.btn_live.clicked.connect(lambda:self.sw_2(5))
        self.ui.btn_live.clicked.connect(self.live)
        self.ui.snap_btn.clicked.connect(self.snapshot)
        #self.ui.btn_odos.clicked.connect(self.ODSet)
        # Connect the single button to a toggle function
        self.ui.btn_odos.clicked.connect(self.toggle_eye)
        self.ui.btn_newdoctor_patient.clicked.connect(self.doctordialog)
        self.ui.btn_slider.clicked.connect(lambda:self.frameslideanimation(1652,1480,1680))
        self.ui.btn_slider_2.clicked.connect(lambda:self.frameslideanimation(1480,1652,1680))
        self.ui.btn_slider_2.hide()
        #report
        self.file_path = ""
        self.setup_logo()
        self.image_path ='/home/npdslitlamp/Pictures/3547-At/1009-06-12-2024 10-47-44'
        self.output_path = '/media/npdslitlamp/AUROSSD/Reports/'+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+'.pdf'
        self.ui.btn_report.clicked.connect(self.for_report)
        self.ui.btn_browser.clicked.connect(self.load_image)
        self.ui.btn_report_set.clicked.connect(lambda:self.setting_sw(0))
        self.ui.btn_report_save.clicked.connect(self.report_data)
        self.selected_report_type = ""
        self.ui.radio_btn_header.toggled.connect(self.update_report_type)
        self.ui.radio_btn_Noheader.toggled.connect(self.update_report_type)
        self.ui.btn_back_report.clicked.connect(self.dashboard1)
        self.ui.btn_set.clicked.connect(self.set_datetime)
        self.ui.btn_dtime_set.clicked.connect(self.setting_date_wnd)
        self.ui.btn_compare.clicked.connect(self.compare_srn)
        '''#compare left
        self.ui.btn_visit_back_left.clicked.connect(self.left_btn_visit_back_clicked_cmp)
        self.ui.btn_visit_next_left.clicked.connect(self.left_btn_visit_next_clicked_cmp)
        #compare right
        self.ui.btn_visit_back_right.clicked.connect(self.right_btn_visit_back_clicked_cmp)
        self.ui.btn_visit_next_right.clicked.connect(self.right_btn_visit_next_clicked_cmp)
        #single wnd screenself.getdateformate()
        self.ui.btn_visit_next_single_img.clicked.connect(self.single_btn_visit_next_clicked_cmp)
        self.ui.btn_visit_back_single_img.clicked.connect(self.single_btn_visit_back_clicked_cmp)
        #privew screen
        self.ui.btn_visit_next_5.clicked.connect(self.preview_btn_visit_next_clicked_cmp)
        self.ui.btn_visit_back_5.clicked.connect(self.preview_btn_visit_back_clicked_cmp)'''
        self.ui.btn_aboutus.clicked.connect(self.aboutus)
        #self.ui.btn_capture.clicked.connect(lambda:self.ssw_2w_2(5))
        self.ui.btn_capture.clicked.connect(self.capture)
        self.setup_recording_button()
        self.ui.btn_start_cam.clicked.connect(self.start)
        self.ui.btn_patient_edit.clicked.connect(self.patient_edit)
        #self.ui.btn_patient_delete.clicked.connect(self.dialogyes)
        self.ui.btn_patient_delete.clicked.connect(self.delete_patient)
        self.ui.btn_adddoctor.clicked.connect(self.doctordialog)
        #self.ui.btn_shutdown.clicked.connect(self.dialogyes)
        self.ui.btn_shutdown.clicked.connect(self.Exit)
        #compare single window
        self.ui.btn_compare_single_wnd_left.clicked.connect(lambda: self.single_wnd_cmp("left"))
        self.ui.btn_compare_single_wnd_right.clicked.connect(lambda: self.single_wnd_cmp("right"))
        self.ui.btn_compare_full__back_single_wnd.clicked.connect(lambda:self.sw_2(3))
        self.state=0
        self.setup_zoom_controls()
        self.ui.btn_visit_back_left.setVisible(False)
        self.ui.btn_visit_next_left.setVisible(False)
        self.ui.btn_visit_back_right.setVisible(False)
        self.ui.btn_visit_next_right.setVisible(False)
        self.ui.btn_visit_next_single_img.setVisible(False)
        self.ui.btn_visit_back_single_img.setVisible(False)
        self.ui.btn_visit_next_5.setVisible(False)
        self.ui.btn_visit_back_5.setVisible(False)

        self.ui.snap_btn.setEnabled(False)
        self.ui.btn_record.setEnabled(False)
        self.ui.btn_odos.setEnabled(False)
        # Define a stylesheetself.getdateformate()
        self.stylesheet_checked = """
        QPushButton
        {
            background-color: #30CFC6;generatelicense
            border-radius: 12px;
            border: 1px solid #30CFC6;
        }
        """
        self.stylesheet_unchecked = """
        QPushButton
        {
            background-color: white;
            border-radius: 12px;self.getdateformate()
            border: 0px solid #30CFC6;
        }
        """
        self.ui.btn_dtime_set.setStyleSheet(self.stylesheet_unchecked)
        self.ui.btn_report_set.setStyleSheet(self.stylesheet_checked)
        self.mplayer_create()
        self.ui.btn_mplay.clicked.connect(self.playMedia)
        self.ui.btn_mstop.clicked.connect(self.stopMedia)
        self.ui.btn_mclose.clicked.connect(self.closeMedia)

    def read_os(self):
        try:
            logging.info(f"Before_application|read_os|This method is called for reading the OS file")
            state=os.path.exists('/etc/os-release')
            if state == True:
                print("file is there OS-RELEASE")
                with open('/etc/os-release', 'r') as file:
                    for line in file:
                        if line.startswith("VERSION="):
                            v = line.strip().split("(", 1)[1].strip('"')
                            version= v.split(")", 1)[0]
                            print(version)
                        elif line.startswith("VERSION_CODENAME="):
                            codename = line.strip().split("=", 1)[1]
                            print(codename)
                if version != "Noble Numbat" or codename != "noble":
                    reply = QMessageBox.question(self, "Information", "UBuntu OS Version is Not Supported, Contact Support Team",
                                                 QMessageBox.Yes)
                    logging.warning(f"Before_application|read_os|Pop-up show,'Information', UBuntu OS is Not Support for Our Application!..")
                    if reply == QMessageBox.Yes:
                        os.system("echo '1' | sudo -S shutdown -h now")
            else:
                os.system("echo '1' | sudo -S shutdown -h now")
        except Exception as e:
            logging.error(f"Before_splashclass|read_os|Error in read_os:{e}")

    def DTimer(self): 
            try:
                self._mtimer = QTimer(self)
                self._mtimer.timeout.connect(self.timerlabel)
                self._mtimer.start(800)
            except Exception as e:
                logging.error(f"splashclass|timerlabel|Error in timerlabel:{e}")

    def timerlabel(self):
        try:
            self.pcount=self.pcount+5
            self.ui.progressBar.setValue(self.pcount)
            if self.pcount==20:
                self.ui.lbl_status.setText("Validating License")
                state=os.path.exists('/usr/local/sltlic/sltapp_lic.lic')
                if state == False:
                    self.pcount=0
                    self.ui.lbl_status.setText("License Not Activated")
            if self.pcount==25:
                board= licenceclass.getserial()
                #print('B:'+board)
                ethnet=licenceclass.getmac()
                #print('e:'+ethnet)
                data= licenceclass.generatelicense()
                if data == False:
                    self.pcount=0
            if self.pcount==40:
                self.ui.lbl_status.setText("Validating Storage Media")
                print('Validating Hardware')
                self.list_usb_ports1()
                print(self.HName)
                if self.HWstate ==0:
                    self.pcount=40
                else:
                    self.ui.lbl_status.setText('Storage Media Detected')

            if self.pcount ==65:
                self.ui.lbl_status.setText("Validating Camera")
                cmsts=cv2.VideoCapture(0)
                if cmsts.isOpened():
                     self.ui.lbl_status.setText("Camera Detected")
                     cmsts.release()
                else:
                     self.ui.lbl_status.setText("Camera not detected")
                     self.pcount=45
            if self.pcount==100:
                self._mtimer.stop()
                self.__setup()
                self.__initcamera()
                self.sw_2(0)
                self.sw(3)
        except Exception as e:
           print(f"splashclass|timerlabel|Error in timerlabel: {e}")

    def spl_load_config(self):
        try:
            with open('config.txt', 'r') as file:
                lines = file.readlines()
            # Print each line
            file.close()
            for line in lines:
                self.dynamic_list.append(line.strip())
            print(self.dynamic_list)
            paths = [folder.split('=')[1].strip("'") for folder in self.dynamic_list]
            # Printing the paths
            count=0
            for path in paths:
                  if count==5:
                    self.HName=path
                  count+=1
            logging.info(f"splashclass|load_config|Config(path patient,database,temp,Logo) are successfully add to theri location...")
        except OSError as e:
                     logging.error(f"splashclass|load_config|Error in config: {e}")

    #this method is used for setting the timer
    def DTimer1(self):
                try:
                    logging.info(f"mainscreen|DTimer|DTimer method is call...")
                    self._mtimer_1 = QTimer(self)
                    self._mtimer_1.timeout.connect(self.timerlabel1)
                    self._mtimer_1.start(1)
                except Exception as e:
                    logging.error(f"mainscreen|DTimer|Error in DTimer: {e}")

    #this method is used for set the time & time  in the label
    def getdateformate(self):
        if self._time_format is None:
            self.cursor = self.connection.cursor()
            query ="""SELECT * FROM tbl_Utitlity """
            self.cursor.execute(query)
            id = self.cursor.fetchall()
            print(id)
            data = id[0]
            self._time_format = data[5]
            print(self._time_format)

    def timerlabel1(self):
        try:
            # Only query database if we don't have the format cached
            if self._time_format == '24':
                # 24-hour format: "DD-MM-YYYY HH:MM"
                self.time_str = datetime.now().strftime("%d-%m-%Y %H:%M")
                self.ui.lbl_datetime.setText(self.time_str)
            else:
                # 12-hour format: "DD-MM-YYYY HH:MM AM/PM"
                self.time_str1 = datetime.now().strftime("%d-%m-%Y %I:%M %p")
                self.ui.lbl_datetime.setText(self.time_str1)
        except Exception as e:
            logging.error(f"mainscreen|timerlabel|Error in timerlabel: {e}")

    def write_date(self):
        try:
            print("HII:")
            self.cursor = self.connection.cursor()
            age = '12'
            if self.ui.radioButton_8.isChecked() :
                age = '24'
            elif self.ui.radioButton_7.isChecked() :
                age = '12'

            query = "UPDATE tbl_Utitlity SET AspectRatio=?"
            print(query)
            self.cursor.execute(query, (age,))
            self.connection.commit()
            self._time_format = None
            self.getdateformate()

        except Exception as e:
               logging.error(f"mainscreen|write_date|Error in write_date: {e}")

    #this method is used for the edit the time and set in the label
    def set_datetime(self):
        try:
            print('set date/time')
            setdate=self.ui.dateTimeEdit.date().toString("yyyy-MM-dd")
            settime=self.ui.dateTimeEdit_2.time().toString("HH:mm:ss")
            subprocess.run(["timedatectl", "set-time", f"{setdate} {settime}"], check=True)
            self.write_date()            
            QMessageBox.information(self,"Update","Date and Time Updated successfully")
        except Exception as e:
            logging.error(f"mainscreen|timerlabel|Error in timerlabel: {e}")

    def setting_date_wnd(self):
        self.setting_sw(1)
        cursor=self.connection.cursor()
        query = "SELECT * FROM tbl_Utitlity"
        cursor.execute(query)
        rows=cursor.fetchall()
        cursor.close()
        row1= rows[0]
        if row1[5] == '24':
            self.ui.radioButton_8.setChecked(True)
        else:
            self.ui.radioButton_7.setChecked(True)

    #this method is used for refresh the dashboard page
    def refresh(self):
        try:
            self.ui.txt_searchbox.setText("")
            self.ui.lbl_visit_count.setText("(0/0)")
            self.ui.label_59.setText("0000")
            self.ui.label_69.setText("----")
            self.ui.label_76.setText("Doctorname")
            self.ui.label_50.setText("00000")
            self.ui.label_51.setText("Patient Name")
            self.ui.label_52.setText("000 Years old ,")
            self.ui.label_53.setText("Male")
            visit_time=datetime.now().strftime("%d-%m-%Y %I:%M %p")
            self.ui.label_60.setText(visit_time)
            self.ui.listView.setModel(None)
            self.tuple_data = None
            self.ListPatient()
        except Exception as e:
            logging.error(f"mainscreen|refresh|Error in the refresh data for patient: {e}")

    #this method is used for Delete visit /Copy to USB in the patient list
    def on_context_menu(self, pos):
            try:
                logging.info(f"mainscreen|on_context_menu|on_context_menu method call...")
                # show context menu
                index = self.ui.tableWidget.indexAt(pos)
                if index.isValid() :
                    menu= QtWidgets.QMenu()
                    #folderopen_action=menu.addAction('OpenFile Location')
                    #folderopen_action=menu.addAction('View Report')
                    delete_action=menu.addAction('Delete Visit')
                    usb_action=menu.addAction('USB Copy')
                    logging.info(f"mainscree|on_context_menu|User click the context menu button...")
                    action=menu.exec(self.ui.tableWidget.viewport().mapToGlobal(pos))

                if action == delete_action:
                    logging.info(f"mainscreen|on_context_menu|delete_action are Done....")
                    path = self.tuple_data[10]
                    self.deletevisit(self.visit_id)                    
                    shutil.rmtree(path)
                    logging.info(f"mainscreen|on_context_menu|User click the delete button in context menu")
                    self.ListPatient()
                if action == usb_action:
                    self.copy_usb()
                    logging.info(f"mainscreen|on_context_menu|User click the copy usb button in context menu")
            except Exception as e:
                logging.error(f"mainscreeen|on_context_menu|Error in the method: {e}")

    #this method is used for Delete Doctor the patient list
    def on_context_menu2(self, pos):
        try:
            logging.info(f"mainscreen|on_context_menu2|on_context_menu method call...")
            # show context menu
            index = self.ui.tableWidget_3.indexAt(pos)
            print(index)
            if index.isValid() :
                menu= QtWidgets.QMenu()
                delete_action=menu.addAction('Delete Doctor')
                logging.info(f"mainscree|on_context_menu2|User click the DELETE button...")
                action=menu.exec(self.ui.tableWidget_3.viewport().mapToGlobal(pos))
            if action == delete_action:
                logging.info(f"mainscreen|on_context_menu2|delete_action are Done....")               
                self.deletedoctor(self.doc_name)
                logging.info(f"mainscreen|on_context_menu2|For delete_action call the deletevisit method with parameter")

        except Exception as e:
            logging.error(f"mainscreeen|on_context_menu2|Error in the method: {e}")

    #this method is used for Delete the image/video in the image_list in the Dashboard
    def on_context_menu_3(self, pos):
        try:
            logging.info(f"mainscreen|on_context_menu|on_context_menu_3 method call...")
            # show context menu
            index = self.ui.listView.indexAt(pos)
            print(index.column())
            if index.isValid() :
                menu1 = QtWidgets.QMenu()
                delete_action=menu1.addAction('Delete')
                logging.info(f"mainscree|on_context_menu_3|User click the DELETE button so (Image/Video/PDF) will be delete...")
                action=menu1.exec(self.ui.listView.viewport().mapToGlobal(pos))
            if action == delete_action:
                reply = QMessageBox.question(self, "Confirmation", "Do you want delete this seleted data?",
                                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply==QMessageBox.Yes:
                    logging.info(f"mainscreen|on_context_menu_3|delete_action are Done....")
                    os.system("rm "+self.image_name)
                    self.ui.listView.setModel(None)
                    self.load_media_to_listview(self.image_path)
                    logging.info(f"mainscreen|on_context_menu_3|For delete_action call the delete method with parameter")
            else:
                print('None')
        except Exception as e:
            logging.error(f"mainscreeen|on_context_menu_3|Error in the method: {e}")

    #this method is used for the getting the data from selected the row in the patient list
    def get_selected_rows_doctor(self):
        try:
            print("doctor")
            row = self.ui.tableWidget_3.currentRow()
            firstColumnInRow = self.ui.tableWidget_3.item(row, 0)
            if firstColumnInRow != None:
                self.doc_name = firstColumnInRow.text()
                print(self.doc_name)
                print("above doctor")
                logging.info(f"mainscreen|get_selected_row_doctor|user selected {self.visit_id} visitid the row in the grid..")
        except Exception as e:
            logging.error(f"mainscreen|get_selected_row_doctor|Error in the get_selected_row: {e}")

    def deletedoctor(self, index):
        try:
            cursor=self.connection.cursor()
            if index is None:
                QMessageBox.warning(self,"Selection Error","Please select a doctor record to delete!")
                return
            try:
                reply = QMessageBox.question(self, "Confirmation", "Do you want to delete this data?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if reply == QMessageBox.Yes:
                        cursor.execute("DELETE FROM tbl_doctor WHERE Doctorname=?",(index,))
                        self.connection.commit()
                        self.load_data()
                        QMessageBox.information(self,"Success","Doctor record deleted successfully!")
            except sqlite3.Error as e:
                QMessageBox.critical(self,"Database Error",f"Failed to delete record:{e}")
        except Exception as e:
               logging.error(f"mainscreen|delete_doctordata|Error:{e}")
    #this method is used for the deletevisit in the patient list
    def deletevisit(self,_visitid):
        try:
            reply = QMessageBox.question(self, "Confirmation", "Do you want to delete this data?",
                                             QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                visitid = _visitid
                cursor=self.connection.cursor()
                cursor.execute("""delete from tbl_PatientVisit
                            WHERE Visitid = ?
                        """, (visitid,))
                logging.info(f"mainscreen|deletevisit|delete the patientVisit using the {visitid}")
                self.connection.commit()
                self.refresh()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to delete data: {e}")
            logging.error(f"mainscreen|deletevisit|Database Error Failed to delete data: {e}")

    #this method is used for the delete patient in the patient list
    def delete_patient(self):
            try:
                if self.tuple_data != None:
                    reply = QMessageBox.question(self, "Confirmation", "Do you want to delete this data?",
                                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                    if reply == QMessageBox.Yes:
                            visitid = self.tuple_data[1]
                            cursor=self.connection.cursor()
                            cursor.execute("""delete from tbl_Patient WHERE PatientID = ? """, (visitid,))
                            cursor.execute("""delete from tbl_PatientVisit WHERE MRNO = ? """, (visitid,))
                            remove=self.folder+self.tuple_data[1]+"-"+self.tuple_data[11]+"/"
                            shutil.rmtree(remove)
                            logging.info(f"mainscreen|deletevisit|delete the patientVisit using the {visitid}")
                            self.connection.commit()
                            self.refresh()
                    else:
                        self.refresh()
            except sqlite3.Error as e:
                    QMessageBox.critical(self, "Database Error", f"Failed to delete data: {e}")
                    logging.error(f"mainscreen|deletevisit|Database Error Failed to delete data: {e}")

    #this is for the compare screen
    def compare_srn(self):
        try:
            if self.tuple_data != None:
                    self.sw_2(3)
                    self.ui.lbl_compare_pid.setText(self.tuple_data[1])
                    self.ui.lbl_compare_pname.setText(self.tuple_data[2])
                    self.Load_data_visit()
                    logging.info(f"mainscreen|compare_srn|compare screen open without an any issues")
            else:
                QMessageBox.information(self, "Invalid Input", "Pls click any patient in the table")
        except Exception as e:
            logging.error(f"mainscreen|compare_srn|Error in the compare_srn data for patient: {e}")

    def cmp_back(self):
        self.sw_2(0)
        self.refresh()

    def back_preview(self):
        try:
            self.sw_2(0)
            self.sw(3)
            self.refresh()
            self.ui.lbl_pre_pid.clear()
            self.ui.lbl_pre_pname.clear()
            self.ui.lbl_pre_vid.clear()
            self.ui.lbl_pre_visitdate.clear()
            self.ui.lbl_pre_img_name.setText("")
            #self.ui.lbl_pre_img.clear()
            logging.info(f"mainscreen|back_preview|user move to the dasloggingaddWidgethboard form the preview screen")
        except Exception as e:
            logging.error(f"mainscreen|compare_srn|Error in the compare_srn data for patient: {e}")


    #this method is for single window
    def single_wnd_cmp(self, side):
        """Handle single window button clicks with proper sequencing"""
        try:
            self.last_clicked_side = side
            self.sw_2(5)
            print("single window")
            if side == "left":
                current_item = self.ui.left_thumbnail_list.currentItem()
                source_pixmap = getattr(self, 'left_original_pixmap', None)
            else:
                current_item = self.ui.right_thumbnail_list.currentItem()
                source_pixmap = getattr(self, 'right_original_pixmap', None)
            if current_item:
                self.display_image(current_item, "single")
            elif source_pixmap and not source_pixmap.isNull():
                self.single_original_pixmap = source_pixmap
                self.single_wnd_pixmap_item.setPixmap(source_pixmap)
                self.reset_zoom_and_fit("single")
            visit_id = self.ui.cmb_left_vid.currentText() if side == "left" else self.ui.cmb_right_vid.currentText()
            print(visit_id)
            index = self.ui.cmb_single_window.findText(visit_id)
            if index >= 0:
                self.ui.cmb_single_window.setCurrentIndex(index)
                self.single_wnd_folder(index)
        except Exception as e:
            logging.error(f"Error handling single window click: {e}")

    #this method is used for load the visit data for the compare patient visit_id
    def Load_data_visit(self):
        try:
            cursor=self.connection.cursor()
            query = "SELECT Visitid FROM tbl_PatientVisit where MRNO='"+self.tuple_data[1]+"'"
            cursor.execute(query)
            rows=cursor.fetchall()
            self.ui.cmb_left_vid.clear()
            self.ui.cmb_right_vid.clear()
            self.ui.cmb_single_window.clear()
            visit_ids = [str(row[0]) for row in rows]  # Assuming Visitid is the first element in each tuple
            print(visit_ids)
            self.all_visits = self.get_all_visits_for_patient()
            self.current_visit_index = self.all_visits.index(self.visit_id)
            self.ui.cmb_left_vid.addItems(visit_ids)
            self.ui.cmb_right_vid.addItems(visit_ids)
            self.ui.cmb_single_window.addItems(visit_ids)
            # Set current visit as default selection
            self.ui.cmb_left_vid.setCurrentIndex(self.current_visit_index)
            self.ui.cmb_right_vid.setCurrentIndex(self.current_visit_index)
            self.ui.cmb_single_window.setCurrentIndex(self.current_visit_index)
            #load data for current visitid
            self.ui.cmb_single_window.activated.connect(self.single_wnd_folder)
            self.ui.cmb_left_vid.activated.connect(self.leftgetfolder)
            self.ui.cmb_right_vid.activated.connect(self.rightgetfolder)
            cursor.close()
            self.LoadCompareLayout()
            self.leftgetfolder(self.current_visit_index)
            logging.info(f"mainscreen|Load_data_visit|load the data to compare form {self.tuple_data[1]}...")
        except Exception as e:
                logging.error(f"mainscreen|Load_data_visit|Error:{e}")

    #this method is used for load the image in the image box left/right side
    def LoadCompareLayout(self):
        try:
            # Initialize zoom levels and buttons
            self.left_zoom_level = 0
            self.right_zoom_level = 0
            self.single_zoom_level = 0
            self.pre_zoom_level = 0
            self.last_clicked_side = "left"  # Default to left side
            self.ui.btn_preview_zoomout.setEnabled(False)
            self.ui.btn_compare_zoomout_single_wnd.setEnabled(False)
            self.ui.btn_compare_left_zoomout.setEnabled(False)
            self.ui.btn_compare_right_zoomout.setEnabled(False)
            '''# Reset any existing scaling
            if hasattr(self, 'left_view'):
                self.left_view.scale(1, 1)
            if hasattr(self, 'right_view'):
                self.right_view.scale(1, 1)'''
            # Clear existing images
            #self.ui.lbl_com_img_single_wnd.clear()
            #self.ui.lbl_compare_left_image.clear()
            #self.ui.lbl_compare_right_image.clear()
            #self.ui.lbl_pre_img.clear()
            # Initialize pixmaps
            self.left_original_pixmap = QPixmap()
            self.right_original_pixmap = QPixmap()
            self.single_original_pixmap = QPixmap()
            self.preview_original_pixmap = QPixmap()
            # Initialize single window
            self.single_wnd_scene = QGraphicsScene()
            self.single_wnd_pixmap_item = QGraphicsPixmapItem()
            self.single_wnd_scene.addItem(self.single_wnd_pixmap_item)
            self.ui.lbl_com_img_single_wnd.setScene(self.single_wnd_scene)
            self.ui.cmp_single_img_list.clear()
            # Initialize preview window
            self.preview_wnd_scene = QGraphicsScene()
            self.preview_wnd_pixmap_item = QGraphicsPixmapItem()
            self.preview_wnd_scene.addItem(self.preview_wnd_pixmap_item)
            self.ui.lbl_pre_img.setScene(self.preview_wnd_scene)
            self.ui.pre_list.clear()
            # Initialize left side
            self.left_scene = QGraphicsScene()
            self.left_pixmap_item = QGraphicsPixmapItem()
            self.left_scene.addItem(self.left_pixmap_item)
            self.ui.lbl_compare_left_image.setScene(self.left_scene)
            self.ui.left_thumbnail_list.clear()
            # Initialize right side
            self.right_scene = QGraphicsScene()
            self.right_pixmap_item = QGraphicsPixmapItem()
            self.right_scene.addItem(self.right_pixmap_item)
            self.ui.lbl_compare_right_image.setScene(self.right_scene)
            self.ui.right_thumbnail_list.clear()

            self.copy_to_single_window()
            self.ui.lbl_com_img_single_wnd.show()
            self.ui.lbl_com_img_single_wnd.setVisible(True)

            # Clear list views
            #self.ui.pre_list.setModel(QStandardItemModel())
            #self.ui.cmp_single_img_list.setModel(QStandardItemModel())
            #self.ui.left_image_list.setModel(QStandardItemModel())
            #self.ui.right_image_list.setModel(QStandardItemModel())
            logging.info("mainscreen|LoadCompareLayout|Initialized compare layout")
        except Exception as e:
            logging.error(f"mainscreen|LoadCompareLayout|Error:{e}")

    #this method is used for getting patient folder single window the in compare window
    def single_wnd_folder(self,index):
        try:
            cursor=self.connection.cursor()
            visit_id = int(self.ui.cmb_single_window.currentText())  # Convert selected text to integer
            query = f"SELECT * FROM PatientList_View WHERE Visitid={visit_id}"
            self.ui.cmp_single_img_list.clear()
            '''model = QStandardItemModel()
            self.ui.cmp_single_img_list.setModel(model)
            model.clear()'''
            cursor.execute(query)
            rows=cursor.fetchall()
            data=rows[0]
            print(data)
            fdate = str(data[5]).replace(' ','-')
            path = self.folder+str(data[1])+"-"+str(data[11])+"/"+str(visit_id)+"-"+fdate+"/"
            self._load_images(self.ui.cmp_single_img_list, "single", path)
            logging.info(f"mainscreen|single_wnd_folder|get the patient folder for the single_window using visitid:{visit_id}...")
        except Exception as e:
                logging.error(f"mainscreen|single_wnd_folder|Error in getting folder:{e}")

    #this method is used for getting patient folder left_side the in compare window
    def leftgetfolder(self,index):
        try:
            cursor=self.connection.cursor()
            visit_id = int(self.ui.cmb_left_vid.currentText())
            print(visit_id)
            query = f"SELECT * FROM PatientList_View WHERE Visitid={visit_id}"
            self.ui.left_thumbnail_list.clear()
            cursor.execute(query)
            rows=cursor.fetchall()
            data=rows[0]
            print(data)
            print("hii this data:       "+data[11])
            fdate = str(data[5]).replace(' ','-')
            path = self.folder+str(data[1])+"-"+str(data[11])+"/"+str(visit_id)+"-"+fdate+"/"
            self._load_images(self.ui.left_thumbnail_list, "left", path)
            logging.info(f"mainscreen|leftgetfolder|get the patient folder for the leftside using visitid:{visit_id}...")
        except Exception as e:
                logging.error(f"mainscreen|leftgetfolder|Error in getting folder:{e}")

    #this method is used for getting patient folder right_side the in compare window
    def rightgetfolder(self,index):
        try:
            cursor=self.connection.cursor()
            visit_id = int(self.ui.cmb_right_vid.currentText())  # Convert selected text to integer
            query = f"SELECT * FROM PatientList_View WHERE Visitid={visit_id}"
            self.ui.right_thumbnail_list.clear()
            cursor.execute(query)
            rows=cursor.fetchall()
            data=rows[0]
            fdate = str(data[5]).replace(' ','-')
            path = self.folder+str(data[1])+"-"+str(data[11])+"/"+str(visit_id)+"-"+fdate+"/"
            self._load_images(self.ui.right_thumbnail_list, "right", path)
            logging.info(f"mainscreen|rightgetfolder|get the patient folder for the rightside using visitid:{visit_id}...")
        except Exception as e:
                logging.error(f"mainscreen|rightgetfolder|Error in getting folder:{e}")

    #this method is used for load image in the compare window image list
    def _load_images(self, list_widget, side, folder_path):
        try:
            list_widget.clear()
            """Load images from a folder into the thumbnail list."""
            image_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".gif"}
            image_files = [
                os.path.join(folder_path, f)
                for f in os.listdir(folder_path)
                if os.path.splitext(f)[1].lower() in image_extensions
            ]
            if len(image_files)==0:
                QMessageBox.information(self,"Alert","No image in this record")
                return
            # Sort the image files in ascending order
            image_files.sort()
            # Configure list widget for horizontal layout
            list_widget.setViewMode(QListView.IconMode)
            list_widget.setFlow(QListView.LeftToRight)  # Horizontal flow
            list_widget.setWrapping(False)  # No wrapping to single line
            list_widget.setResizeMode(QListView.Adjust)
            list_widget.setMovement(QListView.Static)
            list_widget.setSpacing(0)
            list_widget.setIconSize(QSize(100, 80))
            if side == "preview" or side == "single":
                list_widget.setFixedSize(QSize(1614,120))
            else:
                list_widget.setFixedSize(QSize(778,120))
            list_widget.setUniformItemSizes(True)
            fistimage=image_files[0]
            # Add the label to the layout
            item = QListWidgetItem()  # Create a new item for the list
            # Store the image path in the item
            item.setData(Qt.UserRole, fistimage)
            if side == "preview" :
                self.display_image(fistimage, "preview")
            print(image_files)
            for image_file in image_files:
                pixmap = QPixmap(image_file).scaled(60, 60, Qt.KeepAspectRatio)  # Create a thumbnail image
                item_widget = QWidget()  # Create a custom QWidget for the item
                item_layout = QVBoxLayout(item_widget)  # Create a layout for the item widget
                item_layout.setContentsMargins(1,1,1,1)
                item_layout.setSpacing(5)
                label = QLabel()  # Create a QLabel to display the image
                label.setPixmap(pixmap)  # Set the pixmap to the label
                label.setFixedSize(QSize(60,60))
                label.setAlignment(Qt.AlignTop)
                eyename=os.path.basename(image_file)
                eye_name=eyename.split('-')
                filename=eye_name[6].replace('.bmp','')
                print(filename)
                self.image_name_label = QLabel(filename, self)                
                self.image_name_label.setAlignment(Qt.AlignTop)
                self.image_name_label.setFixedSize(QSize(60,30))
                self.image_name_label.setStyleSheet("""
                                            QLabel {
                                                    color: black;
                                                    font: 8pt "Ubuntu Sans";
                                            }
                                        """)
                item_layout.addWidget(label)
                item_layout.addWidget(self.image_name_label)  # Add the label to the layout

                # Add the label to the layout
                item = QListWidgetItem()  # Create a new item for the list
                item.setSizeHint(QSize(100,80))  # Set the item size based on the widget size
                list_widget.addItem(item)  # Add the item to the list
                list_widget.setItemWidget(item, item_widget)  # Set the widget for the item
                # Store the image path in the item
                item.setData(Qt.UserRole, image_file)
            #self.ui.left_image_list.clicked.connect(lambda index: self.on_image_clicked(index, "left"))
            # After loading all images:
            if list_widget.count() > 0:
                # Automatically select first item
                list_widget.setCurrentRow(0)
                current_item = list_widget.currentItem()
                if current_item:
                    self.display_image(current_item, side)
            else:
                print(f"No images loaded for {side}")
                logging.error(f"mainscreen|load_image|Error:No images loaded for {side} {e}")
            print(side)
            # Connect click event
            if side == "left":
                list_widget.itemClicked.connect(lambda item: self.display_image(item, "left"))
                self.ui.btn_compare_fit.clicked.connect(lambda: self.reset_zoom_and_fit("left"))
            elif side == "right":
                list_widget.itemClicked.connect(lambda item: self.display_image(item, "right"))
                self.ui.btn_compare_fit_2.clicked.connect(lambda: self.reset_zoom_and_fit("right"))
            elif side == "preview":
                list_widget.itemClicked.connect(lambda item: self.display_image(item, "preview"))
                self.ui.btn_previewscn_fit.clicked.connect(lambda: self.reset_zoom_and_fit("preview"))
            else:
                list_widget.itemClicked.connect(lambda item: self.display_image(item, "single"))
                self.ui.btn_compare_fit_.clicked.connect(lambda: self.reset_zoom_and_fit("single"))
            logging.info(f"mainscreen|load_image|Load images from a folder into the thumbnail list right or left...")
        except Exception as e:
                logging.error(f"mainscreen|load_image|Error:{e}")

    #this method is used for display the image in the compare windows
    def display_image(self, item, side):
        try:
            """Display the selected image in the main view."""
            image_path = item.data(Qt.UserRole)
            text = image_path.split('/')[-1].split('-')[-1].split('.')[0]
            self.ui.lbl_pre_img_name.setText(text)
            pixmap = QPixmap(image_path)
            # Store original pixmap
            if side == "left":
                self.left_original_pixmap = pixmap
            elif side == "right":
                self.right_original_pixmap = pixmap
            elif side == "preview":
                self.preview_original_pixmap = pixmap
            else:
                self.single_original_pixmap = pixmap
            if side == "left":
                self.left_zoom_level = 0
                view = self.ui.lbl_compare_left_image
                original_pixmap = getattr(self, 'left_original_pixmap', None)
            elif side == "right":
                self.right_zoom_level = 0
                view = self.ui.lbl_compare_right_image
                original_pixmap = getattr(self, 'right_original_pixmap', None)
            elif side == "preview":
                self.pre_zoom_level = 0
                view = self.ui.lbl_pre_img
                original_pixmap = getattr(self, 'preview_original_pixmap', None)
            else:
                self.single_zoom_level = 0
                view = self.ui.lbl_com_img_single_wnd
                original_pixmap = getattr(self, 'single_original_pixmap', None)
            if original_pixmap is None or original_pixmap.isNull():
                return
            # Reset transformation
            view.resetTransform()

            # Fit the image to view while maintaining aspect ratio
            view_size = view.viewport().size()
            scaled_pixmap = original_pixmap.scaled(view_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            if side == "left":
                self.left_pixmap_item.setPixmap(scaled_pixmap)
                self.left_scene.setSceneRect(scaled_pixmap.rect())
            elif side == "right":
                self.right_pixmap_item.setPixmap(scaled_pixmap)
                self.right_scene.setSceneRect(scaled_pixmap.rect())
            elif side == "preview":
                self.preview_wnd_pixmap_item.setPixmap(scaled_pixmap)
                self.preview_wnd_scene.setSceneRect(scaled_pixmap.rect())
            else:
                self.single_wnd_pixmap_item.setPixmap(scaled_pixmap)
                self.single_wnd_scene.setSceneRect(scaled_pixmap.rect())

            # If displaying in left/right view, update last clicked side
            if side in ["left", "right"]:
                self.last_clicked_side = side
                self.copy_to_single_window()

            logging.info(f"mainscreen|display_image|Display the selected image in the main view in comparewnd...")
        except Exception as e:
            logging.error(f"mainscreen|display_image|Error:{e} {side}")

    #this method is used for zoom function in the compare window
    def zoom(self, view, factor, side, zoom_in_button, zoom_out_button):
        try:
            """Zoom in or out on the specified view, with dynamic button management."""
            if side == "left":
                zoom_level = self.left_zoom_level
            elif side == "right":
                zoom_level = self.right_zoom_level
            elif side == "preview":
                zoom_level = self.pre_zoom_level
            else:
                zoom_level = self.single_zoom_level
                # Adjust zoom level and apply scaling
            # Determine if we're zooming in or out
            is_zooming_in = factor > 1
            # Apply zoom if within limits
            if (is_zooming_in and zoom_level < 10) or (not is_zooming_in and zoom_level > 0):
                view.scale(factor, factor)
                zoom_level += 1 if is_zooming_in else -1
                # Update zoom level tracker
                if side == "left":
                    self.left_zoom_level = zoom_level
                elif side == "right":
                    self.right_zoom_level = zoom_level
                elif side == "preview":
                    self.pre_zoom_level = zoom_level
                else:
                    self.single_zoom_level = zoom_level
            # Update button states based on current zoom level
            self.update_zoom_buttons(side)
            logging.info(f"mainscreen|zoom|Zoom {side} view to level {zoom_level}")
        except Exception as e:
            logging.error(f"mainscreen|zoom|Error:{e}")

    #this method is for the update the zoom level for the image
    def update_zoom_buttons(self, side):
        """Enable/disable zoom buttons based on current zoom level"""
        if side == "left":
            zoom_level = self.left_zoom_level
            zoom_in = self.ui.btn_compare_left_zoomin
            zoom_out = self.ui.btn_compare_left_zoomout
        elif side == "right":
            zoom_level = self.right_zoom_level
            zoom_in = self.ui.btn_compare_right_zoomin
            zoom_out = self.ui.btn_compare_right_zoomout
        elif side == "preview":
            zoom_level = self.pre_zoom_level
            zoom_in = self.ui.btn_preview_zoomin
            zoom_out = self.ui.btn_preview_zoomout
        else:
            zoom_level = self.single_zoom_level
            zoom_in = self.ui.btn_compare_zoomin_single_wnd
            zoom_out = self.ui.btn_compare_zoomout_single_wnd
        zoom_in.setEnabled(zoom_level < 10)
        zoom_out.setEnabled(zoom_level > -10)

    def reset_zoom_and_fit(self, side):
        """Reset zoom level and display original image"""
        try:
            # Reset zoom level
            if side == "left":
                self.left_zoom_level = 0
                view = self.ui.lbl_compare_left_image
                original_pixmap = getattr(self, 'left_original_pixmap', None)
            elif side == "right":
                self.right_zoom_level = 0
                view = self.ui.lbl_compare_right_image
                original_pixmap = getattr(self, 'right_original_pixmap', None)
            elif side == "preview":
                self.pre_zoom_level = 0
                view = self.ui.lbl_pre_img
                original_pixmap = getattr(self, 'preview_original_pixmap', None)
            else:
                self.single_zoom_level = 0
                view = self.ui.lbl_com_img_single_wnd
                original_pixmap = getattr(self, 'single_original_pixmap', None)
            if original_pixmap is None or original_pixmap.isNull():
                return
            # Reset transformation
            view.resetTransform()

            # Fit the image to view while maintaining aspect ratio
            view_size = view.viewport().size()
            scaled_pixmap = original_pixmap.scaled(view_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

            if side == "left":
                self.left_pixmap_item.setPixmap(scaled_pixmap)
                self.left_scene.setSceneRect(scaled_pixmap.rect())
            elif side == "right":
                self.right_pixmap_item.setPixmap(scaled_pixmap)
                self.right_scene.setSceneRect(scaled_pixmap.rect())
            elif side == "preview":
                self.preview_wnd_pixmap_item.setPixmap(scaled_pixmap)
                self.preview_wnd_scene.setSceneRect(scaled_pixmap.rect())
            else:
                self.single_wnd_pixmap_item.setPixmap(scaled_pixmap)
                self.single_wnd_scene.setSceneRect(scaled_pixmap.rect())

            # Update button states
            self.update_zoom_buttons(side)
            logging.info(f"mainscreen|reset_zoom_and_fit|Reset zoom and fit image for {side} side")
        except Exception as e:
            logging.error(f"mainscreen|reset_zoom_and_fit|Error:{e}")

    #this method is used for display the image in full_size in the compare windows
    def display_image_in_label(self, pixmap, label, side):
        """Display image in a QLabel with proper scaling"""
        try:
            # Calculate scaled size maintaining aspect ratio
            label_size = label.size()
            scaled_pixmap = pixmap.scaled(
                label_size.width(),
                label_size.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            # Set the pixmap on the label
            label.setAlignment(Qt.AlignCenter)
            label.setPixmap(scaled_pixmap)
            # Also update the graphics scene if needed
            if side == "left" and hasattr(self, 'left_pixmap_item'):
                self.left_pixmap_item.setPixmap(pixmap)
                self.left_scene.setSceneRect(pixmap.rect())
            elif side == "right" and hasattr(self, 'right_pixmap_item'):
                self.right_pixmap_item.setPixmap(pixmap)
                self.right_scene.setSceneRect(pixmap.rect())
            elif side == "preview" and hasattr(self, 'preview_wnd_pixmap_item'):
                self.preview_wnd_pixmap_item.setPixmap(pixmap)
                self.preview_wnd_scene.setSceneRect(pixmap.rect())
            else :
                self.single_wnd_pixmap_item.setPixmap(pixmap)
                self.single_wnd_scene.setSceneRect(pixmap.rect())
            self.ui.lbl_compare_left_image.viewport().update()
            self.ui.lbl_compare_right_image.viewport().update()
        except Exception as e:
            logging.error(f"mainscreen|display_image_in_label|Error:{e}")

    #this method is for the zoom setup level and button control
    def setup_zoom_controls(self):
        try:
            """Initialize zoom controls and connections"""
            self.left_zoom_level = 0
            self.right_zoom_level = 0
            self.single_zoom_level = 0
            self.pre_zoom_level = 0
            # Store original pixmaps for both sides
            self.left_original_pixmap = None
            self.right_original_pixmap = None
            self.single_original_pixmap = None
            self.preview_original_pixmap = None
            #preview window
            self.ui.btn_preview_zoomin.clicked.connect(lambda:  self.zoom(self.ui.lbl_pre_img, 1.2, "preview", self.ui.btn_preview_zoomin, self.ui.btn_preview_zoomout))
            self.ui.btn_preview_zoomout.clicked.connect(lambda:  self.zoom(self.ui.lbl_pre_img, 1 / 1.2, "preview", self.ui.btn_preview_zoomin, self.ui.btn_preview_zoomout))
            #singe wndow
            self.ui.btn_compare_zoomin_single_wnd.clicked.connect(lambda: self.zoom(self.ui.lbl_com_img_single_wnd, 1.2, "single", self.ui.btn_compare_zoomin_single_wnd, self.ui.btn_compare_zoomout_single_wnd))
            self.ui.btn_compare_zoomout_single_wnd.clicked.connect(lambda: self.zoom(self.ui.lbl_com_img_single_wnd, 1 / 1.2, "single", self.ui.btn_compare_zoomin_single_wnd, self.ui.btn_compare_zoomout_single_wnd))
            # Left side zoom controls
            self.ui.btn_compare_left_zoomin.clicked.connect(lambda:  self.zoom(self.ui.lbl_compare_left_image, 1.2, "left", self.ui.btn_compare_left_zoomin, self.ui.btn_compare_left_zoomout))
            self.ui.btn_compare_left_zoomout.clicked.connect(lambda: self.zoom(self.ui.lbl_compare_left_image, 1 / 1.2, "left", self.ui.btn_compare_left_zoomin, self.ui.btn_compare_left_zoomout))
            # Right side zoom controls
            self.ui.btn_compare_right_zoomin.clicked.connect(lambda: self.zoom(self.ui.lbl_compare_right_image, 1.2, "right", self.ui.btn_compare_right_zoomin,self.ui.btn_compare_right_zoomout))
            self.ui.btn_compare_right_zoomout.clicked.connect(lambda: self.zoom(self.ui.lbl_compare_right_image, 1 / 1.2, "right", self.ui.btn_compare_right_zoomin, self.ui.btn_compare_right_zoomout))
            logging.info(f"mainscreen|setup_zoom_controls| zoom level setup and button control intiallzise")
        except Exception as e:
            logging.error(f"mainscreen|setup_zoom_controls|Error:{e}")

    def copy_to_single_window(self):
        try:
            if not hasattr(self, 'last_clicked_side'):
                print("No side selected!")
                return
            source_pixmap = None
            if self.last_clicked_side == "left":
                source_pixmap = getattr(self, 'left_original_pixmap', None)
            else:
                source_pixmap = getattr(self, 'right_original_pixmap', None)

            if source_pixmap and not source_pixmap.isNull():
                logging.info(f"mainscreen|copy_to_single_window|Using stored pixmap")

            else:
                if self.last_clicked_side == "left":
                    current_item = self.ui.left_thumbnail_list.currentItem()
                else:
                    current_item = self.ui.right_thumbnail_list.currentItem()

                if current_item:
                    self.display_image(current_item, "single")
                    return
                else:
                    return

            # Ensure view is ready
            if not hasattr(self, 'single_wnd_pixmap_item'):
                self.single_wnd_pixmap_item = QGraphicsPixmapItem()
                self.single_wnd_scene.addItem(self.single_wnd_pixmap_item)

            # Perform the copy
            self.single_original_pixmap = source_pixmap
            self.single_wnd_pixmap_item.setPixmap(source_pixmap)

            # Force update and fit
            self.ui.lbl_com_img_single_wnd.fitInView(
                self.single_wnd_pixmap_item,
                Qt.KeepAspectRatio
            )
            self.ui.lbl_com_img_single_wnd.viewport().update()

            print("COPY SUCCESSFUL!")
        except Exception as e:
            logging.error(f"mainscreen|copy_to_single_window|Error:{e}")

    #this method is used for getting the report data form the database
    def get_report_data(self):
        try:
            cursor=self.connection.cursor()
            cursor.execute("SELECT * FROM tbl_ReportData")
            id=cursor.fetchall()
            data = id[0]
            if len(id) > 0:
                if data[1]=="Header":
                    self.ui.radio_btn_header.setChecked(True)
                else:
                    self.ui.radio_btn_Noheader.setChecked(True)
                self.ui.txt_hospitalName.setText(data[2])
                self.ui.txt_doctor_fname.setText(data[3])
                self.ui.txt_doctor_lname.setText(data[4])
                self.ui.txt_address1.setText(data[5])
                self.ui.txt_city.setText(data[7])
                self.ui.txt_state.setText(data[8])
                self.ui.txt_pincode.setText(data[10])
                self.ui.txt_mobile_no.setText(data[11])
                self.ui.txt_emailid.setText(data[12])
                #self.ui.txt_time.setText(data[8])
                self.reload_image(self.reportfolder+'logo.png')

            logging.info(f"mainscreen|get_report_data|getting the report data from the database..")
        except Exception as e:
            logging.error(f"mainscreen|get_report_data|Error:{e}")

    #this method is used for setup a logo in the report
    def setup_logo(self):
        try:
            self.logo_label = self.ui.label_33
            #self.logo_label.setGeometry(30, 110, 161, 171)
            self.logo_label.setAlignment(Qt.AlignCenter)
            logging.info(f"mainscreen|setup_logo|setup a logo ...")
        except Exception as e:
            logging.error(f"mainscreen|setup_logo|Error in the logo:{e}")

    #this method is used for loading logo_image in the repot form
    def load_image(self):
                try:
                    logopath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.gif)")
                    if logopath != "":
                        self.file_path =logopath
                        self.extension = os.path.splitext(self.file_path)[1]
                        if self.file_path:
                            pixmap = QPixmap(self.file_path)
                            if pixmap.isNull():
                                QMessageBox.warning(self, "Error", "Failed to load image.")
                                logging.warning(f"mainscreen|load_image|Failed to load image...")
                            else:
                                self.logo_label.setPixmap(
                                                    pixmap.scaled(150, 150, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
                                                )
                                logging.info("mainscreen|reload_image|Image reloaded and resized to 150x150.")
                                '''self.logo_label.setPixmap(pixmap.scaled(131, 131, Qt.AspectRatioMode.KeepAspectRatio))
                                preferred_width, preferred_height = 150,150
                                margin = 50
                                image_width, image_height = pixmap.width(),pixmap.height()
                                width_margin=(preferred_width - margin) <=image_width <= (preferred_width + margin)
                                height_margin=(preferred_height - margin) <=image_height <= (preferred_height + margin)
                                print(image_width)'''

                        else:
                            QMessageBox.warning(self, "No File Selected", "No image was selected.")
                            logging.warning(f"mainscreen|load_image|No File or image Selected...")
                        logging.info(f"mainscreen|load_image|load a data for report in report form...")
                except Exception as e:
                        logging.error(f"mainscreen|load_image|Error in the load data:{e}")

    #this method is used for reloading logo_image in the repot form
    def reload_image(self,filepath):
        try:
                if filepath:
                    self.file_path = filepath
                    pixmap = QPixmap(filepath)
                    if pixmap.isNull():
                        QMessageBox.warning(self, "Error", "Failed to load image.")
                        logging.warning(f"mainscreen|reload_image|Failed to load image...")
                    else:
                        self.logo_label.setPixmap(
                                            pixmap.scaled(150, 150, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)
                                        )
                        logging.info("mainscreen|reload_image|Image reloaded and resized to 150x150.")
                        '''self.logo_label.setPixmap(pixmap.scaled(131, 131, Qt.AspectRatioMode.KeepAspectRatio))
                        preferred_width, preferred_height = 150,150
                        margin = 50
                        image_width, image_height = pixmap.width(),pixmap.height()
                        width_margin=(preferred_width - margin) <=image_width <= (preferred_width + margin)
                        height_margin=(preferred_height - margin) <=image_height <= (preferred_height + margin)
                        print(image_width)'''
                else:
                    QMessageBox.warning(self, "No File Selected", "No image was selected.")
                    logging.warning(f"mainscreen|reload_image|No File or image Selected...")
                logging.info(f"mainscreen|reload_image|load a data for doctor in patient form...")
        except Exception as e:
                    logging.error(f"mainscreen|reload_image|Error in the load data:{e}")


    #this method is used for update the report in the database
    def update_report_type(self):
        try:
            if self.ui.radio_btn_header.isChecked():
                self.selected_report_type = "Header"
            elif self.ui.radio_btn_Noheader.isChecked():
                self.selected_report_type = "No Header"
            logging.info(f"mainscreen|update_report_type|Seleteing the report type for the pdf...")
        except Exception as e:
                logging.error(f"mainscreen|update_report_type|Error:{e}")
    
    #this method is used for save the report data in the database
    def save_reportdata(self):
        try:
            logging.info(f"mainscreen|save_reportdata|save_reportdata method start...")
            ReportType = self.selected_report_type
            Hospitalname = self.ui.txt_hospitalName.text()
            Doctorfname = self.ui.txt_doctor_fname.text()
            Doctorlname = self.ui.txt_doctor_fname.text()
            Address1 = self.ui.txt_address1.text()
            Address2 = self.ui.txt_address2.text()
            City = self.ui.txt_city.text()
            State = self.ui.txt_state.text()
            Country = self.ui.cmb_country.currentText()
            Pincode = self.ui.txt_pincode.text()
            Mobile = self.ui.txt_mobile_no.text()
            Emailid = self.ui.txt_emailid.text()
            Time = "09:00am to 07:00pm" #self.ui.txt_time.toPlainText().strip()
            if not ReportType:
                QMessageBox.warning(self, "Validation Error", "Please select a Report Type!")
                return
            if not Hospitalname:
                QMessageBox.warning(self, "Validation Error", "Hospital name cannot be empty!")
                return
            if not Doctorfname:
                QMessageBox.warning(self, "Validation Error", "Doctor name cannot be empty!")
                return
            if not Address1:
                QMessageBox.warning(self, "Validation Error", "Address cannot be empty!")
                return
            if not Mobile.isdigit() or len(Mobile) < 10:
                QMessageBox.warning(self, "Validation Error", "Mobile number must be numeric and at least 10 digits!")
                return
            if "@" not in Emailid or "." not in Emailid:
                QMessageBox.warning(self, "Validation Error", "Please enter a valid email address!")
                return
            if not Time:
                QMessageBox.warning(self, "Validation Error", "Time field cannot be empty!")
                return
            if not self.file_path:
                QMessageBox.warning(self, "Validation Error", "Logo Image Not Available!")
                return
            logging.warning(f"mainscreen|save_reportdata|After commplet validation for report form...")
            cursor=self.connection.cursor()
            try:
                cursor.execute("""
                    INSERT INTO tbl_ReportData (ReportType, Hospitalname, Doctorname, Doctorlname, Address, Address2, City, State, Country, Pincode ,Mobile, Emailid, Time)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (ReportType, Hospitalname, Doctorfname, Doctorlname, Address1, Address2, City, State, Country, Pincode, Mobile, Emailid, Time))
                self.connection.commit()
                if self.file_path != "":
                    logo_save_path = os.path.join(self.reportfolder , "logo.png")
                    logging.info(f"mainscreen|save_reportdata|{logo_save_path}")
                    with Image.open(self.file_path) as img:
                        img.convert("RGBA").save(logo_save_path, "PNG")
                QMessageBox.information(self, "Success", "Data saved successfully!")
                logging.info(f"mainscreen|save_reportdata|Data saved successfully!...")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Database Error", f"Failed to save data: {e}")
        except Exception as e:
                    logging.error(f"mainscreen|save_reportdata|Error:{e}")

    #this method is used for update the report data in the database
    def update_report_data(self):
        try:
            logging.info(f"mainscreen|update_reportdata|update_reportdata method start...")
            ReportType = self.selected_report_type
            Hospitalname = self.ui.txt_hospitalName.text()
            Doctorfname = self.ui.txt_doctor_fname.text()
            Doctorlname = self.ui.txt_doctor_fname.text()
            Address1 = self.ui.txt_address1.text()
            Address2 = self.ui.txt_address2.text()
            City = self.ui.txt_city.text()
            State = self.ui.txt_state.text()
            Country = self.ui.cmb_country.currentText()
            Pincode = self.ui.txt_pincode.text()
            Mobile = self.ui.txt_mobile_no.text()
            Emailid = self.ui.txt_emailid.text()
            Time = "09:00am to 07:00pm"#self.ui.txt_time.toPlainText().strip()
            if not ReportType:
                QMessageBox.warning(self, "Validation Error", "Please select a Report Type!")
                return
            if not Hospitalname:
                QMessageBox.warning(self, "Validation Error", "Hospital name cannot be empty!")
                return
            if not Doctorfname:
                QMessageBox.warning(self, "Validation Error", "Doctor name cannot be empty!")
                return
            if not Address1:
                QMessageBox.warning(self, "Validation Error", "Address cannot be empty!")
                return
            if not Mobile.isdigit() or len(Mobile) < 10:
                QMessageBox.warning(self, "Validation Error", "Mobile number must be numeric and at least 10 digits!")
                return
            if "@" not in Emailid or "." not in Emailid:
                QMessageBox.warning(self, "Validation Error", "Please enter a valid email address!")
                return
            if not Time:
                QMessageBox.warning(self, "Validation Error", "Time field cannot be empty!")
                return
            if not self.file_path:
                QMessageBox.warning(self, "Validation Error", "Logo Image Not Available!")
                return
            logging.warning(f"mainscreen|update_reportdata|After commplet validation for report form...")
            cursor=self.connection.cursor()
            try:
                cursor.execute("""
                UPDATE tbl_ReportData
                SET ReportType=?, Hospitalname=?, Doctorname=?, Doctorlname=?, Address=?, Address2=?, City=?, State=?, Country=?, Pincode=?, Mobile=?, Emailid=?, Time=?
            """,  (ReportType, Hospitalname, Doctorfname, Doctorlname, Address1, Address2, City, State, Country, Pincode, Mobile, Emailid, Time))
                self.connection.commit()
                QMessageBox.information(self, "Success", "Data updated successfully!")
                logging.info(f"mainscreen|update_reportdata|Data updated successfully!...")
                if self.file_path != "":
                    logo_save_path = os.path.join(self.reportfolder , "logo.png")
                    logging.info(f"mainscreen|update_reportdata|{logo_save_path}")
                    with Image.open(self.file_path) as img:
                        img.convert("RGBA").save(logo_save_path, "PNG")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Database Error", f"Failed to save data: {e}")
        except Exception as e:
                    logging.error(f"mainscreen|update_reportdata|Error:{e}")

    #this method is used for getting the report data form the database if there is any update
    def report_data(self):
        try:
            cursor=self.connection.cursor()
            cursor.execute("SELECT * FROM tbl_ReportData")
            id=cursor.fetchall()
            print(id)
            if len(id)> 0:
                self.update_report_data()
            else:
                self.save_reportdata()
            logging.info(f"mainscreen|report_data|save the reportdata if their is none,or update if the alread data in database")
        except Exception as e:
            logging.error(f"mainscree|report_data|Error:{e}")

    #this method is used for the create a report for the patientvisit
    def for_report(self):
        try:
            print("for_print report")
            # Check if there is any data to process
            if self.tuple_data != None:
                image_extensions = ('.bmp',)
                count = 0
                for filename in os.listdir(self.image_path):
                    if filename.lower().endswith(image_extensions):
                        count += 1

                print(f"BMP count: {count}")
                if count >0:
                    dir_path = self.image_path
                    print("This path is: " + dir_path)
                    # Find PDFs in the folder
                    pdf_files = [file for file in os.listdir(dir_path) if file.lower().endswith('.pdf')]
                    print(f"PDF Files: {pdf_files}")
                    # If PDF exists, ask the user if they want to replace it
                    if pdf_files:
                        response = QMessageBox.question(
                            self,
                            "Replace PDF?",
                            f"A Repot PDF already exists.Do you want to replace it?",
                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                            QMessageBox.StandardButton.No
                        )
                        if response == QMessageBox.Yes:
                            try:
                                self.report_Generator()  # Generate new PDF
                            except Exception as e:
                                logging.error(f"Failed to delete old PDF: {e}")
                                QMessageBox.critical(self, "Error", f"Failed to delete old PDF: {e}")
                                self.setCursor(Qt.CursorShape.ArrowCursor)
                                return
                        else:
                            # User clicked "No" to replace PDF
                            QMessageBox.information(self, "Operation Cancelled", "PDF generation cancelled.")
                            self.setCursor(Qt.CursorShape.ArrowCursor)
                            return  # Cancel operation if user declines replacement
                    else:
                        # No PDF exists, create a new PDF
                        self.report_Generator()
                else:
                    QMessageBox.information(self, "Invalid Input", "No data available for this record")
            else:
                # If there is no data in self.tuple_data
                QMessageBox.information(self, "Invalid Input", "Pls click any patient in the table")
                return
            self.refresh()
        except Exception as e:
            logging.error(f"Error in for_report: {e}")
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            self.setCursor(Qt.CursorShape.ArrowCursor)

    #this method is used for generate a report for seleted patient in the list
    def report_Generator(self):
            try:
                if len(self.tuple_data)>0:
                        self.setCursor(Qt.CursorShape.BusyCursor)
                        report_generator = report(self.connection)
                        patient_id = self.tuple_data[0]
                        p = self.tuple_data[8]
                        print(p)
                        report_data, patient_data = report_generator.fetch_data(patient_id)
                        print("rep"+self.reportfolder)
                        logo_path = os.path.join(self.reportfolder, "logo.png")
                        if not report_data or not patient_data:
                            QMessageBox.critical(self, "Error", "Failed to fetch data for the report.")
                            logging.error(f"mainscreen|report_Generator|Failed to fetch data for the report")
                            return
                        image_paths= report_generator.get_image_paths(self.image_path)
                        od_files = sorted([f for f in image_paths if 'OD' in os.path.basename(f)])
                        os_files = sorted([f for f in image_paths if 'OS' in os.path.basename(f)])
                        od_output_path =self.output_path+"OD.pdf"
                        os_output_path =self.output_path+"OS.pdf"
                        od_count= len(od_files)
                        print(od_files)
                        os_count= len(os_files)
                        if p == 'OD' and od_count > 0:
                            self.output_path=self.output_path+"OD.pdf"
                            report_generator.create_pdf(self.output_path, report_data, patient_data, od_files, logo_path)
                        elif p == 'OS' and os_count > 0:
                            self.output_path=self.output_path+"OS.pdf"
                            report_generator.create_pdf(self.output_path, report_data, patient_data, os_files, logo_path)
                        else:
                            if od_count > 0:
                                report_generator.create_pdf(od_output_path, report_data, patient_data, od_files, logo_path)
                            else:
                                if os.path.exists(od_output_path):
                                    os.remove(od_output_path)
                                    print("Deleted existing OD.pdf due to no OD images")
                            if os_count > 0:
                                report_generator.create_pdf(os_output_path, report_data, patient_data, os_files, logo_path)
                            else:
                                if os.path.exists(os_output_path):
                                    os.remove(os_output_path)
                                    print("Deleted existing OS.pdf due to no OS images")
                        print(self.output_path)

                        self.setCursor(Qt.CursorShape.ArrowCursor)
                        QMessageBox.information(self, "Report Generated", f"Report Generated Successfully")
                        logging.info(f"mainscreen|report_Generator|Report Generated Successfully...")
                        self.load_config()
            except Exception as e:
                logging.error(f"mainscreen|report_Generator|Error:{e}")

    def report_swn(self, pdf):
        self.sw(4)
        self.ui.btn_patients.setDisabled(True)
        self.ui.btn_doctor.setDisabled(True)
        self.ui.btn_aboutus.setDisabled(True)
        self.ui.btn_settings.setDisabled(True)
        self.document = QPdfDocument(self)
        self.pdf_view = QPdfView(self)
        self.pdf_view.setDocument(self.document)
        self.pdf_view.setPageMode(QPdfView.PageMode.MultiPage)
        self.pdf_view.setZoomMode(QPdfView.ZoomMode.FitToWidth)
        if not self.ui.widget.layout():
            self.pdf_layout = QVBoxLayout()
            self.ui.widget.setLayout(self.pdf_layout)
        else:
            self.pdf_layout = self.ui.widget.layout()
        for i in reversed(range(self.pdf_layout.count())):
            widget = self.pdf_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        self.pdf_layout.addWidget(self.pdf_view)
        self.choose_pdf_file(pdf)
    #this method is used for choose the pdf file in the given path
    def choose_pdf_file(self, pdf_path):
        if os.path.isfile(pdf_path) and pdf_path.lower().endswith('.pdf'):
            self.open_pdf(pdf_path)
        else:
            print(f"Invalid PDF file: {pdf_path}")
    # This method loads and displays a single PDF file
    def open_pdf(self, pdf_path):
        status = self.document.load(pdf_path)
        if status == QPdfDocument.Status.Ready:
            print(f"PDF loaded: {pdf_path}")
        else:
            print("Failed to load PDF.")


    def compare(self):
        self.ui.stackedWidget_2.setCurrentIndex(2)
        print('Live')
        self.frameslideanimation2(0,55,0)

    #this method is used for live page
    def live(self):
        try:
            self.is_camera_available()
            if self.c_state == "False":
                print("if part")
                logging.warning("mainscreen|live|Pop-up show,'Information', Camera connection issues.")
            elif self.c_state == "True":
                self.ui.snap_btn.setEnabled(False)
                print(self.tempfolder)
                self.sw_2(6)
                self.ui.lbl_scanpage_title.setText("Live")
                self.ui.label_23.setText("OFF")
                self.cleantemp()
                self.visit_path = self.tempfolder
                print('live data for record')
                print(self.visit_path)
                self.ui.lbl_capture_pid.setText("Patient ID : 0000")
                self.ui.lbl_capture_pname.setText("Patient Name : xxxx")
                self.ui.lbl_capture_visitid.setText("Visit ID : 0000")
                self.ui.label_20.setText(self.time_str1)
                #self.scanpage_lable_clear()
                self.livestatus = 1
                self.current_eye= "OD"
                self.ui.btn_odos.setText(self.current_eye)
                logging.info(f"mainscreen|Live|live page open Successfully...")
        except Exception as e:
            logging.error(f"mainscreen|Live|Error in the Live data for patient: {e}")

    #this method is used for Capture page
    def capture(self):
        try:
            print("capture")
            self.current_eye= "OD"
            self.ui.btn_odos.setText(self.current_eye)
            self.ui.snap_btn.setEnabled(False)
            if self.tuple_data != None:
                self.is_camera_available()
                if self.c_state == "False":
                    print("If part")
                    logging.warning("mainscreen|capture|Pop-up show,'Information', Camera connection issues.")
                elif self.c_state == "True":
                    self.sw_2(6)
                    self.ui.lbl_scanpage_title.setText("Capture")
                    self.ui.label_23.setText("OFF")
                    self.getpatientinfo(self.tuple_data[1])
                    self.followupdata(self.tuple_data[1])
                    logging.info(f"mainscreen|capture|capture screen is open!!!")
            else:
                QMessageBox.information(self, "Invalid Input", "Pls click any patient in the table")
        except Exception as e:
            logging.error(f"mainscreen|capture|Error in the capter data for patient: {e}")

    def setting_wnd(self):
        self.sw(1)
        self.setting_sw(0)
        self.get_report_data()

    def setup_recording_button(self):
        self.recording = False  # Track recording state
        self.ui.btn_record.clicked.connect(self.toggle_recording)
        #self.update_rec_button_ui()

    #this method is used for the single button video recording On/Off
    def toggle_recording(self):
        try:
            if not self.recording:
                self.start_recording()
            else:
                self.stop_recording()
            self.recording = not self.recording
            #self.update_rec_button_ui()
        except Exception as e:
            logging.error(f"mainscreen|toggle_recording|Error: {e}")

    #this method is used for start video record
    def start_recording(self):
        try:
            self.rec = 1
            frame_width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
            dt = time.strftime("%d-%m-%Y-%H-%M-%S")
            self.ui.lbl_rec.setText('Recording ON')
            self.ui.label_25.setStyleSheet("""
                QLabel {
                    background-color: green;
                    color: #fff;
                    border-radius: 5px;
                    padding: 5px;
                }
            """)
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            self.out = cv2.VideoWriter(
                os.path.join(self.visit_path, f"{dt}.mp4"),
                fourcc,
                self.fps,
                (frame_width, frame_height)
            )
            self.start_time = time.time()
            logging.info("mainscreen|start_recording|Recording started")
        except Exception as e:
            logging.error(f"mainscreen|start_recording|Error: {e}")
            raise

    #this method is used for stop the video recording
    def stop_recording(self):
        try:
            self.rec=0
            self.out.release()
            self.ui.lbl_rec.setText('Recording OFF')
            self.ui.label_25.setStyleSheet("""
                QLabel {
                    background-color: red;
                    color: #fff;
                    border-radius: 5px;
                    padding: 5px;
                }
            """)
            self.add_images_from_folder_to_captuerlist(self.ui.lv_capture_image,self.visit_path )
            logging.info("mainscreen|stop_recording|Recording stopped")
        except Exception as e:
            logging.error(f"mainscreen|stop_recording|Error: {e}")
            raise

    #this method is used for back form the scan page (Live/Capture)
    def back(self):
            try:
                if self.livestatus == 0:
                    self.stop()
                    self.update_ODOS(self.ODOS)
                    self.current_eye="OD"
                    self.ODOS = "OD"
                    self.patient_clear()
                    #self.ui.some_label.clear()
                    self.dashboard()
                    self.sw_2(0)
                    self.scanpage_lable_clear()
                    self.refresh()
                    self.count = 0
                else:
                    # Initialize the model if it doesn't exist
                    #self.ui.lv_capture_image.setModel(self.model)
                    self.countimage = 0
                    if self.count >0:
                        self.countimage = self.model.rowCount()
                        print("image count: "+str(self.countimage))
                    if self.countimage > 0:
                        reply = QMessageBox.question(self, "Confirmation", "Do You Want To Save This Data?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                        if reply == QMessageBox.Yes:
                            self.stop()
                            self.count=0
                            self.ODOS = "OD"
                            self.count=0
                            self.current_eye="OD"
                            self.livestatus =0
                            self.sw_2(0)
                            self.ui.stackedWidget.setCurrentIndex(0)
                        else:
                            self.stop()
                            self.sw_2(0)
                            self.ODOS = "OD"
                            self.count=0
                            self.current_eye="OD"
                            self.livestatus =0
                            self.refresh()
                    else:
                        self.stop()
                        self.sw_2(0)
                        self.ODOS = "OD"
                        self.count=0
                        self.current_eye="OD"
                        self.livestatus =0
                        self.refresh()
                    self.stop()
                logging.info(f"mainscreen|back|Back button is pressed in capture screen or scanpage..!")
            except Exception as e:
                logging.error(f"mainscreen|back|Error in back:{e}")

    #this method is used for the save the patient data in the database
    def addpatient(self):
        #dialog = msgdialogok(self)
        #dialog.dialog_signal.connect(self.on_dialog_signSELECT COUNT(*) FROM tbl_Patient WHERE PatientID ='8'al)
        #dialog.exec()txt_search.toPlainText().strip()
        self.patient_clear()
        self.is_camera_available()
        if self.c_state == "False":
            logging.warning("mainscreen|addpatient|Pop-up show,'Information', Camera connection issues.")
        elif self.c_state == "True":
            self.ui.stackedWidget.setCurrentIndex(0)


    #this method is used for the save the patient data in the database
    def save_patientdata(self):
        try:
            if self.edit_check == 1:
                print("Edit")
                self.update_patient_data()
                self.ui.txt_patientid.setEnabled(True)
                self.ui.txt_firstname.setEnabled(True)
                self.ui.txt_lastname.setEnabled(True)

            else:
                self.is_camera_available()
                if self.c_state == "False":
                    logging.warning("mainscreen|save_patientdata|Pop-up show,'Information', Camera connection issues.")
                elif self.c_state == "True":
                    self.cursor = self.connection.cursor()
                    patient_id = self.ui.txt_patientid.text().strip()
                    first_name = self.ui.txt_firstname.text().strip()
                    last_name = self.ui.txt_lastname.text().strip()
                    age = self.ui.txt_age.text().strip()
                    age_int = int(age)
                    today = date.today()
                    dob = today.replace(year=today.year - age_int)
                    dob_str = dob.strftime("%d-%m-%Y")
                    gender = "Male" if self.ui.rbt_male.isChecked() else "Female"
                    examining_dr = self.ui.cmb_doctor_patient.currentText()
                    diagnosis = "OPD"
                    mobile_no = self.ui.txt_mobile.text().strip()
                    cvisit=datetime.now().strftime("%d-%m-%Y %H-%M-%S")
                    lvisit=datetime.now().strftime("%d-%m-%Y %H-%M-%S")
                    visitid = self.GenerateVisitId()
                    self.eye_visitid=visitid
                    pname = first_name + last_name
                    cdate =datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
                    visit_date =cvisit
                    proce ="fwour"
                    eye =""
                    summary ="Nothing be happy"
                    odr="fsdf"
                    archive = self.folder+ patient_id+'-'+first_name+'/'+visitid+'-'+cdate+'/'
                    if not patient_id:
                        QMessageBox.warning(self, "Validation Error", "Please enter a patient_id!")
                        logging.warning(f"mainscreen|save_patientdata|Validation Error Please enter a patient_id!")
                        return
                    if re.search(r'[^a-zA-Z0-9 ]', patient_id):
                        QMessageBox.warning(self, "Validation Error", "Please enter a patient_id without special character!")
                        logging.warning(f"mainscreen|save_patientdata|Validation Error Please enter a patient_id without special character!")
                        return
                    if not first_name.isalnum():
                        QMessageBox.warning(self, "Validation Error", "Enter valid firstname!")
                        logging.warning(f"mainscreen|save_patientdata|Validation Error Enter valid firstname!")
                        return
                    if age.isnumeric() and len(age)>3:
                        QMessageBox.warning(self, "Validation Error", "Age must be numeric!")
                        logging.warning(f"mainscreen|save_patientdata|Validation Error Age must be numeric!")
                        return

                    try:
                        self.cursor.execute("""INSERT INTO tbl_Patient (PatientId, FirstName, LastName, Age, DOB, Gender, EDoctor, DiagInfo, Mobile,CVisit,LVisit) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)""",(patient_id, first_name, last_name, age, dob_str, gender, examining_dr, diagnosis, mobile_no,cvisit,lvisit),)
                        self.connection.commit()
                        logging.info(f"mainscreen|save_patientdata|Insert patent data in the database are successfully..")
                        self.cursor.execute("""INSERT INTO tbl_PatientVisit (Visitid, MRNO, PName, PAge, PGender , VDate, EDR, Proce, EEye, Summary, ODR, EYE, Archive, DiagInfo, CVisit, Age) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(visitid, patient_id, pname, age, gender, visit_date, examining_dr, proce, eye, summary, odr, eye, archive, diagnosis, visit_date, age),)
                        self.connection.commit()
                        logging.info(f"mainscreen|save_patientdata|Insert patentvisit data in the database are successfully..")
                        QMessageBox.information(self, "Success", "Patient data has been inserted successfully!")
                        self.foldercreate(patient_id,first_name,visitid,cdate)
                        self.getpatientinfo(patient_id)
                        print("save Patient:"+ str(self.livestatus))
                        if self.livestatus == 0:
                            print("IF HII")
                            self.ui.lbl_scanpage_title.setText("Capture")
                            self.sw_2(6)
                            #self.buttondisable()
                            #self.scanpage("NewPatient")
                        else :
                            print("ELSE HII")
                            print(self.ODOS)
                            self.update_ODOS(self.ODOS)
                            self.movetemp(self.tempfolder,self.visit_path)
                            self.livestatus = 0
                            self.dashboard()
                            self.count = 0
                            self.current_eye = "OD"
                            self.ODOS = "OD"
                            self.stop()
                        logging.info(f"mainscreen|save_patientdata|scanpage open for the new patient {patient_id}")
                        self.patient_clear()
                        #self.clear_form()
                    except sqlite3.Error as e:
                        QMessageBox.critical(self, "Database Error", f"Failed to insert data: {e}")
                    finally:
                        self.cursor.close()
        except Exception as e:
                logging.error(f"mainscreen|save_patientdata{patient_id}|Error:{e}")

    #this method is used for the save the patient visti id for following data
    def followupdata(self,patientid):
        cursor = self.connection.cursor()
        try:
            query = "SELECT PatientID,FirstName,LastName,Age,Gender FROM tbl_Patient where PatientID='"+patientid+"'"
            cursor.execute(query)
            rows=cursor.fetchall()
            data = rows[0]
            age = data[3]
            gender = data[4]
            examining_dr = self.ui.cmb_doctor_patient.currentText()
            visitid = self.GenerateVisitId()
            self.eye_visitid = visitid
            self.ui.lbl_capture_visitid.setText(visitid)
            pname = data[1] + data[2]
            cdate =datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            visit_date = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
            proce ="fwour"
            eye =""
            summary ="Nothing be happy"
            odr="fsdf"
            archive = self.folder+ patientid+'-'+data[1]+'/'+visitid+'-'+cdate+'/'
            diagnosis =""
            cursor.execute("""INSERT INTO tbl_PatientVisit (Visitid, MRNO, PName, PAge, PGender , VDate, EDR, Proce, EEye, Summary, ODR, EYE, Archive, DiagInfo, CVisit, Age) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(visitid, patientid, pname, age, gender, visit_date, examining_dr, proce, eye, summary, odr, eye, archive, diagnosis, visit_date, age),)
            self.connection.commit()
            logging.info(f"mainscreen|followupdated|patientVisit data insert into database..")
            self.foldercreate(patientid,data[1],visitid,cdate)
            print(self.visit_path)
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to insert data: {e}")
            logging.error(f"mainscreen|followupdate|Database error failed to insert:{e}")
        finally:
            cursor.close()

    #this method is used for the move the temp file when the user need to save the data form live
    def movetemp(self,source_folder,destination_folder):
        try:
            for filename in os.listdir(source_folder):
                # Create the full path of the file
                source_file = os.path.join(source_folder, filename)
                # Check if it's a file (not a subfolder)
                if os.path.isfile(source_file):
                    # Copy the file to the destination folder
                    shutil.copy(source_file, destination_folder)
            logging.info(f"mainscreen|movetemp|successfully move the temp data..")
        except Exception as e:
            logging.error(f"mainscreen|movetemp|Error in move temp data: {e}")

    #this method is used for clean the temp file
    def cleantemp(self):
        try:
            # Directory path
            dir_path = self.tempfolder
            # List all files in the directory
            for filename in os.listdir(dir_path):
                file_path = os.path.join(dir_path, filename)
                # Check if it is a file (not a subdirectory)
                if os.path.isfile(file_path):
                    os.remove(file_path)  # Remove the file
                    print(f"Deleted file: {filename}")
            logging.info(f"mainscreen|cleantemp|celaning the temp file...")
        except Exception as e:
            logging.error(f"mainscreen|cleantemp|Error in clean the temp:{e}")


    #this method is used for the clear the patient form input fields
    def patient_clear(self):
        try:
            self.ui.txt_patientid.clear()
            self.ui.txt_patientid.setFocus()
            self.ui.txt_firstname.clear()
            self.ui.txt_lastname.clear()
            self.ui.txt_age.clear()
            self.ui.txt_mobile.clear()
            self.ui.rbt_male.setChecked(True)
            self.ui.cmb_doctor_patient.setCurrentIndex(0)

            if self.livestatus ==1:
                self.ui.rbt_male.setChecked(True)
                self.scanpage_lable_clear()

            logging.info(f"mainscreen|patient_clear|Clear the patient form..")
        except Exception as e:
            logging.error(f"mainscreen|patient_clear|Error in clear patient_form: {e}")

    #this method is edit the patient data in patient form
    def patient_edit(self):
        try:
            if self.tuple_data != None:
                if len(self.tuple_data) >0:
                    self.sw(0)
                    data = self.tuple_data
                    self.edit_check= 1
                    cursor=self.connection.cursor()
                    query = "SELECT * FROM tbl_Patient where PatientID='"+data[1]+"'"
                    logging.info(f"mainscreen|patient_edit|get the patent deatil using the visitid {str(data[1])}")
                    cursor.execute(query)
                    rows=cursor.fetchall()
                    cursor.close()
                    row1= rows[0]
                    self.ui.txt_patientid.setText(row1[1])
                    self.ui.txt_firstname.setText(row1[2])
                    self.ui.txt_lastname.setText(row1[3])
                    self.ui.txt_age.setText(str(row1[15]))
                    self.ui.txt_mobile.setText(str(row1[11]))
                    self.ui.txt_patientid.setEnabled(False)
                    self.ui.txt_firstname.setEnabled(False)
                    self.ui.txt_lastname.setEnabled(False)
                    # Disable editing for these fields
                    '''self.ui.txt_patientid.setReadOnly(True)
                    self.ui.txt_firstname.setReadOnly(True)
                    self.ui.txt_lastname.setReadOnly(True)'''
                    if row1[5] =="Female":
                        self.ui.rbt_female.setChecked(True)
                    else:
                        self.ui.rbt_male.setChecked(True)
                    self.ui.cmb_doctor_patient.currentText()

        except Exception as e:
                logging.error(f"mainscreen|patient_edit|Error in clear patient_form: {e}")

    #this method is used for the edit the patient in the list table & database
    def update_patient_data(self):
        try:
            # Get updated values from UI
            print(self.edit_check)
            patient_id = self.ui.txt_patientid.text()
            age = self.ui.txt_age.text()
            mobile = self.ui.txt_mobile.text()
            gender = "Female" if self.ui.rbt_female.isChecked() else "Male"
            dr = self.ui.cmb_doctor_patient.currentText()
            # Validate inputs
            if not age.isdigit():
                QMessageBox.warning(self, "Invalid Input", "Age must be a number")
                return
            # Update database
            self.cursor = self.connection.cursor()
            query = "UPDATE tbl_Patient SET Age='"+age+"', Mobile='"+mobile+"', EDoctor='"+dr+"' , Gender='"+gender+"' WHERE PatientID='"+patient_id+"'"
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
            logging.info(f"mainscreen|update_patient_data|Update patent data in the database are successfully..")
            self.cursor.close()
            QMessageBox.information(self, "Success", "Patient data updated successfully")
            self.edit_check =0
            self.sw(3)
            self.ListPatient() # Switch back to previous screen or refresh
        except Exception as e:
            logging.error(f"Error updating patient data: {e}")
            QMessageBox.critical(self, "Error", f"Failed to update patient data: {str(e)}")

    #this method is used for update the OSOD in the data
    def update_ODOS(self,odos):
            try:
                    logging.info(f"mainscreen|updated_ODOS|updated_ODOS method call")
                    eye = odos
                    vid = self.eye_visitid
                    visitid=vid
                    cursor=self.connection.cursor()
                    print("Update odos"+str(visitid))
                    cursor.execute("""
                        UPDATE tbl_PatientVisit
                        SET EEye = ?
                        WHERE Visitid = ?
                    """, (eye,visitid))
                    self.connection.commit()                    
                    logging.info(f"mainscreen|updated_ODOS|Updated the Eye in the database successfully... ")
            except sqlite3.Error as e:
                    QMessageBox.critical(self, "Database Error", f"Failed to save data: {e}")

    #this method is used for the OD set in the image capture page
    def update_eye_button_text(self):
        # Update the button text to show current eye
        print(self.current_eye)
        self.ui.btn_odos.setText(self.current_eye)

    #this method is used for the single button click event in "ODOS"
    def toggle_eye(self):
        try:
            if self.cam_check == 1:
                #self.current_eye = "OD"
                #self.ODOS = "OD"
                count = self.model.rowCount()
                if count == 0:
                    self.ODOS = ""
                if self.current_eye == "OD":
                    self.current_eye = "OS"
                    if 'OS' in  self.ODOS:
                        print('OS')
                    else:
                        self.ODOS+='OS'
                else :
                    self.current_eye = "OD"
                    if 'OD' in  self.ODOS:
                        print('OD')
                    else:
                        self.ODOS+=' OD'
            self.update_eye_button_text()
            logging.info(f"mainscreen|toggle_eye|Eye set to {self.current_eye}")
        except Exception as e:
            logging.error(f"mainscreen|toggle_eye|Error in toggle_eye: {e}")
            QMessageBox.critical(self, "Error", f"Failed to toggle eye selection: {e}")

    #this method is used for generate visit_id
    def GenerateVisitId(self):
        try:
            vid = 0
            cursor =  self.connection.cursor()
            cursor.execute("SELECT MAX(CAST(Visitid AS INTEGER)) FROM tbl_PatientVisit")
            max_visit_id = cursor.fetchone()[0]
            if max_visit_id is not None and max_visit_id > 0:
                vid = int(max_visit_id) + 1
            else:
                vid = 1000
            cursor.close()
            logging.info(f"mainscreen|GenerateVisitId|Generate Visitid {vid} for the patient..")
        except Exception as ex:
            (f"An error occurred while generating VisitId: {ex}")
        return str(vid)

    #this method is used for check the patient in the database using the patient id
    def check_patient(self,patient_id):
        try:
            (patient_id)
            check=0
            cursor =self.connection.cursor()
            cursor.execute("SELECT * FROM tbl_Patient WHERE PatientID ='"+patient_id+"'")
            count= cursor.fetchone()
            if count[0] > 0:
                check =1
            logging.info(f"mainscreen|check_patient|check_patient patient_id {patient_id} for the patient..")
        except Exception as ex:
                print(f"An error occurred while check_patient Patient_id: {ex}")
        return check

    #this method is used to create a folder for the patient
    def foldercreate(self,patientid,fname,visitid,cdate):
        try:
            #cdate =datetime.now().strftime("%d-%m-%Y %H-%M-%S")
            self.patient_path = self.folder+ patientid+'-'+fname
            if not os.path.exists(self.patient_path):
                os.makedirs(self.patient_path)
            logging.info(f"mainscreen|foldercreate|Successfull create a patient folder in the {self.patient_path}")
            self.visit_path = self.folder+ patientid+'-'+fname+'/'+visitid+'-'+cdate+'/'
            print(self.visit_path)
            if not os.path.exists(self.visit_path):
                os.makedirs(self.visit_path)
            logging.info(f"mainscreen|foldercreate|Successfull create a patientvisit folder in the {self.visit_path}")
        except Exception as e:
            logging.error(f"mainscreen|foldercerate|Error in folder create: {e}")

    #this method is used for the getting a patient info form the database
    def getpatientinfo(self,patientid):
        try:
            print(patientid)
            cursor=self.connection.cursor()
            query = "SELECT VisitID,MRNO,PName FROM PatientList_View where MRNO='"+patientid+"'"
            cursor.execute(query)
            rows=cursor.fetchall()
            print(rows)
            data = rows[0]
            logging.info(f"mainscreen|getpatientinto|getting the patient detail using the patientid {patientid}")
            #visit_id= self.GenerateVisitId()
            if len(rows) > 0:
                self.ui.lbl_capture_pid.setText(f"Patient ID: {data[1]}")
                self.ui.lbl_capture_pname.setText(f"Name: {data[2]}")
                self.ui.lbl_capture_visitid.setText(f"Visit ID : {data[0]}")
                self.ui.label_20.setText(f"Visit on :{self.time_str1}")
        except Exception as e:
            logging.error(f"mainscreen|getpatientinfo|Error in patient_info: {e}")

    #this method is used for clear the lable in the dashboard page
    def dashboard_lable_clear(self):
        self.ui.lbl_patientid.clear()
        self.ui.lbl_patientname.clear()
        self.ui.lbl_visitid.clear()

    #this method is used for clear the lable in the scan page
    def scanpage_lable_clear(self):
        self.ui.lbl_capture_pid.clear()
        self.ui.lbl_capture_pname.clear()
        self.ui.lbl_capture_visitid.clear()
        #self.ui.label_20.clear()
        self.tuple_data =None
        self.ui.lbl_preview_image.clear()
        self.model.clear()

    #this method is used for loading a doctor
    def loaddoctor(self):
        try:
            cursor=self.connection.cursor()
            self.ui.tableWidget_3.setRowCount(0)
            self.ui.cmb_doctor_patient.clear()
            cursor.execute("SELECT DoctorName FROM tbl_doctor")
            rows = cursor.fetchall()
            data=[row[0] for row in rows]
            print(data)
            self.ui.cmb_doctor_patient.addItems(data)
            cursor = self.connection.cursor()
            # Example: Count records in 'tbl_patient'
            cursor.execute("SELECT COUNT(*) FROM tbl_doctor")
            count = cursor.fetchone()[0]
            self.ui.lbl_doctor_count.setText(f"{count} Doctor")
            logging.info(f"mainscreen|loaddoctor|load a data for doctor in patient form...")
        except Exception as e:
            logging.error(f"mainscreen|loaddoctor|Error in the load data:{e}")
        finally:
            cursor.close()

    #this method is used for the getting the data from selected the row in the patient list
    def get_selected_rows(self):
        try:
            row = self.ui.tableWidget.currentRow()
            firstColumnInRow = self.ui.tableWidget.item(row, 1)
            if firstColumnInRow != None:
                text = firstColumnInRow.text()
                self.visit_id = text
                # First get the basic patient info
                data = self.patientinfo(self.visit_id)
                print(data)
                self.tuple_data = data[0]
                # Now we can safely get all visits since tuple_data is available
                self.all_visits = self.get_all_visits_for_patient()
                print(self.all_visits)
                self.current_visit_index = self.all_visits.index(self.visit_id)
                # Update UI with visit data
                self.ui.label_59.setText(text)
                self.ui.label_69.setText(str(data[0][8]))
                self.ui.label_76.setText(str(data[0][6]))
                self.ui.label_50.setText(str(data[0][1]))
                self.ui.label_51.setText(str(data[0][2]))
                self.ui.label_52.setText(str(data[0][3])+' Years old ,')
                self.ui.label_53.setText(str(data[0][4]))
                sdate = datetime.strptime(str(data[0][5]), "%d-%m-%Y %H-%M-%S")
                fdate = str(data[0][5]).replace(' ','-')
                stime=sdate.strftime("%d-%m-%Y %I:%M %p")
                self.image_path =  self.folder+str(data[0][1])+"-"+str(data[0][11])+"/"+self.visit_id+"-"+fdate+"/"
                print(self.image_path)
                self.ui.label_60.setText(stime)
                self.ui.lbl_visit_count.setText(f"({self.current_visit_index + 1} / {len(self.all_visits)})")
                self.visitfolder =  self.folder+str(data[0][1])+"-"+str(data[0][11])+"/"+self.visit_id+"-"+fdate+"/"
                #self.ui.listView.setModel(None)
                self.dash_listview_model.clear()
                self.output_path = self.folder+str(data[0][1])+"-"+str(data[0][11])+"/"+self.visit_id+"-"+fdate+"/"
                self.load_media_to_listview(self.image_path)
                self.ui.listView.clicked.connect(self.on_item_clicked_single)
                self.ui.listView.doubleClicked.connect(self.on_item_clicked)
                logging.info(f"mainscreen|get_selected_row|user selected {self.visit_id} visitid the row in the grid..")
        except Exception as e:
            logging.error(f"mainscreen|get_selected_row|Error in the get_selected_row: {e}")

    #this method is for the all visit for the patient
    def get_all_visits_for_patient(self):
        """Query database to get all visit IDs for the current patient"""
        try:
            cursor=self.connection.cursor()
            # Get patient_id from the already loaded tuple_data
            patient_id = self.tuple_data[1]  # Assuming index 1 is patient ID
            query = f"SELECT Visitid FROM tbl_PatientVisit WHERE MRNO = '{patient_id}' ORDER BY Visitid ASC"
            result = cursor.execute(query)  # Replace with your actual DB query method
            return [row[0] for row in result]
        except Exception as e:
            logging.error(f"mainscreen|get_all_visits_for_patient|Error: {e}")
            return []  # Return empty list if there's an error

    #this method is for display the updated visit
    def update_visit_display(self):
        """Update UI with current visit data"""
        try:
            data = self.patientinfo(self.visit_id)
            self.tuple_data = data[0]
            # Update your labels
            self.ui.label_59.setText(self.visit_id)
            self.ui.label_69.setText(str(data[0][8]))
            self.ui.label_76.setText(str(data[0][6]))
            self.ui.label_50.setText(str(data[0][1]))
            self.ui.label_51.setText(str(data[0][2]))
            self.ui.label_52.setText(str(data[0][3])+' Years old ,')
            self.ui.label_53.setText(str(data[0][4]))
            sdate = datetime.strptime(str(data[0][5]), "%d-%m-%Y %H-%M-%S")
            fdate = str(data[0][5]).replace(' ','-')
            stime=sdate.strftime("%d-%m-%Y %I:%M %p")
            self.ui.label_60.setText(stime)
            self.ui.lbl_visit_count.setText(f"({self.current_visit_index + 1} / {len(self.all_visits)})")
            # Update media display
            self.visitfolder =  self.folder+str(data[0][1])+"-"+str(data[0][11])+"/"+self.visit_id+"-"+fdate+"/"
            #self.ui.listView.setModel(None)
            self.dash_listview_model.clear()
            self.image_path =  self.folder+str(data[0][1])+"-"+str(data[0][11])+"/"+self.visit_id+"-"+fdate+"/"
            self.output_path =  self.folder+str(data[0][1])+"-"+str(data[0][11])+"/"+self.visit_id+"-"+fdate+"/"
            self.load_media_to_listview(self.image_path)
        except Exception as e:
            logging.error(f"mainscreen|update_visit_display|Error: {e}")

    #this method is for the previous visit
    def on_btn_visit_back_clicked(self):
        """Navigate to previous visit"""
        try:
            if self.tuple_data != None:
                if hasattr(self, 'all_visits') and self.all_visits and self.current_visit_index > 0:
                    self.current_visit_index -= 1
                    self.visit_id = self.all_visits[self.current_visit_index]
                    self.update_visit_display()
        except Exception as e:
            logging.error(f"mainscreen|on_btn_visit_back_clicked|Error: {e}")

    #this method is for the next visit
    def on_btn_visit_next_clicked(self):
        """Navigate to next visit"""
        try:
            if self.tuple_data != None:
                if hasattr(self, 'all_visits') and self.all_visits and self.current_visit_index < len(self.all_visits) - 1:
                    self.current_visit_index += 1
                    self.visit_id = self.all_visits[self.current_visit_index]
                    self.update_visit_display()
        except Exception as e:
            logging.error(f"mainscreen|on_btn_visit_next_clicked|Error: {e}")

    # Connect the buttons in your setup code:
    #self.ui.listWidget.itemDoubleClicked.connect(self.on_item_clicked)
    #self.ui.listWidget.itemClicked.connect(self.on_item_clicked_single)
    #this method is used for the select a image need to be delete
    def on_item_clicked_single(self, item):
        try:
            self.image_name =item.data(Qt.UserRole + 1)
        except Exception as e:
            logging.error(f"mainscreen|on_item_clicked|Error in the on_item_clicked file is not an image or video: {e}")
    #this method is used for the select data need to preview
    def on_item_clicked(self, item):
        try:
            item_text =item.data(Qt.UserRole + 1)
            if '.pdf' in item_text:
                pdf = item_text
                self.report_swn(pdf)
            elif '.mp4' in item_text:                 
                 self.sw_2(1)
                 url = QUrl.fromLocalFile(item_text)  # Use QUrl directly
                 self.player.setSource(url)
                 self.player.play()
                 self.ui.lbl_status_mplayer.setText("Playing")
                 logging.info(f"mainscreen|on_item_clicked|video click open the mplayer_frm ...")
            else:
                self.previewimageload(self.image_path)
                logging.info(f"mainscreen|on_item_clicked|Image click open the previewimageload...")
                self.pimage_path=item_text

            print(item_text)
        except Exception as e:
            logging.error(f"mainscreen|on_item_clicked|Error in the on_item_clicked file is not an image or video: {e}")


    #this method is used for the load data in preview window
    def previewimageload(self,imagepath):
        try:
            print('Image')
            print(imagepath)
            image = QImage(imagepath)
            simage=QPixmap.fromImage(image)
            scaled_pixmap = simage.scaled(1280,720,Qt.KeepAspectRatio, Qt.SmoothTransformation)
            text = imagepath.split('/')[-1].split('-')[-1].split('.')[0]
            self.sw_2(4)
            self.ui.lbl_pre_pid.setText(self.tuple_data[1])
            self.ui.lbl_pre_pname.setText(self.tuple_data[2])
            self.ui.lbl_pre_vid.setText(self.tuple_data[0])
            self.ui.lbl_pre_visitdate.setText(self.tuple_data[5])
            self.ui.lbl_pre_img_name.setText(text)
            #self.ui.lbl_pre_img.viewport().update()
            self.Load_data_visit()
            self.preview_wnd_folder()
            logging.info(f"mainscreen|previewimageload|Image previewload...")
        except Exception as e:
            logging.error(f"mainscreen|previewimageload|Error:{e}")
            print("mainscreen|previewimageload|Error:{e}")

    #this method is for load the folder in the preview screen
    def preview_wnd_folder(self):
        try:
            cursor=self.connection.cursor()
            visit_id = self.visit_id
            query = f"SELECT Archive FROM tbl_PatientVisit WHERE Visitid={visit_id}"
            '''model = QStandardItemModel()
            self.ui.pre_list.setModel(model)
            model.clear()'''
            cursor.execute(query)
            rows=cursor.fetchall()
            data=rows[0]
            self._load_images(self.ui.pre_list, "preview", self.image_path)
            logging.info(f"mainscreen|preview_wnd_folder|get the patient folder for the Preview using visitid:{visit_id}...")
        except Exception as e:
                logging.error(f"mainscreen|preview_wnd_folder|Error in getting folder:{e}")

    '''#this method is used for load image in the single compare window image list
    def preview_wnd_load_images(self, folder_path):
            try:
                print("preview image list")
                """Load images from a folder into the thumbnail list."""
                image_extensions = {".png", ".jpg", ".jpeg", ".bmp", ".gif"}
                image_files = [
                    os.path.join(folder_path, f)
                    for f in os.listdir(folder_path)
                    if os.path.splitext(f)[1].lower() in image_extensions
                ]
                if len(image_files)==0:
                    return
                model = QStandardItemModel()
                self.ui.pre_list.setModel(model)
                # Set view to vertical-first grid layout (column-wise flow)
                self.ui.pre_list.setViewMode(QListView.IconMode)
                self.ui.pre_list.setResizeMode(QListView.Adjust)
                self.ui.pre_list.setMovement(QListView.Static)
                self.ui.pre_list.setFlow(QListView.TopToBottom)     # Fill top-to-bottom, then next column
                self.ui.pre_list.setWrapping(True)                  # Allow wrapping to new columns
                self.ui.pre_list.setSpacing(10)
                self.ui.pre_list.setIconSize(QSize(100, 80))
                self.ui.pre_list.setSelectionMode(QListView.SingleSelection)# Slightly shorter height for better layout
                for filename in sorted(os.listdir(folder_path)):
                    file_path = os.path.join(folder_path, filename)
                    print("Found file:", file_path)
                    item = QStandardItem()
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                        pixmap = QPixmap(file_path)
                        if not pixmap.isNull():
                            # Scale maintaining aspect ratio, fixed height
                            pixmap = pixmap.scaled(100, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                            item.setIcon(QIcon(pixmap))
                            name =filename.rsplit('.', 1)[0]
                            fname = name.split("-")[-1]
                            item.setText(fname)  # Show label without file extension
                            item.setTextAlignment(Qt.AlignCenter)
                            item.setData(file_path, Qt.UserRole)
                            item.setEditable(False)
                            model.appendRow(item)
                        else:
                            logging.warning(f"Invalid image: {file_path}")
                self.ui.pre_list.clicked.connect(lambda index: self.on_image_clicked(index, "preview"))
                self.ui.btn_previewscn_fit.clicked.connect(lambda: self.reset_zoom_and_fit("preview"))
                logging.info(f"mainscreen|preview_wnd_load_images|Load images from a folder into the thumbnail list for preview...")
            except Exception as e:
                logging.error(f"mainscreen|preview_wnd_load_images|Error:{e}")'''

    '''def reset_zoom_and_fit(self, side):
                    """Reset zoom level and display original image"""
                    try:
                        # Reset zoom level
                        if side == "left":
                            self.left_zoom_level = 0
                        elif side == "right":
                            self.right_zoom_level = 0
                        elif side == "preview":
                            self.pre_zoom_level = 0
                        else:
                            self.single_zoom_level = 0

                        # Display the original image
                        self.display_image(side)

                        # Update button states
                        self.update_zoom_buttons(side)

                        logging.info(f"mainscreen|reset_zoom_and_fit|Reset zoom and fit image for {side} side")
                    except Exception as e:
                        logging.error(f"mainscreen|reset_zoom_and_fit|Error:{e}")'''

    def load_media_to_listview(self, folder_path):
        try:
            if not os.path.exists(folder_path):
                logging.error(f"Folder does not exist: {folder_path}")
                return
            self.dash_listview_model = QStandardItemModel()
            self.ui.listView.setModel(self.dash_listview_model)
            # Set view to vertical-first grid layout (column-wise flow)
            self.ui.listView.setViewMode(QListView.IconMode)
            self.ui.listView.setResizeMode(QListView.Adjust)
            self.ui.listView.setMovement(QListView.Static)
            self.ui.listView.setFlow(QListView.TopToBottom)     # Fill top-to-bottom, then next column
            self.ui.listView.setWrapping(True)                  # Allow wrapping to new columns
            self.ui.listView.setSpacing(10)
            self.ui.listView.setIconSize(QSize(100, 80))        # Slightly shorter height for better layout
            # Calculate dimensions for 3 items per column
            icon_height = 70
            text_height = 20  # Estimated height for text label
            vertical_spacing = 10
            items_per_column = 3

            # Total height needed for one column (3 items)
            column_height = (icon_height + text_height + vertical_spacing) * items_per_column

            # Calculate item width (icon width + margins)
            item_width = 100 + 20  # icon width + margins
            self.ui.listView.setGridSize(QSize(item_width, column_height // items_per_column))
            for filename in sorted(os.listdir(folder_path)):
                file_path = os.path.join(folder_path, filename)
                item = QStandardItem()

                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    pixmap = QPixmap(file_path)
                    if not pixmap.isNull():
                        # Scale maintaining aspect ratio, fixed height
                        pixmap = pixmap.scaled(100, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                        item.setIcon(QIcon(pixmap))
                        name =filename.rsplit('.', 1)[0]
                        fname = name.split("-")[-1]
                        item.setText(fname)  # Show label without file extension
                        item.setTextAlignment(Qt.AlignCenter)
                        item.setData(file_path)
                        item.setEditable(False)
                        # Set consistent item size
                        item.setSizeHint(QSize(item_width, icon_height + text_height))
                        self.dash_listview_model.appendRow(item)
                    else:
                        logging.warning(f"Invalid image: {file_path}")

                elif filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                    video_icon_path = '/home/npdslitlamp/SLTAPPNEW/images/video-clip.png' #this need for logo mark
                    if os.path.exists(video_icon_path):
                        item.setIcon(QIcon(video_icon_path))
                    item.setText(filename.rsplit('.', 1)[0])
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setData(file_path)
                    item.setEditable(False)
                    self.dash_listview_model.appendRow(item)

                elif filename.lower().endswith('.pdf'):
                    # Use a PDF icon or generate a thumbnail
                    pdf_icon_path = '/home/npdslitlamp/SLTAPPNEW/images/pdf.png'
                    if os.path.exists(pdf_icon_path):
                        item.setIcon(QIcon(pdf_icon_path))

                    '''# Extract filename without extension
                    name = filename.rsplit('.', 1)[0]
                    fname = name.split("-")[-1] if "-" in name else name
                    item.setText(fname)'''
                    # Set the full filename as text (including .pdf extension)
                    item.setText(filename)  # This keeps the complete filename
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setData(file_path)
                    item.setEditable(False)
                    self.dash_listview_model.appendRow(item)

        except Exception as e:
            logging.error(f"Error loading media to listview: {e}")

    def patientinfo(self,visitid):
        try:
            cursor=self.connection.cursor()
            query = "SELECT * FROM PatientList_View where Visitid='"+visitid+"'"
            logging.info(f"mainscreen|patentinfo|get the patent deatil using the visitid {visitid}")
            cursor.execute(query)
            rows=cursor.fetchall()
            cursor.close()
        except Exception as e:
            logging.error(f"mainscreen|patentinfo|Error:{e}")
        return rows

    def aboutus(self):
            dialog = aboutclass(self)
            dialog.exec()
    def dialogyes(self):
            dialog = msgdialogyes(self)
            dialog.exec()
    def dashboard(self):
        self.sw(3)
        self.ListPatient()
        self.tuple_data = None
        self.refresh()
    def dashboard1(self):
        self.sw(3)
        self.ui.btn_patients.setDisabled(False)
        self.ui.btn_doctor.setDisabled(False)
        self.ui.btn_aboutus.setDisabled(False)
        self.ui.btn_settings.setDisabled(False)

    #this method is used for doctor list
    def doctorlist(self):
        cursor = self.connection.cursor()
        # Example: Count records in 'tbl_patient'
        cursor.execute("SELECT COUNT(*) FROM tbl_doctor")
        count = cursor.fetchone()[0]
        self.ui.lbl_doctor_count.setText(f"{count} Doctor")
        self.sw(2)
        self.load_data()

    #this method is used for stating the camera in the scanpage
    def start(self):
        try:
            self.cam_check = 1
            self.ui.label_23.setText("ON")
            self.ui.snap_btn.setEnabled(True)
            self._timer = QTimer(self)
            self._timer.timeout.connect(self.update)
            self.snap=1
            self._timer.start(10)
            self.ui.btn_record.setEnabled(True)
            self.ui.btn_odos.setEnabled(True)
            logging.info(f"mainscreen|start|Camera start button clicked.!")
        except Exception as e:
                    logging.error(f"mainscreen|start|Error in camera start:{e}")

    #this method is used for stop the camera in the scanpage
    def stop(self):
        try:
            if self.rec == 1:
                self.stop_recording()
                self.recording = not self.recording
            self.cam_check = 0
            self._timer.stop()
            self.snap=0
            #self.ui.label.clear()
            self.scanpage_lable_clear()
            self.ui.label_23.setText("OFF")
            self.ui.snap_btn.setEnabled(False)
            self.ui.btn_record.setEnabled(False)
            self.ui.btn_odos.setEnabled(False)
            logging.info(f"mainscreen|stop|Camera stop button clicked.!")
        except Exception as e:
                    logging.error(f"mainscreen|stop|Error in camera stop:{e}")

    #this method is used for setup the camera & screen resolution 'utility'
    def __setup(self):
        try:
             #Ch camera image resolution 640 x 480 ,800 x 600 ,1280 x 720, 1280 x 960, 1920 x 1080,4k=2048�1536,2592 x 1944, 3840 x 2160
             self.resolutions = [[640 , 480 ], [800 , 600], [1280, 720],[1280, 960], [1920, 1080],[2048, 1536],[2592, 1944],[3840, 2160]]
             self.cresolutions = ['640 X 480' , '800 X 600', '1280 X 720','1280 X 960', '1920 X 1080','2048 X 1536','2592 X 1944','3840 X 2160']
             rsize=3 #int(self.patientlist[4])
             #res_index = self.resolutions[rsize]
             #self.led=self.setting_detail[5]
             #self.ir=self.setting_detail[6]
             self.camid=0 #self.setting_detail[1]
             self.cameraon=0;
             self.WIDTH = self.resolutions[rsize][0]
             self.HEIGHT = self.resolutions[rsize][1]
             print('setup Finish')
             logging.info(f"mainscreen|__setup__initcamera|initial Setup successfully..!")
        except Exception as e:
                     logging.error(f"mainscreen|__setup|Error in setup page:{e}")

    #this method is used for initial the camera
    def __initcamera(self):
        try:
            self.vid = cv2.VideoCapture(self.camid)
            self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, self.WIDTH)
            self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, self.HEIGHT)
            self.fps = self.vid.get(cv2.CAP_PROP_FPS)
            print('camera inited')
            self.c_state = "True"
            if not self.vid.isOpened():
                QMessageBox.information(self,"Camera not connected",  # Title of the message box
                                                "Please check the camera connection.",  # Main message text
                                                QMessageBox.Ok)
                self.c_state = "False"
            logging.info(f"mainscreen|__initcamera|Camera initialising successfully..!")
        except Exception as e:
            logging.error(f"mainscreen|__initcamera|Error in camera:{e}")

    #this method is used for getting frame for camera
    def get_frame(self):
        try:
                  # print('camera frame getting')
                   if self.vid.isOpened():
                       ret, frame = self.vid.read()
                       if ret:
                           # Return a boolean success flag and the current frame converted to BGR
                           # font
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           # org
                           org = (2, 15)
                           # fontScale
                           fontScale = 0.5
                           # Blue color in BGR
                           color = (255,0,0)
                           # Line thickness of 2 px
                           thickness = 1
                           today = datetime.today()
                           #print(today.strftime("%d/%m/%Y %H:%M:%S"))
                           # Using cv2.putText() method
                           #frame=cv2.resize(frame,none,fx=0.75,fy=0.75)
                           #print(self.flip)
                           frame=cv2.flip(frame, self.flip)
                           frame=cv2.rotate(frame, cv2.ROTATE_180)
                           #frame = self.crop(frame, self.roi_x, self.roi_y, self.roi_w, self.roi_h)
                           #image = cv2.putText(frame, today.strftime("%d-%m-%Y %H:%M:%S"), org, font,fontScale, color, thickness, cv2.LINE_AA)
                           #return (ret, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
                           return (ret, frame)

                       else:
                           return (ret, None)
                   else:
                       return (ret, None)
                   logging.info(f"mainscreen|get_frame|camera frame are geitting")
        except Exception as e:
                           logging.error(f"mainscreen|get_frame|Error in camera get_fraem:{e}")


    #this method is used for update the frame for camera frame
    def update(self):
        try:
            # Get a frame from the video source
                       ret, frame = self.get_frame()
                       font = cv2.FONT_HERSHEY_SIMPLEX
                       # org
                       org = (5, 25)
                       # Blue color in BGR
                       color = (182, 255, 99)
                       # fontScale
                       fontScale = 0.5
                       # Line thickness of 2 px
                       thickness = 1
                       height, width = frame.shape[:2]
                       # EDGE DETECTION // LAPLACIAN
                       gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                       gray_img = cv2.GaussianBlur(frame, ksize=(3, 3),sigmaX=1, sigmaY=1)
                       edges = cv2.Laplacian(gray_img, ddepth=-1)
                       #print(os.path.join(os.path.dirname(os.path.realpath(__file__)),'images/watermarklogo.png'))
                       wlogo= cv2.imread('/home/npdslitlamp/SLTAPPNEW/images/watermarklogo.png', cv2.IMREAD_UNCHANGED)
                       # Resize the logo to fit into the camera frame (adjust the size as needed)
                       logo_width = 120  # Width of the logo in the frame
                       logo_height = int((logo_width / wlogo.shape[1]) * wlogo.shape[0])+25 # Maintain aspect ratio
                       wlogo = cv2.resize(wlogo, (logo_width, logo_height))
                       logo_height, logo_width = wlogo.shape[:2]
                       x_offset = width-180
                       y_offset =height-90
                       # Check if the region fits within the frame
                       if y_offset + logo_height <= height and x_offset + logo_width <= width:
                             # Split the logo into its color (BGR) and alpha (transparency) channels
                             if wlogo.shape[2] == 4:  # Check if there's an alpha channel
                                 overlay_color = wlogo[:, :, :3]
                                 overlay_alpha = wlogo[:, :, 3] / 255.0  # Normalize alpha to 0-1
                                 # Extract the region of interest (ROI) from the frame
                                 roi = frame[y_offset:y_offset + logo_height, x_offset:x_offset + logo_width]
                                 # Perform alpha blending between the logo and the ROI
                                 for c in range(0, 3):  # For each color channel (BGR)
                                     roi[:, :, c] = (overlay_alpha * overlay_color[:, :, c] + (1 - overlay_alpha) * roi[:, :, c])
                                 # Place the blended ROI back into the frame
                                 frame[y_offset:y_offset + logo_height, x_offset:x_offset + logo_width] = roi
                             else:
                                 # If there's no alpha channel, just place the logo directly
                                 frame[y_offset:y_offset + logo_height, x_offset:x_offset + logo_width] = wlogo
                       #cv2.putText(frame,"AUROLAB", (width-180,height-20), font,1, color, 2, cv2.LINE_AA)
                       if ret:
                            if self.rec ==1 :
                                print("frame")
                                elapsed_time = time.time() - self.start_time
                                elapsed_time_td = timedelta(seconds=elapsed_time)
                                # Format the elapsed time as HH:MM:SS
                                elapsed_time_str = str(elapsed_time_td).split('.')[0]
                                #elapsed_time_str = f"Time: {elapsed_time:.4f} s"
                                cv2.putText(frame,f"Time: {elapsed_time_str}", org, font,fontScale, color, thickness, cv2.LINE_AA)
                                self.out.write(frame)
                            simage=QPixmap.fromImage(QImage(frame, width, height, QImage.Format_BGR888))
                            scaled_pixmap = simage.scaled(width,height,Qt.KeepAspectRatio, Qt.FastTransformation)
                            self.ui.lbl_preview_image.setPixmap(scaled_pixmap)
        except Exception as e:
            '''QMessageBox.information(self,"Camera not connected",  # Title of the message box
                                "Please check the camera connection.",  # Main message text
                                QMessageBox.Ok)'''
            logging.error(f"mainscreen|update|Error in update:{e}")

    #this method is used for flipimage
    def flipimage(self):
            self.flip=1

    #this method is used for flipimage1
    def flipimage1(self):
            self.flip=0

    #this method is used for takeing the  snapshot
    def snapshot(self):
        try:
            ret,frame= self.get_frame()
            #frame=cv2.flip(frame, self.flip)
            height, width = frame.shape[:2]
            dt=time.strftime("%d-%m-%Y-%H-%M-%S")
            wlogo= cv2.imread('/home/npdslitlamp/SLTAPPNEW/images/watermarklogo.png', cv2.IMREAD_UNCHANGED)
            # Resize the logo to fit into the camera frame (adjust the size as needed)
            logo_width = 120  # Width of the logo in the frame
            logo_height = int((logo_width / wlogo.shape[1]) * wlogo.shape[0])+25  # Maintain aspect ratio
            wlogo = cv2.resize(wlogo, (logo_width, logo_height))
            logo_height, logo_width = wlogo.shape[:2]
            x_offset = width-120
            y_offset =height-90
            self.count=self.count+1
            # Check if the region fits within the frame
            if y_offset + logo_height <= height and x_offset + logo_width <= width:
                  # Split the logo into its color (BGR) and alpha (transparency) channels
                  if wlogo.shape[2] == 4:  # Check if there's an alpha channel
                      overlay_color = wlogo[:, :, :3]
                      overlay_alpha = wlogo[:, :, 3] / 255.0  # Normalize alpha to 0-1
                      # Extract the region of interest (ROI) from the frame
                      roi = frame[y_offset:y_offset + logo_height, x_offset:x_offset + logo_width]
                      # Perform alpha blending between the logo and the ROI
                      for c in range(0, 3):  # For each color channel (BGR)
                          roi[:, :, c] = (overlay_alpha * overlay_color[:, :, c] + (1 - overlay_alpha) * roi[:, :, c])
                      # Place the blended ROI back into the frame
                      frame[y_offset:y_offset + logo_height, x_offset:x_offset + logo_width] = roi
                  else:
                      # If there's no alpha channel, just place the logo directly
                      frame[y_offset:y_offset + logo_height, x_offset:x_offset + logo_width] = wlogo
            if ret:
                if self.ODOS != '':
                    print("hii i know this"+self.visit_path)
                    simage=QPixmap.fromImage(QImage(frame, width, height, QImage.Format_BGR888))
                    simage.save(self.visit_path +dt+"-"+self.current_eye+""+str(self.count)+".bmp", format='bmp')
                    self.add_images_from_folder_to_captuerlist(self.ui.lv_capture_image,self.visit_path )
                    #self.ui.ImageList_Captuer.itemClicked.connect(self.captuer_on_item_clicked)
                    print(time.time()*1000)
                    print('SNAP')
                    logging.info(f"mainscreen|snapshot|Taking a snap...!")
                else:
                    QMessageBox.information(self,"Select button",  # Title of the message box
                                                    "Please select ODOS button.",  # Main message text
                                                    QMessageBox.Ok)
                    self.count =-1
        except Exception as e:
            logging.error(f"mainscreen|snapshot|Error in snapshot:{e}")

    #this method is used for adding the image from folder to capture list
    def add_images_from_folder_to_captuerlist(self,list_view: QListView ,folder_path: str):
        try:
            """Add images from a folder to a QListWidget as items with fixed sizes."""
            if len(folder_path) != 0:
                if not os.path.exists(folder_path):
                    print(f"Folder not found: {folder_path}")
                    return
                supported_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
                self.visitfiles = sorted(os.listdir(folder_path))
                self.patientimage_count=0
                # Iterate over files in the folder
                for filename in sorted(os.listdir(folder_path)):
                    if filename.lower().endswith(supported_extensions):
                        file_path = os.path.join(folder_path, filename)
                        # list files in img directory

                        self.model = QStandardItemModel()
                        self.ui.lv_capture_image.setModel(self.model)
                        # Set view to vertical-first grid layout (column-wise flow)
                        self.ui.lv_capture_image.setViewMode(QListView.IconMode)
                        self.ui.lv_capture_image.setResizeMode(QListView.Adjust)
                        self.ui.lv_capture_image.setMovement(QListView.Static)
                        self.ui.lv_capture_image.setFlow(QListView.TopToBottom)     # Fill top-to-bottom, then next column
                        self.ui.lv_capture_image.setWrapping(True)                  # Allow wrapping to new columns
                        self.ui.lv_capture_image.setSpacing(10)
                        self.ui.lv_capture_image.setIconSize(QSize(100, 80))        # Slightly shorter height for better layout
                        for filename in sorted(os.listdir(folder_path)):
                            file_path = os.path.join(folder_path, filename)
                            item = QStandardItem()
                            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                                pixmap = QPixmap(file_path)
                                if not pixmap.isNull():
                                    # Scale maintaining aspect ratio, fixed height
                                    pixmap = pixmap.scaled(100, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                                    item.setIcon(QIcon(pixmap))
                                    name =filename.rsplit('.', 1)[0]
                                    fname = name.split("-")[-1]
                                    item.setText(fname)  # Show label without file extension
                                    item.setTextAlignment(Qt.AlignCenter)
                                    item.setData(file_path)
                                    item.setEditable(False)
                                    self.model.appendRow(item)
                                else:
                                    logging.warning(f"Invalid image: {file_path}")

                            elif filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv')):
                                video_icon_path = '/home/npdslitlamp/SLTAPPNEW/images/video-clip.png'
                                if os.path.exists(video_icon_path):
                                    item.setIcon(QIcon(video_icon_path))
                                item.setText(filename.rsplit('.', 1)[0])
                                item.setTextAlignment(Qt.AlignCenter)
                                item.setData(file_path)
                                item.setEditable(False)
                                self.model.appendRow(item)

            logging.info(f"mainscreen|add_images_from_folder_to_capturelist|Add a image to the folder: {folder_path}")
        except Exception as e:
            logging.error(f"mainscreen|add_filecount=+1images_from_folder_to_capturelist|Error in adding image list: {e}")

    def doctordialog(self):
        dialog = doctorclass(self)
        dialog.doctor_signal.connect(self.on_dialog_signal)  # Changed to doctor_signal
        dialog.exec()

    def on_dialog_signal(self, message):
        self.loaddoctor()
        self.load_data()
        print(f"Signal received in main window with message: {message}")

    #this method is for doctor refresh
    def doc_refresh(self):
        self.load_data()
        self.ui.txt_searchbox_doctor.setText("")

    def frameslideanimation(self,startpos,endpos,yloction):
        if self.state==0:
            self.animation= QPropertyAnimation(self.ui.frame_image_list,b'geometry')
            self.animation.setDuration(400)#mm seconds
            self.animation.setStartValue(QRect(startpos,self.ui.frame_image_list.y(),yloction,yloction))
            self.animation.setEndValue(QRect(endpos,self.ui.frame_image_list.y(),yloction,yloction))
            self.animation.start()
            self.state=1
            self.ui.btn_slider_2.show()
            self.ui.btn_slider.hide()
        else:
            self.animation= QPropertyAnimation(self.ui.frame_image_list,b'geometry')
            self.animation.setDuration(400)#mm seconds
            self.animation.setStartValue(QRect(startpos,self.ui.frame_image_list.y(),yloction,yloction))
            self.animation.setEndValue(QRect(endpos,self.ui.frame_image_list.y(),yloction,yloction))
            self.animation.start()
            self.state=0
            self.ui.btn_slider.show()
            self.ui.btn_slider_2.hide()

    def frameslideanimation2(self,startpos,endpos,yloction):
            self.animation1= QPropertyAnimation(self.ui.frame_buttons,b'geometry')
            self.animation1.setDuration(100)#mm seconds
            self.animation1.setStartValue(QRect(0,self.ui.frame_buttons.y(),270,270))
            self.animation1.setEndValue(QRect(20,self.ui.frame_buttons.y(),270,270))
            self.animation1.start()
            print('start')

    def sw_2(self,index):
        self.ui.stackedWidget_2.setCurrentIndex(index)
        if index== 6:
            self.frameslideanimation2(0,55,0)
    def sw(self,index):
            self.ui.stackedWidget.setCurrentIndex(index)
    def setting_sw(self,index):
            self.ui.stackedWidget_setting.setCurrentIndex(index)
            if index==0:
                 self.ui.btn_dtime_set.setStyleSheet(self.stylesheet_unchecked)
                 self.ui.btn_report_set.setStyleSheet(self.stylesheet_checked)
            if index==1:
                self.ui.btn_dtime_set.setStyleSheet(self.stylesheet_checked)
                self.ui.btn_report_set.setStyleSheet(self.stylesheet_unchecked)

    '''def odos_state(self):
        if self.odos==0:
            self.odos=1
            self.ui.btn_odos.setText('OS')
        else:
            self.odos=0
            self.ui.btn_odos.setText('OD')'''

    #this method is for the load the config file
    def load_config(self):
        try:
            with open('config.txt', 'r') as file:
                lines = file.readlines()
            # Print each line
            for line in lines:
                self.dynamic_list.append(line.strip())
            print(self.dynamic_list)
            paths = [folder.split('=')[1].strip("'") for folder in self.dynamic_list]
            # Printing the paths
            count=0
            for path in paths:
                if count==0:
                    self.folder=path
                    print (self.folder)
                if count==1:
                    self.tempfolder=path
                if count==2:
                    self.dbfile=path
                if count==3:
                    self.reportfolder=path
                    print(self.reportfolder)
                if count==4:
                    self.Marker=path
                if count==6:
                    self.backup_path=path
                count+=1
            logging.info(f"mainscreen|load_config|Config(path patient,database,temp,Logo) are successfully add to theri location...")
        except OSError as e:
                    logging.error(f"mainscreen|load_config|Error in config: {e}")

    #this method is for the list the patient data in the table
    def ListPatient(self):
        try:
            self.ui.txt_searchbox.clear()
            #self.ui.txt_search.clear()
            #self.ui.listWidget.clear()
            self.cursor=self.connection.cursor()
            #Visitid ,MRNO ,PName ,PAge ,PGender ,VDate ,EDR ,Proce ,EEye ,tbl_Patient.Archive
            query = """SELECT MRNO,Visitid, PName, PAge, PGender, VDate, EEye,EDR FROM PatientList_View ORDER BY Visitid DESC"""
            self.cursor.execute(query)
            rows=self.cursor.fetchall()
            data = str(len(rows))
            self.ui.lbl_patient_count.setText(f"Patient({data})")
            #self.ui.mytable.clear()
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.setHorizontalHeaderLabels(['Patient ID', 'Visitid','Patient Name', 'Age', 'Gender', 'Visit Date', 'Eye','Doctor'])
            self.ui.tableWidget.setColumnWidth(3,50);
            self.ui.tableWidget.setColumnWidth(6,50);
            self.ui.tableWidget.setColumnWidth(0,120);
            self.ui.tableWidget.setColumnWidth(1,120);
            self.ui.tableWidget.setColumnWidth(2,280);
            for lineIndex, lineData in enumerate(rows):
                if lineIndex >= 0:
                    # SET COLUMN COUNT
                    self.ui.tableWidget.setColumnCount(len(lineData))
                    #self.ui.mytable.setColumnCount(len(lineData))
                    # ADD NEW ROW
                    self.ui.tableWidget.insertRow(lineIndex)
                    #self.ui.mytable.insertRow(lineIndex)
                    for columnIndex, columnData in enumerate(lineData):
                        # FILL ROW
                        self.item=QtWidgets.QTableWidgetItem(str(columnData))
                        self.item.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.ui.tableWidget.setItem(lineIndex, columnIndex, self.item)

                        #self.ui.mytable.setItem(lineIndex, columnIndex, QtWidgets.QTableWidgetItem(str(columnData))
            self.cursor.close()
            logging.info(f"mainscreen|ListPatient|list the patient in the dashboard..")
        except Exception as e:
            logging.error(f"mainscreen|ListPatient|Error in dasabase:{e}")


    #this method is used for serach the patient in the list patientList_view
    def SearchListPatient(self):
                try:
                    cursor=self.connection.cursor()
                    #Visitid ,MRNO ,PName ,PAge ,PGender ,VDate ,EDR ,Proce ,EEye ,tbl_Patient.Archive
                    searchdata=self.ui.txt_searchbox.text().strip()
                    if searchdata != "":
                        #query = "SELECT MRNO,Visitid,PName, PAge, PGender, VDate, EEye,EDR FROM PatientList_View where MRNO='"+searchdata+"' ORDER BY Visitid DESC"
                        query = "SELECT MRNO, Visitid, PName, PAge, PGender, VDate, EEye, EDR FROM PatientList_View WHERE UPPER(MRNO) LIKE '%' || UPPER('" + searchdata + "') || '%' ORDER BY Visitid DESC"
                        cursor.execute(query)
                        rows=cursor.fetchall()
                        data = len(rows)
                        print(data)
                        if data==0:
                            QMessageBox.information(self, "Info", "No data found")
                            self.refresh()
                        else:
                            self.ui.lbl_patient_count.setText(f"Patient({data})")
                            self.ui.tableWidget.setRowCount(0)
                            self.ui.tableWidget.setHorizontalHeaderLabels(['Patient ID', 'Visitid','Patient Name', 'Age', 'Gender', 'Visit Date', 'Eye','Doctor'])
                            for lineIndex, lineData in enumerate(rows):
                                    if lineIndex >= 0:
                                    # SET COLUMN COUNT
                                        self.ui.tableWidget.setColumnCount(len(lineData))
                                        # ADD NEW ROW
                                        self.ui.tableWidget.insertRow(lineIndex)
                                        for columnIndex, columnData in enumerate(lineData):
                                        # FILL ROW
                                            self.ui.tableWidget.setItem(lineIndex, columnIndex, QtWidgets.QTableWidgetItem(str(columnData)))
                                    else:
                                        QMessageBox.information(self, "Info", "No data found")
                    logging.info(f"mainscreen|SearchListPatient|User serach a patientid {searchdata} in the list")
                except Exception as e:
                    logging.error(f"maniscreen|SearchListPatient|Error in searching the list:{e}")
                finally:
                        cursor.close()

    #this method is used for load the doctor data in the list
    def load_data(self):
        try:
            cursor=self.connection.cursor()
            self.ui.tableWidget_3.setRowCount(0)
            cursor.execute("SELECT Doctorname,Specality FROM tbl_doctor")
            rows = cursor.fetchall()
            count = len(rows)
            self.ui.lbl_doctor_count.setText(f"Doctor({count})")
            for row in rows:
                row_count = self.ui.tableWidget_3.rowCount()
                self.ui.tableWidget_3.insertRow(row_count)
                for col, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                    self.ui.tableWidget_3.setItem(row_count, col, item)
            logging.info(f"mainscreen|load_data|load the doctor data in the list..")
        except Exception as e:
            logging.error(f"mainscreen|load_data|Error in load doctor data:{e}")

    #this method is for searching the doctor in the list
    def SearchListDoctor(self):
        try:
            cursor=self.connection.cursor()
            #Visitid ,MRNO ,PName ,PAge ,PGender ,VDate ,EDR ,Proce ,EEye ,tbl_Patient.Archive
            searchdata=self.ui.txt_searchbox_doctor.text().strip()
            if searchdata !="":
                query = "SELECT Doctorname,Specality FROM tbl_doctor where UPPER(Doctorname) LIKE '%' || UPPER('" + searchdata + "') || '%' "
                cursor.execute(query)
                rows=cursor.fetchall()
                count = len(rows)
                self.ui.lbl_doctor_count.setText(f"Doctor({count})")
                self.ui.tableWidget_3.setRowCount(0)
                self.ui.tableWidget_3.setHorizontalHeaderLabels([' Speciality', 'Doctor Name'])
                for lineIndex, lineData in enumerate(rows):
                        if lineIndex >= 0:
                        # SET COLUMN COUNT
                            self.ui.tableWidget_3.setColumnCount(len(lineData))
                            # ADD NEW ROW
                            self.ui.tableWidget_3.insertRow(lineIndex)
                            for columnIndex, columnData in enumerate(lineData):
                            # FILL ROW
                                self.ui.tableWidget_3.setItem(lineIndex, columnIndex, QtWidgets.QTableWidgetItem(str(columnData)))
            logging.info(f"mainscreen|SearchListDoctor|User serach a patientid {searchdata} in the list")
        except Exception as e:
            logging.error(f"maniscreen|SearchListPatient|Error in searching the list:{e}")
        finally:
                cursor.close()

    #this method is for the checking the database
    def check_db(self):
                #DB Connection
                try:

                    self.db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.dbfile)
                    print(self.db_path)
                    if not os.path.exists(self.db_path):
                        print("DB IS NOT THERE")
                        self.create_db(self.db_path)
                    else:
                        print("file is there")
                    self.connection = sqlite3.connect(self.db_path)  # Replace with your database file

                    logging.info(f"mainscreen|check_db|Database connection successfull database file is: {self.dbfile}")
                except sqlite3.Error as e:
                        logging.error(f"maniscreen|check_db|Database connection error: {e}")

    #this method is for Create a database
    def create_db(self,db_path):
                conn = sqlite3.connect(self.db_path)
                conn.close()
                self.create_table()

    #this method is for Create a table in the database
    def create_table(self):
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE VIEW PatientList_View AS SELECT Visitid ,MRNO ,PName ,PAge ,PGender ,VDate ,EDR ,Proce ,EEye ,Summary,tbl_PatientVisit.Archive,FirstName FROM tbl_Patient INNER JOIN tbl_PatientVisit ON tbl_Patient.PatientID = tbl_PatientVisit.MRNO
                """)
                cursor.execute("""
                            CREATE TABLE IF NOT EXISTS tbl_CameraData (
                                `Sno` INTEGER PRIMARY KEY AUTOINCREMENT, `Mode` TEXT, `BacklightCompensation` TEXT, `Brightness` INTEGER, `Contrast` INTEGER, `Gain` INTEGER, `Gamma` INTEGER, `Hue` INTEGER, `Saturation` INTEGER, `Sharpness` INTEGER, `WhiteBalance` INTEGER, `Exposure` INTEGER, `Focus` INTEGER, `Iris` INTEGER, `Pan` INTEGER, `Roll` INTEGER, `Tilt` INTEGER, `Zoom` INTEGER, `AWB` INTEGER, `AEX` INTEGER
                            )
                        """)
                cursor.execute("""
                            CREATE TABLE IF NOT EXISTS tbl_EmailSetting (
                                `Sno` INTEGER PRIMARY KEY AUTOINCREMENT, `Emailserver` TEXT, `Smtpserver` TEXT, `Port` NUMERIC, `Username` TEXT, `Password` TEXT,`Message` TEXT , `Status` TEXT
                            )
                """)
                cursor.execute("""
                            CREATE TABLE IF NOT EXISTS tbl_Patient(
                                `Sno` INTEGER PRIMARY KEY AUTOINCREMENT, `PatientID` TEXT,`FirstName` TEXT, `LastName` TEXT, `DOB` TEXT, `Gender` TEXT, `EDoctor` TEXT, `RDR` INTEGER, `Archive` TEXT, `Address` TEXT, `Email` TEXT, `Mobile` NUMERIC, `DiagInfo` TEXT, `CVisit` TEXT, `LVisit` TEXT,`Age` TEXT
                            )
                """)
                cursor.execute("""
                            CREATE TABLE IF NOT EXISTS tbl_PatientVisit (
                                `Sno` INTEGER PRIMARY KEY AUTOINCREMENT, `Visitid` TEXT,`MRNO` TEXT, `PName` TEXT, `PAge` TEXT, `PGender` TEXT, `VDate` TEXT, `EDR` TEXT, `Proce` TEXT, `EEye` TEXT, `Summary` TEXT, `ODR` TEXT, `EYE` TEXT, `Archive` TEXT, `DiagInfo` TEXT, `CVisit` TEXT, `Age` TEXT
                            )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tbl_Utitlity (
                        `Sno` INTEGER PRIMARY KEY AUTOINCREMENT, `CameraId` INTEGER, `Devicename` TEXT, `VResolution` INTEGER, `IResolution` INTEGER,`AspectRatio` TEXT, `Spath` TEXT, `Mirror` TEXT
                    )
                """)
                cursor.execute("""
                    INSERT INTO tbl_Utitlity (CameraId, Devicename, VResolution, IResolution, AspectRatio, Spath, Mirror)VALUES (0,"HD USB Camera",0,1,"NULL","/home/npdslitlamp/Pictures/","No")
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS tbl_doctor (
                        `Sno` INTEGER PRIMARY KEY AUTOINCREMENT, `Doctorname` TEXT, `Specality` TEXT, `SetDefault` TEXT
                    )
                """)
                cursor.execute("""
                    INSERT INTO tbl_doctor(Doctorname,Specality,SetDefault)VALUES ("Dr.Smith","IOL","True")
                """)
                cursor.execute("""
                    CREATE TABLE "tbl_ReportData" (
                            "Sno"	INTEGER,
                            "ReportType"	TEXT,
                            "Hospitalname"	TEXT,
                            "Doctorname"	TEXT,
                            "Doctorlname"	TEXT,
                            "Address"	TEXT,
                            "Address2"	TEXT,
                            "City"	TEXT,
                            "State"	TEXT,
                            "Country"	TEXT,
                            "Pincode"	TEXT,
                            "Mobile"	TEXT,
                           "Emailid"	TEXT,
                            "Time"	TEXT,
                            "Logo"	BLOB,
                            PRIMARY KEY("Sno" AUTOINCREMENT)
                    )
                """)

                cursor.execute("""
                    INSERT INTO tbl_ReportData(ReportType, Hospitalname, Doctorname, Doctorlname, Address, Address2, City, State, Country, Pincode ,Mobile, Emailid, Time,Logo) VALUES ("Header", "Eye Hospital aurolab", "DR.SHANKARANATHAN", "", "1 Anna Nagar St", "", "Madurai", "Tamil Nadu", "India", "625 020", "8649839093", "patient@caree.com", "7:30 am to 5:00 pm","")
                """)
                conn.commit()
                conn.close()


    #this method is find which key is pressed by user
    def keyPressEvent(self, event):
        try:
            # This method is called when a key is pressed
            key = event.key()
            key_name = QKeySequence(key).toString()
            modifiers = event.modifiers()
            logging.info(f"mainscreen|keyPressEvent|{key_name}.")
            if key == Qt.Key_F12:
                 if self.snap==1:
                      self.snapshot()
                      logging.info(f"mainscreen|keyPressEvent|image snap clicked ")
            '''if key==Qt.Key_Delete:
                 print(self.visit_id)
                 #self.deletevisit(self.visit_id)
                 logging.info(f"mainscreen|keyPressEvent|For delete_action call the deletevisit method with parameter")
                 self.ListPatient()'''

        except Exception as e:
            logging.error(f"mainscreen|keyPressEvent| Error in the event: {e}")
            print(e)

    #this method is used for exit form the software/appliction
    def Exit(self):
        try:
            reply = QMessageBox.question(self, "Confirmation", "Are you sure you want to Shutdown?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            logging.warning(f"mainscreen|Exit|Show the pop-up Are you sure you want to Shutdown?")
            if reply == QMessageBox.Yes:
                self.dbbackup()
                self.logbackup()
                self.unmount_drive(self.backup_path)
                os.system("echo '1' | sudo -S shutdown -h now")
                logging.info(f"mainscreen|Exit|In pop-up user click yes so shutdown...")
                #sys.exit() # Proceed with the close event
            else:
                print('Not Close')
                #event.ignore()  # Ignore the close event to prevent the window from closing
                logging.info(f"mainscreen|Exit|ignore the Shutdown event")
        except Exception as e:
            logging.error(f"mainscreen|Exit|Error in shutdown:{e}")

    #this method is used for closed or shutdown the sofftware
    def closeEvent(self, event):
        try:
            # This method is called when the window is closed (e.g., the user clicks the close button)
            logging.info(f"mainscreen|closeEvent|This method is called when the window is closed")
            self.dbbackup()
            self.logbackup()
            reply = QMessageBox.question(self, "Confirmation", "Are you sure you want to Shutdown?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            logging.warning(f"mainscreen|closeEvent|Pop-up show,'Confirmation', Are you sure you want to Shutdown?..")
            if reply == QMessageBox.Yes:
                event.accept()  # Proceed with the close event
                self.unmount_drive(self.backup_path)
                logging.info(f"mainscreen|closeEvent|In Pop-up they click 'YES', so system is shutdown.")
                os.system("echo '1' | sudo -S shutdown -h now")
            else:
                event.ignore()  # Ignore the close event to prevent the window from closing
                logging.info(f"mainscreen|closeEvent|In Pop-up they click 'NO', so system is not shutdown.")
        except Exception as e:
            logging.error(f"mainscreen|closeEvent|Error in closeEvent:{e}")

    #this method is for check camera
    def is_camera_available(self):
        try:
            cap = self.vid
            self.c_state = ""
            if cap.isOpened():
                cap.release()
                self.__initcamera()
            else:
                self.__initcamera()
        except Exception as e:
            logging.error(f"mainscreen|camera_check|Error in camera_check:{e}")

    #unmount the hard disk
    def unmount_drive(self,mount_drive):
        try:
            command=["umount",mount_drive]
            subprocess.run(command,check=True)
            logging.info(f"mainscreen|unmount_drive|Drive at {mount_drive} umounted successfully.")
            print(f"Drive at {mount_drive} umounted successfully.")
        except subprocess.CalledProcessError as e:
            logging.error(f"mainscreen|unmount_drive|Error in Drive at {mount_drive} umounted:{e}.")
            print(f"Drive at {mount_drive} umounted:{e}")
        except Exception as e:
            logging.error(f"mainscreen|unmount_drive|Error in Drive at {mount_drive} umounted:{e}")
            print(f"Drive at {mount_drive} umounted:{e}")
    #this method is for the database backup
    def dbbackup(self):
        print(self.backup_path)
        path=self.backup_path+"DBBackup/ThirdI.db"
        print(path)
        logging.info(f"mainscreen|dbbackup|Database data are successfully copy to Hard Disk in the shutdwon")
        shutil.copy(self.db_path,path)

    #this method is for the log bakckup
    def logbackup(self):
        path=self.backup_path+"LOGS/backuplog.log"
        logging.info(f"mainscreen|logbackup|Log data are successfully copy to Hard Disk in the shutdwon")
        shutil.copy("/home/npdslitlamp/SLTAPPNEW/LOGS/main.log",path)

    #this method is for the checking the hard disk connection / hard disk powersupply
    def list_usb_ports1(self):
        mount_point= ["/media/npdslitlamp"]
        self.usb_drive= []
        self.HWstate =0
        for mount_point in mount_point:
            if os.path.exists(mount_point):
                self.drive = os.listdir(mount_point)
                for dv in self.drive:
                    print(dv)
                    print("SSD:"+self.HName)
                    if self.HName == dv:
                        self.HWstate = 1
                        self.ui.lbl_status.setText('')
                    else:
                        self.HWstate = 0
                if self.HWstate == 0:
                    self.ui.lbl_status.setText("Validating Storage Media")
                    QMessageBox.information(self, "Info", "Check The harddisk power supply")
                    logging.info(f"mainscreen|list_usb_ports1|In Pop-up will show, so system is shutdown.")
                    os.system("echo '1' | sudo -S shutdown -h now")

    #This method checks for any USB connection other than "AUROSSD"
    def list_usb_ports(self):
        try:
            mount_point= "/media/npdslitlamp"
            self.usb_drive1=[]
            drive1 = os.listdir(mount_point)
            for dv in drive1:
                print("SSD Drive Name"+self.HName)
                # Check if drive name doesn't start with "AUROSSD"
                if dv != self.HName:
                    full_path = os.path.join(mount_point, dv)                    
                    if os.path.ismount(full_path):
                        self.usb_drive1.append(full_path)
                    else:
                        print("NO USB connected")
                        QMessageBox.information(self, "Info", "NO USB connected!")
            if not self.usb_drive:
                print("No valid USB drives connected (excluding AUROSSD*)")
                logging.info("mainscreen|list_usb_ports|Please connect a USB pendrive ")
            else:
                print("Mount point does not exist")
                logging.info(f"mainscreen|list_usb_ports|Mount point {mount_point} not found")

        except Exception as e:
            logging.error(f"mainscreen|list_usb_ports|Error in list_usb_ports:{e}")
    #this method is for copying the data to USB
    def copy_usb(self):
        try:
            self.list_usb_ports()
            if not self.usb_drive1:
                    QMessageBox.information(self, "Info", "No valid USB drive found. Please connect a USB.")
                    return
            if len(self.usb_drive1) > 0:
                if self.visitfolder != '':
                    usb_path=os.path.join(self.usb_drive1[0], time.strftime("%d-%m-%Y-%H-%M-%S"))
                    os.makedirs(usb_path)
                    for filename in os.listdir(self.visitfolder):
                        source_file = os.path.join(self.visitfolder, filename)
                        if os.path.isfile(source_file):
                            shutil.copy(source_file, usb_path)
                            print(usb_path)
                    QMessageBox.information(self, "Info", "Data copy to the USB Pendrive Successfully!")
                    logging.info("mainscreen|copy_usb|Data copy to the USB Pendrive Successfully!")
                else:
                    QMessageBox.information(self, "Info", "select the patient and Then click copy")
                    logging.info("mainscreen|copy_usb|select the patient and Then click copy")
            else:
                QMessageBox.information(self, "Info", "Check the USB Pendrive Connection")
                logging.info("mainscreen|copy_usb|Check the USB Pendrive Connection")

        except Exception as e:
            logging.error(f"mainscreen|copy_usb|Error in copy_usb:{e}")

    def mplayer_create(self):
        # Create the media player and video widget
        self.player = QMediaPlayer(self)
        self.videoWidget = QVideoWidget(self)
        self.videoWidget.resize(1680,1000)
        self.player.mediaStatusChanged.connect(self.handle_media_status_changed)
        # Set video output to video widget
        self.player.setVideoOutput(self.videoWidget)
        self.player.setPlaybackRate(1)
        self.ui.medialayout.addWidget(self.videoWidget)
    def playMedia(self):
        try:
            self.player.play()
            self.ui.lbl_status_mplayer.setText("Playing")
            self.ui.btn_mstop.setIcon(QIcon.fromTheme("media-playback-pause"))
            logging.info(f"dashboard|palyMedia|Media are play...")
        except Exception as e:
            logging.error(f"dashboard|palyMedia|Error in play:{e}")

    def stopMedia(self):
        try:
            self.player.pause()
            self.ui.lbl_status_mplayer.setText("Pause")
            logging.info(f"dashboard|stopMedia|Media is stop")
        except Exception as e:
            logging.error(f"dashboard|stopMedia|Error in stop:{e}")

    def handle_media_status_changed(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.ui.lbl_status_mplayer.setText("Stop")            
            self.ui.btn_mstop.setIcon(QIcon.fromTheme("media-playback-stop"))
            print("Playback has reached the end of the media.")
    def closeMedia(self):
        try:
            self.player.stop()
            self.sw_2(0)
            self.ui.lbl_status_mplayer.setText("Stop")
            logging.info(f"myfile|closeMedia|Media is close")
        except Exception as e:
            logging.error(f"myfile|closeMedia|Error in close:{e}")

class report:
    def __init__(self,db_path = None):
        self.conn = db_path
        logging.info(f"Report|__init__|Database connection established.{db_path}")
    def create_pdf(self,output_path, report_data, patient_data, image_paths,logo):
        try:
            c = canvas.Canvas(output_path, pagesize=A4)
            width, height = A4
            print(logo)
            def add_header():
                        try:
                            """Add the report header."""
                            logging.info(f"Report|create_pdf|add_header|Add the report Header & Logo to Report PDF...")
                            if report_data['ReportType']== 'Header':
                                logging.info(f"Report|create_pdf|add_header|Add the report HeaderType is Header in Report PDF...")
                                logo_path = logo
                                logo_width = 150
                                logo_height = 150
                                x_logo = 43
                                y_logo = height - 165
                                if os.path.exists(logo_path):
                                    img = ImageReader(logo_path)
                                    c.drawImage(img, x_logo, y_logo, logo_width, logo_height, preserveAspectRatio=False)
                                c.setFont("Helvetica-Bold", 16)
                                c.drawString(220, height - 50, report_data['Hospitalname'])
                                c.setFont("Helvetica", 10)
                                c.drawString(220, height - 70, f"{report_data['Doctorname']}")
                                c.drawString(220, height - 90, f"Address: {report_data['Address']},{report_data['City']},{report_data['State']}-{report_data['Pincode']} {report_data['Country']}")
                                c.drawString(220, height - 110, f"Phone:{report_data['Mobile']}")
                                c.line(30, height - 170, width - 30, height - 170)
                            logging.info(f"Report|create_pdf|add_header|Add the report HeaderType is NoHeader to Report PDF...")
                            c.setFont("Helvetica-Bold", 14)
                            c.drawString(250, height - 185, "Patient Report")
                        except Exception as e:
                                logging.error(f"Report|create_pdf|add_header|Error adding header: {e}")

            def add_patient_table():
                try:
                    """Add the patient details table."""
                    logging.info(f"Repot|create_pdf|add_patient_table|Patient details are add to the Report PDF...")
                    data = [
                        ["MRNO", "Patient Name", "Age"],
                        [patient_data['MRNO'], patient_data['PName'], patient_data['PAge']],
                        ["Gender", "Doctor", "Visit Date"],
                        [patient_data['PGender'], patient_data['EDR'], patient_data['VDate']],
                    ]
                    table = Table(data, colWidths=[150, 150, 150])
                    table.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
                        ('BACKGROUND', (0, 2), (-1, 2), colors.lightblue),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                        ('TEXTCOLOR', (0, 2), (-1, 2), colors.black),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTNAME', (0, 2), (-1, 2), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, -1), 10),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                        ('BOTTOMPADDING', (0, 2), (-1, 2), 8),
                        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
                    ]))
                    table.wrapOn(c, width, height)
                    table.drawOn(c, 60, height - 280)

                except Exception as e:
                        logging.error(f"Report|create_pdf|add_patient_table|Error adding patient table: {e}")

            def add_images_on_first_page(images):
                try:
                    logging.info(f"Report|create_pdf|add_images_on_first_page|Adding a image to first page in the pdf...")
                    y_position = height - 440
                    x_start = 50
                    cell_width = 250
                    cell_height = 150
                    padding = 5

                    for i, img_path in enumerate(images[:6]):
                        if os.path.exists(img_path):
                            img = ImageReader(img_path)
                            c.drawImage(img, x_start, y_position, cell_width, cell_height, preserveAspectRatio=False)
                            x_start += cell_width + padding

                            if (i + 1) % 2 == 0:
                                x_start = 50
                                y_position -= cell_height + padding

                except Exception as e:
                    logging.error(f"Report|create_pdf|add_images_on_first_page|Error add_images_on_first_page: {e}")

            def add_remaining_images(images):
                try:
                    logging.info(f"Report|create_pdf|add_remaining_images|Adding a image to Second the pdf...")
                    c.showPage()
                    y_position = height - 200
                    x_start = 50
                    cell_width = 250
                    cell_height = 150
                    padding = 5

                    for i, img_path in enumerate(images[6:]):
                        if os.path.exists(img_path):
                            img = ImageReader(img_path)
                            c.drawImage(img, x_start, y_position, cell_width, cell_height, preserveAspectRatio=False)
                            x_start += cell_width + padding

                            if (i + 1) % 2 == 0:
                                x_start = 50
                                y_position -= cell_height + padding

                            if y_position < 100:
                                c.showPage()
                                y_position = height - 200

                except Exception as e:
                    logging.error(f"Report|create_pdf|add_remaining_images|Error add_remaining_images: {e}")


            add_header()
            add_patient_table()
            add_images_on_first_page(image_paths)
            add_remaining_images(image_paths)
            c.save()

        except Exception as e:
                logging.error(f"Report|create_pdf|Error in creating PDF: {e}")



    def fetch_data(self, patient_id):
            #conn = None
            try:
                logging.info(f"Report|fetch_data|Fetching the data form the database...")
                #conn = sqlite3.connect(self.db_path)
                cursor = self.conn.cursor()
                cursor.execute("SELECT * FROM tbl_ReportData LIMIT 1")
                report_row = cursor.fetchone()
                if not report_row:
                    raise ValueError("No data found in tbl_ReportData.")
                report_columns = [col[0] for col in cursor.description]
                report_data = dict(zip(report_columns, report_row))

                # Fetch patient data
                cursor.execute("SELECT * FROM tbl_PatientVisit WHERE Visitid = ?", (patient_id,))
                patient_row = cursor.fetchone()
                if not patient_row:
                    raise ValueError("No data found in tbl_Patient.")
                patient_columns = [col[0] for col in cursor.description]
                patient_data = dict(zip(patient_columns, patient_row))

                return report_data, patient_data
            except sqlite3.Error as e:
                print(f"Database error: {e}")
                logging.error(f"Report|fetch_data|Database error: {e}")
                return {}, {}
            except ValueError as ve:
                print(f"Data error: {ve}")
                logging.error(f"Report|fetch_data|Data error: {ve}")
                return {}, {}




    def get_image_paths(self, directory):
        try:
            logging.info(f"Report|get_image_paths|Getting the image path form directory")
            return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.bmp', '.jpg'))]
        except FileNotFoundError:
            print(f"Directory not found: {directory}")
            logging.error(f"Report|get_image_paths|Directory not found: {directory}")
            return []




class ImageListItem(QWidget):
            def __init__(self, image_path: str, parent=None):
                try:
                     super().__init__(parent)
                     self.image_path = image_path
                     # QLabel to display the image
                     self.image_label = QLabel(self)
                     self.set_image_to_label(self.image_label, self.image_path)
                     self.image_label.setAlignment(Qt.AlignCenter)
                     # QLabel to display the image name
                     eyename=os.path.basename(image_path)
                     eye_name=eyename.split('-')
                     filename=eye_name[6].replace('.bmp','')
                     print(filename)
                     self.image_name_label = QLabel(filename, self)
                     self.image_name_label.setAlignment(Qt.AlignCenter)
                     self.image_name_label.setStyleSheet("""
                                 QLabel{
                                        color: #fff;
                                 }
                             """)
                     # Layout for the item: display image on top and name below
                     layout = QHBoxLayout(self)
                     layout.addWidget(self.image_label)
                     #layout.addWidget(self.image_name_label)
                     # Set fixed size for each item in the list
                     self.setFixedSize(170, 155)  # Increased height to accommodate the name
                     logging.info(f"ImageListItem|__init__|ImageListItem class initialising successfully...!")
                except Exception as e:
                     logging.error(f"ImageListItem|__init__|Error:{e}")

            def set_image_to_label(self, label: QLabel, image_path: str):
                 try:
                     """Set a QPixmap to a QLabel from an image file."""
                     if os.path.exists(image_path):
                         pixmap = QPixmap(image_path).scaled(
                             150, 150
                         )
                         label.setProperty('Imagepath',image_path)
                         label.setPixmap(pixmap)
                     else:
                         label.setText("Image not found")
                         logging.error(f"ImageListItem|set_image_to_label|Image not found")
                         label.setStyleSheet("background-color: lightgray;")
                         label.setAlignment(Qt.AlignCenter)

                 except Exception as e:
                     logging.error(f"ImageListItem|set_image_to_label|Error:{e}")

class VideoListItem(QWidget):
       def __init__(self, image_path: str, parent=None):
            try:
                super().__init__(parent)
                self.image_path = image_path
                # QLabel to display the image
                self.image_label = QLabel(self)
                self.set_vimage_to_label(self.image_label, self.image_path)
                self.image_label.setAlignment(Qt.AlignCenter)
                # QLabel to display the image name
                #self.image_name_label = QLabel(os.path.basename(image_path), self)
                #self.image_name_label.setAlignment(Qt.AlignCenter)
                # Layout for the item: display image on top and name below
                layout = QHBoxLayout(self)
                layout.addWidget(self.image_label)
                #layout.addWidget(self.image_name_label)
                # Set fixed size for each item in the list
                self.setFixedSize(120, 105)  # Increased height to accommodate the name
                logging.error(f"VideoListItem|__init__|VideoListItem class initialising successfully...!")
            except Exception as e:
                logging.error(f"VideoListItem|__init__|Error:{e}")

       def set_vimage_to_label(self, label: QLabel, image_path: str):
            try:
                """Set a QPixmap to a QLabel from an image file."""
                if os.path.exists('/home/npdslitlamp/SLTAPP/images/video-clip.png'):
                    pixmap = QPixmap('/home/npdslitlamp/SLTAPP/images/video-clip.png').scaled(
                        100, 100
                    )
                    label.setProperty('Imagepath',image_path)
                    label.setPixmap(pixmap)
                else:
                    label.setText("Image not found")
                    label.setStyleSheet("background-color: lightgray;")
                    label.setAlignment(Qt.AlignCenter)
                logging.error(f"VideoListItem|set_vimage_to_label|Set a QPixmap to a QLabel from an video file")

            except Exception as e:
                    logging.error(f"VideoListItem|set_vimage_to_label|Error:{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = dash_screen()
    widget.showFullScreen()
    sys.exit(app.exec())
