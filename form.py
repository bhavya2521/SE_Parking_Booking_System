from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QLabel,QLineEdit,QApplication
import sys
from DataBaseOperation import DBOperation
from admin import Admin
from PyQt5.QtCore import Qt,QTimer
import time
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui


class form(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Signup")
        self.resize(300,100)
        layout=QVBoxLayout()
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.dboperation = DBOperation()

        label_username=QLabel("Username : ")
        label_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        self.input_username=QLineEdit()
        self.input_username.setStyleSheet("padding:5px;font-size:17px")


        label_password=QLabel("Password : ")
        label_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        self.input_password=QLineEdit()
        self.input_password.setStyleSheet("padding:5px;font-size:17px")
        self.input_password.setEchoMode(QLineEdit.Password)

        label_password2 = QLabel("Confirm Password : ")
        label_password2.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        self.input_password2 = QLineEdit()
        self.input_password2.setStyleSheet("padding:5px;font-size:17px")
        self.input_password2.setEchoMode(QLineEdit.Password)

        label_email = QLabel("Email-Id: ")
        label_email.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        self.input_email = QLineEdit()
        self.input_email.setStyleSheet("padding:5px;font-size:17px")

        label_number = QLabel("Contact Number: ")
        label_number.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        self.input_number = QLineEdit()
        self.input_number.setStyleSheet("padding:5px;font-size:17px")

        self.error_msg = QLabel()
        self.error_msg.setStyleSheet("color:red;padding:8px 0px;font-size:18px;text-align:center")

        btn_login = QPushButton("Sign Up")
        btn_login.setStyleSheet("padding:5px;font-size:20px;background:green;color:#fff")

        layout.addWidget(label_username)
        layout.addWidget(self.input_username)

        layout.addWidget(label_password)
        layout.addWidget(self.input_password)

        layout.addWidget(label_password2)
        layout.addWidget(self.input_password2)

        layout.addWidget(label_email)
        layout.addWidget(self.input_email)

        layout.addWidget(label_number)
        layout.addWidget(self.input_number)

        layout.addWidget(btn_login)
        layout.addWidget(self.error_msg)
        layout.addStretch()
        btn_login.clicked.connect(self.showHome)
        self.setLayout(layout)

    def showform(self):
        self.show()

    def showHome(self):
        self.error_msg.setText("")
        data=self.dboperation.getAllUsers()
        if self.input_username.text()=="":
            self.error_msg.setText("Please Enter Username")
            return
        for d in data:
            if self.input_username.text()==d[1]:
                self.error_msg.setText("Username Already Taken")
                return
            if self.input_email.text()==d[3]:
                self.error_msg.setText("Email Id Already registered")
                return
            if self.input_number.text()==d[4]:
                self.error_msg.setText("Mobile Number Already registered")
                return


        if self.input_password.text()=="":
            self.error_msg.setText("Please Enter Password")
            return

        if self.input_password2.text()=="":
            self.error_msg.setText("Please Confirm your Password")
            return

        if self.input_password.text()!=self.input_password2.text():
            self.error_msg.setText("Password Confirmaion Failed")
            return

        if self.input_email.text()=="":
            self.error_msg.setText("Please Enter Email")
            return

        if self.input_number.text()=="":
            self.error_msg.setText("Please Enter Contact")
            return

        result=self.dboperation.InsertUser(self.input_username.text(), self.input_password.text(), self.input_email.text(), self.input_number.text())
        if result:
            QMessageBox.about(self, "Congrats!!", "SignUp Successful")
            self.close()
        else:
            QMessageBox.about(self, "Oops", "SignUp Failed. Try Again")
            self.close()
