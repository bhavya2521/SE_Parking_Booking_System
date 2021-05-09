from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QLabel
from AdminLoginScreen import AdminLoginScreen
from UserLoginScreen import UserLoginScreen
from PyQt5 import QtGui

class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Let's get started")
        self.resize(300,100)
        layout=QVBoxLayout()
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        label=QLabel("Login As:")
        label.setStyleSheet("color:#000;padding:8px 0px;font-size:18px;")
        layout.addWidget(label)

        admin_btn = QPushButton("Admin")
        admin_btn.setStyleSheet("padding:5px;font-size:20px;background:green;color:#fff")
        layout.addWidget(admin_btn)
        admin_btn.clicked.connect(self.showAdmin)

        user_btn=QPushButton("User")
        user_btn.setStyleSheet("padding:5px;font-size:20px;background:green;color:#fff")
        layout.addWidget(user_btn)
        user_btn.clicked.connect(self.showUser)

        layout.addStretch()
        self.setLayout(layout)

    def showLoginScreen(self):
        self.show()

    def showAdmin(self):

        self.home = AdminLoginScreen()
        self.home.show()

    def showUser(self):

        self.home = UserLoginScreen()
        self.home.show()





