# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fanyi.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication,QMainWindow, QAction, qApp,QMessageBox
from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtGui import QFont
import urllib.request
import urllib.parse
import time
import json
import os
import re


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputbox = QtWidgets.QTextEdit(self.centralwidget)
        self.inputbox.setGeometry(QtCore.QRect(160, 100, 451, 121))
        self.inputbox.setObjectName("inputbox")
        self.outputbox = QtWidgets.QTextEdit(self.centralwidget)
        self.outputbox.setGeometry(QtCore.QRect(160, 320, 451, 121))
        self.outputbox.setObjectName("outputbox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 250, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setShortcut('Ctrl+F')    #快捷键
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 470, 91, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setToolTip("保存在"+os.getcwd()+"下*.txt")  #悬停提示
        self.pushButton_2.sizeHint()                       #自适应文字

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 5, 350, 51))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setWindowIcon(QIcon('E:/pachong/fanyi.png'))

        self.pushButton.clicked.connect(self.getdata)    #定义信号
        self.pushButton_2.clicked.connect(self.wfile)

        # self.look(MainWindow)
        self.retranslateUi(MainWindow)
        self.caidan(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #设置按钮名称
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "百度翻译"))
        self.pushButton.setText(_translate("MainWindow", "翻译"))
        self.pushButton_2.setText(_translate("MainWindow", "写入文件"))
        self.label.setText(_translate("MainWindow", "欢迎使用百度翻译API！"))

        #设置字体大小
        self.label.setFont(QFont('SansSerif',20))
        self.pushButton.setFont(QFont('SansSerif', 15))
        self.pushButton_2.setFont(QFont('SansSerif', 13))

    #菜单栏跟状态栏
    def caidan(self,MainWindow):

        exitAction = QAction('&退出',MainWindow)     #文件菜单
        exitAction.setShortcut('Ctrl+Q')       #快捷键
        exitAction.setStatusTip('退出程序')     #提示
        exitAction.triggered.connect(qApp.quit) #结束程序

        exitAction_1 = QAction('关于',MainWindow)
        exitAction_1.setShortcut('Ctrl+W')
        exitAction_1.setStatusTip('作者：吴浪    Email：wulang@mail.com')
        exitAction_1.triggered.connect(self.msg)


        MainWindow.statusBar()
        menubar = MainWindow.menuBar()
        fileMenu = menubar.addMenu('&文件')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(exitAction_1)
    def msg(self):
        QMessageBox.about(self,"关于本程序","作者：吴浪。\n     邮箱：wulang@mail.com。")


    '''
    #悬停鼠标显示提示信息
    def look(self,MainWindow):
        QToolTip.setFont(QFont('SansSerif',10))
        # # btn = QPushButton("pushButton_2",MainWindow)
        # btn.setToolTip('保存到当前目录')
        # btn.resize(btn.sizeHint())
        # btn.move(40,50)
     '''

    #获取数据
    def getdata(self):
        try:
            getdata = self.inputbox.toPlainText()
            #print(getdata)测试数据是否读写进来
            url = "http://fanyi.baidu.com/v2transapi"
            data = {}
            data['from'] = 'auto'
            data['to'] = 'auto'
            data['query'] = getdata
            data['transtype'] = 'realtime'
            data['simple_means_flag'] = '3'
            data = urllib.parse.urlencode(data).encode('utf-8')
            head = {}
            head[
                'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
            req = urllib.request.Request(url, data, head)
            response = urllib.request.urlopen(req)
            html = response.read().decode('utf-8')
            target = json.loads(html)
            tgt = target['trans_result']['data'][0]['dst']
            #print("翻译的结果是：%s" % tgt) 测试是否翻译成功
            self.outputbox.setText(tgt)  #将文本传输给outputBOX
        except:
            pass #print(sys.exc_info())

    #写入文件
    def wfile(self):
        wfile = self.outputbox.toPlainText()
        n = re.sub('[^A-Za-z]','',wfile)
        if len(n)>5:
            name = n[0:5]
        else:
            name = n
        with open(os.getcwd()+'/'+name+'.txt','w+',buffering=-1,encoding='utf-8') as file:
            file.write(wfile.rstrip())
            #print("写入成功，文件位置为"+os.getcwd())测试文件是否写入成功
