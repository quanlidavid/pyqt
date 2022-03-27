import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("PYQT6 QHBoxLayout")
        self.setWindowIcon(QIcon('images/camera.png'))

        hbox = QHBoxLayout()

        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Click Two")
        btn3 = QPushButton("Click Three")
        btn4 = QPushButton("Click Four")

        hbox.addStretch(1)
        hbox.addWidget(btn1)
        hbox.addStretch(1)
        hbox.addWidget(btn2)
        hbox.addStretch(1)
        # hbox.addSpacing(100)
        hbox.addWidget(btn3)
        hbox.addStretch(1)
        hbox.addWidget(btn4)
        hbox.addStretch(2)

        self.setLayout(hbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
