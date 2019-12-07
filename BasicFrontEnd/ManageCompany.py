from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *
from db_filter import *

class ManageCompany(QWidget):
    def __init__(self, db):
        super(ManageCompany, self).__init__()

        self.sortColumn = 0
        self.sortOrder = Qt.AscendingOrder

        self.resize(535, 768)
        self.db = db
        title = QLabel("Manage Company")
        title.setStyleSheet("font: 30pt")

        city = QHBoxLayout()
        city.addWidget(QLabel("# City Covered"))
        self.cityLow = QLineEdit()
        self.cityLow.setMaxLength(5)
        self.cityLow.setValidator(QIntValidator(0, 99999))
        city.addWidget(self.cityLow)

        city.addWidget(QLabel(" -- "))
        self.cityHigh = QLineEdit()
        self.cityHigh.setMaxLength(5)
        self.cityHigh.setValidator(QIntValidator(0, 99999))
        city.addWidget(self.cityHigh)

        theaters = QHBoxLayout()
        theaters.addWidget(QLabel("# Theaters"))
        self.theaterLow = QLineEdit()
        self.theaterLow.setMaxLength(5)
        self.theaterLow.setValidator(QIntValidator(0, 99999))
        theaters.addWidget(self.theaterLow)
        theaters.addWidget(QLabel(" -- "))

        self.theaterHigh = QLineEdit()
        self.theaterHigh.setMaxLength(5)
        self.theaterHigh.setValidator(QIntValidator(0, 99999))
        theaters.addWidget(self.theaterHigh)



        employees = QHBoxLayout()
        employees.addWidget(QLabel("# Employees"))
        self.employeeLow = QLineEdit()
        self.employeeLow.setMaxLength(5)
        self.employeeLow.setValidator(QIntValidator(0, 99999))
        employees.addWidget(self.employeeLow)

        employees.addWidget(QLabel(" -- "))
        self.employeeHigh = QLineEdit()
        self.employeeHigh.setMaxLength(5)
        self.employeeHigh.setValidator(QIntValidator(0, 99999))
        employees.addWidget(self.employeeHigh)

        # get all companies in the database
        companyList = select_all_company(self.db)
        # setup company combo box
        compBox = QGroupBox()
        layout = QFormLayout()
        self.compComboBox = QComboBox()
        self.compComboBox.addItem('ALL')
        for company in companyList:
            self.compComboBox.addItem(company)
        layout.addRow(QLabel("Company"), self.compComboBox)
        compBox.setLayout(layout)

        hbox = QHBoxLayout()
        self.companyBtn = QPushButton("Company")
        self.companyBtn.clicked.connect(lambda: self.sortTable(0))

        self.cityBtn = QPushButton("City Cover")
        self.cityBtn.clicked.connect(lambda: self.sortTable(1))

        self.theaterBtn = QPushButton("Theaters")
        self.theaterBtn.clicked.connect(lambda: self.sortTable(2))

        self.employeeBtn = QPushButton("Employees")
        self.employeeBtn.clicked.connect(lambda: self.sortTable(3))

        hbox.addWidget(self.companyBtn)
        hbox.addWidget(self.cityBtn)
        hbox.addWidget(self.theaterBtn)
        hbox.addWidget(self.employeeBtn)

        self.table = QTableWidget()
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(4)
        # default to showing all users when screen loads
        companyList = filter_company(self.db)
        # update table with user data
        self.update_company_table(companyList)

        self.FilterButton = QPushButton("Filter")
        self.FilterButton.clicked.connect(self.get_filter_company)

        self.CreateTheaterButton = QPushButton("Create Theater")


        self.DetailsButton = QPushButton("Details")

        grid = QGridLayout()
        grid.addWidget(self.FilterButton, 0, 0)
        grid.addWidget(self.CreateTheaterButton, 0 ,1)
        grid.addWidget(self.DetailsButton, 0, 2)

        self.BackButton = QPushButton("Back")



        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignCenter)
        vbox.addWidget(compBox)
        vbox.addLayout(city)
        vbox.addLayout(theaters)
        vbox.addLayout(employees)
        vbox.addLayout(grid)
        vbox.addLayout(hbox)
        vbox.addWidget(self.table)
        vbox.addWidget(self.BackButton)

        self.setLayout(vbox)

    def update_company_table(self, companyList):
        numComps = len(companyList)
        self.table.setRowCount(numComps)
        for count, companyData in enumerate(companyList):
            self.table.setItem(count, 0, QTableWidgetItem(companyData[0]))
            self.table.setItem(count, 1, QTableWidgetItem(companyData[1]))
            self.table.setItem(count, 2, QTableWidgetItem(companyData[2]))
            self.table.setItem(count, 3, QTableWidgetItem(companyData[3]))

    def get_filter_company(self):
        name = str(self.compComboBox.currentText())
        try:
            cityLow = int(self.cityLow.text())
        except:
            cityLow = None
        try:
            cityHigh = int(self.cityHigh.text())
        except:
            cityHigh = None
        try:
            theaterLow = int(self.theaterLow.text())
        except:
            theaterLow = None
        try:
            theaterHigh = int(self.theaterHigh.text())
        except:
            theaterHigh = None
        try:
            employeeLow = int(self.employeeLow.text())
        except:
            employeeLow = None
        try:
            employeeHigh = int(self.employeeHigh.text())
        except:
            employeeHigh = None
        companyList = filter_company(self.db, name, cityLow, cityHigh, theaterLow, theaterHigh, employeeLow, employeeHigh)
        self.update_company_table(companyList)

    def view_company_details(self):
        for company in self.table.selectedItems():
            allCompanyList = select_all_company(self.db)
            if company.text() in allCompanyList:
                return company.text()
        return False

    def sortTable(self, column):
        print("new sort col:", column)
        print("cur:", self.sortColumn, self.sortOrder)
        if column == self.sortColumn:
            if self.sortOrder == Qt.AscendingOrder:
                self.sortOrder = Qt.DescendingOrder
            else:
                self.sortOrder = Qt.AscendingOrder
        else:
            self.sortColumn = column
            self.sortOrder = Qt.AscendingOrder
        self.table.sortByColumn(self.sortColumn, self.sortOrder)