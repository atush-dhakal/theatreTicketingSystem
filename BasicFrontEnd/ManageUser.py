from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *
from db_filter import *
from db_insert_update import *

class ManageUser(QWidget):
    def __init__(self, db):
        super(ManageUser, self).__init__()

        self.sortColumn = 0
        self.sortOrder = Qt.AscendingOrder

        self.db = db

        # set the size of the window
        self.resize(535, 768)

        title = QLabel("Manage User")
        title.setStyleSheet("font: 30pt")

        username = QGroupBox()
        layout1 = QFormLayout()
        self.user_name = QLineEdit()
        layout1.addRow(QLabel("Username"), self.user_name)
        username.setLayout(layout1)

        StatusBox = QGroupBox()
        self.status = QComboBox()
        layout2 = QFormLayout()
        self.status.addItem("All")
        self.status.addItem("Pending")
        self.status.addItem("Declined")
        self.status.addItem("Approved")
        layout2.addRow(QLabel("Status"), self.status)
        StatusBox.setLayout(layout2)

        hbox = QHBoxLayout()
        self.usernameBtn = QPushButton("Username")
        self.usernameBtn.clicked.connect(lambda: self.sortTable(0))

        self.creditCardBtn = QPushButton("Credit Card Count")
        self.creditCardBtn.clicked.connect(lambda: self.sortTable(1))

        self.userTypeBtn = QPushButton("User Type")
        self.userTypeBtn.clicked.connect(lambda: self.sortTable(2))

        self.statusBtn = QPushButton("Status")
        self.statusBtn.clicked.connect(lambda: self.sortTable(3))

        hbox.addWidget(self.usernameBtn)
        hbox.addWidget(self.creditCardBtn)
        hbox.addWidget(self.userTypeBtn)
        hbox.addWidget(self.statusBtn)
        
        self.table = QTableWidget()
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(4)
        # default to showing all users when screen loads
        userList = select_all_user(self.db)
        # update table with user data
        self.update_user_table(userList)

        self.FilterButton = QPushButton("Filter")
        self.FilterButton.clicked.connect(self.get_filter_user)

        self.ApproveButton = QPushButton("Approve")
        self.ApproveButton.clicked.connect(self.run_approve_user)

        self.DeclineButton = QPushButton("Decline")
        self.DeclineButton.clicked.connect(self.run_decline_user)

        grid = QGridLayout()
        grid.addWidget(username, 0, 0)
        grid.addWidget(StatusBox, 0, 1)
        grid.addWidget(self.FilterButton, 1, 0)
        grid.addWidget(self.ApproveButton, 2, 0)
        grid.addWidget(self.DeclineButton, 2, 1)

        self.BackButton = QPushButton("Back")

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignCenter)
        vbox.addLayout(grid)
        vbox.addLayout(hbox)
        vbox.addWidget(self.table)
        vbox.addWidget(self.BackButton)	

        self.setLayout(vbox)

    def update_user_table(self, userList):
        numUsers = len(userList)
        self.table.setRowCount(numUsers)
        for count, userData in enumerate(userList):
            self.table.setItem(count, 0, QTableWidgetItem(userData[0]))
            self.table.setItem(count, 1, QTableWidgetItem(str(len(get_user_ccs(self.db, userData[0])))))
            self.table.setItem(count, 2, QTableWidgetItem(userData[2]))
            self.table.setItem(count, 3, QTableWidgetItem(userData[3]))




    def get_filter_user(self):
        username = self.user_name.text()
        status = str(self.status.currentText()).lower()
        print("Filter on username:{} and status:{}".format(username, status))
        userList = filter_user(self.db, username, status)
        self.update_user_table(userList)
        self.table.sortByColumn(0, Qt.AscendingOrder)

    def run_approve_user(self):
        for username in self.table.selectedItems():
            allUsernameList = select_pending_declined_username(self.db)
            if username.text() in allUsernameList:
                update_user_reg_status(self.db, username.text(), "Approved")
                self.table.setItem(username.row(), 3, QTableWidgetItem("Approved"))

    def run_decline_user(self):
        for username in self.table.selectedItems():
            allUsernameList = select_pending_username(self.db)
            if username.text() in allUsernameList:
                update_user_reg_status(self.db, username.text(), "Declined")
                self.table.setItem(username.row(), 3, QTableWidgetItem("Declined"))


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
