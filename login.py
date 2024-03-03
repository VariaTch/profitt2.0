from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("\n"
"background-color: rgb(65, 65, 105);")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(-1, 15, 15, 15)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setStyleSheet("background-color: rgba(0, 0, 0, 100);\n"
"border-radius: 15px;")
        self.frame.setInputMethodHints(QtCore.Qt.ImhLatinOnly)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_log_in = QtWidgets.QLabel(self.frame)
        self.label_log_in.setGeometry(QtCore.QRect(100, 10, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(30)
        self.label_log_in.setFont(font)
        self.label_log_in.setStyleSheet("color: rgba(255, 255, 255,210);")
        self.label_log_in.setAlignment(QtCore.Qt.AlignCenter)
        self.label_log_in.setObjectName("label_log_in")
        self.le_name = QtWidgets.QLineEdit(self.frame)
        self.le_name.setGeometry(QtCore.QRect(70, 165, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.le_name.setFont(font)
        self.le_name.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.le_name.setObjectName("le_name")
        self.le_password = QtWidgets.QLineEdit(self.frame)
        self.le_password.setGeometry(QtCore.QRect(70, 265, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.le_password.setFont(font)
        self.le_password.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgba(255,255,255,230);\n"
"padding-bottom:7px;")
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setObjectName("le_password")
        self.pb_enter = QtWidgets.QPushButton(self.frame)
        self.pb_enter.setGeometry(QtCore.QRect(70, 365, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(15)
        self.pb_enter.setFont(font)
        self.pb_enter.setStyleSheet("QPushButton{\n"
"    color: rgba(255, 255, 255, 210);\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: rgba(105,118,132,200);\n"
"}")
        self.pb_enter.setObjectName("pb_enter")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(70, 330, 300, 30))
        self.label.setStyleSheet("font: 25 10pt \"Calibri Light\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border:none;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 230, 300, 30))
        self.label_2.setStyleSheet("font: 25 10pt \"Calibri Light\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border:none;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_log_in.setText(_translate("Form", "Log in"))
        self.le_name.setPlaceholderText(_translate("Form", "User name"))
        self.le_password.setPlaceholderText(_translate("Form", "Password"))
        self.pb_enter.setText(_translate("Form", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
