from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *

class CompanyDetails(QWidget):
    def __init__(self, db, company):
        super(CompanyDetails, self).__init__()

        self.resize(685, 500)
        self.db = db
        title = QLabel("Company Detail")
        title.setStyleSheet("font: 30pt")

        companyname = company
        theaters = select_company_theater(db, company)
        print("detail theaters:", theaters)
        employeenames = select_company_employees(db, company)

        name = QGroupBox()
        layout1 = QFormLayout()
        layout1.addRow(QLabel("Name: " + companyname))#, companyname)
        name.setLayout(layout1)

        employees = QGroupBox()
        layout2 = QFormLayout()
        layout2.addRow(QLabel("Employees: " + ", ".join(employeenames)))#, employeenames)
        employees.setLayout(layout2)

        # here
        self.table = QTableWidget()
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(5)
        # default to showing all users when screen loads
        # update table with user data
        self.update_theater_table(theaters)

        self.BackButton = QPushButton("Back")

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignCenter)
        vbox.addWidget(name)
        vbox.addWidget(employees)
        vbox.addWidget(QLabel("Theaters"),  alignment=Qt.AlignCenter)
        vbox.addWidget(self.table)
        vbox.addWidget(self.BackButton)

        self.setLayout(vbox)

    def update_theater_table(self, theaters):
        numTheaters = len(theaters)
        self.table.setRowCount(numTheaters + 1)

        self.table.setItem(0, 0, QTableWidgetItem("Name"))
        self.table.setItem(0, 1, QTableWidgetItem("Manager"))
        self.table.setItem(0, 2, QTableWidgetItem("City"))
        self.table.setItem(0, 3, QTableWidgetItem("State"))
        self.table.setItem(0, 4, QTableWidgetItem("Capacity"))

        for count, theaterData in enumerate(theaters):
            self.table.setItem(count + 1, 0, QTableWidgetItem(theaterData[0]))
            self.table.setItem(count + 1, 1, QTableWidgetItem(theaterData[1]))
            self.table.setItem(count + 1, 2, QTableWidgetItem(theaterData[2]))
            self.table.setItem(count + 1, 3, QTableWidgetItem(theaterData[3]))
            self.table.setItem(count + 1, 4, QTableWidgetItem(str(theaterData[4])))