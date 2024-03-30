#------------------------
# 창의 크기를 지정
#------------------------

import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('hi..창 크기 조절')
        btn = QPushButton('난 버튼')
        self.setFixedSize(QSize(200,100))
        self.setCentralWidget(btn)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWin()
    win.show()

    sys.exit(app.exec())