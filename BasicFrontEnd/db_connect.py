"""
CS 4400 Team 84

This file contains methods to query and return all of the data required for the
database screens in the Atlanta Movie application

pip install PyQt5
pip install mysql-connector-python
"""

import mysql.connector

def connect_db():
	db = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="your_password",
		database="team84")
	return db