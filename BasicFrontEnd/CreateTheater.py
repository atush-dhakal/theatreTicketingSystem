from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *
from db_insert_update import *

class CreateTheater(QDialog):
    def __init__(self, db):
        super(CreateTheater, self).__init__()
        print("initializing create theater")
        self.db = db

        title = QLabel("Create Theater")
        title.setStyleSheet("font: 30pt")

        name = QGroupBox()
        layout = QFormLayout()
        self.name = QLineEdit()
        layout.addRow(QLabel("Name"), self.name)
        name.setLayout(layout)

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
        self.compComboBox.currentIndexChanged.connect(self.update_manager_dropdown)

        grid = QGridLayout()
        grid.addWidget(name, 0, 0)
        grid.addWidget(compBox, 0, 1)

        street = QHBoxLayout()
        street.addWidget(QLabel("Street Address"))
        self.addr = QLineEdit()
        street.addWidget(self.addr)

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

        capacity = QGroupBox()
        layout = QFormLayout()
        self.capacity = QLineEdit()
        layout.addRow(QLabel("Capacity"), self.capacity)
        capacity.setLayout(layout)

        managerBox = QGroupBox()
        layout = QFormLayout()
        self.manComboBox = QComboBox()
        currentCompany = str(self.compComboBox.currentText())
        managerList = select_unassigned_company_managers(self.db, currentCompany)
        print("managerlist:", managerList)
        for fname, lname, username in managerList:
            print("manager:", fname, lname)
            self.manComboBox.addItem(fname + " " + lname, username)
        layout.addRow(QLabel("Manager"), self.manComboBox)
        managerBox.setLayout(layout)

        grid3 = QGridLayout()
        grid3.addWidget(capacity, 0, 0)
        grid3.addWidget(managerBox, 0, 1)

        buttons = QHBoxLayout()

        self.BackButton = QPushButton("Back")
        self.CreateButton = QPushButton("Create")

        buttons.addWidget(self.BackButton)
        buttons.addWidget(self.CreateButton)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title,alignment=Qt.AlignCenter)
        vbox_layout.addLayout(grid)
        vbox_layout.addLayout(street)
        vbox_layout.addLayout(grid2)
        vbox_layout.addLayout(grid3)
        vbox_layout.addLayout(buttons)
        self.setLayout(vbox_layout)
        print("initialized create theater")

    def create_new_theater(self):
        theater_name = self.name.text()
        print("theater name:", theater_name)
        company = str(self.compComboBox.currentText())
        print("company:", company)
        address = self.addr.text()
        print("address:", address)
        city = self.city.text()
        print("city:", city)
        state = str(self.state.currentText())
        print("state:", state)
        zip_code = self.zipcode.text()
        print("zipcode:", "'" + zip_code + "'")
        capacity = self.capacity.text()
        print("capacity:", capacity)
        manager = str(self.manComboBox.currentData())
        print("manager:", manager)

        if self.empty(theater_name) or self.empty(company) or self.empty(address) or self.empty(city) \
                or self.empty(zip_code) or len(zip_code) != 5 or self.empty(capacity) or self.empty(manager):
            self.required_field_msg()
            return False

        try:
            insert_theater(self.db,
                       theater_name,
                       company,
                       manager,
                       zip_code,
                       address,
                       city,
                       state,
                       capacity)
            self.create_theater_success_msg()
            return True
        except Exception as e:
            print("create theater error:", e)
            self.creater_theater_fail_msg()
            return False

    def update_manager_dropdown(self):
        companyName = self.compComboBox.currentText()
        managerList = select_unassigned_company_managers(self.db, companyName)
        self.manComboBox.clear()
        print("managerlist:", managerList)
        for fname, lname, username in managerList:
            print("manager:", fname, lname)
            self.manComboBox.addItem(fname + " " + lname, username)



    def create_theater_success_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Theater Creation Successful")
        msgText = ("Your theater has been created")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return

    def creater_theater_fail_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Invalid Input")
        msgText = ("Failed to create theater. Make sure your input is valid.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()

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