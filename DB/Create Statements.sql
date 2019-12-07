DROP DATABASE IF EXISTS `atlanta_movie`;
CREATE DATABASE IF NOT EXISTS `atlanta_movie`;
USE `atlanta_movie`;

DROP TABLE IF EXISTS `user`;
create table `user` (
	username varchar(20) not null,
    # store sha-512 hashed passwords as binary
    user_password binary(64) not null,
    user_type enum('admin', 'admin-customer', 'customer', 'manager', 'manager-customer', 'user') not null,
    user_status enum('approved', 'declined', 'pending') not null,
    firstname varchar(20) not null,
    lastname varchar(20) not null,
    primary key (username)
);

DROP TABLE IF EXISTS `company`;
create table `company` (
	company_name varchar(20) not null,
    primary key (company_name)
);

#the application will make sure only customers can have credit cards
#and will make sure each customer has at least 1 credit card
DROP TABLE IF EXISTS `credit_card`;
create table `credit_card` (
	credit_card_num char(16) not null,
    username varchar(20) not null,
    primary key (credit_card_num),
    foreign key (username) references user(username)
		on update cascade on delete cascade
);

DROP TABLE IF EXISTS `state`;
create table `state` (
    postal_code char(2) not null,
    state_name varchar(20) not null unique,
    primary key (postal_code)
);

DROP TABLE IF EXISTS `manager`;
create table `manager` (
    username varchar(20) not null,
    zipcode char(5) not null,
    street varchar(20) not null,
    city varchar(20) not null,
    state char(2) not null,
    company varchar(20) not null,
    primary key (username),
    foreign key (username) references user(username)
		on update cascade on delete cascade,
    foreign key (state) references state(postal_code)
        on update restrict on delete restrict,
    foreign key (company) references company(company_name)
        on update cascade on delete cascade
);
create unique index address on manager(zipcode, street, city, state, company);

# application will ensure that a manager works for a theater
# only when that manager and theater belong to the same company
DROP TABLE IF EXISTS `theater`;
create table `theater` (
	theater_name varchar(20) not null,
	company_name varchar(20) not null,
    manager varchar(20) not null unique,
    zipcode char(5) not null,
    street varchar(20) not null,
    city varchar(20) not null,
    state char(2) not null,
    capacity tinyint unsigned not null,
    primary key (theater_name, company_name),
    foreign key (company_name) references company(company_name)
		on update cascade on delete cascade,
    foreign key (manager) references manager(username)
		on update cascade on delete restrict,
    foreign key (state) references state(postal_code)
        on update restrict on delete restrict
);

DROP TABLE IF EXISTS `visit`;
create table `visit` (
	visit_id int unsigned not null auto_increment,
    visit_date date not null,
    username varchar(20) not null,
    theater_name varchar(20) not null,
    company_name varchar(20) not null,
    primary key (visit_id),
    foreign key (username) references user(username)
		on update cascade on delete cascade,
    foreign key (theater_name, company_name) references theater(theater_name, company_name)
        on update cascade on delete cascade
);

DROP TABLE IF EXISTS `movie`;
create table `movie` (
	movie_name varchar(20) not null,
    release_date date not null,
    duration time not null,
    primary key (movie_name, release_date)
);

DROP TABLE IF EXISTS `movie_play`;
create table `movie_play` (
	company_name varchar(20) not null,
    theater_name varchar(20) not null,
    movie_name varchar(20) not null,
    movie_release_date date not null,
    movie_play_date date not null,
    primary key (company_name, theater_name, movie_name, movie_release_date, movie_play_date),
    foreign key (company_name, theater_name) references theater(company_name, theater_name)
		on update cascade on delete cascade,
    foreign key (movie_name, movie_release_date) references movie(movie_name, release_date)
		on update cascade on delete cascade
);

DROP TABLE IF EXISTS `credit_card_payment`;
create table `credit_card_payment` (
	credit_card_num char(16) not null,
    company_name varchar(20) not null,
    theater_name varchar(20) not null,
    movie_name varchar(20) not null,
    movie_release_date date not null,
	movie_play_date date not null,
    primary key (credit_card_num, company_name, theater_name, movie_name, movie_release_date, movie_play_date),
    foreign key (credit_card_num) references credit_card(credit_card_num)
		on update cascade on delete cascade,
    foreign key (company_name, theater_name, movie_name, movie_release_date, movie_play_date) references movie_play(company_name, theater_name, movie_name, movie_release_date, movie_play_date)
		on update cascade on delete cascade
);