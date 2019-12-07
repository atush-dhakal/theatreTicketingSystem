"""
Filter all users in the user table by username or status. Use this method for manage user screen.

Returns: [(username1, user_password1, ...), (username2, user_password2, ...), ...]
"""
def filter_user(db, username=None, status=None):
	cursor = db.cursor()
	query = "select * from user"
	if (username is not None):
		query += " where username like '%{}%'".format(username)
		if (status is not None and status != "all"):
			query += " and user_status = '{}'".format(status)
	if (username is None and status != "all"):
		query += " where user_status = '{}'".format(status)
	query += ";"
	cursor.execute(query)
	userList = cursor.fetchall()
	cursor.close()
	return userList

def get_user_ccs(db, username=None):
	cursor = db.cursor()
	query = "select credit_card_num from credit_card"
	if (username is not None):
		query += " where username = '{}'".format(username)
	query += ";"
	cursor.execute(query)
	ccList = cursor.fetchall()
	cursor.close()
	print("cc list for", username, ":", ccList)
	return ccList

def filter_company(db, name=None, cityLow=None, cityHigh=None, theaterLow=None, theaterHigh=None, employeeLow=None, employeeHigh=None):
	companyList = get_all_companies(db, name)

	finalData = []
	for company in companyList:
		print("company:", company)
		theaters = get_all_company_theaters(db, company[0])
		print("theaters:", theaters)
		if theaterHigh != None and len(theaters) > theaterHigh:
			continue
		if theaterLow != None and len(theaters) < theaterLow:
			continue
		cityStateSet = set()
		for city, state in theaters:
			cityStateSet.add((city, state))
		if cityHigh != None and len(cityStateSet) > cityHigh:
			continue
		if cityLow != None and len(cityStateSet) < cityLow:
			continue
		employees = get_all_company_employees(db, company[0])
		print("employees:", employees)
		if employeeHigh != None and len(employees) > employeeHigh:
			continue
		if employeeLow != None and len(employees) < employeeLow:
			continue
		finalData.append((company[0], str(len(cityStateSet)), str(len(theaters)), str(len(employees))))
	print("final data:", finalData)
	return finalData

def get_all_companies(db, name):
	cursor = db.cursor()
	query = "select * from company"
	if (name is not None and name != 'ALL'):
		query += " where company_name like '%{}%'".format(name)
	query += ";"
	cursor.execute(query)
	companyList = cursor.fetchall()
	cursor.close()
	return companyList

def get_all_company_theaters(db, company):
	cursor = db.cursor()
	query = "select city, state from theater"
	query += " where company_name = '{}';".format(company)
	print("query:", query)
	cursor.execute(query)
	theaterList = cursor.fetchall()
	cursor.close()
	return theaterList

def get_all_company_employees(db, company):
	cursor = db.cursor()
	query = "select * from manager"
	query += " where company = '{}';".format(company)
	cursor.execute(query)
	employeeList = cursor.fetchall()
	cursor.close()
	return employeeList