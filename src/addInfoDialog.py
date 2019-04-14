from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDialog,
        QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
        QPushButton, QVBoxLayout, QWidget,QComboBox,QRadioButton,QGroupBox)
from config import Config,Data

class AddInfoDialog(QDialog):
    def __init__(self, parent=None):
        super(AddInfoDialog, self).__init__(parent)
        # young
        layout_young = QHBoxLayout()
        label1 = QLabel("晚辈")
        self.line_young_name = QLineEdit()
        self.box_youngman = QRadioButton("男")
        self.box_youngman.setChecked(True)
        self.box_youngwoman = QRadioButton("女")
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
        self.line_old_name = QLineEdit()
        self.box_oldman = QRadioButton("男")
        self.box_oldman.setChecked(True)
        self.box_oldwoman = QRadioButton("女")
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
        self.comb_relation = QComboBox()
        self.comb_relation.addItems(Config.RELATIONSHIP)  # 添加关系选项
        layout_relation.addWidget(label3)
        layout_relation.addWidget(self.comb_relation)
        # info layout
        layout_info = QVBoxLayout()
        layout_info.addLayout(layout_young)
        layout_info.addLayout(layout_old)
        layout_info.addLayout(layout_relation)
        # Yes/NO button
        self.YesButton = QPushButton("确定")
        self.NoButton = QPushButton("取消")
        YN_layout = QHBoxLayout()
        YN_layout.addWidget(self.YesButton)
        YN_layout.addWidget(self.NoButton)
        # main layout and setting
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout_info)
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
            print("未填晚辈写姓名.")
        elif old_name == "":
            print("未填写长辈姓名.")
        else:
            Data.young_name = self.line_young_name.text()
            Data.old_name = self.line_old_name.text()
            Data.young_isMan = self.box_youngman.isChecked()
            Data.old_isMan = self.box_youngwoman.isChecked()
            Data.relation = self.comb_relation.currentText()
            print(self.line_young_name.text(),self.line_old_name.text(),self.box_youngman.isChecked(),self.box_youngwoman.isChecked())
            self.close()

    def cancel(self):
        self.close()

    def get_ip(self):
        return self.ip

    def get_port(self):
        return self.port

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    dialog = AddInfoDialog()
    dialog.show()
    sys.exit(app.exec_())
