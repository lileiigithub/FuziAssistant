from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from config import Config,GlobalData
from fuziLog import FzLog

class MessageBox(QDialog):
    def __init__(self, parent=None):
        super(MessageBox, self).__init__(parent)
        self.msg = QMessageBox()
        print(self.msg)

    def informationBox(self,_str):
        self.msg.text(_str)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    dialog = MessageBox()
    dialog.informationBox("da")
    # dialog.show()
    sys.exit(app.exec_())
