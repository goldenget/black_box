# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_userkbjvRt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_create_user_window(object):
    def setupUi(self, create_user_window):
        if not create_user_window.objectName():
            create_user_window.setObjectName(u"create_user_window")
        create_user_window.resize(464, 306)
        self.centralwidget = QWidget(create_user_window)
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
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.back_frame = QFrame(self.frame)
        self.back_frame.setObjectName(u"back_frame")
        self.back_frame.setMinimumSize(QSize(0, 50))
        self.back_frame.setMaximumSize(QSize(16777215, 50))
        self.back_frame.setFrameShape(QFrame.StyledPanel)
        self.back_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.back_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.back_btn = QPushButton(self.back_frame)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setMinimumSize(QSize(40, 40))
        font = QFont()
        font.setPointSize(16)
        self.back_btn.setFont(font)
        self.back_btn.setStyleSheet(u"background:black;\n"
"border-radius:20;\n"
"color: white")

        self.horizontalLayout_2.addWidget(self.back_btn)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.back_frame)

        self.username_txt = QLineEdit(self.frame)
        self.username_txt.setObjectName(u"username_txt")
        font1 = QFont()
        font1.setPointSize(12)
        self.username_txt.setFont(font1)
        self.username_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.username_txt)

        self.email_txt = QLineEdit(self.frame)
        self.email_txt.setObjectName(u"email_txt")
        self.email_txt.setFont(font1)
        self.email_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.email_txt)

        self.phone_txt = QLineEdit(self.frame)
        self.phone_txt.setObjectName(u"phone_txt")
        self.phone_txt.setFont(font1)
        self.phone_txt.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.phone_txt)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 60))
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.create_user_btn = QPushButton(self.frame_2)
        self.create_user_btn.setObjectName(u"create_user_btn")
        self.create_user_btn.setMinimumSize(QSize(150, 30))
        self.create_user_btn.setFont(font1)
        self.create_user_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.create_user_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame)

        create_user_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(create_user_window)

        QMetaObject.connectSlotsByName(create_user_window)
    # setupUi

    def retranslateUi(self, create_user_window):
        create_user_window.setWindowTitle(QCoreApplication.translate("create_user_window", u"MainWindow", None))
        self.back_btn.setText(QCoreApplication.translate("create_user_window", u"<-", None))
        self.username_txt.setPlaceholderText(QCoreApplication.translate("create_user_window", u"Username", None))
        self.email_txt.setPlaceholderText(QCoreApplication.translate("create_user_window", u"Email", None))
        self.phone_txt.setPlaceholderText(QCoreApplication.translate("create_user_window", u"Phone", None))
        self.create_user_btn.setText(QCoreApplication.translate("create_user_window", u"Create", None))
    # retranslateUi

