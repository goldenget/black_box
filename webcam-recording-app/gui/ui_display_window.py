# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'display_windowaTgAEZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Display_window(object):
    def setupUi(self, Display_window):
        if not Display_window.objectName():
            Display_window.setObjectName(u"Display_window")
        Display_window.resize(803, 648)
        self.centralwidget = QWidget(Display_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.back_frame = QFrame(self.frame)
        self.back_frame.setObjectName(u"back_frame")
        self.back_frame.setMaximumSize(QSize(16777215, 50))
        self.back_frame.setFrameShape(QFrame.StyledPanel)
        self.back_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.back_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.back_frame)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 100))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(80, 16777215))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.back_btn = QPushButton(self.frame_9)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setMinimumSize(QSize(40, 40))
        self.back_btn.setMaximumSize(QSize(40, 40))
        font = QFont()
        font.setPointSize(16)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.back_btn)


        self.horizontalLayout_3.addWidget(self.frame_9)

        self.frame_2 = QFrame(self.frame_8)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.camera_view_lbl_1 = QLabel(self.frame_4)
        self.camera_view_lbl_1.setObjectName(u"camera_view_lbl_1")
        self.camera_view_lbl_1.setStyleSheet(u"background-color:gray;")
        self.camera_view_lbl_1.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.camera_view_lbl_1)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 200))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.camera_view_lbl_3 = QLabel(self.frame_6)
        self.camera_view_lbl_3.setObjectName(u"camera_view_lbl_3")
        self.camera_view_lbl_3.setStyleSheet(u"background-color:gray;")
        self.camera_view_lbl_3.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.camera_view_lbl_3)


        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 200))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.camera_view_lbl_4 = QLabel(self.frame_7)
        self.camera_view_lbl_4.setObjectName(u"camera_view_lbl_4")
        self.camera_view_lbl_4.setStyleSheet(u"background-color:gray;")
        self.camera_view_lbl_4.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.camera_view_lbl_4)


        self.gridLayout.addWidget(self.frame_7, 1, 1, 1, 1)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 200))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.camera_view_lbl_2 = QLabel(self.frame_5)
        self.camera_view_lbl_2.setObjectName(u"camera_view_lbl_2")
        self.camera_view_lbl_2.setStyleSheet(u"background-color:gray;")
        self.camera_view_lbl_2.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.camera_view_lbl_2)


        self.gridLayout.addWidget(self.frame_5, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(80, 16777215))
        self.frame_10.setFont(font)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.send_btn = QPushButton(self.frame_10)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setMinimumSize(QSize(40, 40))
        self.send_btn.setMaximumSize(QSize(40, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.send_btn.setFont(font1)
        self.send_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.send_btn)


        self.horizontalLayout_3.addWidget(self.frame_10)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 80))
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.record_btn = QPushButton(self.frame_3)
        self.record_btn.setObjectName(u"record_btn")
        self.record_btn.setMinimumSize(QSize(150, 30))
        self.record_btn.setFont(font1)
        self.record_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.record_btn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        Display_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Display_window)

        QMetaObject.connectSlotsByName(Display_window)
    # setupUi

    def retranslateUi(self, Display_window):
        Display_window.setWindowTitle(QCoreApplication.translate("Display_window", u"MainWindow", None))
#if QT_CONFIG(statustip)
        self.back_btn.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.back_btn.setText(QCoreApplication.translate("Display_window", u"<", None))
        self.camera_view_lbl_1.setText("")
        self.camera_view_lbl_3.setText("")
        self.camera_view_lbl_4.setText("")
        self.camera_view_lbl_2.setText("")
        self.send_btn.setText(QCoreApplication.translate("Display_window", u">", None))
        self.record_btn.setText(QCoreApplication.translate("Display_window", u"Start Recording", None))
    # retranslateUi

