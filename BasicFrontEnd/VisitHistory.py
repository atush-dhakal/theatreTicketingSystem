from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *

class VisitHistory(QWidget):
    def __init__(self, db, username):
        super(VisitHistory, self).__init__()

        self.username = username
        self.db = db

        title = QLabel("Visit History")
        title.setStyleSheet("font: 30pt")

        company = QGroupBox()
        compLayout = QFormLayout()
        self.companies = QComboBox()
        self.companies.addItem("ALL")
        for comp in select_all_company(self.db):
            self.companies.addItem(comp)
        compLayout.addRow(QLabel("Company"), self.companies)
        company.setLayout(compLayout)

        visitdate1 = QHBoxLayout()
        self.minMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        visitdate1.addWidget(self.minMonth)
        visitdate1.addWidget(QLabel("/"))
        self.minDay = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        visitdate1.addWidget(self.minDay)
        visitdate1.addWidget(QLabel("/"))
        self.minYear = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        visitdate1.addWidget(self.minYear)

        visitdate2 = QHBoxLayout()
        self.maxMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        visitdate2.addWidget(self.maxMonth)
        visitdate2.addWidget(QLabel("/"))
        self.maxDay = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        visitdate2.addWidget(self.maxDay)
        visitdate2.addWidget(QLabel("/"))
        self.maxYear = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        visitdate2.addWidget(self.maxYear)

        visit = QHBoxLayout()
        visit.addWidget(QLabel("Visit Date"))
        visit.addLayout(visitdate1)
        visit.addWidget(QLabel("--"))
        visit.addLayout(visitdate2)

        visits = select_visits(self.db, username=self.username)
        self.table = QTableWidget()
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(4)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # default to showing all users when screen loads
        # update table with user data
        self.update_visit_table(visits)

        self.BackButton = QPushButton("Back")
        self.FilterButton = QPushButton("Filter")
        self.FilterButton.clicked.connect(self.filter_visits)

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignCenter)
        vbox.addWidget(company)
        vbox.addLayout(visit)
        vbox.addWidget(self.FilterButton)
        vbox.addWidget(self.table)
        vbox.addWidget(self.BackButton)

        self.setLayout(vbox)

    def filter_visits(self):
        companyName = self.companies.currentText()
        minDate = self.minYear.text() + "-" + self.minMonth.text() + "-" + self.minDay.text()
        maxDate = self.maxYear.text() + "-" + self.maxMonth.text() + "-" + self.maxDay.text()
        print("minDate:", minDate, len(minDate))
        print("maxDate:", maxDate, len(maxDate))
        visits = select_visits(self.db, self.username, companyName, minDate, maxDate)
        self.update_visit_table(visits)

    def update_visit_table(self, visits):
        numVisits = len(visits)
        self.table.setRowCount(numVisits + 1)

        self.table.setItem(0, 0, QTableWidgetItem("Theater"))
        self.table.setItem(0, 1, QTableWidgetItem("Address"))
        self.table.setItem(0, 2, QTableWidgetItem("Company"))
        self.table.setItem(0, 3, QTableWidgetItem("Visit Date"))

        for count, theaterData in enumerate(visits):
            self.table.setItem(count + 1, 0, QTableWidgetItem(theaterData[0]))
            self.table.setItem(count + 1, 1, QTableWidgetItem(theaterData[3] + ", " + theaterData[4] + ", " + theaterData[5] + " " + theaterData[6]))
            self.table.setItem(count + 1, 2, QTableWidgetItem(theaterData[1]))
            self.table.setItem(count + 1, 3, QTableWidgetItem(str(theaterData[2])))
