from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QCheckBox, QDialog,
        QDialogButtonBox, QGridLayout, QHBoxLayout, QLabel, QLayout, QLineEdit,
        QPushButton, QVBoxLayout, QWidget,QComboBox,QRadioButton,QGroupBox)
from config import Config

class AddInfoDialog(QDialog):
    def __init__(self, parent=None):
        super(AddInfoDialog, self).__init__(parent)
        # young
        layout_young = QHBoxLayout()
        label1 = QLabel("晚辈")
        line_young_name = QLineEdit()
        box_youngman = QRadioButton("男")
        box_youngwoman = QRadioButton("女")
        layout_youngGender = QHBoxLayout()
        layout_youngGender.addWidget(box_youngman)
        layout_youngGender.addWidget(box_youngwoman)
        groupbox_youngGender = QGroupBox()
        groupbox_youngGender.setLayout(layout_youngGender)
        layout_young.addWidget(label1)
        layout_young.addWidget(line_young_name)
        layout_young.addWidget(groupbox_youngGender)

        # old
        layout_old = QHBoxLayout()
        label2 = QLabel("长辈")
        line_old_name = QLineEdit()
        box_oldman = QRadioButton("男")
        box_oldwoman = QRadioButton("女")
        layout_oldGender = QHBoxLayout()
        layout_oldGender.addWidget(box_oldman)
        layout_oldGender.addWidget(box_oldwoman)
        groupbox_oldGender = QGroupBox()
        groupbox_oldGender.setLayout(layout_oldGender)
        layout_old.addWidget(label2)
        layout_old.addWidget(line_old_name)
        layout_old.addWidget(groupbox_oldGender)
        # relationship
        layout_relation = QHBoxLayout()
        label3 = QLabel("关系")
        comb_relation = QComboBox()
        comb_relation.addItems(Config.RELATIONSHIP)  # 添加关系选项
        layout_relation.addWidget(label3)
        layout_relation.addWidget(comb_relation)
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
        # ip = self.ip_lineEdit.text()
        # port = self.port_lineEdit.text()
        # if port!="" and ip !="":
        #     Data.address = (ip,int(port))
        #     print("设置新网络连接：",Data.address)
        self.close()
        # return self.address

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
