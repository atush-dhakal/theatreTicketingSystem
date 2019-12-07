from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_insert_update import *
from db_select import *

class ManagerCustomerRegistration(QDialog):
    def __init__(self, db):
        super(ManagerCustomerRegistration, self).__init__()

        self.db = db

        title = QLabel("Manager-Customer Registration")
        title.setStyleSheet("font: 30pt")

        fn = QGroupBox()
        layout = QFormLayout()
        self.fName = QLineEdit()
        layout.addRow(QLabel("First Name"), self.fName)
        fn.setLayout(layout)

        ln = QGroupBox()
        layout = QFormLayout()
        self.lName = QLineEdit()
        layout.addRow(QLabel("Last Name"), self.lName)
        ln.setLayout(layout)

        uname = QGroupBox()
        layout = QFormLayout()
        self.user = QLineEdit()
        layout.addRow(QLabel("Username"), self.user)
        uname.setLayout(layout)

        # get all companies in the database
        companyList = select_all_company(self.db)
        # setup company combo box
        compBox = QGroupBox()
        layout = QFormLayout()
        self.compComboBox = QComboBox()
        for company in companyList:
            self.compComboBox.addItem(company)
        layout.addRow(QLabel("Company"), self.compComboBox)
        compBox.setLayout(layout)

        passw = QGroupBox()
        layout = QFormLayout()
        self.password = QLineEdit()
        layout.addRow(QLabel("Password"), self.password)
        passw.setLayout(layout)

        confpassw = QGroupBox()
        layout = QFormLayout()
        self.cPassword = QLineEdit()
        layout.addRow(QLabel("Confirm Password"), self.cPassword)
        confpassw.setLayout(layout)

        grid = QGridLayout()
        grid.addWidget(fn, 0, 0)
        grid.addWidget(ln, 0, 1)
        grid.addWidget(uname, 1, 0)
        grid.addWidget(compBox, 1, 1)
        grid.addWidget(passw, 2, 0)
        grid.addWidget(confpassw, 2, 1)

        street = QHBoxLayout()
        street.addWidget(QLabel("Street Address"))
        self.stAddr = QLineEdit()
        street.addWidget(self.stAddr)

        city = QGroupBox()
        layout = QFormLayout()
        self.city = QLineEdit()
        layout.addRow(QLabel("City"), self.city)
        city.setLayout(layout)

        state = QGroupBox()
        layout = QFormLayout()
        self.state = QComboBox()
        abvs = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        for abv in abvs:
            self.state.addItem(abv)
        layout.addRow(QLabel("State"), self.state)
        state.setLayout(layout)

        zipcode = QGroupBox()
        layout = QFormLayout()
        self.zipcode = QLineEdit()
        self.zipcode.setMaxLength(5)
        self.zipcode.setValidator(QIntValidator(0, 99999))
        layout.addRow(QLabel("Zipcode"), self.zipcode)
        zipcode.setLayout(layout)

        grid2 = QGridLayout()
        grid2.addWidget(city, 0, 0)
        grid2.addWidget(state, 0, 1)
        grid2.addWidget(zipcode, 0, 2)

        creditCardGrid = QGridLayout()
        validator = QRegExpValidator(QRegExp("[0-9]+"))
        creditCardGrid.addWidget(QLabel("Credit Card 1"),0,0)
        self.cardNum1 = QLineEdit()
        self.cardNum1.setMaxLength(16)
        self.cardNum1.setValidator(validator)
        creditCardGrid.addWidget(self.cardNum1,0,1)

        creditCardGrid.addWidget(QLabel("Credit Card 2"),1,0)
        self.cardNum2 = QLineEdit()
        self.cardNum2.setMaxLength(16)
        self.cardNum2.setValidator(validator)
        creditCardGrid.addWidget(self.cardNum2,1,1)

        creditCardGrid.addWidget(QLabel("Credit Card 3"),2,0)
        self.cardNum3 = QLineEdit()
        self.cardNum3.setMaxLength(16)
        self.cardNum3.setValidator(validator)
        creditCardGrid.addWidget(self.cardNum3,2,1)

        creditCardGrid.addWidget(QLabel("Credit Card 4"),3,0)
        self.cardNum4 = QLineEdit()
        self.cardNum4.setMaxLength(16)
        self.cardNum4.setValidator(validator)
        creditCardGrid.addWidget(self.cardNum4,3,1)

        creditCardGrid.addWidget(QLabel("Credit Card 5"),4,0)
        self.cardNum5 = QLineEdit()
        self.cardNum5.setMaxLength(16)
        self.cardNum5.setValidator(validator)
        creditCardGrid.addWidget(self.cardNum5,4,1)

        buttons = QHBoxLayout()
        self.BackButton = QPushButton("Back")
        self.RegisterButton =  QPushButton("Register")
        buttons.addWidget(self.BackButton)
        buttons.addWidget(self.RegisterButton)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title,alignment=Qt.AlignCenter)
        vbox_layout.addLayout(grid)
        vbox_layout.addLayout(street)
        vbox_layout.addLayout(grid2)
        vbox_layout.addLayout(creditCardGrid)
        vbox_layout.addLayout(buttons)
        self.setLayout(vbox_layout)

    def register_manager_cust(self):
        # user data
        fName = self.fName.text()
        lName = self.lName.text()
        user = self.user.text()
        userType = "CustomerManager"
        password = self.password.text()
        cPassword = self.cPassword.text()
        # manager data
        stAddr = self.stAddr.text()
        city = self.city.text()
        state = str(self.state.currentText())
        zipcode = self.zipcode.text()
        company = str(self.compComboBox.currentText())
        # credit card data
        cardList = list()
        cardList.append(self.cardNum1.text())
        cardList.append(self.cardNum2.text())
        cardList.append(self.cardNum3.text())
        cardList.append(self.cardNum4.text())
        cardList.append(self.cardNum5.text())

        if self.empty(fName) or self.empty(lName) or self.empty(user) or self.empty(password) or self.empty(stAddr) \
                or self.empty(city) or self.empty(state) or self.empty(zipcode) or len(zipcode) != 5 or self.empty(company):
            self.required_field_msg()
            return False

        if password is not None and len(password) < 8:
            self.password_too_short_msg()
            return False

        # need failure on everything in this - db.commit() not in db file
        if (password == cPassword):
            # insert user data
            try:
                insert_user(self.db, user, password, userType, fName, lName)
            except:
                self.register_user_fail_msg()
                return False
            # insert manager data
            try:
                insert_manager(self.db, user, stAddr, city, state, zipcode, company)
            except:
                delete_user(self.db, user)
                self.register_manager_fail_msg()
                return False
            # insert credit card data
            addedCard = False
            for cardNum in cardList:
                try:
                    if (len(cardNum) == 16):
                        print("found valid card:", cardNum)
                        insert_credit_card(self.db, user, cardNum)
                        addedCard = True
                    elif len(cardNum) > 0:
                        print("found card of invalid length:", cardNum)
                        delete_user(self.db, user)
                        delete_manager(self.db, user)
                        self.invalid_card_length_msg()
                        return False
                except Exception as e:
                    print("register customer exception:", e)
                    delete_user(self.db, user)
                    delete_manager(self.db, user)
                    self.register_card_fail_msg()
                    return False
            # return success on inserting user and credit cards
            if addedCard:
                self.register_success_msg()
                return True
            else:
                delete_user(self.db, user)
                delete_manager(self.db, user)
                self.credit_card_required_msg()
                return False

    def register_user_fail_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Manager Registration Failed")
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

    def register_manager_fail_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Manager Registration Failed")
        msgText = ("Your adddress information is already in the database."
            "Please check that your address information is correct."
            "If this is not a user error, please contact an admin.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return

    def register_card_fail_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Credit Card Registration Failed")
        msgText = ("Your credit card number already exists in the database. "
            "Please use another credit card. If this is an error, please contact an admin")
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
        msg.setWindowTitle("Manager Customer Registration Successful")
        msgText = ("Your manager customer registration request has been recieved. "
            "Please wait for an admin to approve your manager customer account.")
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

    def invalid_card_length_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Invalid Credit Card Number")
        msgText = ("Your credit card numbers must be 16 digits long.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return

    def credit_card_required_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Credit Card Number Required")
        msgText = ("You must enter at least 1 valid credit card number.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return

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