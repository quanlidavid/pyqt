import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit, QSpinBox


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("PYQT6 QSpinBox")
        self.setWindowIcon(QIcon('images/camera.png'))

        hbox = QHBoxLayout()

        label = QLabel("Laptop Price: ")
        label.setFont(QFont("Times", 14))

        self.lineedit = QLineEdit()

        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.spin_selected)

        self.total_result = QLineEdit()

        hbox.addWidget(label)
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.spinbox)
        hbox.addWidget(self.total_result)

        self.setLayout(hbox)

    def spin_selected(self):
        if self.lineedit.text() != '':
            price = int(self.lineedit.text())
            totalPrice = self.spinbox.value() * price
            self.total_result.setText(str(totalPrice))
        else:
            print("Wrong value")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
