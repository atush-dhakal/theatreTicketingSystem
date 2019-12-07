"""
Select all companies in the database. Use this method for manage company functionality.

Returns: [(company1_name), (company2_name), ...]
"""
def select_all_company(db):
	cursor = db.cursor()
	query = "select * from company"
	cursor.execute(query)
	companyTupList = cursor.fetchall()
	cursor.close()
	# get db list in easy to use python list
	companyList = list()
	for compTuple in companyTupList:
		companyList.append(compTuple[0])
	return companyList

def select_all_username(db):
	cursor = db.cursor()
	query = "select username from user;"
	cursor.execute(query)
	userTupList = cursor.fetchall()
	userList = list()
	for userTup in userTupList:
		userList.append(userTup[0])
	cursor.close()
	return userList

def select_pending_username(db):
	cursor = db.cursor()
	query = "select username from user where user_status = 'Pending';"
	cursor.execute(query)
	userTupList = cursor.fetchall()
	userList = list()
	for userTup in userTupList:
		userList.append(userTup[0])
	cursor.close()
	return userList

def select_pending_declined_username(db):
	cursor = db.cursor()
	query = "select username from user where user_status = 'Pending' or user_status = 'Declined';"
	cursor.execute(query)
	userTupList = cursor.fetchall()
	userList = list()
	for userTup in userTupList:
		userList.append(userTup[0])
	cursor.close()
	return userList

def select_all_user(db):
	cursor = db.cursor()
	query = "select * from user;"
	cursor.execute(query)
	userList = cursor.fetchall()
	cursor.close()
	return userList

"""
Select all managers for a specific company from the manager table. Use this method for company
detail screen.

Returns: [(firstname1, lastname1), (firstname2, lastname2), ...]
"""
def select_company_manager(db, company):
	cursor = db.cursor()
	query = ("select firstname, lastname, manager.username from user, manager where manager.username ="
		"user.username;")
	cursor.execute(query)
	compManagerList = cursor.fetchall()
	cursor.close()
	return compManagerList

def select_company_manager2(db, company):
	cursor = db.cursor()
	query = "select firstname, lastname, manager.username from user, manager "
	query += "where manager.username = user.username"
	query += " and manager.company = '{}'".format(company)
	query += ';'
	cursor.execute(query)
	compManagerList = cursor.fetchall()
	cursor.close()
	return compManagerList

def select_unassigned_company_managers(db, company):
	allManagers = select_company_manager2(db, company)

	finalList = []
	for manager in allManagers:
		firstname = manager[0]
		lastname = manager[1]
		managerUsername = manager[2]
		theaters = select_manager_theater(db, managerUsername)
		print("theaters for", managerUsername, ":", theaters)
		if theaters is None or len(theaters) < 1:
			finalList.append((firstname, lastname, managerUsername))
	print("unassigned managers:", finalList)
	return finalList



"""
Select all theaters for a specific company. Use this method for company detail screen.

Returns: [(theater1_name, theater1_manager, ...), (theater2_name, theater2_manager, ...)]
"""
def select_company_theater(db, company):
	cursor = db.cursor()
	query = "select theater_name, manager, city, state, capacity from theater"
	query += " where company_name = '{}';".format(company)
	cursor.execute(query)
	userList = cursor.fetchall()
	cursor.close()
	return userList

def select_theaters_for_dropdown(db, company=None):
	cursor = db.cursor()
	query = "select theater_name from theater"
	if company != None and company != "ALL":
		query += " where company_name = '{}'".format(company)
	query += ";"
	cursor.execute(query)
	theaterList = cursor.fetchall()
	cursor.close()
	return theaterList

def select_theaters_where(db, company=None, theaterName=None, city=None, state=None):
	cursor = db.cursor()
	query = "select theater_name, company_name, street, city, state, zipcode from theater"
	query += " where true"
	if company != None and company != "ALL":
		query += " and company_name = '{}'".format(company)
	if theaterName != None and theaterName != "ALL":
		query += " and theater_name = '{}'".format(theaterName)
	if city != None and len(city) > 0:
		query += " and city = '{}'".format(city)
	if state != None and state != "ALL":
		query += " and state = '{}'".format(state)
	query += ";"
	cursor.execute(query)
	theaterList = cursor.fetchall()
	cursor.close()
	return theaterList


