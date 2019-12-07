from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from db_select import *
from db_insert_update import *

class ExploreMovie(QWidget):
    def __init__(self, db, username):
        super(ExploreMovie, self).__init__()

        self.releaseDateDict = {}
        self.username = username
        self.db = db
        self.title = QLabel("Explore Movie")
        self.title.setStyleSheet("font: 30pt")

        self.movies = QComboBox()
        self.movies.addItem("ALL")
        for movie in select_movie_names(self.db):
            print("movie name:", movie)
            self.movies.addItem(movie[0])

        moviename = QGroupBox()
        layout1 = QFormLayout()
        layout1.addRow(QLabel("Movie Name"), self.movies)
        moviename.setLayout(layout1)

        company = QGroupBox()
        compLayout = QFormLayout()
        self.companies = QComboBox()
        self.companies.addItem("ALL")
        for comp in select_all_company(self.db):
            self.companies.addItem(comp)
        compLayout.addRow(QLabel("Company Name"), self.companies)
        company.setLayout(compLayout)

        self.cityName = QLineEdit()
        city = QGroupBox()
        layout = QFormLayout()
        layout.addRow(QLabel("City"), self.cityName)
        city.setLayout(layout)

        state = QGroupBox()
        layout = QFormLayout()
        self.states = QComboBox()
        abvs = ["ALL", "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        for abv in abvs:
            self.states.addItem(abv)
        layout.addRow(QLabel("State"), self.states)
        state.setLayout(layout)

        visitdate1 = QHBoxLayout()
        self.minMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        visitdate1.addWidget(self.minMonth)
        visitdate1.addWidget(QLabel("/"))
        self.minDay = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        visitdate1.addWidget(self.minDay)
        visitdate1.addWidget(QLabel("/"))
        self.minYear = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        visitdate1.addWidget(self.minYear)

        visitdate2 = QHBoxLayout()
        self.maxMonth = QLineEdit(QCalendarWidget().selectedDate().toString("MM"))
        visitdate2.addWidget(self.maxMonth)
        visitdate2.addWidget(QLabel("/"))
        self.maxDay = QLineEdit(QCalendarWidget().selectedDate().toString("dd"))
        visitdate2.addWidget(self.maxDay)
        visitdate2.addWidget(QLabel("/"))
        self.maxYear = QLineEdit(QCalendarWidget().selectedDate().toString("yyyy"))
        visitdate2.addWidget(self.maxYear)

        visit = QHBoxLayout()
        visit.addWidget(QLabel("Play Date"))
        visit.addLayout(visitdate1)
        visit.addWidget(QLabel("--"))
        visit.addLayout(visitdate2)

        self.cards = QComboBox()
        for card in select_credit_cards(db, self.username):
            print("cc nums:", card)
            self.cards.addItem(card[0])

        cardnums = QGroupBox()
        layout1 = QFormLayout()
        layout1.addRow(QLabel("Card Number"), self.cards)
        cardnums.setLayout(layout1)

        #table here
        self.table = QTableWidget()
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        self.table.setColumnCount(5)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # default to showing all users when screen loads
        # update table with user data
        movies = select_movies(db)
        self.update_movie_table(movies)

        self.BackButton = QPushButton("Back")
        self.FilterButton = QPushButton("Filter")
        self.FilterButton.clicked.connect(self.filter_movies)

        self.ViewButton = QPushButton("View")
        self.ViewButton.clicked.connect(self.view_movie)

        vbox = QVBoxLayout()
        vbox.addWidget(self.title, alignment=Qt.AlignCenter)
        vbox.addWidget(moviename)
        vbox.addWidget(company)
        vbox.addWidget(city)
        vbox.addWidget(state)
        vbox.addLayout(visit)
        vbox.addWidget(self.FilterButton)
        #table here
        vbox.addWidget(self.table)
        vbox.addWidget(cardnums)
        vbox.addWidget(self.BackButton)
        vbox.addWidget(self.ViewButton)

        self.setLayout(vbox)


    def view_movie(self):
        rows = sorted(set(index.row() for index in
                          self.table.selectedIndexes()))
        if len(rows) == 1:
            movieReleaseDate = self.releaseDateDict[rows[0]]
            movieName = self.table.item(rows[0], 0).text()
            theaterName = self.table.item(rows[0], 1).text()
            companyName = self.table.item(rows[0], 3).text()
            moviePlayDate = self.table.item(rows[0], 4).text()
            creditCardNum = self.cards.currentText()
            print("movie release date:", movieReleaseDate)
            print("theatername:", theaterName)
            print("companyname:", companyName)
            print("playDate:", moviePlayDate)
            print("username:", self.username)
            try:
                moviesViewedToday = select_movies_viewed(self.db, self.username, moviePlayDate)
                if moviesViewedToday is not None and len(moviesViewedToday) >= 3:
                    self.too_many_view_msg()
                    return False
                log_movie_view(self.db, creditCardNum, companyName, theaterName, movieName, movieReleaseDate, moviePlayDate)
                self.movie_view_success_msg()
                return
            except Exception as e:
                print("view movie error:", e)
        self.movie_view_fail_msg()

    def movie_view_fail_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Invalid Input")
        msgText = ("Failed to view movie. Make sure your input is valid.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()

    def too_many_view_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Too Many Movies Viewed")
        msgText = ("You've already viewed 3 movies on this day.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()

    def movie_view_success_msg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Viewing Logged")
        msgText = ("Your movie viewing has been logged.")
        msg.setText(msgText)
        msg.setStandardButtons(QMessageBox.Ok)
        self.m = msg
        self.m.show()

    def filter_movies(self):
        movieName = str(self.movies.currentText())
        company = str(self.companies.currentText())
        state = str(self.states.currentText())
        city = str(self.cityName.text())
        minDate = self.minYear.text() + "-" + self.minMonth.text() + "-" + self.minDay.text()
        maxDate = self.maxYear.text() + "-" + self.maxMonth.text() + "-" + self.maxDay.text()
        movies = select_movies(self.db, movieName, company, city, state, minDate, maxDate)
        self.update_movie_table(movies)

    def update_movie_table(self, movies):
        numMovies = len(movies)
        self.table.setRowCount(numMovies + 1)

        self.table.setItem(0, 0, QTableWidgetItem("Movie"))
        self.table.setItem(0, 1, QTableWidgetItem("Theater"))
        self.table.setItem(0, 2, QTableWidgetItem("Address"))
        self.table.setItem(0, 3, QTableWidgetItem("Company"))
        self.table.setItem(0, 4, QTableWidgetItem("Play Date"))

        for count, movieData in enumerate(movies):
            print("movieData:", movieData)
            print("movieData[0]:", movieData[0])
            self.releaseDateDict[count + 1] = movieData[5]
            self.table.setItem(count + 1, 0, QTableWidgetItem(movieData[0]))
            self.table.setItem(count + 1, 1, QTableWidgetItem(movieData[1]))
            self.table.setItem(count + 1, 2, QTableWidgetItem(movieData[2]))
            self.table.setItem(count + 1, 3, QTableWidgetItem(movieData[3]))
            self.table.setItem(count + 1, 4, QTableWidgetItem(str(movieData[4])))