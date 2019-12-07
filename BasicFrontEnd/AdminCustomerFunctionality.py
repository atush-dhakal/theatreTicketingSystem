from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class AdminCustomerFunctionality(QWidget):
    def __init__(self, db):
        super(AdminCustomerFunctionality, self).__init__()

        self.db = db
        title = QLabel("Admin-Customer Functionality")
        title.setStyleSheet("font: 30pt")

        self.ManageUserButton = QPushButton("Manage User")
        self.ManageCompanyButton = QPushButton("Manage Company")
        self.CreateMovieButton = QPushButton("Create Movie")
        self.ExploreMovieButton = QPushButton("Explore Movie")
        self.ExploreTheaterButton = QPushButton("Explore Theater")
        self.VisitHistoryButton = QPushButton("Visit History")
        self.ViewHistoryButton = QPushButton("View History")
        self.BackButton = QPushButton("Back")

        grid = QGridLayout()
        grid.addWidget(self.ManageUserButton, 0, 0)
        grid.addWidget(self.ManageCompanyButton, 1, 0)
        grid.addWidget(self.CreateMovieButton, 2, 0)
        grid.addWidget(self.ExploreTheaterButton, 1, 1)
        grid.addWidget(self.VisitHistoryButton, 3, 0)
        grid.addWidget(self.ViewHistoryButton, 2, 1)
        grid.addWidget(self.ExploreMovieButton, 0, 1)
        grid.addWidget(self.BackButton, 3, 1)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title)
        vbox_layout.addLayout(grid)

        self.setLayout(vbox_layout)