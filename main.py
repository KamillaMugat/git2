import sys
import random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.аp = False
        self.pushButton.clicked.connect(self.no)

    def no(self):
        self.аp = True
        self.update()

    def paintEvent(self, event):
        if self.аp:
            p = QPainter()
            p.begin(self)
            p.setBrush(QColor('yellow'))
            d = random.randint(20, 140)
            p.drawEllipse(150, 150, d, d)
            p.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())