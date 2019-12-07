-- SCREEN 1
DROP PROCEDURE IF EXISTS user_login;
DELIMITER $$
CREATE PROCEDURE `user_login`(IN i_username VARCHAR(50), IN i_password VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS UserLogin;
    CREATE TABLE UserLogin
    SELECT  username,
            user_status AS status,
            case when user_type = 'Customer' or user_type = 'CustomerManager' or user_type = 'CustomerAdmin'
                then 1
                else 0
            end as isCustomer,
            case when user_type = 'Admin' or user_type = 'CustomerAdmin'
                then 1
                else 0
            end as isAdmin,
            case when user_type = 'Manager' or user_type = 'CustomerManager'
                then 1
                else 0
            end as isManager
    FROM user
    WHERE username = i_username and user_password = MD5(i_password);
END$$
DELIMITER ;


-- SCREEN 3
DROP PROCEDURE IF EXISTS user_register;
DELIMITER $$
CREATE PROCEDURE `user_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50))
BEGIN
		INSERT INTO user (username, user_password, firstname, lastname, user_type, user_status) VALUES (i_username, MD5(i_password), i_firstname, i_lastname, 'User', 'Pending');
END$$
DELIMITER ;


-- SCREEN 4
DROP PROCEDURE IF EXISTS customer_only_register;
DELIMITER $$
CREATE PROCEDURE `customer_only_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50))
BEGIN
        INSERT INTO user (username, user_password, firstname, lastname, user_type, user_status) VALUES (i_username, MD5(i_password), i_firstname, i_lastname, 'Customer', 'Pending');
END$$
DELIMITER ;


-- SCREEN 4
DROP PROCEDURE IF EXISTS customer_add_creditcard;
DELIMITER $$
CREATE PROCEDURE `customer_add_creditcard`(IN i_username VARCHAR(50), IN i_creditCardNum CHAR(16))
BEGIN
	DROP TABLE IF EXISTS AddCreditCardHelper;
    CREATE TABLE AddCreditCardHelper
    SELECT username as username, count(*) as credit_card_count FROM credit_card GROUP BY username;
	
    IF 	(SELECT credit_card_count from AddCreditCardHelper where username = i_username) < 5 
			and LENGTH(i_creditCardNum) = 16 THEN
        INSERT INTO credit_card (credit_card_num, username) VALUES (i_creditCardNum, i_username);
	END IF;
    
    DROP TABLE IF EXISTS AddCreditCardHelper;
END$$
DELIMITER ;


-- SCREEN 5
DROP PROCEDURE IF EXISTS manager_only_register;
DELIMITER $$
CREATE PROCEDURE `manager_only_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50), IN i_comName VARCHAR(50), IN i_empStreet VARCHAR(50), IN i_empCity VARCHAR(50), IN i_empState CHAR(2), IN i_empZipcode CHAR(5))
BEGIN
        INSERT INTO user (username, user_password, firstname, lastname, user_type, user_status) VALUES (i_username, MD5(i_password), i_firstname, i_lastname, 'Manager', 'Pending');
        INSERT INTO manager (username, zipcode, street, city, state, company) VALUES (i_username, i_empZipcode, i_empStreet, i_empCity, i_empState, i_comName);
END$$
DELIMITER ;


-- SCREEN 6
DROP PROCEDURE IF EXISTS manager_customer_register;
DELIMITER $$
CREATE PROCEDURE `manager_customer_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50), IN i_comName VARCHAR(50), IN i_empStreet VARCHAR(50), IN i_empCity VARCHAR(50), IN i_empState CHAR(2), IN i_empZipcode CHAR(5))
BEGIN
        INSERT INTO user (username, user_password, firstname, lastname, user_type, user_status) VALUES (i_username, MD5(i_password), i_firstname, i_lastname, 'CustomerManager', 'Pending');
        INSERT INTO manager (username, zipcode, street, city, state, company) VALUES (i_username, i_empZipcode, i_empStreet, i_empCity, i_empState, i_comName);
