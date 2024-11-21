#DemoForm.py
#DomoForm.ui 화면 + DemoForm.py 로직

import sys  
from PyQt5.QtWidgets import *
from PyQt5 import uic

from_class = uic.loadUiType("DemoForm.ui")[0]

class DemoForm(QDialog, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.label.setText("첫번째 윈도우")
        #OK버튼 클릭 시 label 변경
        self.btnOk.clicked.connect(self.btn1_clicked)

    def btn1_clicked(self):
        self.label.setText("버튼 클릭")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()