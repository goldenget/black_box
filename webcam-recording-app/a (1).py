from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
import cv2
import numpy as np

import os
import sys
import numpy as np
from gui.ui_create_user import Ui_create_user_window
from gui.ui_display_window import Ui_Display_window
from gui.ui_obd_window import Ui_obd_window
from gui.ui_main_window import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, QThread
from pymongo import MongoClient
from email.mime.multipart import MIMEMultipart
import smtplib
import zipfile
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

client = MongoClient('mongodb+srv://user1:13579007@cluster0.a5eimuq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['video_database']
collection = db['video_collection']

VIDEO_PATH, VIDEO_PATH_2, VIDEO_PATH_3, VIDEO_PATH_4 = 0,1,2,3

#4 threads to run for camera
class CameraThread(QThread):
    update_signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)


    def run(self):
        cap = cv2.VideoCapture(VIDEO_PATH)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("VIDEO 1 ENDED")
                self.update_signal.emit([np.zeros((500, 500, 3), dtype=np.uint8)])
            
            self.update_signal.emit([frame])


class CameraThread2(QThread):
    update_signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)


    def run(self):
        
        cap = cv2.VideoCapture(VIDEO_PATH_2)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("VIDEO 2 ENDED")
                self.update_signal.emit([np.zeros((500, 500, 3), dtype=np.uint8)])

            self.update_signal.emit([frame])


class CameraThread3(QThread):
    update_signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)


    def run(self):
        
        cap = cv2.VideoCapture(VIDEO_PATH_3)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("VIDEO 3 ENDED")
                self.update_signal.emit([np.zeros((500, 500, 3), dtype=np.uint8)])
            
            self.update_signal.emit([frame])


class CameraThread4(QThread):
    update_signal = pyqtSignal(list)

    def __init__(self, parent=None):
        super().__init__(parent)


    def run(self):
        cap = cv2.VideoCapture(VIDEO_PATH_4)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("VIDEO 4 ENDED")
                self.update_signal.emit([np.zeros((500, 500, 3), dtype=np.uint8)])
            
            self.update_signal.emit([frame])


