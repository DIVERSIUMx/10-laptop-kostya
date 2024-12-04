from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint
from PyQt6 import uic
import sys
from random import randint


class YellowCircles(QMainWindow):
    def __init__(self):
        self.circle_radius = 0
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.btn.clicked.connect(self.make_circle)

    def make_circle(self):
        self.circle_radius = randint(30, 290)
        self.update()

    def paintEvent(self, a0):
        painter = QPainter(self)
        painter.setPen(QColor(255, 240, 3, 255))
        painter.drawEllipse(QPoint(300, 300), self.circle_radius, self.circle_radius)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = YellowCircles()
    win.show()
    sys.exit(app.exec())
