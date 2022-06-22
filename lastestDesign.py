# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lastestDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



import json
from statistics import mean
import sys
from turtle import color
from unittest import result

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import requests
 


import imsrc
import numpy as np
from PyQt5 import*
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
import sys
import glob
import serial
from random import randint
import pyqtgraph as pg
import os
class video:
    def __init__(self, id=None, emotion_dev=None, emotion_test=None, device_data=None):
        self.id = id 
        self.emotion_dev = emotion_dev
        self.emotion_test = emotion_test
        self.device_data = device_data
    
    def to_file(self, filepath):
        with open(filepath, 'a') as f:
            f.write(str(self.id) + ',' + str(self.emotion_dev) + ',' + str(self.emotion_test) + ',' + str(self.device_data) +'\n')
            f.close()


class user:
    def __init__(self, id, sex=None, age=None, height=None, weight=None, location=None, emotional=None, frequency=None, video_data=None):
        self.id = id
        self.sex = sex #M:male F:female
        self.age = age
        self.location = location
        self.height = height
        self.weight = weight
        self.emotional = emotional #Y: emotional N: not emotional
        self.frequency = frequency #0: never 1: every year 2: every 6 months 3: every month 4: every week 5: every 1-3 days
        self.video_data = video_data
        self.videos = []

    def to_file(self, filepath):
        with open(filepath, 'a') as f:
            f.write(str(self.id) + ',' + str(self.sex) + ',' + str(self.age) + ',' + str(self.height) + ',' + str(self.weight) + ',' + str(self.location) + ',' + str(self.emotional) + ',' + str(self.frequency) + ',' + str(self.video_data) + '\n')
            f.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1900, 970)
        MainWindow.setStyleSheet("background-color: rgb(12, 45, 72);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1740, 790, 141, 61))
        self.label.setStyleSheet("image: url(:/logo/imgsrc/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1740, 860, 81, 31))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("    border: 3px solid ;\n"
"    border-color: rgb(65, 114, 159);\n"
"    border-radius: 10px;\n"
"    margin-top: 0.5em;")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 210, 331, 61))
        self.groupBox.setMaximumSize(QtCore.QSize(16700000, 16700000))
        self.groupBox.setStyleSheet("border: 0px;\n"
"background-color: rgb(65, 114, 159);\n"
"border-radius:10px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(100, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft YaHei UI Light\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(190, 10, 111, 41))
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 11pt \"Microsoft YaHei UI Light\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(70, 280, 331, 61))
        self.groupBox_2.setStyleSheet("border: 0px;\n"
"background-color: rgb(65, 114, 159);\n"
"border-radius:10px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox.setGeometry(QtCore.QRect(70, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:0 px;\n"
"")
        self.spinBox.setMinimum(6)
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(70, 490, 331, 61))
        self.groupBox_3.setStyleSheet("border: 0px;\n"
"background-color: rgb(65, 114, 159);\n"
"border-radius:10px;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setGeometry(QtCore.QRect(210, 10, 41, 31))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 0, 331, 61))
        self.groupBox_4.setStyleSheet("border: 0px;\n"
"background-color: rgb(65, 114, 159);\n"
"border-radius:10px;")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_4)
        self.checkBox_4.setGeometry(QtCore.QRect(210, 10, 41, 31))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 780, 191, 91))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Poppins\";\n"
