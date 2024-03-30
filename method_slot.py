#---------------------------
# 메서드 슬롯에 시그널 연결
#---------------------------
import sys
from random import choice
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

window_title=[
    "111111",
    "111112",
    "111113",
    "111114",
    "111115",
    "111116",
    "Something"
]

class MainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.times_clicked=0
        self.setWindowTitle('My App')

        self.btn = QPushButton('Press Me')
        self.btn.clicked.connect(self.btn_clicked)

        self.windowTitleChanged.connect(self.win_title_changed)
        self.setCentralWidget(self.btn)

    def btn_clicked(self):
        new_title = choice(window_title)
        self.setWindowTitle(new_title)

    def win_title_changed(self, window_title):
        if window_title == "Something":
            self.btn.setDisabled(True)

app = QApplication(sys.argv)            
win= MainWin()
win.show()

sys.exit(app.exec())