END$$
DELIMITER ;


-- SCREEN 6
DROP PROCEDURE IF EXISTS manager_customer_add_creditcard;
DELIMITER $$
CREATE PROCEDURE `manager_customer_add_creditcard`(IN i_username VARCHAR(50), IN i_creditCardNum CHAR(16))
BEGIN
	DROP TABLE IF EXISTS AddCreditCardHelper2;
    CREATE TABLE AddCreditCardHelper2
    SELECT username as username, count(*) as credit_card_count FROM credit_card GROUP BY username;
	
    IF (SELECT credit_card_count from AddCreditCardHelper2 where username = i_username) < 5 THEN
        INSERT INTO credit_card (credit_card_num, username) VALUES (i_creditCardNum, i_username);
	END IF;
    
    DROP TABLE IF EXISTS AddCreditCardHelper2;
END$$
DELIMITER ;


-- SCREEN 13
DROP PROCEDURE IF EXISTS admin_approve_user;
DELIMITER $$
CREATE PROCEDURE `admin_approve_user`(IN i_username VARCHAR(50))
BEGIN
	IF (SELECT user_status from user where username = i_username) in ('Pending', 'Declined') THEN
        UPDATE user
        SET
            user_status = 'Approved'
        WHERE
            username = i_username;
	END IF;
END$$
DELIMITER ;


-- SCREEN 13
DROP PROCEDURE IF EXISTS admin_decline_user;
DELIMITER $$
CREATE PROCEDURE `admin_decline_user`(IN i_username VARCHAR(50))
BEGIN
	IF 'Pending' = (SELECT user_status from user where username = i_username) THEN
        UPDATE user
        SET
            user_status = 'Declined'
        WHERE
            username = i_username;
	END IF;
END$$
DELIMITER ;


-- SCREEN 13
DROP PROCEDURE IF EXISTS admin_filter_user;
DELIMITER $$
-- example https://stackoverflow.com/questions/848340/descending-ascending-parameter-to-a-stored-procedure
CREATE PROCEDURE `admin_filter_user`(IN i_username VARCHAR(50), IN i_status VARCHAR(50), IN i_sortBy VARCHAR(50), IN i_sortDirection VARCHAR(50))
BEGIN
	-- Create separate table with user and credit card count and other needed info
    DROP TABLE IF EXISTS AdFilterUserHelper;
    CREATE TABLE AdFilterUserHelper
    SELECT username as username, count(*) as credit_card_count FROM credit_card GROUP BY username;

    DROP TABLE IF EXISTS AdFilterUser;
    CREATE TABLE AdFilterUser
    SELECT u.username, (SELECT COALESCE(a.credit_card_count, 0)) as creditCardCount, u.user_type as userType, u.user_status as status
    FROM user u left outer join AdFilterUserHelper a on u.username = a.username
    WHERE (u.username = i_username or i_username = '' or i_username = NULL) and (u.user_status = i_status or i_status = 'ALL' or i_status = '')
    ORDER BY
        (CASE
            WHEN i_sortBy = 'username' and i_sortDirection = 'ASC' THEN u.username
            WHEN i_sortBy = 'creditCardCount' and i_sortDirection = 'ASC' THEN a.credit_card_count
            WHEN i_sortBy = 'userType' and i_sortDirection = 'ASC' THEN u.user_type
            WHEN i_sortBy = 'status' and i_sortDirection = 'ASC' THEN u.user_status
            WHEN i_sortDirection = 'ASC' AND i_sortBy NOT IN ('username', 'creditCardCount', 'userType', 'status') THEN u.username
        END) ASC,
        (CASE
            WHEN i_sortBy = 'username' and i_sortDirection != 'ASC' THEN u.username
            WHEN i_sortBy = 'creditCardCount' and i_sortDirection != 'ASC' THEN a.credit_card_count
            WHEN i_sortBy = 'userType' and i_sortDirection != 'ASC' THEN u.user_type
            WHEN i_sortBy = 'status' and i_sortDirection != 'ASC' THEN u.user_status
            WHEN i_sortBy NOT IN ('username', 'creditCardCount', 'userType', 'status') and i_sortDirection != 'ASC' THEN u.username
        END) DESC;

	-- drop the helper table
    DROP TABLE IF EXISTS AdFilterUserHelper;
