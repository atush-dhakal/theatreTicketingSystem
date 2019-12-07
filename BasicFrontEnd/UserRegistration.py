from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from db_insert_update import *

class UserRegistration(QDialog):
    def __init__(self, db):
        super(UserRegistration, self).__init__()

        self.db = db

        title = QLabel("User Registration")
        title.setStyleSheet("font: 30pt")

        fn = QGroupBox()
        layout = QFormLayout()
        self.firstNameBox =QLineEdit()
        layout.addRow(QLabel("First Name"), self.firstNameBox)
        fn.setLayout(layout)

        ln = QGroupBox()
        layout = QFormLayout()
        self.lastNameBox = QLineEdit()
        layout.addRow(QLabel("Last Name"), self.lastNameBox)
        ln.setLayout(layout)

        uname = QGroupBox()
        layout = QFormLayout()
        self.userBox = QLineEdit()
        layout.addRow(QLabel("Username"), self.userBox)
        uname.setLayout(layout)

        passw = QGroupBox()
        layout = QFormLayout()
        self.passBox = QLineEdit()
        self.passBox.setEchoMode(QLineEdit.Password)
        layout.addRow(QLabel("Password"), self.passBox)
        passw.setLayout(layout)

        confpassw = QGroupBox()
        layout = QFormLayout()
        self.confirmPassBox = QLineEdit()
        self.confirmPassBox.setEchoMode(QLineEdit.Password)
        layout.addRow(QLabel("Confirm Password"), self.confirmPassBox)
        confpassw.setLayout(layout)

        grid = QGridLayout()
        grid.addWidget(fn, 0, 0)
        grid.addWidget(ln, 0, 1)
        grid.addWidget(uname, 1, 0)
        grid.addWidget(passw, 2, 0)
        grid.addWidget(confpassw, 2, 1)

        self.BackButton = QPushButton("Back")
        self.RegisterButton = QPushButton("Register")

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(self.BackButton)
        hbox_layout.addWidget(self.RegisterButton)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title,alignment=Qt.AlignCenter)
        vbox_layout.addLayout(grid)
        vbox_layout.addLayout(hbox_layout)
        self.setLayout(vbox_layout)

    # returns True if registration successful
    def register_user(self):
        password = self.passBox.text()
        confirmPass = self.confirmPassBox.text()

        if password is not None and len(password) < 8:
            self.password_too_short_msg()
            return False

        if (password == confirmPass):
            username = self.userBox.text()
            userType = "User"
            firstName = self.firstNameBox.text()
            lastName = self.lastNameBox.text()

            if self.empty(firstName) or self.empty(lastName) or self.empty(username) or self.empty(password):
                self.required_field_msg()
                return False

            try:
                insert_user(self.db, username, password, userType, firstName, lastName)
            except:
                self.register_fail_msg()
                return False
            # return success message object on register user success
            self.register_success_msg()
            # return control to MAIN.py after success msg is accepted
            return True
        else:
            self.show_pass_error()
            self.passBox.setText("")
            self.confirmPassBox.setText("")
            return False

    def show_pass_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Passwords Did Not Match")
        msgText = ("The password in the password box and the confirm password "
            " box did not match. Please try to enter a valid password again.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return

    def register_fail_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("User Registration Failed")
        msgText = ("Your username already exists in the database. "
            "Please use another username.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return

    def register_success_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("User Registration Successful")
        msgText = ("Your user registration request has been recieved. "
            " Please wait for an admin to approve your user account.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return

    def empty(self, text):
        if text is None or len(text) < 1:
            return True

    def required_field_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Required Field Missing")
        msgText = ("Make sure you have completed all fields.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return

    def password_too_short_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Password Too Short")
        msgText = ("Your password must be at least 8 characters.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return