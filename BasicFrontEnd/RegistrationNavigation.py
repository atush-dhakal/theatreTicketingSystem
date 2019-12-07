from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class RegistrationNavigation(QWidget):
    def __init__(self, db):
        super(RegistrationNavigation, self).__init__()

        self.db = db

        title = QLabel("Registration Navigation")
        title.setStyleSheet("font: 30pt")

        self.UserOnlyButton = QPushButton("User Only")
        self.CustomerOnlyButton = QPushButton("Customer Only")
        self.ManagerOnlyButton = QPushButton("Manager Only")
        self.ManagerCustomerButton = QPushButton("Manager Customer")
        self.BackButton = QPushButton("Back")

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(title)
        vbox_layout.addWidget(self.UserOnlyButton)
        vbox_layout.addWidget(self.CustomerOnlyButton)
        vbox_layout.addWidget(self.ManagerOnlyButton)
        vbox_layout.addWidget(self.ManagerCustomerButton)
        vbox_layout.addWidget(self.BackButton)

        self.setLayout(vbox_layout)