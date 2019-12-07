from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *

class TheaterOverview(QWidget):
    def __init__(self, db, username):
        super(TheaterOverview, self).__init__()

        self.username = username
        self.db = db
        title = QLabel("Theater Overview")
        title.setStyleSheet("font: 30pt")

        moviename = QGroupBox()
        layout1 = QFormLayout()
        self.movieName = QLineEdit()
        layout1.addRow(QLabel("Movie Name"), self.movieName)
        moviename.setLayout(layout1)

        movieduration = QHBoxLayout()
        movieduration.addWidget(QLabel("Movie Duration"))
        self.minDuration = QLineEdit()
        self.minDuration.setMaxLength(5)
        self.minDuration.setValidator(QIntValidator(0, 99999))
        movieduration.addWidget(self.minDuration)

        movieduration.addWidget(QLabel("--"))
        self.maxDuration = QLineEdit()
        self.maxDuration.setMaxLength(5)
        self.maxDuration.setValidator(QIntValidator(0, 99999))
        movieduration.addWidget(self.maxDuration)

        date1 = QHBoxLayout()
        self.minReleaseMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        date1.addWidget(self.minReleaseMonth)
        date1.addWidget(QLabel("/"))
        self.minReleaseDay = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        date1.addWidget(self.minReleaseDay)
        date1.addWidget(QLabel("/"))
        self.minReleaseYear = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        date1.addWidget(self.minReleaseYear)

        date2 = QHBoxLayout()
        self.maxReleaseMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        date2.addWidget(self.maxReleaseMonth)
        date2.addWidget(QLabel("/"))
        self.maxReleaseDay = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        date2.addWidget(self.maxReleaseDay)
        date2.addWidget(QLabel("/"))
        self.maxReleaseYear = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        date2.addWidget(self.maxReleaseYear)

        date3 = QHBoxLayout()
        self.minPlayMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        date3.addWidget(self.minPlayMonth)
        date3.addWidget(QLabel("/"))
        self.minPlayDay = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        date3.addWidget(self.minPlayDay)
        date3.addWidget(QLabel("/"))
        self.minPlayYear = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        date3.addWidget(self.minPlayYear)

        date4 = QHBoxLayout()
        self.maxPlayMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        date4.addWidget(self.maxPlayMonth)
        date4.addWidget(QLabel("/"))
        self.maxPlayDay = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        date4.addWidget(self.maxPlayDay)
        date4.addWidget(QLabel("/"))
        self.maxPlayYear = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        date4.addWidget(self.maxPlayYear)

        release = QHBoxLayout()
        release.addWidget(QLabel("Movie Release Date"))
        release.addLayout(date1)
        release.addWidget(QLabel("--"))
        release.addLayout(date2)

        play = QHBoxLayout()
        play.addWidget(QLabel("Movie Play Date"))
        play.addLayout(date3)
        play.addWidget(QLabel("--"))
        play.addLayout(date4)

        notPlayed = QHBoxLayout()
        self.checkbox = QCheckBox()
        notPlayed.addWidget(self.checkbox, alignment=Qt.AlignRight)
        notPlayed.addWidget(QLabel("Only Include Not Played Movies"), alignment=Qt.AlignLeft)

        plays = select_theater_plays(self.db, self.username)
        self.table = QTableWidget()
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(4)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # default to showing all users when screen loads
        # update table with user data
        self.update_theater_plays_table(plays)

        self.BackButton = QPushButton("Back")
        self.FilterButton = QPushButton("Filter")
        self.FilterButton.clicked.connect(self.filter_theater_plays)

        vbox = QVBoxLayout()
        vbox.addWidget(title, alignment=Qt.AlignCenter)
        vbox.addWidget(moviename)
        vbox.addLayout(movieduration)
        vbox.addLayout(release)
        vbox.addLayout(play)
        vbox.addLayout(notPlayed)
        vbox.addWidget(self.FilterButton)
        vbox.addWidget(self.table)
        vbox.addWidget(self.BackButton)	

        self.setLayout(vbox)

    def filter_theater_plays(self):
        movieName = self.movieName.text()
        minDuration = self.minDuration.text()
        maxDuration = self.maxDuration.text()

        minReleaseDate = self.minReleaseYear.text() + "-" + self.minReleaseMonth.text() + "-" + self.minReleaseDay.text()
        maxReleaseDate = self.maxReleaseYear.text() + "-" + self.maxReleaseMonth.text() + "-" + self.maxReleaseDay.text()
        minPlayDate = self.minPlayYear.text() + "-" + self.minPlayMonth.text() + "-" + self.minPlayDay.text()
        maxPlayDate = self.maxPlayYear.text() + "-" + self.maxPlayMonth.text() + "-" + self.maxPlayDay.text()

        onlyIncludeNotPlayed = self.checkbox.isChecked()

        plays = select_theater_plays(self.db,
                                     self.username,
                                     movieName,
                                     minDuration,
                                     maxDuration,
                                     minReleaseDate,
                                     maxReleaseDate,
                                     minPlayDate,
                                     maxPlayDate,
                                     onlyIncludeNotPlayed)
        self.update_theater_plays_table(plays)
    def update_theater_plays_table(self, plays):
        numPlays = len(plays)
        self.table.setRowCount(numPlays + 1)

        self.table.setItem(0, 0, QTableWidgetItem("Movie Name"))
        self.table.setItem(0, 1, QTableWidgetItem("Duration"))
        self.table.setItem(0, 2, QTableWidgetItem("Release Date"))
        self.table.setItem(0, 3, QTableWidgetItem("Play Date"))

        for count, playData in enumerate(plays):
            print("playData:", playData)
            self.table.setItem(count + 1, 0, QTableWidgetItem(playData[0]))
            self.table.setItem(count + 1, 1, QTableWidgetItem(str(playData[1])))
            self.table.setItem(count + 1, 2, QTableWidgetItem(str(playData[2])))
            self.table.setItem(count + 1, 3, QTableWidgetItem(str(playData[3])))