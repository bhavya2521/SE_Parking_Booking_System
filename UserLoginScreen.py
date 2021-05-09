from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QApplication, QMessageBox
import sys
from DataBaseOperation import DBOperation
from admin import Admin
from PyQt5.QtCore import Qt,QTimer
from form import form
from PyQt5 import QtGui
from user import User


class UserLoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("User Login")
        self.resize(300,100)
        layout=QVBoxLayout()
        self.setWindowIcon(QtGui.QIcon('icon.png'))


        label_username=QLabel("Username : ")
        label_username.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        self.input_username=QLineEdit()
        self.input_username.setStyleSheet("padding:5px;font-size:17px")

        label_password=QLabel("Password : ")
        label_password.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")

        self.input_password=QLineEdit()
        self.input_password.setStyleSheet("padding:5px;font-size:17px")
        self.input_password.setEchoMode(QLineEdit.Password)

        self.error_msg = QLabel()
        self.error_msg.setStyleSheet("color:red;padding:8px 0px;font-size:18px;text-align:center")

        btn_login = QPushButton("Login")
        btn_login.setStyleSheet("padding:5px;font-size:20px;background:green;color:#fff")

        new_btn = QPushButton("New User!!")
        new_btn.setStyleSheet("padding:5px;font-size:20px;background:green;color:#fff")

        layout.addWidget(label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(btn_login)
        layout.addWidget(new_btn)
        layout.addWidget(self.error_msg)
        layout.addStretch()
        btn_login.clicked.connect(self.showHome)
        new_btn.clicked.connect(self.showform)
        self.setLayout(layout)

    def showLoginScreen(self):
        self.show()

    def showform(self):
        self.close()
        self.home = form()
        self.home.show()



    def showHome(self):
        if self.input_username.text()=="":
            self.error_msg.setText("Please Enter Username")
            return

        if self.input_password.text()=="":
            self.error_msg.setText("Please Enter Password")
            return
        dboperation=DBOperation()
        result=dboperation.doUserLogin(self.input_username.text(),self.input_password.text())
        if result:
            QMessageBox.about(self, "Congrats!!", "SignIn Successful")
            self.close()
            self.home = User(self.input_username.text())
            self.home.show()
        else:
            QMessageBox.about(self, "Oops", "Invalid Login. Try Again")
            self.close()
