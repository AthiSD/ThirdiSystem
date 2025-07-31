# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Signal
from ui_doctordialog import Ui_doctor

from PySide6.QtWidgets import QDialog, QMessageBox,QTableWidgetItem,QDialogButtonBox
from PySide6.QtCore import Signal
import sqlite3
import os
import logging
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

class doctorclass(QDialog):
        doctor_signal = Signal(str)  # This is the correct signal name
        def __init__(self, parent=None):
            try:
                super().__init__(parent)
                self.ui = Ui_doctor()
                self.ui.setupUi(self)
                self.dynamic_list = []
                self.dbfile = ''
                self.load_config()
                self.check_db()
                self.ui.btn_savedoctor.clicked.connect(self.save_doctordata)

                logging.info("testpython|__init__|testpython initialising successfully..")
            except Exception as e:
                logging.error(f"testpython|__init__|Error:{e}")

        def check_db(self):
            #DB Connection
            try:
                self.db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), self.dbfile)
                self.connection = sqlite3.connect(self.db_path)  # Replace with your database file
                logging.info(f"testpython|check_db|Database connection successfull database file is: {self.dbfile}")
            except sqlite3.Error as e:
                logging.error(f"testpython|check_db|Database connection error: {e}")

        def save_doctordata(self):
            try:
                logging.info("testpython|save_doctordata|Doctor save method initialising successfully...")
                doctor_name = self.ui.le_doctor_name.text()
                speciality = self.ui.cmb_specialty.currentText()
                if not doctor_name or not speciality:
                    QMessageBox.warning(self, "Input Error", "Doctor name and Speciality must be given!")
                    return
                cursor = self.connection.cursor()
                try:
                    # Get the maximum ID first
                    cursor.execute("SELECT MAX(Sno) FROM tbl_doctor")
                    max_id = cursor.fetchone()[0]
                    doctor_id = 1 if max_id is None else max_id + 1
                    cursor.execute("""INSERT INTO tbl_doctor (Sno, DoctorName, Specality)
                                    VALUES (?, ?, ?)""",
                                    (doctor_id, doctor_name, speciality))
                    self.connection.commit()
                    QMessageBox.information(self, "Success", "Data saved successfully!")
                    logging.info("testpython|save_doctordata|Doctor Data saved successfully...")
                    # Emit the correct signal name
                    self.doctor_signal.emit("Doctor data saved successfully!")
                    self.accept()
                except sqlite3.Error as e:
                    QMessageBox.critical(self, "Database Error", f"Failed to save data: {e}")
                    logging.error(f"testpython|save_doctordata|Database Error Failed to save data: {e}")
                self.cancel_doctordata()
            except Exception as e:
                logging.error(f"testpython|save_doctordata|Error in the save doctor: {e}")

        def cancel_doctordata(self):
            try:
                logging.info(f"testpython|cancel_doctordata|Doctor cancel method initialising successfully...")
                self.ui.le_doctor_name.clear()
                self.ui.cmb_specialty.setCurrentIndex(0)
                self.selected_id = None
                self.ui.le_doctor_name.setFocus()
                logging.info(f"testpython|cancel_doctordata| Cancel method clear all data in the doctor form...")
            except Exception as e:
                logging.error(f"testpython|cancel_doctordata|error in cancel: {e}")

        def load_config(self):
            try:
                with open('config.txt', 'r') as file:
                    lines = file.readlines()
                    logging.info(f"testpython|load_config|read the data form the config.txt file...")
                # Print each line
                for line in lines:
                    self.dynamic_list.append(line.strip())
                print(self.dynamic_list)
                paths = [folder.split('=')[1].strip("'") for folder in self.dynamic_list]
                logging.info(f"testpython|load_config|read the path form the config.txt file: {paths}")
                # Printing the paths
                count=0
                for path in paths:
                    if count==0:
                        self.folder=path
                    if count==1:
                        self.tempfolder=path
                    if count==2:
                        self.dbfile=path
                    count+=1
                    print(path)
            except OSError as e: #FileNotFoundError
                QMessageBox.information(self, "file is missing..!")
                logging.error(f"testpython|load_config|error in cancel: {e}")
