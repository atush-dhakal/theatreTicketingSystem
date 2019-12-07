from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_insert_update import *

class CreateMovie(QWidget):
    def __init__(self, db):
        super(CreateMovie, self).__init__()

        self.db = db
        title = QLabel("Create Movie")
        title.setStyleSheet("font: 30pt")

        name = QGroupBox()
        layout1 = QFormLayout()
        self.mName = QLineEdit()
        layout1.addRow(QLabel("Name"), self.mName)
        name.setLayout(layout1)

        duration = QGroupBox()
        layout2 = QFormLayout()
        self.duration = QLineEdit()
        layout2.addRow(QLabel("Duration"), self.duration)
        duration.setLayout(layout2)

        date = QHBoxLayout()
        self.month = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        date.addWidget(self.month)
        date.addWidget(QLabel("-"))
        self.day = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        date.addWidget(self.day)
        date.addWidget(QLabel("-"))
        self.year = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        date.addWidget(self.year)

        release = QGroupBox()
        layout3 = QFormLayout()
        layout3.addRow(QLabel("Release Date"), date)#, QCalendarWidget()).toString("dd-mm-yyyy"))
        release.setLayout(layout3)

        self.BackButton = QPushButton("Back")
        self.CreateButton = QPushButton("Create")
        self.CreateButton.clicked.connect(self.create_new_movie)

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignCenter)
        vbox.addWidget(name)
        vbox.addWidget(duration)
        vbox.addWidget(release)
        vbox.addWidget(self.BackButton)
        vbox.addWidget(self.CreateButton)	

        self.setLayout(vbox)

    def create_new_movie(self):
        name = self.mName.text()
        duration = self.duration.text()
        month = self.month.text()
        day = self.day.text()
        year = self.year.text()
        release = year + "-" + month + "-" + day

        if self.empty(name) or self.empty(duration) or self.empty(release) or len(release) != 10:
            self.required_field_msg()
            return False

        try:
            insert_movie(self.db, name, release, duration)
        except Exception as e:
            print("create movie failed:", e)
            self.creater_movie_fail_msg()
            return

        self.create_movie_success_msg()

    def create_movie_success_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Create Movie Successful")
        msgText = ("Your movie has been created and saved.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            self.mName.setText("")
            self.duration.setText("")
            self.month.setText("")
            self.day.setText("")
            self.year.setText("")
            return

    def creater_movie_fail_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Invalid Input")
        msgText = ("Failed to create movie. Make sure your input is valid.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()

    def empty(self, text):
        if text is None or len(text) < 1:
            return True

    def required_field_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Required Field Missing")
        msgText = ("Make sure you have completed all fields.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return