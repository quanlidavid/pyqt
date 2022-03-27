import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("PYQT6 QVBoxLayout")
        self.setWindowIcon(QIcon('images/camera.png'))

        vbox = QVBoxLayout()

        btn1 = QPushButton("Click One")
        btn2 = QPushButton("Click Two")
        btn3 = QPushButton("Click Three")
        btn4 = QPushButton("Click Four")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        # vbox.addSpacing(100)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        vbox.addStretch(1)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
