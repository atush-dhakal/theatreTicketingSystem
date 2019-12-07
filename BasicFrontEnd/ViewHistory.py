from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *

class ViewHistory(QWidget):
    def __init__(self, db, username):
        super(ViewHistory, self).__init__()

        self.resize(685, 500)
        self.username = username
        self.db = db

        title = QLabel("View History")
        title.setStyleSheet("font: 30pt")

        views = select_views(self.db, self.username)
        self.table = QTableWidget()
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(5)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        # default to showing all users when screen loads
        # update table with user data
        self.update_view_table(views)

        self.BackButton = QPushButton("Back")

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignCenter)
        vbox.addWidget(self.table)
        vbox.addWidget(self.BackButton)
        self.setLayout(vbox)


    def update_view_table(self, views):
        numViews = len(views)
        self.table.setRowCount(numViews + 1)

        self.table.setItem(0, 0, QTableWidgetItem("Movie"))
        self.table.setItem(0, 1, QTableWidgetItem("Theater"))
        self.table.setItem(0, 2, QTableWidgetItem("Company"))
        self.table.setItem(0, 3, QTableWidgetItem("Card#"))
        self.table.setItem(0, 4, QTableWidgetItem("View Date"))

        for count, viewData in enumerate(views):
            self.table.setItem(count + 1, 0, QTableWidgetItem(viewData[0]))
            self.table.setItem(count + 1, 1, QTableWidgetItem(viewData[1]))
            self.table.setItem(count + 1, 2, QTableWidgetItem(viewData[2]))
            self.table.setItem(count + 1, 3, QTableWidgetItem(viewData[3]))
            self.table.setItem(count + 1, 4, QTableWidgetItem(str(viewData[4])))