#-----------------------------
# 버튼의 클릭 이벤트
#-----------------------------
import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('버튼 이벤트 처리')
        self.btn = QPushButton('난 버튼')
        self.btn.setCheckable(True)
        self.btn.clicked.connect(self.btn_clicked)
        self.setFixedSize(QSize(200,100))
        self.setCentralWidget(self.btn)

    def btn_clicked(self):
        print("ok...click")
        self.btn.setText('앗, 클릭되었다...')
        self.btn.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyWin()
    win.show()

    sys.exit(app.exec())