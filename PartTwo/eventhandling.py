import sys

from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle("PYQT6 Event Handling")
        self.setWindowIcon(QIcon('images/camera.png'))
        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn = QPushButton("Change Text")
        btn.clicked.connect(self.clicked_btn)
        self.label = QLabel("Default Text")

        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def clicked_btn(self):
        self.label.setText("Another Text")
        self.label.setFont(QFont("Times", 15))
        self.label.setStyleSheet("color:red")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