END$$
DELIMITER ;


-- SCREEN 14
DROP PROCEDURE IF EXISTS admin_filter_company;
DELIMITER $$
CREATE PROCEDURE `admin_filter_company`(IN i_comName VARCHAR(50), IN i_minCity INT, IN i_maxCity INT, IN i_minTheater INT, IN i_maxTheater INT, IN i_minEmployee INT, IN i_maxEmployee INT, IN i_sortBy VARCHAR(50), IN i_sortDirection VARCHAR(50))
BEGIN
	DROP TABLE IF EXISTS CityCoverHelper;
    CREATE TABLE CityCoverHelper
    Select 	theater.company_name as company_name,
			COUNT(distinct theater.city, theater.state) as cityCover 
            FROM theater 
            WHERE theater.company_name = i_comName or i_comName = '' or i_comName = 'ALL'
            group by theater.company_name; 

	DROP TABLE IF EXISTS TheaterNumHelper;
    CREATE TABLE TheaterNumHelper
    Select 	theater.company_name as company_name,
			COUNT(*) as theaterNum 
            FROM theater
            group by theater.company_name
            having theater.company_name = i_comName or i_comName = '' or i_comName = 'ALL';
            
	DROP TABLE IF EXISTS EmployeeNumHelper;
    CREATE TABLE EmployeeNumHelper
    Select 	manager.company as company_name, 
			COUNT(*) as employeeNum 
            FROM manager 
            group by manager.company
            having manager.company = i_comName or i_comName = '' or i_comName = 'ALL';

    DROP TABLE IF EXISTS AdFilterCom;
    CREATE TABLE AdFilterCom
    SELECT  comp.company_name as comName,
            cc.cityCover as numCityCover,
            tn.theaterNum as numTheater,
            en.employeeNum as numEmployee
    FROM company comp, CityCoverHelper cc, TheaterNumHelper tn, EmployeeNumHelper en 
    WHERE 
		comp.company_name = cc.company_name and comp.company_name = tn.company_name and comp.company_name = en.company_name
		and ((i_minCity is NULL or cc.cityCover >= i_minCity) and (i_maxCity is NULL or cc.cityCover <= i_maxCity)) 
        and ((i_minTheater is NULL or tn.theaterNum >= i_minTheater) and (i_maxTheater is NULL or tn.theaterNum <= i_maxTheater)) 
        and ((i_minEmployee is NULL or en.employeeNum >= i_minEmployee) and (i_maxEmployee is NULL or en.employeeNum <= i_maxEmployee))
    ORDER BY
        (CASE
            WHEN i_sortBy = 'comName' and i_sortDirection = 'ASC' THEN comp.company_name
            WHEN i_sortBy = 'numCityCover' and i_sortDirection = 'ASC' THEN cc.cityCover
            WHEN i_sortBy = 'numTheater' and i_sortDirection = 'ASC' THEN tn.theaterNum
            WHEN i_sortBy = 'numEmployee' and i_sortDirection = 'ASC' THEN en.employeeNum
            WHEN i_sortDirection = 'ASC' and i_sortBy NOT IN ('comName', 'numCityCover', 'numTheater', 'numEmployee') THEN comp.company_name
        END) ASC,
        (CASE
            WHEN i_sortBy = 'comName' and i_sortDirection != 'ASC' THEN comp.company_name
            WHEN i_sortBy = 'numCityCover' and i_sortDirection != 'ASC' THEN cc.cityCover
            WHEN i_sortBy = 'numTheater' and i_sortDirection != 'ASC' THEN tn.theaterNum
            WHEN i_sortBy = 'numEmployee' and i_sortDirection != 'ASC' THEN en.employeeNum
            WHEN  i_sortDirection != 'ASC' and i_sortBy NOT IN ('comName', 'numCityCover', 'numTheater', 'numEmployee') THEN comp.company_name
        END) DESC;
        
	DROP TABLE IF EXISTS CityCoverHelper;
	DROP TABLE IF EXISTS TheaterNumHelper;
	DROP TABLE IF EXISTS EmployeeNumHelper;
