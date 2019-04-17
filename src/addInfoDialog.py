from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from config import Config,GlobalData
from fuziLog import FzLog

class AddInfoDialog(QDialog):
    infoFilledSIGNAL = pyqtSignal()   #  自定义信号，表单填写完成就发射改信号
    def __init__(self, parent=None):
        super(AddInfoDialog, self).__init__(parent)
        # young
        layout_young = QHBoxLayout()
        label1 = QLabel("晚辈")
        label1.setFont(QFont("Roman times", 15, QFont.Bold))
        self.line_young_name = QLineEdit()
        self.line_young_name.setFont(QFont("Roman times", 15))
        self.box_youngman = QRadioButton("男")
        self.box_youngman.setFont(QFont("Roman times", 15))
        self.box_youngman.setChecked(True)
        self.box_youngwoman = QRadioButton("女")
        self.box_youngwoman.setFont(QFont("Roman times", 15))
        layout_youngGender = QHBoxLayout()
        layout_youngGender.addWidget(self.box_youngman)
        layout_youngGender.addWidget(self.box_youngwoman)
        groupbox_youngGender = QGroupBox()
        groupbox_youngGender.setLayout(layout_youngGender)
        layout_young.addWidget(label1)
        layout_young.addWidget(self.line_young_name)
        layout_young.addWidget(groupbox_youngGender)

        # old
        layout_old = QHBoxLayout()
        label2 = QLabel("长辈")
        label2.setFont(QFont("Roman times", 15, QFont.Bold))
        self.line_old_name = QLineEdit()
        self.line_old_name.setFont(QFont("Roman times", 15))
        self.box_oldman = QRadioButton("男")
        self.box_oldman.setFont(QFont("Roman times", 15))
        self.box_oldman.setChecked(True)
        self.box_oldwoman = QRadioButton("女")
        self.box_oldwoman.setFont(QFont("Roman times", 15))
        layout_oldGender = QHBoxLayout()
        layout_oldGender.addWidget(self.box_oldman)
        layout_oldGender.addWidget(self.box_oldwoman)
        groupbox_oldGender = QGroupBox()
        groupbox_oldGender.setLayout(layout_oldGender)
        layout_old.addWidget(label2)
        layout_old.addWidget(self.line_old_name)
        layout_old.addWidget(groupbox_oldGender)
        # relationship
        layout_relation = QHBoxLayout()
        label3 = QLabel("关系")
        label3.setFont(QFont("Roman times", 15, QFont.Bold))
        self.comb_relation = QComboBox()
        self.comb_relation.addItems(Config.RELATIONSHIP)  # 添加关系选项
        self.comb_relation.setFont(QFont("Roman times", 15))
        self.comb_relation.setMinimumWidth(120)   #  comb最小长度
        layout_relation.addWidget(label3)
        layout_relation.addStretch(1)
        # layout_relation.addSpacerItem(QSpacerItem(10,10))
        layout_relation.addWidget(self.comb_relation)
        # layout_relation.addSpacerItem(QSpacerItem(80, 10))
        layout_relation.addStretch(1)
        # info layout
        layout_info = QVBoxLayout()
        layout_info.addLayout(layout_young)
        layout_info.addLayout(layout_old)
        layout_info.addSpacerItem(QSpacerItem(100, 20))
        layout_info.addLayout(layout_relation)
        # Yes/NO button
        self.YesButton = QPushButton("确定")
        self.YesButton.setFont(QFont("Roman times", 15))
        self.NoButton = QPushButton("取消")
        self.NoButton.setFont(QFont("Roman times", 15))
        YN_layout = QHBoxLayout()
        YN_layout.addWidget(self.YesButton)
        YN_layout.addWidget(self.NoButton)
        # main layout and setting
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout_info)
        mainLayout.addSpacerItem(QSpacerItem(100, 40))
        mainLayout.addLayout(YN_layout)
        self.setLayout(mainLayout)
        self.setWindowTitle("添加成员")
        self.resize(300,300)
        self.NoButton.clicked.connect(self.cancel)
        self.YesButton.clicked.connect(self.ok) # 连接信号与槽

    def ok(self):
        young_name = self.line_young_name.text()
        old_name = self.line_old_name.text()
        if young_name == "":
            QMessageBox.about(self, "警告", "<font size='6'>未填写晚辈姓名!</font>")
        elif old_name == "":
            QMessageBox.about(self, "警告", "<font size='6'>未填写长辈姓名!</font>")
        else:
            aFamilyInfo = {}   #  局部变量，成为全局变量出错
            aFamilyInfo["young_name"] = self.line_young_name.text()
            aFamilyInfo["old_name"] = self.line_old_name.text()
            aFamilyInfo["young_isMan"] = self.box_youngman.isChecked()
            aFamilyInfo["old_isMan"] = self.box_oldman.isChecked()
            aFamilyInfo["relation"] = self.comb_relation.currentText()
            GlobalData.familyInfosList.append(aFamilyInfo)  #  写入familyInfo列表
            FzLog.info("加入家庭信息：%s",aFamilyInfo)
            # print("global:",GlobalData.AFamilyInfo)
            self.infoFilledSIGNAL.emit()  #  发射信号
            self.close()

    def cancel(self):
        self.close()

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    dialog = AddInfoDialog()
    dialog.show()
    sys.exit(app.exec_())
