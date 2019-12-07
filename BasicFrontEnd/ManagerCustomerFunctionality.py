from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ManagerCustomerFunctionality(QWidget):
    def __init__(self, db):
        super(ManagerCustomerFunctionality, self).__init__()

        self.db = db

        title = QLabel("Manager-Customer Functionality")
        title.setStyleSheet("font: 30pt")

        self.TheaterOverviewButton = QPushButton("Theater Overview")
        self.ScheduleMovieButton = QPushButton("Schedule Movie")
        self.ExploreTheaterButton = QPushButton("Explore Theater")
        self.VisitHistoryButton = QPushButton("Visit History")
        self.ExploreMovieButton = QPushButton("Explore Movie")
        self.ViewHistoryButton = QPushButton("View History")
        self.BackButton = QPushButton("Back")

        grid = QGridLayout()
        grid.addWidget(self.TheaterOverviewButton, 0, 0)
        grid.addWidget(self.ScheduleMovieButton, 1, 0)
        grid.addWidget(self.ExploreTheaterButton, 1, 1)
        grid.addWidget(self.VisitHistoryButton, 2, 1)
        grid.addWidget(self.ExploreMovieButton, 0, 1)
        grid.addWidget(self.ViewHistoryButton, 2, 0)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title)
        vbox_layout.addLayout(grid)
        vbox_layout.addWidget(self.BackButton)

        self.setLayout(vbox_layout)