END$$
DELIMITER ;


-- SCREEN 15
DROP PROCEDURE IF EXISTS admin_create_theater;
DELIMITER $$
CREATE PROCEDURE `admin_create_theater`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_thStreet VARCHAR(50), IN i_thCity VARCHAR(50), IN i_thState CHAR(2), IN i_thZipcode CHAR(5), IN i_capacity INT, IN i_managerUsername VARCHAR(50))
BEGIN
	IF (NOT EXISTS (SELECT * from theater where manager = i_managerUsername) and i_comName = (SELECT company from manager where manager.username = i_managerUsername)) THEN
        INSERT INTO theater(theater_name, company_name, manager, zipcode, street, city, state, capacity) VALUES (i_thName, i_comName, i_managerUsername, i_thZipcode, i_thStreet, i_thCity, i_thState, i_capacity);
	END IF;
END$$
DELIMITER ;


-- SCREEN 16
DROP PROCEDURE IF EXISTS admin_view_comDetail_emp;
DELIMITER $$
CREATE PROCEDURE `admin_view_comDetail_emp`(IN i_comName VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS AdComDetailEmp;
    CREATE TABLE AdComDetailEmp
    SELECT firstname as empFirstName, lastname as empLastName
    FROM user
    WHERE user.username in (SELECT manager.username FROM manager WHERE company = i_comName);

END$$
DELIMITER ;


-- SCREEN 16
DROP PROCEDURE IF EXISTS admin_view_comDetail_th;
DELIMITER $$
CREATE PROCEDURE `admin_view_comDetail_th`(IN i_comName VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS AdComDetailTh;
    CREATE TABLE AdComDetailTh
    SELECT theater_name as thName, manager as thManagerUsername, city as thCity, state as thState, capacity as thCapacity
    FROM theater
    WHERE theater.company_name = i_comName;
END$$
DELIMITER ;


-- SCREEN 17
DROP PROCEDURE IF EXISTS admin_create_mov;
DELIMITER $$
CREATE PROCEDURE `admin_create_mov`(IN i_movName VARCHAR(50), IN i_movDuration INT, IN i_movReleaseDate DATE)
BEGIN
        INSERT INTO movie (movie_name, release_date, duration) VALUES (i_movName, i_movReleaseDate, i_movDuration);
END$$
DELIMITER ;


-- SCREEN 18
DROP PROCEDURE IF EXISTS manager_filter_th;
DELIMITER $$
CREATE PROCEDURE `manager_filter_th`(IN i_manUsername VARCHAR(50), IN i_movName VARCHAR(50), IN i_minMovDuration INT, IN i_maxMovDuration INT, IN i_minMovReleaseDate DATE,  IN i_maxMovReleaseDate DATE, IN i_minMovPlayDate DATE,  IN i_maxMovPlayDate DATE, IN i_includeNotPlayed BOOLEAN)
BEGIN
    DROP TABLE IF EXISTS ManFilterTh;
    CREATE TABLE ManFilterTh
    SELECT m.movie_name as movName, m.duration as movDuration, m.release_date as movReleaseDate, mp.movie_play_date as movPlayDate
    FROM    movie m
            LEFT OUTER JOIN
            (	SELECT * 
				FROM movie_play 
				WHERE 	(i_manUsername = ''
						or (
							movie_play.theater_name in (SELECT theater.theater_name FROM theater where theater.manager = i_manUsername)
							and movie_play.company_name in (SELECT theater.company_name FROM theater where theater.manager = i_manUsername)
                            )
                        )
                        and movie_play.movie_name LIKE CONCAT('%', i_movName, '%')
			) mp
            on m.movie_name = mp.movie_name and m.release_date = mp.movie_release_date
    WHERE
		(i_includeNotPlayed is NOT TRUE or (i_includeNotPlayed is TRUE and movie_play_date is NULL))
		and (
			((i_minMovDuration is NULL or duration >= i_minMovDuration) and (i_maxMovDuration is NULL or duration <= i_maxMovDuration))
			and ((i_minMovReleaseDate is NULL or m.release_date >= i_minMovReleaseDate) and (i_maxMovReleaseDate is NULL or m.release_date <= i_maxMovReleaseDate))
			and (movie_play_date is NULL or ((i_minMovPlayDate is NULL or movie_play_date >= i_minMovPlayDate) and (i_maxMovPlayDate is NULL or movie_play_date <= i_maxMovPlayDate)))
		);
END$$
DELIMITER ;


-- SCREEN 19
DROP PROCEDURE IF EXISTS manager_schedule_mov;
DELIMITER $$
CREATE PROCEDURE `manager_schedule_mov`(IN i_manUsername VARCHAR(50), IN i_movName VARCHAR(50), IN i_movReleaseDate DATE, IN i_movPlayDate DATE)
BEGIN
	IF i_movReleaseDate <= i_movPlayDate THEN
        INSERT INTO movie_play (company_name, theater_name, movie_name, movie_release_date, movie_play_date)
        VALUES (
                (SELECT company_name FROM theater WHERE manager = i_manUsername),
                (SELECT theater_name FROM theater WHERE manager = i_manUsername),
                i_movName,
                i_movReleaseDate,
                i_movPlayDate
            );
	END IF;
END$$
DELIMITER ;


-- SCREEN 20
DROP PROCEDURE IF EXISTS customer_filter_mov;
DELIMITER $$
CREATE PROCEDURE `customer_filter_mov`(IN i_movName VARCHAR(50), IN i_comName VARCHAR(50), IN i_city VARCHAR(50), IN i_state VARCHAR(50), IN i_minMovPlayDate DATE,  IN i_maxMovPlayDate DATE)
BEGIN
    DROP TABLE IF EXISTS CosFilterMovie;
    CREATE TABLE CosFilterMovie
    SELECT
        movie_name as movName,
        theater_name as thName,
        (SELECT street from theater where theater.theater_name = movie_play.theater_name and theater.company_name = movie_play.company_name) as thStreet,
        (SELECT city from theater where theater.theater_name = movie_play.theater_name and theater.company_name = movie_play.company_name) as thCity,
        (SELECT state from theater where theater.theater_name = movie_play.theater_name and theater.company_name = movie_play.company_name) as thState,
        (SELECT zipcode from theater where theater.theater_name = movie_play.theater_name and theater.company_name = movie_play.company_name) as thZipcode,
        company_name as comName,
        movie_play_date as movPlayDate,
        movie_release_date as movReleaseDate
    FROM movie_play
    WHERE
        (movie_name = i_movName or i_movName = '' or i_movName = 'ALL')
        and (company_name = i_comName or i_comName = '' or i_comName = 'ALL')
        and movie_play.theater_name in (SELECT theater.theater_name from theater
                                        where (theater.city = i_city or i_city = '') and (theater.state = i_state or i_state = '' or i_state = 'ALL') and (theater.company_name = i_comName or i_comName = '' or i_comName = 'ALL'))
        and ((i_minMovPlayDate is NULL or movie_play_date >= i_minMovPlayDate) and (i_maxMovPlayDate is NULL or movie_play_date <= i_maxMovPlayDate));
        
END$$
DELIMITER ;


-- SCREEN 20
DROP PROCEDURE IF EXISTS customer_view_mov;
DELIMITER $$
CREATE PROCEDURE `customer_view_mov`(IN i_creditCardNum CHAR(16), IN i_movName VARCHAR(50), IN i_movReleaseDate DATE, IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_movPlayDate DATE)
BEGIN
	IF 3 > (SELECT COUNT(*) FROM credit_card_payment 
		WHERE 	i_creditCardNum in (SELECT cc1.credit_card_num from credit_card as cc1 where cc1.username = (SELECT cc2.username from credit_card as cc2 where cc2.credit_card_num = i_creditCardNum))
				and credit_card_payment.movie_play_date = i_movPlayDate) 
	THEN
                
        INSERT INTO credit_card_payment (credit_card_num, company_name, theater_name, movie_name, movie_release_date, movie_play_date)
        VALUES (
                i_creditCardNum,
                i_comName,
                i_thName,
                i_movName,
                i_movReleaseDate,
                i_movPlayDate
            );
	END IF;
END$$
DELIMITER ;


-- SCREEN 21
DROP PROCEDURE IF EXISTS customer_view_history;
DELIMITER $$
CREATE PROCEDURE `customer_view_history`(IN i_cusUsername VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS CosViewHistory;
    CREATE TABLE CosViewHistory
    SELECT movie_name as movName, theater_name as thName, company_name as comName, credit_card_num as creditCardNum, movie_play_date as movPlayDate
    FROM credit_card_payment
    WHERE credit_card_payment.credit_card_num IN (SELECT credit_card.credit_card_num FROM credit_card WHERE credit_card.username = i_cusUsername or i_cusUsername = '');
END$$
DELIMITER ;


-- SCREEN 22
DROP PROCEDURE IF EXISTS user_filter_th;
DELIMITER $$
CREATE PROCEDURE `user_filter_th`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_city VARCHAR(50), IN i_state VARCHAR(3))
BEGIN
    DROP TABLE IF EXISTS UserFilterTh;
    CREATE TABLE UserFilterTh
	SELECT theater.theater_name as thName, theater.street as thStreet, theater.city as thCity, theater.state as thState, theater.zipcode as thZipcode, theater.company_name as comName
    FROM theater
    WHERE
		(theater_name = i_thName OR i_thName = "ALL" or i_thName = '') AND
        (company_name = i_comName OR i_comName = "ALL" or i_comName = '') AND
        (city = i_city OR i_city = '') AND
        (state = i_state OR i_state = "ALL" or i_state = '');
END$$
DELIMITER ;


-- SCREEN 22
DROP PROCEDURE IF EXISTS user_visit_th;
DELIMITER $$
CREATE PROCEDURE `user_visit_th`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_visitDate DATE, IN i_username VARCHAR(50))
BEGIN
    INSERT INTO visit (theater_name, company_name, visit_date, username)
    VALUES (i_thName, i_comName, i_visitDate, i_username);
END$$
DELIMITER ;


-- SCREEN 23
DROP PROCEDURE IF EXISTS user_filter_visitHistory;
DELIMITER $$
CREATE PROCEDURE `user_filter_visitHistory`(IN i_username VARCHAR(50), IN i_minVisitDate DATE, IN i_maxVisitDate DATE)
BEGIN
    DROP TABLE IF EXISTS UserVisitHistory;
    CREATE TABLE UserVisitHistory
	SELECT theater_name as thName, street as thStreet, city as thCity, state as thState, zipcode as thZipcode, company_name as comName, visit_date as visitDate
    FROM visit
		NATURAL JOIN
        theater
	WHERE
		(username = i_username) AND
        (i_minVisitDate IS NULL OR visit_date >= i_minVisitDate) AND
        (i_maxVisitDate IS NULL OR visit_date <= i_maxVisitDate);
END$$
DELIMITER ;