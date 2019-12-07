import sys
from os import path

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from AtlantaMovieLogin import *
from AdminCustomerFunctionality import *
from AdminOnlyFunctionality import *
from CompanyDetails import *
from CreateMovie import *
from CreateTheater import *
from CustomerRegistration import *
from CustomerFunctionality import *
from ExploreMovie import *
from ExploreTheater import *
from ManageCompany import *
from ManagerCustomerFunctionality import *
from ManagerCustomerRegistration import *
from ManagerOnlyFunctionality import *
from ManagerOnlyRegistration import *
from ManageUser import *
from RegistrationNavigation import *
from ScheduleMovie import *
from TheaterOverview import *
from UserFunctionality import *
from UserRegistration import *
from ViewHistory import *
from VisitHistory import *

from db_connect import *
from functools import partial

class AtlantaMovieLoginScreen(AtlantaMovieLogin):
    def __init__(self, db):
        super(AtlantaMovieLoginScreen, self).__init__(db)
        self.LoginButton.clicked.connect(self.run_login)
        self.RegisterButton.clicked.connect(partial(self.get_next_screen, "RegistrationNavigation"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

    def run_login(self):
        nextScreen = self.login()
        show_next_screen(self, nextScreen)

class RegistrationNavigationScreen(RegistrationNavigation):
    def __init__(self, db):
        super(RegistrationNavigationScreen, self).__init__(db)
        self.UserOnlyButton.clicked.connect(partial(self.get_next_screen, "UserRegistration"))
        self.CustomerOnlyButton.clicked.connect(partial(self.get_next_screen, "CustomerRegistration"))
        self.ManagerOnlyButton.clicked.connect(partial(self.get_next_screen, "ManagerOnlyRegistration"))
        self.ManagerCustomerButton.clicked.connect(partial(self.get_next_screen, "ManagerCustomerRegistration"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "AtlantaMovieLogin"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

class ManagerOnlyRegistrationScreen(ManagerOnlyRegistration):
    def __init__(self, db):
        super(ManagerOnlyRegistrationScreen, self).__init__(db)
        self.RegisterButton.clicked.connect(partial(self.run_register_manager, "AtlantaMovieLogin"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "RegistrationNavigation"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

    def run_register_manager(self, nextScreen):
        regSuccess = self.register_manager()
        if (regSuccess):
            show_next_screen(self, nextScreen)

class ManagerCustomerRegistrationScreen(ManagerCustomerRegistration):
    def __init__(self, db):
        super(ManagerCustomerRegistrationScreen, self).__init__(db)
        self.RegisterButton.clicked.connect(partial(self.run_register_manager_cust, "AtlantaMovieLogin"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "RegistrationNavigation"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

    def run_register_manager_cust(self, nextScreen):
        regSuccess = self.register_manager_cust()
        if (regSuccess):
            show_next_screen(self, nextScreen)

class CustomerRegistrationScreen(CustomerRegistration):
    def __init__(self, db):
        super(CustomerRegistrationScreen, self).__init__(db)
        self.RegisterButton.clicked.connect(partial(self.run_register_cust, "AtlantaMovieLogin"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "RegistrationNavigation"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

    def run_register_cust(self, nextScreen):
        regSuccess = self.register_cust()
        if (regSuccess):
            show_next_screen(self, nextScreen)

class UserRegistrationScreen(UserRegistration):
    def __init__(self, db):
        super(UserRegistrationScreen, self).__init__(db)
        self.RegisterButton.clicked.connect(partial(self.run_register_user, "AtlantaMovieLogin"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "RegistrationNavigation"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

    def run_register_user(self, nextScreen):
        regSuccess = self.register_user()
        if (regSuccess):
            show_next_screen(self, nextScreen)

class AdminOnlyFunctionalityScreen(AdminOnlyFunctionality):
    def __init__(self, db, userType, username):
        super(AdminOnlyFunctionalityScreen, self).__init__(db)
        self.userType = userType
        self.username = username
        self.ManageUserButton.clicked.connect(partial(self.get_next_screen, "ManageUser"))
        self.ManageCompanyButton.clicked.connect(partial(self.get_next_screen, "ManageCompany"))
        self.CreateMovieButton.clicked.connect(partial(self.get_next_screen, "CreateMovie"))
        self.ExplorTheaterButton.clicked.connect(partial(self.get_next_screen, "ExploreTheater"))
        self.VisitHistoryButton.clicked.connect(partial(self.get_next_screen, "VisitHistory"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "AtlantaMovieLogin"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

class AdminCustomerFunctionalityScreen(AdminCustomerFunctionality):
    def __init__(self, db, userType, username):
        super(AdminCustomerFunctionalityScreen, self).__init__(db)
        self.userType = userType
        self.username = username
        self.ManageUserButton.clicked.connect(partial(self.get_next_screen, "ManageUser"))
        self.ManageCompanyButton.clicked.connect(partial(self.get_next_screen, "ManageCompany"))
        self.CreateMovieButton.clicked.connect(partial(self.get_next_screen, "CreateMovie"))
        self.VisitHistoryButton.clicked.connect(partial(self.get_next_screen, "VisitHistory"))
        self.ExploreMovieButton.clicked.connect(partial(self.get_next_screen, "ExploreMovie"))
        self.ExploreTheaterButton.clicked.connect(partial(self.get_next_screen, "ExploreTheater"))
        self.ViewHistoryButton.clicked.connect(partial(self.get_next_screen, "ViewHistory"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "AtlantaMovieLogin"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

class ManagerOnlyFunctionalityScreen(ManagerOnlyFunctionality):
    def __init__(self, db, userType, username):
        super(ManagerOnlyFunctionalityScreen, self).__init__(db)
        self.userType = userType
        self.username = username
        self.TheaterOverviewButton.clicked.connect(partial(self.get_next_screen, "TheaterOverview"))
        self.ExploreTheaterButton.clicked.connect(partial(self.get_next_screen, "ExploreTheater"))
        self.ScheduleMovieButton.clicked.connect(partial(self.get_next_screen, "ScheduleMovie"))
        self.VisitHistoryButton.clicked.connect(partial(self.get_next_screen, "VisitHistory"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "AtlantaMovieLogin"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

class ManagerCustomerFunctionalityScreen(ManagerCustomerFunctionality):
    def __init__(self, db, userType, username):
        super(ManagerCustomerFunctionalityScreen, self).__init__(db)
        self.userType = userType
        self.username = username
        self.TheaterOverviewButton.clicked.connect(partial(self.get_next_screen, "TheaterOverview"))
        self.ExploreMovieButton.clicked.connect(partial(self.get_next_screen, "ExploreMovie"))
        self.ScheduleMovieButton.clicked.connect(partial(self.get_next_screen, "ScheduleMovie"))
        self.ExploreTheaterButton.clicked.connect(partial(self.get_next_screen, "ExploreTheater"))
        self.ViewHistoryButton.clicked.connect(partial(self.get_next_screen, "ViewHistory"))
        self.VisitHistoryButton.clicked.connect(partial(self.get_next_screen, "VisitHistory"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "AtlantaMovieLogin"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

class CustomerFunctionalityScreen(CustomerFunctionality):
    def __init__(self, db, userType, username):
        super(CustomerFunctionalityScreen, self).__init__(db)
        self.userType = userType
        self.username = username
        self.ExploreMovieButton.clicked.connect(partial(self.get_next_screen, "ExploreMovie"))
        self.ViewHistoryButton.clicked.connect(partial(self.get_next_screen, "ViewHistory"))
        self.ExploreTheaterButton.clicked.connect(partial(self.get_next_screen, "ExploreTheater"))
        self.VisitHistoryButton.clicked.connect(partial(self.get_next_screen, "VisitHistory"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "AtlantaMovieLogin"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

class UserFunctionalityScreen(UserFunctionality):
    def __init__(self, db, userType, username):
        super(UserFunctionalityScreen, self).__init__(db)
        self.userType = userType
        self.username = username
        self.ExploreTheaterButton.clicked.connect(partial(self.get_next_screen, "ExploreTheater"))
        self.VisitHistoryButton.clicked.connect(partial(self.get_next_screen, "VisitHistory"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "AtlantaMovieLogin"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

class ManageUserScreen(ManageUser):
    def __init__(self, db, userType, username):
        super(ManageUserScreen, self).__init__(db)
        self.userType = userType
        self.username = username
        self.BackButton.clicked.connect(self.get_back_screen)

    def get_back_screen(self):
        back_user_home_screen(self)

class ManageCompanyScreen(ManageCompany):
    def __init__(self, db, userType, username):
        super(ManageCompanyScreen, self).__init__(db)
        self.userType = userType
        self.username = username
        self.CreateTheaterButton.clicked.connect(partial(self.get_next_screen, 'CreateTheater'))
        self.DetailsButton.clicked.connect(partial(self.run_view_details))
        self.BackButton.clicked.connect(self.get_back_screen)

    def run_view_details(self):
        result = self.view_company_details()
        if result != False:
            self.companyDetails = result
            show_next_screen(self, "CompanyDetails")

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

    def get_back_screen(self):
        back_user_home_screen(self)

class CreateMovieScreen(CreateMovie):
    def __init__(self, db, userType, username):
        self.userType = userType
        self.username = username
        super(CreateMovieScreen, self).__init__(db)
        self.BackButton.clicked.connect(self.get_back_screen)

    def get_back_screen(self):
        back_user_home_screen(self)

class ExploreMovieScreen(ExploreMovie):
    def __init__(self, db, userType, username):
        super(ExploreMovieScreen, self).__init__(db, username)
        self.userType = userType
        self.username = username
        self.BackButton.clicked.connect(self.get_back_screen)

    def get_back_screen(self):
        back_user_home_screen(self)

class ViewHistoryScreen(ViewHistory):
    def __init__(self, db, userType, username):
        super(ViewHistoryScreen, self).__init__(db, username)
        self.userType = userType
        self.username = username
        self.BackButton.clicked.connect(self.get_back_screen)

    def get_back_screen(self):
        back_user_home_screen(self)

class TheaterOverviewScreen(TheaterOverview):
    def __init__(self, db, userType, username):
        super(TheaterOverviewScreen, self).__init__(db, username)
        self.userType = userType
        self.username = username
        self.BackButton.clicked.connect(self.get_back_screen)

    def get_back_screen(self):
        back_user_home_screen(self)

class ScheduleMovieScreen(ScheduleMovie):
    def __init__(self, db, userType, username):
        super(ScheduleMovieScreen, self).__init__(db, username)
        self.userType = userType
        self.username = username
        self.BackButton.clicked.connect(self.get_back_screen)

    def get_back_screen(self):
        back_user_home_screen(self)

class ExploreTheaterScreen(ExploreTheater):
    def __init__(self, db, userType, username):
        super(ExploreTheaterScreen, self).__init__(db, username)
        self.userType = userType
        self.username = username
        print("username:", self.username)
        self.BackButton.clicked.connect(self.get_back_screen)

    def get_back_screen(self):
        back_user_home_screen(self)

class VisitHistoryScreen(VisitHistory):
    def __init__(self, db, userType, username):
        super(VisitHistoryScreen, self).__init__(db, username)
        self.userType = userType
        self.username = username
        self.BackButton.clicked.connect(self.get_back_screen)

    def get_back_screen(self):
        back_user_home_screen(self)

class CreateTheaterScreen(CreateTheater):
    def __init__(self, db, userType, username):
        super(CreateTheaterScreen, self).__init__(db)
        self.userType = userType
        self.username = username
        self.CreateButton.clicked.connect(partial(self.run_create_theater, "ManageCompany"))
        self.BackButton.clicked.connect(partial(self.get_next_screen, "ManageCompany"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

    def run_create_theater(self, next_screen):
        createSuccess = self.create_new_theater()
        if (createSuccess):
            show_next_screen(self, next_screen)

class CompanyDetailsScreen(CompanyDetails):
    def __init__(self, db, userType, company, username):
        super(CompanyDetailsScreen, self).__init__(db, company)
        self.userType = userType
        self.companyDetails = company
        self.username = username
        self.BackButton.clicked.connect(partial(self.get_next_screen, "ManageCompany"))

    def get_next_screen(self, nextScreen):
        show_next_screen(self, nextScreen)

def show_next_screen(self, nextScreen):
    # login screen
    if (nextScreen == "AtlantaMovieLogin"):
        self.w = AtlantaMovieLoginScreen(self.db)
    # register navigation
    elif (nextScreen == "RegistrationNavigation"):
        self.w = RegistrationNavigationScreen(self.db)
    #  register screens
    elif (nextScreen == "ManagerOnlyRegistration"):
        self.w = ManagerOnlyRegistrationScreen(self.db)
    elif (nextScreen == "ManagerCustomerRegistration"):
        self.w = ManagerCustomerRegistrationScreen(self.db)
    elif (nextScreen == "CustomerRegistration"):
        self.w = CustomerRegistrationScreen(self.db)
    elif (nextScreen == "UserRegistration"):
        self.w = UserRegistrationScreen(self.db)
    # user functionality screens
    elif (nextScreen == "AdminOnlyFunctionality"):
        self.w = AdminOnlyFunctionalityScreen(self.db, self.userType, self.username)
    elif (nextScreen == "AdminCustomerFunctionality"):
        self.w = AdminCustomerFunctionalityScreen(self.db, self.userType, self.username)
    elif (nextScreen == "ManagerOnlyFunctionality"):
        self.w = ManagerOnlyFunctionalityScreen(self.db, self.userType, self.username)
    elif (nextScreen == "ManagerCustomerFunctionality"):
        self.w = ManagerCustomerFunctionalityScreen(self.db, self.userType, self.username)
    elif (nextScreen == "CustomerFunctionality"):
        self.w = CustomerFunctionalityScreen(self.db, self.userType, self.username)
    elif (nextScreen == "UserFunctionality"):
        self.w = UserFunctionalityScreen(self.db, self.userType, self.username)
    # admin data screens
    elif (nextScreen == "ManageUser"):
        self.w = ManageUserScreen(self.db, self.userType, self.username)
    elif (nextScreen == "ManageCompany"):
        self.w = ManageCompanyScreen(self.db, self.userType, self.username)
    elif (nextScreen == "CreateTheater"):
        self.w = CreateTheaterScreen(self.db, self.userType, self.username)
    elif (nextScreen == "CreateMovie"):
        self.w = CreateMovieScreen(self.db, self.userType, self.username)
    elif (nextScreen == "CompanyDetails"):
        self.w = CompanyDetailsScreen(self.db, self.userType, self.companyDetails, self.username)
    # manager data screens
    elif (nextScreen == "TheaterOverview"):
        self.w = TheaterOverviewScreen(self.db, self.userType, self.username)
    elif (nextScreen == "ScheduleMovie"):
        self.w = ScheduleMovieScreen(self.db, self.userType, self.username)
    # customer data screens
    elif (nextScreen == "ExploreMovie"):
        self.w = ExploreMovieScreen(self.db, self.userType, self.username)
    elif (nextScreen == "ViewHistory"):
        self.w = ViewHistoryScreen(self.db, self.userType, self.username)
    # general data screens
    elif (nextScreen == "ExploreTheater"):
        self.w = ExploreTheaterScreen(self.db, self.userType, self.username)
    elif (nextScreen == "VisitHistory"):
        self.w = VisitHistoryScreen(self.db, self.userType, self.username)
    else:
        print("Error with show_next_screen() in main.py")
        return
    self.w.show()
    self.hide()

def back_user_home_screen(self):
    print("user type:", self.userType)
    if (self.userType == "Admin"):
        show_next_screen(self, "AdminOnlyFunctionality")
    elif (self.userType == "CustomerAdmin"):
        show_next_screen(self, "AdminCustomerFunctionality")
    elif (self.userType == "Manager"):
        show_next_screen(self, "ManagerOnlyFunctionality")
    elif (self.userType == "CustomerManager"):
        show_next_screen(self, "ManagerCustomerFunctionality")
    elif (self.userType == "Customer"):
        show_next_screen(self, "CustomerFunctionality")
    elif (self.userType == "User"):
        show_next_screen(self, "UserFunctionality")
    else:
        print("error")

if __name__=='__main__':
    # establish the db connection
    db = connect_db()
    app = QApplication(sys.argv)

    # pass db connection to login screen
    main = AtlantaMovieLoginScreen(db)
    main.show()
    sys.exit(app.exec_())