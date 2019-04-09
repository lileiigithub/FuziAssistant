# -*- coding: utf-8 -*-
#############################################################################
## 主窗口
##
#############################################################################
from PyQt5.QtCore import QFile, QFileInfo, QSettings, Qt, QTextStream,QThread
from PyQt5.QtGui import QKeySequence,QFont,QPixmap,QImage,QRgba64
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,QLabel,QPushButton,QWidget,QSpacerItem,
                             QMessageBox, QTextEdit, QGraphicsView, QTextBrowser, QGraphicsScene,QHBoxLayout,QVBoxLayout)
from PyQt5 import QtWidgets
from datetime import datetime
from config import Config

class MainWindow(QMainWindow):
    windowList = []

    def __init__(self):
        super(MainWindow, self).__init__()
        # 菜单
        self.recentFileActs = []
        # 将mainwindow的中心组件设置为widget,然后在里面布局
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.createActions()
        self.createMenus()
        self.statusBar()
        # self.toolBarArea()

        #主界面
        self.img_label = QLabel("接收的原始岩土图像")
        self.img_label.setAlignment(Qt.AlignCenter) # label 居中
        self.img_label.setFont(QFont("Roman times", 14)) #, QFont.Bold
        self.raw_img_view = QGraphicsView()
        # self.hide_button.setVisible(False)
        # 布局
        mainlayout = QHBoxLayout()
        # mainlayout.addLayout(left_layout)
        # mainlayout.addLayout(right_layout)
        self.widget.setLayout(mainlayout)
        #
        self.setWindowTitle("福纸")
        self.setGeometry(250,100,1080,820) # posx,posy,w,h

        # self.chooseImgButton.clicked.connect(self.clicked_local_button) # 更新各种信息
        # self.onlineButton.clicked.connect(self.clicked_online_button)  # 更新各种信息

        self.networkset = None  # 网络设置
        self.ReceiceImgThread = None # 多线程

    def newFile(self):
        other = MainWindow()
        MainWindow.windowList.append(other)
        other.show()

    def open(self):
        fileName, _ = QFileDialog.getOpenFileName(self)
        if fileName:
            self.loadFile(fileName)

    def save(self):
        pass

    def about(self):
        information = "版本：1.0\n" + "作者：李磊\n"
        # QMessageBox.setFont(QFont("Roman times", 10))
        QMessageBox.about(self, "福纸助手", information)

    def createActions(self):
        self.newAct = QAction("&New", self, shortcut=QKeySequence.New,
                              statusTip="Create a new file", triggered=self.newFile)

        self.openAct = QAction("&Open...", self, shortcut=QKeySequence.Open,
                               statusTip="Open an existing file", triggered=self.open)

        self.saveAct = QAction("&Save", self, shortcut=QKeySequence.Save,
                               statusTip="Save the document to disk", triggered=self.save)

        self.exitAct = QAction("E&xit", self, shortcut="Ctrl+Q",
                               statusTip="Exit the application",
                               triggered=QApplication.instance().closeAllWindows)

        self.aboutAct = QAction("&About", self,
                                statusTip="Show the application's About box",
                                triggered=self.about)

        self.aboutQtAct = QAction("About &Qt", self,
                                  statusTip="Show the Qt library's About box",
                                  triggered=QApplication.instance().aboutQt)

        # self.cameraSet = QAction("下位机摄像头设置", self,
        #                          statusTip="设置摄像头参数",
        #                          triggered=self.cameraSetDialog)

        # self.networkSet = QAction("下位机ip地址设置", self,
        #                          statusTip="设置网络连接",
        #                          triggered=self.networkDialog)

        # self.denoiseSet = QAction("去噪算法选择", self,
        #                          statusTip="去噪算法选择",
        #                          triggered=self.denoiseDialog)

    def createMenus(self):
        # 创建菜单
        self.fileMenu = self.menuBar().addMenu("&文件")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.separatorAct = self.fileMenu.addSeparator()
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAct)

        self.menuBar().addSeparator()
        self.setting = self.menuBar().addMenu("&设置")
        # self.setting.addAction(self.cameraSet)
        # self.setting.addAction(self.networkSet)
        # self.setting.addAction(self.denoiseSet)

        self.helpMenu = self.menuBar().addMenu("&帮助")
        self.helpMenu.addAction(self.aboutAct)
        self.helpMenu.addAction(self.aboutQtAct)

    def loadFile(self, fileName):
        pass

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())