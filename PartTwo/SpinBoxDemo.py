# Form implementation generated from reading ui file 'SpinBoxDemo.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(654, 242)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_penPrice = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_penPrice.setFont(font)
        self.lineEdit_penPrice.setObjectName("lineEdit_penPrice")
        self.horizontalLayout.addWidget(self.lineEdit_penPrice)
        self.spinBox = QtWidgets.QSpinBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.spinBox.setFont(font)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.editingFinished.connect(self.first_result)
        self.horizontalLayout.addWidget(self.spinBox)
        self.lineEdit_pTotal = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_pTotal.setFont(font)
        self.lineEdit_pTotal.setObjectName("lineEdit_pTotal")
        self.horizontalLayout.addWidget(self.lineEdit_pTotal)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_sugerPrice = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_sugerPrice.setFont(font)
        self.lineEdit_sugerPrice.setObjectName("lineEdit_sugerPrice")
        self.horizontalLayout_2.addWidget(self.lineEdit_sugerPrice)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.editingFinished.connect(self.second_result)
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        self.lineEdit_sTotal = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lineEdit_sTotal.setFont(font)
        self.lineEdit_sTotal.setObjectName("lineEdit_sTotal")
        self.horizontalLayout_2.addWidget(self.lineEdit_sTotal)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def first_result(self):
        penPrice = int(self.lineEdit_penPrice.text())
        totalPenPrice = self.spinBox.value() * penPrice
        self.lineEdit_pTotal.setText(str(totalPenPrice))

    def second_result(self):
        sugerPrice = int(self.lineEdit_sugerPrice.text())
        totalSugerPrice = self.doubleSpinBox.value() * sugerPrice
        self.lineEdit_sTotal.setText(str(totalSugerPrice))

        totalPenPrice = int(self.lineEdit_pTotal.text())

        totalAmount = totalPenPrice + totalSugerPrice

        self.label_result.setText("Total Price is : {}".format(totalAmount))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Pen Price:"))
        self.label_2.setText(_translate("Form", "Sugar Price:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