"border-radius: 30px;\n"
"background-color: rgb(27, 157, 70);\n"
"border-style: outset;")
        self.pushButton.setObjectName("pushButton")
        self.button_counter = 0
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 780, 191, 91))
        self.pushButton.clicked.connect(self.clickme)
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 18pt \"Poppins\";\n"
"border-radius: 30px;\n"
"border-style: outset;\n"
"background-color: rgb(219, 31, 72);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1820, 860, 61, 31))
        self.label_8.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(70, 560, 331, 311))
        self.groupBox_6.setMaximumSize(QtCore.QSize(16700000, 16700000))
        self.groupBox_6.setStyleSheet("border: 0px;\n"
"background-color: rgb(65, 114, 159);\n"
"border-radius:10px;")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.freq0 = QtWidgets.QRadioButton(self.groupBox_6)
        self.freq0.setGeometry(QtCore.QRect(10, 80, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.freq0.setFont(font)
        self.freq0.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Microsoft JhengHei UI Light\";")
        self.freq0.setObjectName("freq0")
        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setTextFormat(QtCore.Qt.RichText)
        self.label_13.setObjectName("label_13")
        self.freq1 = QtWidgets.QRadioButton(self.groupBox_6)
        self.freq1.setGeometry(QtCore.QRect(10, 110, 131, 31))
        self.freq1.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Microsoft YaHei UI Light\";\n"
"")
        self.freq1.setObjectName("freq1")
        self.freq2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.freq2.setGeometry(QtCore.QRect(10, 150, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.freq2.setFont(font)
        self.freq2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.freq2.setObjectName("freq2")
        self.freq3 = QtWidgets.QRadioButton(self.groupBox_6)
        self.freq3.setGeometry(QtCore.QRect(10, 180, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.freq3.setFont(font)
        self.freq3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.freq3.setObjectName("freq3")
        self.freq4 = QtWidgets.QRadioButton(self.groupBox_6)
        self.freq4.setGeometry(QtCore.QRect(10, 220, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.freq4.setFont(font)
        self.freq4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Microsoft JhengHei UI Light\";\n"
"")
        self.freq4.setObjectName("freq4")
        self.freq5 = QtWidgets.QRadioButton(self.groupBox_6)
        self.freq5.setGeometry(QtCore.QRect(10, 250, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        self.freq5.setFont(font)
        self.freq5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 25 11pt \"Microsoft JhengHei UI Light\";")
        self.freq5.setObjectName("freq5")
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(70, 350, 331, 61))
        self.groupBox_7.setStyleSheet("border: 0px;\n"
"background-color: rgb(65, 114, 159);\n"
"border-radius:10px;")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.spinBox_11 = QtWidgets.QSpinBox(self.groupBox_7)
        self.spinBox_11.setGeometry(QtCore.QRect(90, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        self.spinBox_11.setFont(font)
        self.spinBox_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:0 px;\n"
"")
        self.spinBox_11.setMinimum(6)
        self.spinBox_11.setObjectName("spinBox_11")
        self.label_19 = QtWidgets.QLabel(self.groupBox_7)
        self.label_19.setGeometry(QtCore.QRect(10, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.groupBox_7)
        self.label_20.setGeometry(QtCore.QRect(160, 10, 71, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.spinBox_12 = QtWidgets.QSpinBox(self.groupBox_7)
        self.spinBox_12.setGeometry(QtCore.QRect(250, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        self.spinBox_12.setFont(font)
        self.spinBox_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:0 px;\n"
"")
        self.spinBox_12.setMinimum(6)
        self.spinBox_12.setObjectName("spinBox_12")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(70, 420, 331, 61))
        self.groupBox_5.setStyleSheet("border: 0px;\n"
"background-color: rgb(65, 114, 159);\n"
"border-radius:10px;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei Light")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit.setGeometry(QtCore.QRect(160, 10, 141, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:0 px;")
        self.textEdit.setUndoRedoEnabled(True)
        self.textEdit.setObjectName("textEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, -80, 791, 271))
        self.label_7.setStyleSheet("image: url(:/logo/imgsrc/Moodie.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(920, 760, 321, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("    border: 3px solid ;\n"
"    border-color: rgb(255, 255, 255);\n"
"    font: 75 12pt \"Microsoft JhengHei UI\";\n"
"    border-radius: 20px;\n"
"    margin-top: 0.5em;\n"
"    color: rgb(255, 255, 255);")
        self.label_15.setTextFormat(QtCore.Qt.RichText)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1846, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt; font-weight:600; color:#ea8b37;\">NEURO</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Personal Informations</span></p></body></html>"))
        self.radioButton_4.setText(_translate("MainWindow", "Male"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gender :</span></p></body></html>"))
        self.radioButton_3.setText(_translate("MainWindow", "Female"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Age :</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Are you emotional ?</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Are you emotional ?</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "STOP"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#e5e5e5;\">TECH</span></p></body></html>"))
        self.freq0.setText(_translate("MainWindow", "Never"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">How often do you watch movies?</span></p></body></html>"))
        self.freq1.setText(_translate("MainWindow", "Every year"))
        self.freq2.setText(_translate("MainWindow", "Every 6 month"))
        self.freq3.setText(_translate("MainWindow", "Every month"))
        self.freq4.setText(_translate("MainWindow", "Every week"))
        self.freq5.setText(_translate("MainWindow", "Every 1-3 days"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Height:</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Weight:</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Location:</span></p></body></html>"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p>Not recording</p></body></html>"))

    def clickme(self):
        self.button_counter = self.button_counter + 1

    #    self.horizontalSlider_MovieFreq.setValue(0)
        self.spinBox_11.setValue(6)
#import imsrc_rc

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        print("-------------------")
        EXIT_CODE_REBOOT = -123
        super(MainWindow, self).__init__(parent)        
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.reset) 


     


        self.graphWidget = pg.PlotWidget(self)
        self.graphWidget.showGrid(x = True, y = True)
        self.graphWidget.move(450,130)
        #self.graphWidget.resize(1300,600)
        self.graphWidget.resize(1200,300)
        #self.setCentralWidget(self.graphWidget)

        self.x1 = list(range(1))  # 100 time points
        self.y1 = [randint(0,1500) for _ in range(1)]  # 100 data points

        self.y2 = [randint(0,1500) for _ in range(1)]  # 100 data points
        self.y3 = [randint(0,1500) for _ in range(1)]  # 100 data points
        self.y4 = [randint(0,1500) for _ in range(1)]  # 100 data points

        self.graphWidget.setBackground(background=None)

        pen = pg.mkPen(color=(255, 0, 0))
        self.x1 = self.x1[1:]  # Remove the first y1 element.
        self.y1 = self.y1[1:]  # Remove the first
        self.y2 = self.y2[1:]  # Remove the first
        self.y3 = self.y3[1:]  # Remove the first
        self.y4 = self.y4[1:]  # Remove the first

        self.graphWidget.addLegend()
        self.data_line =  self.graphWidget.plot(self.x1, self.y1, pen=pen,name ='Sensor 1: 28mm')
        self.data_line2 =  self.graphWidget.plot(self.x1, self.y2, pen=("g"),name = 'Sensor 2: 24mm')
        self.data_line3 =  self.graphWidget.plot(self.x1, self.y3, pen=("m"),name = 'Sensor 3: 10mm')
        self.data_line4 =  self.graphWidget.plot(self.x1, self.y4, pen=("y"), name = 'Sensor 4: 5mm')
        self.sensor_val1 = 0
        self.sensor_val2 = 0
        self.sensor_val3 = 0
        self.sensor_val4 = 0


        self.y_axis = [1,2,3,4,5,6]
        xlab = ['ANGER', 'ANTIPATHY', 'DISGUST', 'FEAR', 'JOY', 'SAD']
        self.xval = list(range(1,len(xlab)+1))

        ticks=[]
        for i, item in enumerate(xlab):
            ticks.append( (self.xval[i], item) )
        ticks = [ticks]
        
        self.barGraphWidget = pg.PlotWidget(self)
        self.barGraphWidget.resize(1200,300)
        self.barGraphWidget.move(450,450)
        self.barGraph = pg.BarGraphItem(x=self.xval, height=self.y_axis, width=0.5)
        self.barGraphWidget.addItem(self.barGraph)
        #self.data_line5 = self.barGraphWidget.plot(self.xval,self.y_axis)
        self.barGraphWidget.setBackground(background=None)

        ax = self.barGraphWidget.getAxis('bottom')
        ax.setTicks(ticks)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()
        self.second = 0

        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(500)
        self.timer2.timeout.connect(self.get_sensor_data)
        self.timer2.start()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.data)
        timer.start(100) #Veri akış gecikmesi.
        self.data() # Veri tazeleme fonksiyonu.

        self.setWindowTitle("PyQtChart Pie Chart")
    

    def data(self):
        if self.radioButton_4.isChecked():
            user_data.sex = 'M'
        if self.radioButton_3.isChecked():
            user_data.sex = 'F'
        if self.checkBox.isChecked():
            user_data.emotional = 'Y'
        else:
            user_data.emotional = 'N'
   #     user_data.frequency = self.horizontalSlider_MovieFreq.value()
        if self.button_counter%2 != 0:
   #         self.pushButton.setText("STOP")
            self.label_15.setText("Recording")
        else:
            self.pushButton.setText("START")
            self.label_15.setText("Not Recording")
        if self.freq0.isChecked():
            user_data.frequency = 0
        elif self.freq1.isChecked():
            user_data.frequency = 1
        elif self.freq2.isChecked():
            user_data.frequency = 2
        elif self.freq3.isChecked():
            user_data.frequency = 3
        elif self.freq4.isChecked():
            user_data.frequency = 4
        elif self.freq5.isChecked():
            user_data.frequency = 5

        user_data.age = self.spinBox.value()
        user_data.location = self.textEdit   
        user_data.height = self.spinBox_11
        user_data.weight = self.spinBox_12

    def update_plot_data(self):
        #self.x1 = self.x1[1:]  # Remove the first y element.
        if len(self.x1)>60:
            self.x1 = self.x1[1:]  # Add a new value 1 higher than the last.
            self.y1 = self.y1[1:]  # Remove the first
            self.y2 = self.y2[1:]  # Remove the first
            self.y3 = self.y3[1:]  # Remove the first
            self.y4 = self.y4[1:]  # Remove the first
        self.x1.append(self.second)
        self.second = self.second + 1
        self.y1.append(self.sensor_val1)  # Add a new random value.
        self.y2.append(self.sensor_val2)  # Add a new random value.
        self.y3.append(self.sensor_val3)  # Add a new random value.
        self.y4.append(self.sensor_val4)  # Add a new random value.

        self.data_line.setData(self.x1, self.y1)  # Update the data.
        self.data_line2.setData(self.x1, self.y2)  # Update the data
        self.data_line3.setData(self.x1, self.y3)  # Update the data
        self.data_line4.setData(self.x1, self.y4)  # Update the data

        
        results = self.model_com()
        if results != None:
        #arr = json.loads(results)

            my_json = results.content.decode('utf8').replace("'", '"')
            print(my_json)
            print('- ' * 20)

            my_json = " ".join(my_json.split())
            str = my_json[2:len(my_json)-2]
            a = list()
            a = str.split(" ")

            self.y_axis = [float(a[0])*100, float(a[1])*100, float(a[2])*100, float(a[3])*100, float(a[4])*100, float(a[5])*100]
        else :
            self.y_axis = [0,0,0,0,0,0]
            
        self.barGraphWidget.plotItem.clear()
        self.barGraph = pg.BarGraphItem(x=self.xval, height=self.y_axis, width=0.5,  brush=(255,31,72))

        self.barGraphWidget.addItem(self.barGraph)
        
        #self.data_line5.setData(self.xval,self.y_axis)


    def get_sensor_data(self):
        data_str = str(ser.readline())
        data_str = data_str.replace("b'", '')
        data_str = data_str.replace("\\r\\n'", '')
        data_str = data_str.split('\\')[0]
        data_list = data_str.split(' ')
        F1 = np.fft.fft(data_list)
        print("F1: "+str(F1))
        self.sensor_val1 = float(data_list[0])
        #self.sensor_val1 = randint(100,1000)

        data_str = str(ser.readline())
        data_str = data_str.replace("b'", '')
        data_str = data_str.replace("\\r\\n'", '')
        data_str = data_str.split('\\')[0]
        data_list = data_str.split(' ')
        F2 = np.fft.fft(data_list)
        print("F2 "+str(F2))
        self.sensor_val2 = float(data_list[0])
        #self.sensor_val2 = randint(100,1000)

        data_str = str(ser.readline())
        data_str = data_str.replace("b'", '')
        data_str = data_str.replace("\\r\\n'", '')
        data_str = data_str.split('\\')[0]
        data_list = data_str.split(' ')
        F3 = np.fft.fft(data_list)
        print("F3 "+str(F3))
        self.sensor_val3 = float(data_list[0])
        #self.sensor_val3 = randint(100,1000)

        data_str = str(ser.readline())
        data_str = data_str.replace("b'", '')
        data_str = data_str.replace("\\r\\n'", '')
        data_str = data_str.split('\\')[0]
        data_list = data_str.split(' ')
        F4 = np.fft.fft(data_list)
        print("F4 "+str(F4))
        self.sensor_val4 = float(data_list[0])
        #self.sensor_val4 = randint(100,1000)


    def reset(self):
       # self.radioButton_3.setChecked(False)
      #  self.radioButton_4.setChecked(False)
      #  self.checkBox.setChecked(False)
        print("XXXXXXXXXXXXXXXXXxXX")

        self.show()
        self.create_piechart()

    def model_com(self):
        req = []
        req.append(0)
        req.append(21)
        req.append(1)

        if self.sensor_val1 == 0 and self.sensor_val2 == 0 and self.sensor_val3 == 0 and self.sensor_val4 == 0:
            return None
        req.append(self.sensor_val1)
        req.append(self.sensor_val1)
        req.append(self.sensor_val1)

        req.append(self.sensor_val2)
        req.append(self.sensor_val2)
        req.append(self.sensor_val2)

        req.append(self.sensor_val3)
        req.append(self.sensor_val3)
        req.append(self.sensor_val3)

        req.append(self.sensor_val4)
        req.append(self.sensor_val4)
        req.append(self.sensor_val4)

        URL = 'https://neurotech-model.azurewebsites.net/api/HttpTrigger1?code=H_b77QaGW6eeF8UvewZONUSBFuBUfZ1R9yGftNQKHKXEAzFuGLjiqQ=='

        body = {'data':req, 'model_num': 0}

        res = requests.post(URL,json=body)

        print(res.status_code)
        return res

    def create_piechart(self):
    
            self.series = QPieSeries()
            self.series.append("Anger", 8)
            self.series.append("Antipathy", 12)
            self.series.append("Disgust", 25)
            self.series.append("Fear", 5)
            self.series.append("Joy", 10)
            self.series.append("Sad", 5)
            self.series.append("Surprise", 15)
            self.series.append("Trust", 10)

    
            #adding slice - burada max value verilecek, o slice edilecek
            self.slice = QPieSlice()
            self.slice = self.series.slices()[2]
            self.slice.setExploded(True)
            self.slice.setLabelVisible(True)
            self.slice.setPen(QPen(Qt.darkGreen, 2))
            self.slice.setBrush(Qt.darkGreen)
    
    
            self.chart = QChart()
            self.chart.legend().hide()
            self.chart.addSeries(self.series)
            self.chart.createDefaultAxes()
            self.chart.setAnimationOptions(QChart.SeriesAnimations)
            self.chart.setTitle("Pie Chart Of The Test Results")

    
            self.chart.legend().setVisible(True)
            self.chart.legend().setAlignment(Qt.AlignBottom)
    


            self.chartview = QChartView(self.chart)
            self.chartview.setRenderHint(QPainter.Antialiasing)
            self.setCentralWidget(self.chartview)

 



if __name__ == "__main__":
    #fd = open('data/user_count', 'r')
    #id = int(fd.readline())
    #fd.close()
    ser = serial.Serial('COM4',115200)
    user_data = user(id)

    print("Baslatiliyor...")
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow() # Ana pencere oluşturulur.
    window.show() #Oluşturulan pencere ekranda gösterilir.
    sys.exit(app.exec_())
