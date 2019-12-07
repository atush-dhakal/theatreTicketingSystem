import hashlib
from db_select import *
"""
Insert a customer's credit card information into the credit_card table. Use this method with
customer registration screens.

Returns: N/A
"""
def insert_credit_card(db, username, credit_card_num):
	cursor = db.cursor()
	# flip order of username and credit_card_num in query
	query = ("insert into credit_card(credit_card_num, username)"
		" values ('{}', '{}')".format(credit_card_num, username))
	cursor.execute(query)
	db.commit()
	cursor.close()

# need method for inserting multiple credit cards later

"""
Insert a manager's information into the manager table. Use this method with manager registration
screens.

Need to add status column to this table

Returns: N/A
"""
# reformat table if there is more time
def insert_manager(db, username, street, city, state, zipcode, company):
	cursor = db.cursor()
	query = ("insert into manager(username, zipcode, street, city, state, company)"
		"values ('{}','{}','{}','{}','{}','{}')".format(username, zipcode, street, city, state, company))
	cursor.execute(query)
	db.commit()
	cursor.close()

"""
Insert a movie's information into the movie table. Use this method with create movie screen.

Returns: N/A
"""
def insert_movie(db, name, release, duration):
	cursor = db.cursor()
	query = ("insert into movie(movie_name, release_date, duration) values ('{}','{}','{}')"
		.format(name, release, duration))
	cursor.execute(query)
	db.commit()
	cursor.close()

"""
Insert a movie's play date into the movie_play table. Use this method with schedule movie screen.
You will need to call select_manager() to get the comapny and theater input data.

Returns: N/A
"""
def insert_movie_play(db, company, theater, name, release, play_date):
	cursor = db.cursor()
	query = ("insert into movie_play(company_name, theater_name, movie_name, movie_release_date, "
		"movie_play_date) values ('{}','{}','{}','{}','{}')".format(company, theater, name,
			release, play_date))
	cursor.execute(query)
	db.commit()
	cursor.close()

"""
Insert a new theater into the theater table. Use this method with create theater screen.

Input: db, name, company, address, city, state, zipcode, capacity, manager

Returns: N/A
"""
def insert_theater(db, name, company, manager, zipcode, street, city, state, capacity):
	cursor = db.cursor()
	query = ("insert into theater(theater_name, company_name, manager, zipcode, street, city,"
		"state, capacity) values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(name, company, manager, zipcode, street, city, state, capacity))
	cursor.execute(query)
	db.commit()
	cursor.close()

"""
Insert a user or a customer's information into the user table. Use this method with the user
registration and customer registration screens.

Returns: N/A
"""
def insert_user(db, username, password, userType, firstname, lastname):
	cursor = db.cursor()
	query = ("insert into user(username, user_password, user_type, user_status, firstname, lastname) "
		"values ('{}','{}','{}','pending','{}','{}')".format(username, hashlib.md5(password.encode('utf-8')).hexdigest(), userType, firstname, lastname))
	cursor.execute(query)
	db.commit()
	cursor.close()

"""
Update a user's registration status to 'approve' or 'decline'

Returns: N/A
"""
def update_user_reg_status(db, username, status):
	print("updating user status")
	cursor = db.cursor()
	query = ("update user set user_status='{}' where username='{}';".format(status, username))
	print(query)
	cursor.execute(query)
	db.commit()
	print("Row Count:{}".format(cursor.rowcount))
	cursor.close()
	print("status updated")


def log_theater_visit(db, theaterName, companyName, visitDate, username):
	cursor = db.cursor()
	query = "INSERT INTO visit(theater_name, company_name, visit_date, username) "
	query += "VALUES('{}', '{}', '{}', '{}');".format(theaterName, companyName, visitDate, username)
	cursor.execute(query)
	db.commit()
	cursor.close()

def log_movie_view(db, creditCardNum, companyName, theaterName, movieName, movieReleaseDate, moviePlayDate):
	cursor = db.cursor()
	query = "INSERT INTO credit_card_payment (credit_card_num, company_name, theater_name, movie_name, movie_release_date, movie_play_date) "
	query += 'VALUES("{}", "{}", "{}", "{}", "{}", "{}");'.format(creditCardNum, companyName, theaterName, movieName, movieReleaseDate, moviePlayDate)
	cursor.execute(query)
	db.commit()
	cursor.close()

def schedule_movie_play(db, manager, movieName, movieReleaseDate, moviePlayDate):
	managerTheater = select_manager_theater(db, manager)
	print("managertheater:", managerTheater)
	theaterName = managerTheater[0][0]
	companyName = managerTheater[0][1]

	cursor = db.cursor()
	query = "INSERT INTO movie_play (company_name, theater_name, movie_name, movie_release_date, movie_play_date) "
	query += 'VALUES("{}", "{}", "{}", "{}", "{}");'.format(companyName, theaterName, movieName, movieReleaseDate, moviePlayDate)
	cursor.execute(query)
	db.commit()
	cursor.close()

def movies_played_on_day(db, manager, moviePlayDate):
	managerTheater = select_manager_theater(db, manager)
	print("managertheater:", managerTheater)
	if managerTheater != None and len(managerTheater) > 0:
		theaterName = managerTheater[0][0]
		companyName = managerTheater[0][1]
	else:
		return []
	print("theaterName:", theaterName)
	print("companyName:", companyName)
	cursor = db.cursor()
	query = "SELECT * from movie_play "
	query += "where theater_name = '{}'".format(theaterName)
	query += " and company_name = '{}'".format(companyName)
	query += " and movie_play_date = '{}'".format(moviePlayDate)
	print("mpod query:", query)
	cursor.execute(query)
	moviesOnDay = cursor.fetchall()
	cursor.close()
	return moviesOnDay



def delete_user(db, username):
	cursor = db.cursor()
	query = "DELETE FROM user "
	query += 'where username = "{}";'.format(username)
	cursor.execute(query)
	db.commit()
	cursor.close()

def delete_manager(db, username):
	cursor = db.cursor()
	query = "DELETE FROM manager "
	query += 'where username = "{}";'.format(username)
	cursor.execute(query)
	db.commit()
	cursor.close()