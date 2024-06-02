# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'obd_windowcETcTQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_obd_window(object):
    def setupUi(self, obd_window):
        if not obd_window.objectName():
            obd_window.setObjectName(u"obd_window")
        obd_window.resize(764, 168)
        self.centralwidget = QWidget(obd_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.back_frame = QFrame(self.centralwidget)
        self.back_frame.setObjectName(u"back_frame")
        self.back_frame.setMaximumSize(QSize(16777215, 50))
        self.back_frame.setFrameShape(QFrame.StyledPanel)
        self.back_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.back_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.back_btn = QPushButton(self.back_frame)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setMinimumSize(QSize(40, 40))
        self.back_btn.setMaximumSize(QSize(40, 40))
        font = QFont()
        font.setPointSize(16)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.back_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.back_frame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.obd_path = QLineEdit(self.frame)
        self.obd_path.setObjectName(u"obd_path")
        self.obd_path.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(14)
        self.obd_path.setFont(font1)

        self.horizontalLayout.addWidget(self.obd_path)

        self.open_obd_btn = QPushButton(self.frame)
        self.open_obd_btn.setObjectName(u"open_obd_btn")
        self.open_obd_btn.setMinimumSize(QSize(200, 30))
        self.open_obd_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.open_obd_btn)


        self.verticalLayout.addWidget(self.frame)

        obd_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(obd_window)

        QMetaObject.connectSlotsByName(obd_window)
    # setupUi

    def retranslateUi(self, obd_window):
        obd_window.setWindowTitle(QCoreApplication.translate("obd_window", u"MainWindow", None))
        self.back_btn.setText(QCoreApplication.translate("obd_window", u"<", None))
        self.open_obd_btn.setText(QCoreApplication.translate("obd_window", u"Open OBD", None))
    # retranslateUi

