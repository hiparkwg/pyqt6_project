#--------------------------
# normal한 윈도우 창 만들기
#--------------------------
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys

app = QApplication(sys.argv)
#win = QPushButton("push")
win = QWidget()
win.show()

sys.exit(app.exec())
