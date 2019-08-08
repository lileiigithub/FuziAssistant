# -*- coding: utf-8 -*-
#############################################################################
## 主窗口
##
#############################################################################
from PyQt5.QtCore import QFile, QFileInfo, QSettings, Qt, QTextStream,QThread
from PyQt5.QtGui import QKeySequence,QFont,QPixmap,QImage,QRgba64,QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QMainWindow,QLabel,QPushButton,QWidget,QSpacerItem,
                             QMessageBox, QTextEdit, QGraphicsView, QTextBrowser, QGraphicsScene,QHBoxLayout,QVBoxLayout,
                             QTabWidget,QLineEdit,QDialog,QTableWidget,QTableView)
from datetime import datetime
from config import GlobalData
from addInfoDialog import AddInfoDialog
from delInfoDialog import DelInfoDialog
from relationship import AFamily
from fuziLog import FzLog

class MainWindow(QMainWindow):
    windowList = []

    def __init__(self):
        super(MainWindow, self).__init__()
        # 菜单
        self.recentFileActs = []
        # 将mainwindow的中心组件设置为widget,然后在里面布局
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.mainwidget = QWidget()
        self.setCentralWidget(self.mainwidget)
        self.createActions()
        self.createMenus()
        self.statusBar()

        #主界面
        self.tabWigdet = QTabWidget()
        self.tabNewFamily = QWidget()
        self.tabSearch = QWidget()
        self.tabWigdet.addTab(self.tabNewFamily,"新建")
        self.tabWigdet.addTab(self.tabSearch, "查询")
        self.tabWigdet.setTabPosition(QTabWidget.West)
        self.tabFamilyUI()
        self.searchFamilyUI()
        # 布局
        mainlayout = QHBoxLayout()
        mainlayout.addWidget(self.tabWigdet)
        # mainlayout.addLayout(left_layout)
        # mainlayout.addLayout(right_layout)
        self.mainwidget.setLayout(mainlayout)
        #
        self.setWindowTitle("苟氏福纸")
        self.setGeometry(250,100,800,850) # posx,posy,w,h

    def tabFamilyUI(self):
        self.addButton = QPushButton("新建家庭")
        self.addButton.setFont(QFont("Roman times",15))
        self.addButton.setMaximumWidth(150)
        self.addButton.clicked.connect(self.showAddInfoDialog)
        self.delButton = QPushButton("删除信息")
        self.delButton.setFont(QFont("Roman times", 15))
        self.delButton.setMaximumWidth(150)
        self.delButton.clicked.connect(self.showDelInfoDialog)
        self.enterButton = QPushButton("提交信息")
        self.enterButton.setFont(QFont("Roman times", 15))
        self.enterButton.setMaximumWidth(150)
        self.enterButton.clicked.connect(self.pushFamilyInfo)
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.addButton)
        # buttonLayout.addSpacerItem(QSpacerItem(100,10))
        buttonLayout.addWidget(self.delButton)
        # buttonLayout.addSpacerItem(QSpacerItem(100, 10))
        buttonLayout.addWidget(self.enterButton)
        buttonLayout.addStretch(1)

        self.infoBoard = QTableView()
        newLayout = QVBoxLayout()
        newLayout.addLayout(buttonLayout)
        newLayout.addWidget(self.infoBoard)
        self.tabNewFamily.setLayout(newLayout)

    def searchFamilyUI(self):
        #  搜索界面
        self.searchEdit = QLineEdit()
        self.searchEdit.setFont(QFont("Roman times",20))
        self.searchEdit.setMaximumHeight(40)
        self.searchButton = QPushButton("搜索")
        self.searchButton.setFont(QFont("Roman times",20))
        self.searchButton.clicked.connect(self.search_contents)
        searchLayout = QHBoxLayout()
        searchLayout.addWidget(self.searchEdit)
        searchLayout.addWidget(self.searchButton)

        self.searchInfoBoard = QTableView()
        newLayout = QVBoxLayout()
        newLayout.addLayout(searchLayout)
        newLayout.addWidget(self.searchInfoBoard)
        self.tabSearch.setLayout(newLayout)

    def get_search_word(self):
        search_words = self.searchEdit.text()
        return search_words

    def setInfoBoard(self):
        pass

    def search_contents(self):
        search_words = self.get_search_word()
        print("search_words:",search_words)
        GlobalData.searchFamilyInfo(search_words)
        self.updateSearchView()

    def createFamilyInfoModel(self,_model_data):
        # self.model.clear()
        _model = QStandardItemModel(0, 5)
        _model.setHorizontalHeaderLabels(['姓名', '性别', '关系', '姓名', '性别'])
        # self.infoBoard.setModel(_model)
        for aInfo in _model_data:
            print("aInfo:", aInfo)
            item1 = QStandardItem("%s" % aInfo["young_name"])
            item1.setFont(QFont("Roman times",15))
            item1.setTextAlignment(Qt.AlignCenter)
            item1.setEditable(False)
            item2 = QStandardItem("%s" % ["女", "男"][aInfo["young_isMan"]])
            item2.setFont(QFont("Roman times", 15))
            item2.setTextAlignment(Qt.AlignCenter)
            item2.setEditable(False)
            item3 = QStandardItem("%s" % aInfo["relation"])
            item3.setFont(QFont("Roman times", 15))
            item3.setTextAlignment(Qt.AlignCenter)
            item3.setEditable(False)
            item4 = QStandardItem("%s" % aInfo["old_name"])
            item4.setFont(QFont("Roman times", 15))
            item4.setTextAlignment(Qt.AlignCenter)
            item4.setEditable(False)
            item5 = QStandardItem("%s" % ["女", "男"][aInfo["old_isMan"]])
            item5.setFont(QFont("Roman times", 15))
            item5.setTextAlignment(Qt.AlignCenter)
            item5.setEditable(False)
            _model.appendRow([item1,item2,item3,item4,item5])
        return _model

    def updateTableView(self):
        # self.model.clear()
        self.info_family_model = self.createFamilyInfoModel(GlobalData.familyInfosList)
        self.infoBoard.setModel(self.info_family_model)
        print(GlobalData.familyInfosList)
        self.infoBoard.show()  # 显示更新

    def updateSearchView(self):
        self.search_family_model = self.createFamilyInfoModel(GlobalData.searchInfoList) # GlobalData.searchInfoList
        self.searchInfoBoard.setModel(self.search_family_model)
        print(GlobalData.searchInfoList)
        self.searchInfoBoard.show()  # 显示更新

    def showAddInfoDialog(self):
        self.addInfodialog = AddInfoDialog()
        self.addInfodialog.infoFilledSIGNAL.connect(self.updateTableView)  #  将信号连接到槽
        self.addInfodialog.show()

    def showDelInfoDialog(self):
        if len(GlobalData.familyInfosList) == 0:  #  列表为空
            QMessageBox.about(self, "警告", "<font size='6'>无信息可删除!</font>")
            return
        self.delInfodialog = DelInfoDialog()
        self.delInfodialog.deletedSIGNAL.connect(self.updateTableView)  # 将信号连接到槽
        self.delInfodialog.show()

    def pushFamilyInfo(self):
        if len(GlobalData.familyInfosList) == 0:  #  列表为空
            QMessageBox.about(self, "警告", "<font size='6'>无数据写入!</font>")
            return
        # 将一个家庭数据 写入数据库
        theFamily = AFamily(GlobalData.lastFamilyIndex()+1)
        theFamily.insert_family_info_list(GlobalData.familyInfosList)
        QMessageBox.about(self, "提示", "<font size='6'>已将家庭信息写入数据库!</font>")
        FzLog.info("已将家庭信息写入数据库.")
        GlobalData.familyInfosList = []   #  提交后清空familyInfosList列表
        self.updateTableView()  # 跟新显示

    def addNewFamilyInfoUI(self):
        pass

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