class MainWindow(QMainWindow):
    def __init__(self):
        global  VIDEO_PATH, VIDEO_PATH_2, VIDEO_PATH_3, VIDEO_PATH_4
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.create_user_win = QMainWindow()
        self.create_user_ui = Ui_create_user_window()
        self.create_user_ui.setupUi(self.create_user_win)


        self.display_win = QMainWindow()
        self.display_ui = Ui_Display_window()
        self.display_ui.setupUi(self.display_win)


        self.obd_win = QMainWindow()
        self.obd_ui = Ui_obd_window()
        self.obd_ui.setupUi(self.obd_win)

        self.ui.create_user_btn.clicked.connect(lambda: self.goto_create_window(self))
        self.obd_ui.back_btn.clicked.connect(lambda: self.goto_record_window(self.obd_win))
        self.create_user_ui.back_btn.clicked.connect(lambda: self.goto_main(self.create_user_win))
        self.display_ui.back_btn.clicked.connect(lambda: self.goto_main(self.display_win))
        self.ui.select_user_btn.clicked.connect(lambda: self.select_user())
        self.create_user_ui.create_user_btn.clicked.connect(lambda: self.create_user())
        self.obd_ui.open_obd_btn.clicked.connect(lambda: self.open_application())
        self.display_ui.record_btn.clicked.connect(lambda: self.record_clicked())
        self.display_ui.send_btn.clicked.connect(lambda: self.send_mail())
        self.record = False

        try:
            os.mkdir('captures')
        except:
            pass

        cursor = collection.find()
        self.data = {'username': [], 'email': [], 'phone': []}
        self.selected_user = None

        for document in cursor:
            self.data['username'].append(document['username'])
            self.data['email'].append(document['email'])
            self.data['phone'].append(document['phone'])

        with open("gui/theme.qss", "r") as f:
            stylee = f.read()
            self.setStyleSheet(stylee)
            self.create_user_win.setStyleSheet(stylee)
            self.display_win.setStyleSheet(stylee)
            self.obd_win.setStyleSheet(stylee)

        self.ui.listWidget.addItems(self.data['username'])
        self.show()
        self.recording_done = False

        if not os.path.exists('data-files'):
            os.mkdir('data-files')

        app_path = ''
        try:
            with open('data-files/obd-app-path.txt','r') as r:
                app_path = r.read()
        except:
            app_path = 'design.png'


        self.obd_ui.obd_path.setText(app_path)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out1 = self.out2 = self.out3 = self.out4 = False

        #Trying connection with 1st camera
        try:
            cap_num = self.get_cap_num('data-files/cam1.txt')
            cap = cv2.VideoCapture(cap_num)
            ret, frame = cap.read()
            cap.release()

            if ret:
                VIDEO_PATH = cap_num
                h,w,_ = frame.shape
                self.out1 = cv2.VideoWriter('captures/output1.mp4', fourcc, 20.0, (w, h))
                self.camera_thread = CameraThread()
                self.camera_thread.update_signal.connect(self.main_loop)
                self.camera_thread.start()
        except:
            print('CAMERA 1 FILE NOT FOUND')

        #Trying connection with 2nd camera
        try:
            cap_num = self.get_cap_num('data-files/cam2.txt')
            cap = cv2.VideoCapture(cap_num)
            ret, frame = cap.read()
            cap.release()

            if ret:
                VIDEO_PATH_2 = cap_num
                h,w,_ = frame.shape
                self.out2 = cv2.VideoWriter('captures/output2.mp4', fourcc, 20.0, (w, h))
                self.camera_thread2 = CameraThread2()
                self.camera_thread2.update_signal.connect(self.main_loop2)
                self.camera_thread2.start()
        except:
            print('CAMERA 2 FILE NOT FOUND')

        #Trying connection with 3rd camera
        try:
            cap_num = self.get_cap_num('data-files/cam3.txt')
            cap = cv2.VideoCapture(cap_num)
            ret, frame = cap.read()
            cap.release()
            
            if ret:
                VIDEO_PATH_3 = cap_num
                h,w,_ = frame.shape
                self.out3 = cv2.VideoWriter('captures/output3.mp4', fourcc, 20.0, (w, h))
                self.camera_thread3 = CameraThread3()
                self.camera_thread3.update_signal.connect(self.main_loop3)
                self.camera_thread3.start()
        except:
            print('CAMERA 3 FILE NOT FOUND')

        #Trying connection with 4th camera
        try:
            cap_num = self.get_cap_num('data-files/cam4.txt')
            cap = cv2.VideoCapture(cap_num)
            ret, frame = cap.read()
            cap.release()

            if ret:
                VIDEO_PATH_4 = cap_num
                h,w,_ = frame.shape
                self.out4 = cv2.VideoWriter('captures/output4.mp4', fourcc, 20.0, (w, h))
                self.camera_thread4 = CameraThread4()
                self.camera_thread4.update_signal.connect(self.main_loop4)
                self.camera_thread4.start()
        except:
            print('CAMERA 4 FILE NOT FOUND')

    def get_cap_num(self, path):
        cap_num = ''
        with open(path,'r') as r:
            cap_num = int(r.read())

        if str(cap_num).isnumeric():
            cap_num = int(cap_num)
        
        return cap_num

    def zip_folder(self, folder_path, zip_filename):
        """
        This function takes the videos folder and zips it
        """
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))

    def send_mail(self):
        """
        This function handles the zipping of videos and sending the mail
        It gets triggered when user stops recording.
        """
        if not self.recording_done:
            self.write_msg('Error','Please record something first',QMessageBox.Critical)
            return
        
        receiver_mail = self.selected_user['email']
        self.write_msg('Information', 'Sending Email to ' + receiver_mail, QMessageBox.Information)

        try:
            email_sender = 'kai.official.003@gmail.com'
            email_password = 'ijir vtam hemy uypd'

            # Email content
            msg = MIMEMultipart()
            msg['From'] = email_sender
            msg['To'] = receiver_mail
            msg['Subject'] = f'Recorded videos'

            # Zip the captures folder
            zip_filename = 'captures.zip'
            self.zip_folder('captures', zip_filename)  # Assuming captures folder is in the current directory

            # Attach the zip file to the email
            with open(zip_filename, 'rb') as file:
                attachment = MIMEBase('application', 'octet-stream')
                attachment.set_payload(file.read())
                encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', f'attachment; filename="{zip_filename}"')
                msg.attach(attachment)

            # SMTP Configuration
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_sender, email_password)

            # Send the email
            server.sendmail(email_sender, receiver_mail, msg.as_string())

            # Close the SMTP server
            server.quit()

            # Remove the temporary zip file
            os.remove(zip_filename)
            self.goto_obd_window(self.display_win)
        except Exception as e:
            print(e)
            self.write_msg('Error', 'Error sending Email to ' + receiver_mail, QMessageBox.Critical)
            return

        self.write_msg('Information', 'Email sent to ' + receiver_mail, QMessageBox.Information)

    def record_clicked(self):
        """
        This function gets triggered when user clicks the recording button
        """
        if self.display_ui.record_btn.text() == 'Start Recording':
            self.recording_done = False
            self.record = True
            self.display_ui.record_btn.setText('Stop Recording')
        else:
            self.record = False
            self.display_ui.record_btn.setText('Start Recording')

            try:
                self.out1.release()
            except:
                pass

            try:
                self.out2.release()
            except:
                pass

            try:
                self.out3.release()
            except:
                pass

            try:
                self.out4.release()
            except:
                pass

            self.recording_done = True

   # These functions take user between different UIs 
    def goto_main(self,win):
        win.hide()
        self.show()

    def goto_record_window(self, win):
        
        if self.selected_user is None:
            self.write_msg('Error','No user is selected',QMessageBox.Critical)
            return
        
        win.hide()
        self.display_win.showMaximized()
    
    def goto_obd_window(self, win):
        win.hide()
        self.obd_win.show()

    def goto_create_window(self, win):
        win.hide()
        self.create_user_win.show()
    # -- 

    def create_user(self):
        """
        This function takes all 3 fields and makes a user
        The username has to be unique
        """
        username = self.create_user_ui.username_txt.text().lower()
        email = self.create_user_ui.email_txt.text()
        phone = self.create_user_ui.phone_txt.text()

        if username == '' or email == '' or phone == '':
            self.write_msg('Error','Please fill out all fields to continue!',QMessageBox.Critical)
            return

        existing_user = collection.find_one({'username': username})
        if existing_user:
            self.write_msg('Error','Username already taken!',QMessageBox.Critical)
            return

        user_data = {
            'username': username,
            'email': email,
            'phone': phone
        }
        
        collection.insert_one(user_data)

        self.create_user_ui.username_txt.clear()
        self.create_user_ui.email_txt.clear()
        self.create_user_ui.phone_txt.clear()

        self.data['username'].append(username)
        self.data['email'].append(email)
        self.data['phone'].append(phone)

        self.ui.listWidget.addItem(username)
        self.write_msg('Information','User added successfully!',QMessageBox.Information)

    def select_user(self):
        """
        This function takes the selected user and takes user to recording video
        """
        selected_item = self.ui.listWidget.currentItem()
        text = ''

        if selected_item is not None:
            text = selected_item.text()

        for i, val in enumerate(self.data['username']):
            if val == text:
                self.selected_user = {'username':text, 'email':self.data['email'][i], 'phone':self.data['phone'][i]}
        print(self.selected_user)
        self.goto_record_window(self)

    def write_msg(self, heading, message, icon):
        """
        This function is responsible for making all pop ups
        """
        msg = QMessageBox()
        msg.setWindowTitle(heading)
        msg.setIcon(icon)
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    # These are the functions that run alongside threads
    def main_loop(self, pixmaps):
        try:
            frame = pixmaps[0]
        except:
        
            return
        
        if self.record:
            self.out1.write(frame)
            frame = cv2.circle(frame,(50,50),1,(0,0,255),-1)

        self.set_camera_frame(frame, self.display_ui.camera_view_lbl_1)

    def main_loop2(self, pixmaps):
        try:
            frame = pixmaps[0]
        except:
        
            return
        
        if self.record:
            self.out2.write(frame)
            frame = cv2.circle(frame,(50,50),1,(0,0,255),-1)

        self.set_camera_frame(frame, self.display_ui.camera_view_lbl_2)

    def main_loop3(self, pixmaps):
        try:
            frame = pixmaps[0]
        except:
        
            return
        
        if self.record:
            self.out3.write(frame)
            frame = cv2.circle(frame,(50,50),1,(0,0,255),-1)

        self.set_camera_frame(frame, self.display_ui.camera_view_lbl_3)

    def main_loop4(self, pixmaps):
        try:
            frame = pixmaps[0]
        except:
        
            return
        
        if self.record:
            self.out4.write(frame)
            frame = cv2.circle(frame,(50,50),1,(0,0,255),-1)

        self.set_camera_frame(frame, self.display_ui.camera_view_lbl_4)
    # --

    def open_application(self):
        """
        This function takes a path and opens whatever it finds at that path
        """
        path = self.obd_ui.obd_path.text()
        if path == '':
            self.write_msg('Error','Please provide a path',QMessageBox.Critical)
            return
        try:
            os.system(path)
        except:
            self.write_msg('Error','Can not find the desired application.',QMessageBox.Critical)

    def set_camera_frame(self, frame, label):
        """
        This function sets frame to view
        it takes a frame and a label and sets that frame as labels background
        """
        
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        step = channel * width
        qImg = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qImg)

        label.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