def select_company_employees(db, company):
	usernames = select_employee_usernames(db, company)
	print("usernames:", usernames)
	finalNames = []
	for username in usernames:
		name = select_employee_names(db, username[0])[0]
		print("name:", name)
		finalNames.append(name[0] + " " + name[1])
	print("finalnames:", finalNames)
	return finalNames

def select_employee_usernames(db, company):
	print("getting usernames of employees of company:", company)
	cursor = db.cursor()
	query = "select username from manager"
	query += " where company = '{}';".format(company)
	cursor.execute(query)
	userList = cursor.fetchall()
	cursor.close()
	return userList

def select_employee_names(db, username):
	print("getting firstname, lastname for:", username)
	cursor = db.cursor()
	query = "select firstname, lastname from user"
	query += " where username = '{}';".format(username)
	cursor.execute(query)
	userList = cursor.fetchall()
	cursor.close()
	return userList
"""
Select a customer's movie view history. Use this method for the view history screen.

May need to change "movie_play_date" to "movie_view_date"

Returns [(movie1, theater1, company1, ...), (movie2, theater2, company2, ...), ...]
"""
def select_customer_payment(db, username):
	cursor = db.cursor()
	query = ("select movie_name, theater_name, company_name, credit_card_num, movie_play_date "
		"from credit_card_payment where credit_card_num in (select credit_card_num from "
		"credit_card where username = {}".format(username))
	cursor.execute(query)
	custViewHistory = cursor.fetchall()
	cursor.close()
	return custViewHistory

"""
Select a single manager's data after their password has been verified. Use this for the schedule
movie screen.

Returns: (username, user_password, user_type, user_status, firstname, lastname)
"""
def select_manager(db, username):
	cursor = db.cursor()
	query = "select * from manager where username = '{}';".format(username)
	cursor.execute(query)
	userData = cursor.fetchone()
	cursor.close()
	return userData


"""
Select a single user's information after their password has been verified. Use this for the
functionality home screen.

Returns: (username, user_password, user_type, user_status, firstname, lastname)
"""
def select_user(db, username):
	cursor = db.cursor()
	query = "select * from user where username = '{}';".format(username)
	cursor.execute(query)
	userData = cursor.fetchone()
	cursor.close()
	return userData

"""
Select the single password for a username from the database

Returns: (password)
"""
def select_password(db, username):
	cursor = db.cursor()
	query = "select user_password from user where username = '{}';".format(username)
	cursor.execute(query)
	password = cursor.fetchone()
	cursor.close()
	return password

def select_visits(db, username=None, company=None, minDate=None, maxDate=None):
	cursor = db.cursor()
	query = "select theater_name, company_name, visit_date from visit"
	query += " where true"
	if username != None and len(username) > 0:
		query += " and username = '{}'".format(username)
	if company != None and company != "ALL":
		query += " and company_name = '{}'".format(company)
	if minDate != None and len(maxDate) == 10:
		query += " and visit_date >= '{}'".format(minDate)
	if maxDate != None and len(maxDate) == 10:
		query += " and visit_date <= '{}'".format(maxDate)
	query += ";"
	cursor.execute(query)
	visitList = cursor.fetchall()
	print("visitList:", visitList)
	cursor.close()

	visitsWithAddresses = []
	for visit in visitList:
		theaterName = visit[0]
		companyName = visit[1]
		visitDate = visit[2]
		addressList = select_theater_address(db, theaterName, companyName)[0]
		visitsWithAddresses.append((theaterName, companyName, visitDate, addressList[0], addressList[1], addressList[2], addressList[3]))
	return visitsWithAddresses

def select_theater_address(db, theaterName=None, companyName=None):
	cursor = db.cursor()
	query = "select street, city, state, zipcode from theater"
	query += " where true"
	if companyName != None and companyName != "ALL":
		query += " and company_name = '{}'".format(companyName)
	if theaterName != None and theaterName != "ALL":
		query += " and theater_name = '{}'".format(theaterName)
	cursor.execute(query)
	addressList = cursor.fetchall()
	cursor.close()
	return addressList

