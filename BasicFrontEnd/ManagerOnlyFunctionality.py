from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ManagerOnlyFunctionality(QWidget):
    def __init__(self, db):
        super(ManagerOnlyFunctionality, self).__init__()

        self.db = db

        title = QLabel("Manager-Only Functionality")
        title.setStyleSheet("font: 30pt")

        self.TheaterOverviewButton = QPushButton("Theater Overview")
        self.ScheduleMovieButton = QPushButton("Schedule Movie")
        self.ExploreTheaterButton = QPushButton("Explore Theater")
        self.VisitHistoryButton = QPushButton("Visit History")
        self.BackButton = QPushButton("Back")

        grid = QGridLayout()
        grid.addWidget(self.TheaterOverviewButton, 0, 0)
        grid.addWidget(self.ScheduleMovieButton, 1, 0)
        grid.addWidget(self.ExploreTheaterButton, 0, 1)
        grid.addWidget(self.VisitHistoryButton, 1, 1)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title)
        vbox_layout.addLayout(grid)
        vbox_layout.addWidget(self.BackButton)

        self.setLayout(vbox_layout)