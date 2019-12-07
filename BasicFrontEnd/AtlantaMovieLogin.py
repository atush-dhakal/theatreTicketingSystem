from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *
import hashlib

class AtlantaMovieLogin(QDialog):
    def __init__(self, db):
        super(AtlantaMovieLogin, self).__init__()
        self.setModal(True)

        # attach db connection to class instance for access in methods
        self.db = db
        # make input boxes self variables for super access
        self.userbox = QLineEdit()
        self.passbox = QLineEdit()

        title = QLabel("Atlanta Movie Login")
        title.setStyleSheet("font: 30pt")

        form_group_box = QGroupBox()
        layout = QFormLayout()

        layout.addRow(QLabel("Username:"), self.userbox)
        layout.addRow(QLabel("Password:"), self.passbox)
        form_group_box.setLayout(layout)

        self.LoginButton = QPushButton("Login")
        self.RegisterButton =  QPushButton("Register")

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.LoginButton)
        hbox_layout.addWidget(self.RegisterButton)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title)
        vbox_layout.addWidget(form_group_box)
        vbox_layout.addLayout(hbox_layout)

        self.setLayout(vbox_layout)

    def login(self):
        # get username and pass from gui
        username = self.userbox.text()
        # m = hashlib.md5()
        # m.update(str(self.passbox.text()))
        password = hashlib.md5(self.passbox.text().encode('utf-8')).hexdigest()
        # password = hashlib.md5(self.passbox.text())
        # get password from db
        print("user:", username, "pass:", password)
        dbPassword = select_password(self.db, username)
        print("db pass:", dbPassword)
        # get db password out of tuple and strip empty binary chars
        dbPassword = dbPassword[0].rstrip('\x00')
        print("db pass strip:", dbPassword)
        # check if db password and gui password match
        if (dbPassword == password):
            print("matched")
            userData = select_user(self.db, username)
            print("userdata:", userData)
        else:
            print("password didn't match")
            # pop-up box to show login error then exit
            self.show_login_error()
            return
        # open correct screen according to user type
        self.username = username
        self.userType = userData[2]
        if (self.userType == "User"):
            return "UserFunctionality"
        elif(self.userType == "Customer"):
            return "CustomerFunctionality"
        elif (self.userType == "Manager"):
            return "ManagerOnlyFunctionality"
        elif (self.userType == "CustomerManager"):
            return "ManagerCustomerFunctionality"
        elif (self.userType == "Admin"):
            return "AdminOnlyFunctionality"
        elif (self.userType == "CustomerAdmin"):
            return "AdminCustomerFunctionality"
        else:
            # pop-up box to show user type error then exit
            self.show_usertype_error()
            return

    def show_login_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Login Failed")
        msgText = ("The username and password combination was not valid. "
            " Please try to login again.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()

    def show_usertype_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Login Failed")
        msgText = ("The account's user type was not valid. "
            "Please contact an Atlanta Movie administrator.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()