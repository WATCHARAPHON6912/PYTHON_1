# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage
from PyQt5.QtCore import QTimer,QDateTime
import cv2, imutils
import keyboard as kb
from socket import *
import resuoe_rc
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 788)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWhatsThis("")
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.IP_label = QtWidgets.QLabel(self.centralwidget)
        self.IP_label.setGeometry(QtCore.QRect(40, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.IP_label.setFont(font)
        self.IP_label.setObjectName("IP_label")
        self.PORT_label = QtWidgets.QLabel(self.centralwidget)
        self.PORT_label.setGeometry(QtCore.QRect(510, 20, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PORT_label.setFont(font)
        self.PORT_label.setObjectName("PORT_label")
        self.IP_input = QtWidgets.QLineEdit(self.centralwidget)
        self.IP_input.setGeometry(QtCore.QRect(102, 21, 381, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.IP_input.setFont(font)
        self.IP_input.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.IP_input.setObjectName("IP_input")
        self.PORT_input = QtWidgets.QLineEdit(self.centralwidget)
        self.PORT_input.setGeometry(QtCore.QRect(640, 20, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.PORT_input.setFont(font)
        self.PORT_input.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.PORT_input.setObjectName("PORT_input")
        self.W_Button = QtWidgets.QPushButton(self.centralwidget)
        self.W_Button.setGeometry(QtCore.QRect(104, 516, 93, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.W_Button.setFont(font)
        self.W_Button.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-color: rgb(0, 0, 255);")
        self.W_Button.setObjectName("W_Button")
        self.A_Button = QtWidgets.QPushButton(self.centralwidget)
        self.A_Button.setGeometry(QtCore.QRect(10, 610, 93, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.A_Button.setFont(font)
        self.A_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.A_Button.setObjectName("A_Button")
        self.S_Button = QtWidgets.QPushButton(self.centralwidget)
        self.S_Button.setGeometry(QtCore.QRect(105, 610, 93, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.S_Button.setFont(font)
        self.S_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.S_Button.setObjectName("S_Button")
        self.D_Button = QtWidgets.QPushButton(self.centralwidget)
        self.D_Button.setGeometry(QtCore.QRect(200, 610, 93, 91))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.D_Button.setFont(font)
        self.D_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.D_Button.setObjectName("W_Button_3")
        self.Connect_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Connect_Button.setGeometry(QtCore.QRect(802, 17, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Connect_Button.setFont(font)
        self.Connect_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.Connect_Button.setObjectName("Connect_Button")
        self.Video_Streaming = QtWidgets.QLabel(self.centralwidget)
        self.Video_Streaming.setGeometry(QtCore.QRect(444, 165, 511, 501))
        self.Video_Streaming.setStyleSheet("background-image: url(:/newPrefix/QT5_UI_Image/image-30938-800.jpg);")
        self.Video_Streaming.setText("")
        self.Video_Streaming.setPixmap(QtGui.QPixmap("QT5_UI_Image/image-30938-800.jpg"))
        self.Video_Streaming.setObjectName("Video_Streaming")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)
        self.Connect_Button.clicked.connect(self.Connect)

        self.i = False

        self.tmp = None  # Will hold the temporary image for display

        self.cap = cv2.VideoCapture(1)

    def loadImage(self):
        """ This function will load the user selected image
            and set it to label using the setPhoto function
        """
        _, ff = self.cap.read()
        # print(ff)
        # self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        # self.image = cv2.imread(self.filename)
        self.image = ff

        self.setPhoto(self.image)

    def setPhoto(self, image):
        """ This function will take image input and resize it
            only for display purpose and convert it to QImage
            to set at the label.
        """
        self.tmp = image
        image = imutils.resize(image, width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.Video_Streaming.setPixmap(QtGui.QPixmap.fromImage(image))

    def Connect(self):
        self.i = not self.i
        print(self.i)
        if self.i == True:
            self.Connect_Button.setText("DisConnect")
            self.Connect_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.IP_input.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.PORT_input.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.timer.start(1)
            self.IP_input.setEnabled(False)
            self.PORT_input.setEnabled(False)
        if self.i == False:
            self.Connect_Button.setText("Connect")
            self.Connect_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.IP_input.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.PORT_input.setStyleSheet("background-color: rgb(85, 255, 255);")
            self.timer.stop()
            self.IP_input.setEnabled(True)
            self.PORT_input.setEnabled(True)

    def showTime(self):
        self.loadImage()
        if kb.is_pressed('w'):
            print("W")
            self.W_Button.setEnabled(False)
            self.W_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            self.W_Button.setEnabled(True)
            self.W_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        if kb.is_pressed('a'):
            print("A")
            self.A_Button.setEnabled(False)
            self.A_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            self.A_Button.setEnabled(True)
            self.A_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        if kb.is_pressed('s'):
            print("S")
            self.S_Button.setEnabled(False)
            self.S_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            self.S_Button.setEnabled(True)
            self.S_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
        if kb.is_pressed('d'):
            print("D")
            self.D_Button.setEnabled(False)
            self.D_Button.setStyleSheet("background-color: rgb(0, 255, 0);")
        else:
            self.D_Button.setEnabled(True)
            self.D_Button.setStyleSheet("background-color: rgb(255, 0, 0);")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MYAPP"))
        self.IP_label.setText(_translate("MainWindow", "IP"))
        self.PORT_label.setText(_translate("MainWindow", "PORT"))
        self.IP_input.setText(_translate("MainWindow", "192.168.1.243"))
        self.PORT_input.setText(_translate("MainWindow", "8888"))
        self.W_Button.setText(_translate("MainWindow", "W"))
        self.A_Button.setText(_translate("MainWindow", "A"))
        self.S_Button.setText(_translate("MainWindow", "S"))
        self.D_Button.setText(_translate("MainWindow", "D"))
        self.Connect_Button.setText(_translate("MainWindow", "Connect"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
