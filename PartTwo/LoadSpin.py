import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout, QLabel, QVBoxLayout, QLineEdit, QSpinBox, \
    QDoubleSpinBox
from PyQt6 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("DoubleSpinDemo.ui", self)

        self.linePrice = self.findChild(QLineEdit, "lineEdit_price")
        self.doubleSpin = self.findChild(QDoubleSpinBox, "doubleSpinBox")
        self.lineResult = self.findChild(QLineEdit, "lineEdit_result")

        self.doubleSpin.valueChanged.connect(self.spin_selected)

    def spin_selected(self):
        if self.linePrice.text() != '':
            price = int(self.linePrice.text())
            totalPrice = self.doubleSpin.value() * price
            self.lineResult.setText(str(totalPrice))
        else:
            print("Wrong value")


app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
