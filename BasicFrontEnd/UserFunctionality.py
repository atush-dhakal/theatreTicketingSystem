from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class UserFunctionality(QWidget):
    def __init__(self, db):
        super(UserFunctionality, self).__init__()

        self.db = db

        title = QLabel("User Functionality")
        title.setStyleSheet("font: 30pt")

        self.ExploreTheaterButton = QPushButton("Explore Theater")
        self.VisitHistoryButton = QPushButton("Visit History")
        self.BackButton = QPushButton("Back")

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title)
        vbox_layout.addWidget(self.ExploreTheaterButton)
        vbox_layout.addWidget(self.VisitHistoryButton)
        vbox_layout.addWidget(self.BackButton)

        self.setLayout(vbox_layout)