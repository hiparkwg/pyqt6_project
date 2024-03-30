import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout, QPushButton

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Signal and Slot')
        self.setGeometry(30, 30, 500, 400)
        btn=QPushButton('종료',self)
        btn.setGeometry(600,600,30,40)
        lcd = QLCDNumber(self)
        lcd.setGeometry(10,10,100,100)        
        dial = QDial(self)
        dial.setGeometry(140,10, 100,100)

        btn.clicked.connect(self.close)
        dial.valueChanged.connect(lcd.display)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())