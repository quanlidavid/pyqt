from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("PYQT6 QPushButton")
        self.setWindowIcon(QIcon('images/camera.png'))

        self.create_button()

    def create_button(self):
        btn = QPushButton("Click", self)
        btn.setGeometry(100, 100, 130, 130)
        btn.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon("images/camera.png"))
        btn.setIconSize(QSize(36, 36))

        # popup menu
        menu = QMenu()
        menu.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        menu.setStyleSheet('background-color:red')
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
