from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class CustomerFunctionality(QWidget):
    def __init__(self, db):
        super(CustomerFunctionality, self).__init__()

        self.db = db

        title = QLabel("Customer Functionality")
        title.setStyleSheet("font: 30pt")

        self.ExploreMovieButton = QPushButton("Explore Movie")
        self.ViewHistoryButton = QPushButton("View History")
        self.ExploreTheaterButton = QPushButton("Explore Theater")
        self.VisitHistoryButton = QPushButton("Visit History")
        self.BackButton = QPushButton("Back")

        grid = QGridLayout()
        grid.addWidget(self.ExploreMovieButton, 0, 0)
        grid.addWidget(self.ExploreTheaterButton, 1, 0)
        grid.addWidget(self.VisitHistoryButton, 1, 1)
        grid.addWidget(self.ViewHistoryButton, 0, 1)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title)
        vbox_layout.addLayout(grid)
        vbox_layout.addWidget(self.BackButton)

        self.setLayout(vbox_layout)