def select_movie_names(db):
	cursor = db.cursor()
	query = "select distinct movie_name from movie;"
	cursor.execute(query)
	movies = cursor.fetchall()
	cursor.close()
	return movies

def select_credit_cards(db, username=None):
	cursor = db.cursor()
	query = "select credit_card_num from credit_card"
	query += " where true"
	if username != None and len(username) > 0:
		query += " and username = '{}'".format(username)
	query += ";"
	cursor.execute(query)
	creditCards = cursor.fetchall()
	cursor.close()
	return creditCards

def select_movies(db, movieName=None, companyName=None, city=None, state=None, minDate=None, maxDate=None):
	cursor = db.cursor()
	print("select movie input:", movieName, companyName, city, state, minDate, maxDate)
	query = "select movie_name, theater_name, company_name, movie_play_date, movie_release_date from movie_play"
	query += " where true"
	if movieName != None and movieName != "ALL":
		query += ' and movie_name = "{}"'.format(movieName)
	if companyName != None and companyName != "ALL":
		query += " and company_name = '{}'".format(companyName)
	if minDate != None and len(minDate) == 10:
		query += " and movie_play_date >= '{}'".format(minDate)
	if maxDate != None and len(maxDate) == 10:
		query += " and movie_play_date <= '{}'".format(maxDate)
	query += ";"
	print("query:", query)
	cursor.execute(query)
	movieList = cursor.fetchall()
	print("movieList:", movieList)
	cursor.close()

	finalMovieList = []
	for movie in movieList:
		movieName = movie[0]
		theaterName = movie[1]
		companyName = movie[2]
		playDate  = movie[3]
		releaseDate = movie[4]
		addressList = select_theater_address(db, theaterName, companyName)[0]
		cityName = addressList[1]
		stateName = addressList[2]
		print("stateName:", stateName, state)
		print("cityName:", cityName, city)

		if city != None and len(city) > 0:
			if cityName.lower().strip() != city.lower().strip():
				continue
		if state != None and state != "ALL":
			if stateName.lower().strip() != state.lower().strip():
				continue

		finalMovieList.append((movieName, theaterName, addressList[0] + ", " + cityName + ", " + stateName + " " + addressList[3], companyName, playDate, releaseDate))
	return finalMovieList

def select_views(db, username=None):
	userCreditCards = select_credit_cards(db, username)

	finalViewList = []
	print("user ccs:", userCreditCards)
	for creditCard in userCreditCards:
		payments = select_credit_card_payments(db, creditCard[0])
		print("payments:", payments)
		for payment in payments:
			movieName = payment[0]
			theaterName = payment[1]
			companyName = payment[2]
			cardNum = payment[3]
			viewDate = payment[4]
			finalViewList.append((movieName, theaterName, companyName, cardNum, viewDate))
	return finalViewList


def select_credit_card_payments(db, creditCardNum=None):
	print("creditCardNum:::", creditCardNum)
	cursor = db.cursor()
	query = "select movie_name, theater_name, company_name, credit_card_num, movie_play_date from credit_card_payment"
	query += " where true"
	if creditCardNum != None:
		query += " and credit_card_num = '{}'".format(creditCardNum)
	query += ";"
	print("query:", query)
	cursor.execute(query)
	payments = cursor.fetchall()
	cursor.close()
	return payments

def select_credit_card_payments2(db, creditCardNum=None, moviePlayDate=None):
	print("creditCardNum:::", creditCardNum)
	cursor = db.cursor()
	query = "select movie_name, theater_name, company_name, credit_card_num, movie_play_date from credit_card_payment"
	query += " where true"
	if creditCardNum != None:
		query += " and credit_card_num = '{}'".format(creditCardNum)
	if moviePlayDate != None and len(moviePlayDate) == 10:
		query += " and movie_play_date = '{}'".format(moviePlayDate)
	query += ";"
	print("query:", query)
	cursor.execute(query)
	payments = cursor.fetchall()
	cursor.close()
	return payments

