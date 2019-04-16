from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from config import Config,GlobalData
from fuziLog import FzLog

class DelInfoDialog(QDialog):
    deletedSIGNAL = pyqtSignal()   #  自定义信号，表单填写完成就发射改信号
    def __init__(self, parent=None):
        super(DelInfoDialog, self).__init__(parent)
        # young
        layout_del = QHBoxLayout()
        label1 = QLabel("删除行的序号")
        self.line_del_line = QLineEdit()
        layout_del.addWidget(label1)
        layout_del.addWidget(self.line_del_line)
        # Yes/NO button
        self.YesButton = QPushButton("确定")
        self.NoButton = QPushButton("取消")
        YN_layout = QHBoxLayout()
        YN_layout.addWidget(self.YesButton)
        YN_layout.addWidget(self.NoButton)
        # main layout and setting
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(layout_del)
        mainLayout.addLayout(YN_layout)
        self.setLayout(mainLayout)
        self.setWindowTitle("删除信息")
        self.resize(300,300)
        self.NoButton.clicked.connect(self.cancel)
        self.YesButton.clicked.connect(self.ok) # 连接信号与槽

    def ok(self):
        if len(GlobalData.familyInfosList) == 0:
            QMessageBox.about(self,"警告","无信息可删除!")
            return
        lineNumber = self.line_del_line.text()
        if lineNumber.isdigit()==False:
            QMessageBox.about(self, "警告", "请填写数字!")
            return
        lineNumber = int(lineNumber)
        if lineNumber <= 0 or lineNumber > len(GlobalData.familyInfosList):
            QMessageBox.about(self, "警告", "删除行超出范围!")
            return

        del(GlobalData.familyInfosList[lineNumber-1])
        self.deletedSIGNAL.emit()
        FzLog.info("输出行：%s",lineNumber)
        self.close()

    def cancel(self):
        self.close()


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    dialog = DelInfoDialog()
    dialog.show()
    sys.exit(app.exec_())
