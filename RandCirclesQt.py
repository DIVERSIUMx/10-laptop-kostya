from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint
from PyQt6 import uic

import sys
from random import randint
from forms import Ui_MainWindow


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.circle_radius = 0
        self.col = QColor(0, 0, 0, 0)
        super().__init__()
        self.setupUi(self)
        self.btn.clicked.connect(self.make_circle)

    def make_circle(self):
        self.circle_radius = randint(30, 290)
        self.col = QColor(randint(0, 255), randint(0, 255), randint(0, 255), 255)
        self.update()

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setPen(self.col)
        painter.drawEllipse(QPoint(300, 300), self.circle_radius, self.circle_radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = YellowCircles()
    win.show()
    sys.exit(app.exec())