def select_manager_theater(db, manager):
	print("manager:", manager)
	cursor = db.cursor()
	query = "select theater_name, company_name from theater"
	query += " where manager = '{}';".format(manager)
	print("query:", query)
	cursor.execute(query)
	theaters = cursor.fetchall()
	cursor.close()
	return theaters

def select_theater_plays(db, manager, movie_name=None, minDuration=None, maxDuration=None, minReleaseDate=None, maxReleaseDate=None, minPlayDate=None, maxPlayDate=None, onlyIncludeNotPlayed=False):
	managerTheater = select_manager_theater(db, manager)
	if managerTheater != None and len(managerTheater) > 0:
		theaterName = managerTheater[0][0]
		companyName = managerTheater[0][1]
	else:
		return []

	allMovies = select_all_movies(db, movie_name, minDuration, maxDuration, minReleaseDate, maxReleaseDate)
	finalMovieList = []
	for movie in allMovies:
		isScheduled = False
		movieName = movie[0]
		movieReleaseDate = movie[1]
		movieDuration = movie[2]

		scheduled = select_theater_movies(db, theaterName, companyName, movieName, movieReleaseDate, minPlayDate, maxPlayDate)
		for scheduledMovie in scheduled:
			print("sm:", scheduledMovie)
			playDate = scheduledMovie[0]
			if onlyIncludeNotPlayed != True:
				finalMovieList.append((movieName, movieDuration, movieReleaseDate, playDate))
			isScheduled = True

		if not isScheduled:
			finalMovieList.append((movieName, movieDuration, movieReleaseDate, ''))

	print("final movies list:", finalMovieList)
	return finalMovieList

def select_theater_movies(db, theaterName, companyName, movieName, movieReleaseDate, minPlaydate=None, maxPlayDate=None):
	cursor = db.cursor()
	query = "select movie_play_date from movie_play"
	query += " where theater_name = '{}'".format(theaterName)
	query += " and company_name = '{}'".format(companyName)
	query += ' and movie_name = "{}"'.format(movieName)
	query += " and movie_release_date = '{}'".format(movieReleaseDate)
	if minPlaydate != None and len(minPlaydate) == 10:
		query += " and movie_play_date >= '{}'".format(minPlaydate)
	if maxPlayDate != None and len(maxPlayDate) == 10:
		query += " and movie_play_date <= '{}'".format(maxPlayDate)
	query += ';'
	print("query:", query)
	cursor.execute(query)
	movies = cursor.fetchall()
	cursor.close()
	return movies

def select_all_movies(db, movieName=None, minDuration=None, maxDuration=None, minReleaseDate=None, maxReleaseDate=None):
	cursor = db.cursor()
	query = "select movie_name, release_date, duration from movie"
	query += " where true"
	if movieName != None and len(movieName) > 0:
		query += ' and movie_name = "{}"'.format(movieName)
	if minDuration != None and len(minDuration) > 0:
		query += " and duration >= '{}'".format(minDuration)
	if maxDuration != None and len(maxDuration) > 0:
		query += " and duration <= '{}'".format(maxDuration)
	if minReleaseDate != None and len(minReleaseDate) == 10:
		query += " and release_date >= '{}'".format(minReleaseDate)
	if maxReleaseDate != None and len(maxReleaseDate) == 10:
		query += " and release_date <= '{}'".format(maxReleaseDate)

	query += ";"
	print("query:", query)
	cursor.execute(query)
	movies = cursor.fetchall()
	cursor.close()
	return movies

def manager_theater_capacity(db, manager):
	cursor = db.cursor()
	query = "select capacity from theater"
	query += " where manager = '{}';".format(manager)
	print("query:", query)
	cursor.execute(query)
	capacities = cursor.fetchall()
	cursor.close()
	return capacities

def select_movies_viewed(db, username, moviePlayDate):
	userCreditCards = select_credit_cards(db, username)
	allPayments = []
	for creditCard in userCreditCards:
		payments = select_credit_card_payments2(db, creditCard[0], moviePlayDate)
		for payment in payments:
			allPayments.append(payments)
	return allPayments