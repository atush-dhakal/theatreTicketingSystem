from db_connect import *
from db_insert_update import *
from db_select import *
from db_filter import *

if __name__ == '__main__':
	db = connect_db()

	# test insert user / customer
	# fName = "Bob"
	# lName = "Johnson"
	# email = "bob1@gmail.com"
	# userType = "customer"
	# password = "123"
	# insert_user(db, email, password, userType, fName, lName)

	fname = "admin1"
	lname = "admin lastname"
	email = "myadmin"
	userType = "admin"
	password = "12345678"
	insert_user(db, email, password, userType, fname, lname)

	# test insert credit card
	# email = "bob1@gmail.com"
	# cardNum = "2222333344445555"
	# insert_credit_card(db, email, cardNum)

	# test insert manager
	# stAddr = "123 Main Street"
	# city = "Roswell"
	# state = "GA"
	# zipcode = "30075"
	# company = "MovieMax"
	# insert_manager(db, email, stAddr, city, state, zipcode, company)

	# username = "b"
	# status = "pending"
	# filter_user(db, username, status)

	# username = "g2@gmail.com"
	# status = "approved"
	# update_user_reg_status(db, username, status)

	movie = "Mad Max"
	duration = "1:20:20"
	year = "2017-08-08"
	insert_movie(db, movie, year, duration)