# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowyaiLgq.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(713, 489)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.main_frame)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setMinimumSize(QSize(0, 80))
        self.top_frame.setMaximumSize(QSize(16777215, 80))
        self.top_frame.setCursor(QCursor(Qt.ArrowCursor))
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.emergency_btn = QPushButton(self.top_frame)
        self.emergency_btn.setObjectName(u"emergency_btn")
        self.emergency_btn.setMinimumSize(QSize(150, 30))
        font = QFont()
        font.setPointSize(12)
        self.emergency_btn.setFont(font)
        self.emergency_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.emergency_btn)

        self.horizontalSpacer = QSpacerItem(532, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.frame = QFrame(self.top_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.top_frame)

        self.mid_frame = QFrame(self.main_frame)
        self.mid_frame.setObjectName(u"mid_frame")
        self.mid_frame.setFrameShape(QFrame.StyledPanel)
        self.mid_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.mid_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.listWidget = QListWidget(self.mid_frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFont(font)
        self.listWidget.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_4.addWidget(self.listWidget)

        self.frame_2 = QFrame(self.mid_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(50, 0))
        self.frame_2.setMaximumSize(QSize(50, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.select_user_btn = QPushButton(self.frame_2)
        self.select_user_btn.setObjectName(u"select_user_btn")
        self.select_user_btn.setMinimumSize(QSize(30, 30))
        self.select_user_btn.setMaximumSize(QSize(30, 16777215))
        self.select_user_btn.setFont(font)
        self.select_user_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_5.addWidget(self.select_user_btn)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.mid_frame)

        self.bottom_frame = QFrame(self.main_frame)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 100))
        self.bottom_frame.setMaximumSize(QSize(16777215, 100))
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.create_user_btn = QPushButton(self.bottom_frame)
        self.create_user_btn.setObjectName(u"create_user_btn")
        self.create_user_btn.setMinimumSize(QSize(150, 30))
        self.create_user_btn.setFont(font)
        self.create_user_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_3.addWidget(self.create_user_btn)


        self.verticalLayout.addWidget(self.bottom_frame)


        self.horizontalLayout.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.emergency_btn.setText(QCoreApplication.translate("MainWindow", u"Emergency", None))
        self.select_user_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.create_user_btn.setText(QCoreApplication.translate("MainWindow", u"Create Profile", None))
    # retranslateUi

