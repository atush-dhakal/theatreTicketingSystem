from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *
from db_insert_update import *

class ScheduleMovie(QWidget):
    def __init__(self, db, username):
        super(ScheduleMovie, self).__init__()

        self.username = username
        self.db = db
        title = QLabel("Schedule Movie")
        title.setStyleSheet("font: 30pt")

        self.movies = QComboBox()
        for movie in select_movie_names(self.db):
            print("movie name:", movie)
            self.movies.addItem(movie[0])

        moviename = QGroupBox()
        layout1 = QFormLayout()
        layout1.addRow(QLabel("Name"), self.movies)
        moviename.setLayout(layout1)

        releasedate = QHBoxLayout()
        self.releaseDateMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        releasedate.addWidget(self.releaseDateMonth)
        releasedate.addWidget(QLabel("/"))
        self.releaseDateDay = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        releasedate.addWidget(self.releaseDateDay)
        releasedate.addWidget(QLabel("/"))
        self.releaseDateYear = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        releasedate.addWidget(self.releaseDateYear)

        playdate = QHBoxLayout()
        self.playDateMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        playdate.addWidget(self.playDateMonth)
        playdate.addWidget(QLabel("/"))
        self.playDateDay = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        playdate.addWidget(self.playDateDay)
        playdate.addWidget(QLabel("/"))
        self.playDateYear = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        playdate.addWidget(self.playDateYear)

        release = QGroupBox()
        layout3 = QFormLayout()
        layout3.addRow(QLabel("Release Date"), releasedate)
        release.setLayout(layout3)

        play = QGroupBox()
        layout4 = QFormLayout()
        layout4.addRow(QLabel("Play Date"), playdate)
        play.setLayout(layout4)

        self.BackButton = QPushButton("Back")
        self.AddButton = QPushButton("Add")
        self.AddButton.clicked.connect(self.schedule_movie)

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignCenter)
        vbox.addWidget(moviename)
        vbox.addWidget(release)
        vbox.addWidget(play)
        vbox.addWidget(self.BackButton)
        vbox.addWidget(self.AddButton)	

        self.setLayout(vbox)

    def schedule_movie(self):
        movieName = str(self.movies.currentText())
        releaseDate = self.releaseDateYear.text() + "-" + self.releaseDateMonth.text() + "-" + self.releaseDateDay.text()
        playDate = self.playDateYear.text() + "-" + self.playDateMonth.text() + "-" + self.playDateDay.text()

        if self.empty(movieName) or self.empty(releaseDate) or len(releaseDate) != 10 or self.empty(playDate) or len(playDate) != 10:
            self.required_field_msg()
            return False

        if releaseDate > playDate:
            self.play_before_release_msg()
            return False

        try:
            alreadyScheduled = movies_played_on_day(self.db, self.username, playDate)
            print("alreadyScheduled:", alreadyScheduled)
            capacities = manager_theater_capacity(self.db, self.username)
            print("capacities:", capacities)
            if capacities is not None and len(capacities) > 0 and alreadyScheduled is not None and len(alreadyScheduled) >= capacities[0][0]:
                self.too_many_msg()
                return False
            schedule_movie_play(self.db, self.username, movieName, releaseDate, playDate)
            self.schedule_movie_success_msg()
        except Exception as e:
            self.schedule_movie_fail_msg()
            print("schedule movie error:", e)

    def schedule_movie_fail_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Invalid Input")
        msgText = ("Failed to schedule movie. Make sure your input is valid.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()

    def schedule_movie_success_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Movie Scheduled")
        msgText = ("Your movie play date has been scheduled.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()

    def play_before_release_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Invalid Play Date")
        msgText = ("Play Date cannot be before Release Date.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return

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

    def too_many_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Too Many Movies Scheduled")
        msgText = ("You already have too many movies schedlued on this day.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()
        # wait for user response
        result = self.m.exec_()
        if (result == QMessageBox.Ok):
            return