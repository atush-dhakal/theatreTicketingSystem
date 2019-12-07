from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *
from db_insert_update import *

class ExploreTheater(QWidget):
    def __init__(self, db, username):
        super(ExploreTheater, self).__init__()

        self.username = username
        self.db = db
        title = QLabel("Explore Theater")
        title.setStyleSheet("font: 30pt")

        self.theaters = QComboBox()
        print("theaters")
        self.theaters.addItem("ALL")
        for theater in select_theaters_for_dropdown(self.db):
            self.theaters.addItem(theater[0])

        theaterName = QGroupBox()
        theaterLayout = QFormLayout()
        theaterLayout.addRow(QLabel("Theater Name"), self.theaters)
        theaterName.setLayout(theaterLayout)

        company = QGroupBox()
        compLayout = QFormLayout()
        self.companies = QComboBox()
        self.companies.addItem("ALL")
        for comp in select_all_company(self.db):
            self.companies.addItem(comp)
        compLayout.addRow(QLabel("Company"), self.companies)
        company.setLayout(compLayout)


        # companyname = QGroupBox()
        # layout1 = QFormLayout()
        # layout1.addRow(QLabel("Company Name"), companies)
        # companyname.setLayout(layout1)

        self.cityName = QLineEdit()
        city = QGroupBox()
        layout = QFormLayout()
        layout.addRow(QLabel("City"), self.cityName)
        city.setLayout(layout)

        state = QGroupBox()
        layout = QFormLayout()
        self.states = QComboBox()
        abvs = ["ALL", "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        for abv in abvs:
            self.states.addItem(abv)
        layout.addRow(QLabel("State"), self.states)
        state.setLayout(layout)

        visitdate = QHBoxLayout()
        self.visitMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        visitdate.addWidget(self.visitMonth)
        visitdate.addWidget(QLabel("/"))
        self.visit_day = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        visitdate.addWidget(self.visit_day)
        visitdate.addWidget(QLabel("/"))
        self.visit_year = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        visitdate.addWidget(self.visit_year)

        visit = QGroupBox()
        layout4 = QFormLayout()
        layout4.addRow(QLabel("Visit Date"), visitdate)
        visit.setLayout(layout4)


        # here
        self.table = QTableWidget()
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(3)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)

        # default to showing all users when screen loads
        # update table with user data
        theaterTableEntries = select_theaters_where(self.db)
        self.update_theater_table(theaterTableEntries)

        self.BackButton = QPushButton("Back")
        self.FilterButton = QPushButton("Filter")
        self.FilterButton.clicked.connect(self.filter_theaters)
        self.LogVisitButton = QPushButton("Log Visit")
        self.LogVisitButton.clicked.connect(self.log_visit)

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignCenter)
        vbox.addWidget(theaterName)
        vbox.addWidget(company)
        vbox.addWidget(city)
        vbox.addWidget(state)
        vbox.addWidget(self.FilterButton)
        # here
        vbox.addWidget(self.table)
        vbox.addWidget(self.BackButton)
        vbox.addWidget(visit)
        vbox.addWidget(self.LogVisitButton)

        self.setLayout(vbox)

    def filter_theaters(self):
        company = str(self.companies.currentText())
        theaterName = str(self.theaters.currentText())
        state = str(self.states.currentText())
        city = str(self.cityName.text())
        theaters = select_theaters_where(self.db, company, theaterName, city, state)
        self.update_theater_table(theaters)

    def update_theater_table(self, theaters):
        numTheaters = len(theaters)
        self.table.setRowCount(numTheaters + 1)

        self.table.setItem(0, 0, QTableWidgetItem("Theater"))
        self.table.setItem(0, 1, QTableWidgetItem("Address"))
        self.table.setItem(0, 2, QTableWidgetItem("Company"))

        for count, theaterData in enumerate(theaters):
            self.table.setItem(count + 1, 0, QTableWidgetItem(theaterData[0]))
            self.table.setItem(count + 1, 1, QTableWidgetItem(theaterData[2] + ", " + theaterData[3] + ", " + theaterData[4] + " " + theaterData[5]))
            self.table.setItem(count + 1, 2, QTableWidgetItem(theaterData[1]))

    def log_visit(self):
        rows = sorted(set(index.row() for index in
                          self.table.selectedIndexes()))
        if len(rows) == 1:
            theaterName = self.table.item(rows[0], 0).text()
            companyName = self.table.item(rows[0], 2).text()
            visitDate = self.visit_year.text() + "-" + self.visitMonth.text() + "-" + self.visit_day.text()
            print("theatername:", theaterName)
            print("companyname:", companyName)
            print("visitdate:", visitDate)
            print("username:", self.username)
            try:
                log_theater_visit(self.db, theaterName, companyName, visitDate, self.username)
                self.theater_visit_success_msg()
                return
            except Exception as e:
                print("visit theater error:", e)
        self.theater_visit_fail_msg()

    def theater_visit_fail_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Invalid Input")
        msgText = ("Failed to visit theater. Make sure your input is valid.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()

    def theater_visit_success_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Visit Logged")
        msgText = ("Your visit to the theater has been logged.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()