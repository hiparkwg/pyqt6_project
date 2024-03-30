import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QMainWindow, QApplication
form_class= uic.loadUiType("./test.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myw = MyWindow()
    myw.resize(300,300)
    myw.setWindowTitle("내첫번째 ui 테스트")
    sys.exit(app.exec())