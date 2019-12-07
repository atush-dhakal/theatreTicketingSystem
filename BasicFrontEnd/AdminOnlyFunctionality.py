from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class AdminOnlyFunctionality(QWidget):
    def __init__(self, db):
        super(AdminOnlyFunctionality, self).__init__()

        self.db = db

        title = QLabel("Admin Only Functionality")
        title.setStyleSheet("font: 30pt")

        self.ManageUserButton = QPushButton("Manage User")
        self.ManageCompanyButton = QPushButton("Manage Company")
        self.CreateMovieButton = QPushButton("Create Movie")
        self.ExplorTheaterButton = QPushButton("Explore Theater")
        self.VisitHistoryButton = QPushButton("Visit History")
        self.BackButton = QPushButton("Back")

        grid = QGridLayout()
        grid.addWidget(self.ManageUserButton, 0, 0)
        grid.addWidget(self.ManageCompanyButton, 1, 0)
        grid.addWidget(self.CreateMovieButton, 2, 0)
        grid.addWidget(self.ExplorTheaterButton, 0, 1)
        grid.addWidget(self.VisitHistoryButton, 1, 1)
        grid.addWidget(self.BackButton, 2, 1)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title)
        vbox_layout.addLayout(grid)

        self.setLayout(vbox_layout)