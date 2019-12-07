CREATE DATABASE  IF NOT EXISTS `team84` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `team84`;
-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: team84
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `company_name` varchar(50) NOT NULL,
  PRIMARY KEY (`company_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES ('4400 Theater Company'),('AI Theater Company'),('Awesome Theater Company'),('EZ Theater Company');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_card`
--

DROP TABLE IF EXISTS `credit_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `credit_card` (
  `credit_card_num` char(16) NOT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`credit_card_num`),
  KEY `username` (`username`),
  CONSTRAINT `credit_card_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_card`
--

LOCK TABLES `credit_card` WRITE;
/*!40000 ALTER TABLE `credit_card` DISABLE KEYS */;
INSERT INTO `credit_card` VALUES ('1111111111000000','calcultron'),('1111111100000000','calcultron2'),('1111111110000000','calcultron2'),('1111111111100000','calcwizard'),('2222222222000000','cool_class4400'),('2220000000000000','DNAhelix'),('2222222200000000','does2Much'),('2222222222222200','eeqmcsquare'),('2222222222200000','entropyRox'),('2222222222220000','entropyRox'),('1100000000000000','fullMetal'),('1111111111110000','georgep'),('1111111111111000','georgep'),('1111111111111100','georgep'),('1111111111111110','georgep'),('1111111111111111','georgep'),('2222222222222220','ilikemoney$$'),('2222222222222222','ilikemoney$$'),('9000000000000000','ilikemoney$$'),('1111110000000000','imready'),('1110000000000000','isthisthekrustykrab'),('1111000000000000','isthisthekrustykrab'),('1111100000000000','isthisthekrustykrab'),('1000000000000000','notFullMetal'),('2222222000000000','programerAAL'),('3333333333333300','RitzLover28'),('2222222220000000','thePiGuy3.14'),('2222222222222000','theScienceGuy');
/*!40000 ALTER TABLE `credit_card` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `credit_card_payment`
--

DROP TABLE IF EXISTS `credit_card_payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `credit_card_payment` (
  `credit_card_num` char(16) NOT NULL,
  `company_name` varchar(50) NOT NULL,
  `theater_name` varchar(50) NOT NULL,
  `movie_name` varchar(50) NOT NULL,
  `movie_release_date` date NOT NULL,
  `movie_play_date` date NOT NULL,
  PRIMARY KEY (`credit_card_num`,`company_name`,`theater_name`,`movie_name`,`movie_release_date`,`movie_play_date`),
  KEY `company_name` (`company_name`,`theater_name`,`movie_name`,`movie_release_date`,`movie_play_date`),
  CONSTRAINT `credit_card_payment_ibfk_1` FOREIGN KEY (`credit_card_num`) REFERENCES `credit_card` (`credit_card_num`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `credit_card_payment_ibfk_2` FOREIGN KEY (`company_name`, `theater_name`, `movie_name`, `movie_release_date`, `movie_play_date`) REFERENCES `movie_play` (`company_name`, `theater_name`, `movie_name`, `movie_release_date`, `movie_play_date`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credit_card_payment`
--

LOCK TABLES `credit_card_payment` WRITE;
/*!40000 ALTER TABLE `credit_card_payment` DISABLE KEYS */;
INSERT INTO `credit_card_payment` VALUES ('1111111111111111','4400 Theater Company','Cinema Star','How to Train Your Dragon','2010-03-21','2010-04-02'),('1111111111111111','EZ Theater Company','Main Movies','How to Train Your Dragon','2010-03-21','2010-03-22'),('1111111111111111','EZ Theater Company','Main Movies','How to Train Your Dragon','2010-03-21','2010-03-23'),('1111111111111100','EZ Theater Company','Star Movies','How to Train Your Dragon','2010-03-21','2010-03-25');
/*!40000 ALTER TABLE `credit_card_payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manager` (
  `username` varchar(50) NOT NULL,
  `zipcode` char(5) NOT NULL,
  `street` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` char(2) NOT NULL,
  `company` varchar(50) NOT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `address` (`zipcode`,`street`,`city`,`state`,`company`),
  KEY `state` (`state`),
  KEY `company` (`company`),
  CONSTRAINT `manager_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `manager_ibfk_2` FOREIGN KEY (`state`) REFERENCES `state` (`postal_code`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `manager_ibfk_3` FOREIGN KEY (`company`) REFERENCES `company` (`company_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager`
--

LOCK TABLES `manager` WRITE;
/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
INSERT INTO `manager` VALUES ('fatherAI','10001','456 Main St','New York','NY','EZ Theater Company'),('calcultron','30308','123 Peachtree St','Atlanta','GA','EZ Theater Company'),('manager4','30332','000 Ferst Drive','Atlanta','GA','4400 Theater Company'),('manager1','30332','123 Ferst Drive','Atlanta','GA','4400 Theater Company'),('manager2','30332','456 Ferst Drive','Atlanta','GA','AI Theater Company'),('manager3','30332','789 Ferst Drive','Atlanta','GA','4400 Theater Company'),('ghcghc','31415','100 Pi St','Pallet Town','KS','AI Theater Company'),('imbatman','78653','800 Color Dr','Austin','TX','Awesome Theater Company'),('entropyRox','94016','200 Cool Place','San Francisco','CA','4400 Theater Company'),('radioactivePoRa','94088','100 Blu St','Sunnyvale','CA','4400 Theater Company'),('georgep','98105','10 Pearl Dr','Seattle','WA','4400 Theater Company');
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie` (
  `movie_name` varchar(50) NOT NULL,
  `release_date` date NOT NULL,
  `duration` int(11) NOT NULL,
  PRIMARY KEY (`movie_name`,`release_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES ('4400 The Movie','2019-08-12',130),('Avengers: Endgame','2019-04-26',181),('Calculus Returns: A ML Story','2019-09-19',314),('George P Burdell\'s Life Story','1927-08-12',100),('Georgia Tech The Movie','1985-08-13',100),('How to Train Your Dragon','2010-03-21',98),('Spaceballs','1987-06-24',96),('Spider-Man: Into the Spider-Verse','2018-12-01',117),('The First Pokemon Movie','1998-07-19',75),('The King\'s Speech','2010-11-26',119);
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_play`
--

DROP TABLE IF EXISTS `movie_play`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_play` (
  `company_name` varchar(50) NOT NULL,
  `theater_name` varchar(50) NOT NULL,
  `movie_name` varchar(50) NOT NULL,
  `movie_release_date` date NOT NULL,
  `movie_play_date` date NOT NULL,
  PRIMARY KEY (`company_name`,`theater_name`,`movie_name`,`movie_release_date`,`movie_play_date`),
  KEY `movie_name` (`movie_name`,`movie_release_date`),
  CONSTRAINT `movie_play_ibfk_1` FOREIGN KEY (`company_name`, `theater_name`) REFERENCES `theater` (`company_name`, `theater_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `movie_play_ibfk_2` FOREIGN KEY (`movie_name`, `movie_release_date`) REFERENCES `movie` (`movie_name`, `release_date`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_play`
--

LOCK TABLES `movie_play` WRITE;
/*!40000 ALTER TABLE `movie_play` DISABLE KEYS */;
INSERT INTO `movie_play` VALUES ('4400 Theater Company','Cinema Star','4400 The Movie','2019-08-12','2019-09-12'),('Awesome Theater Company','ABC Theater','4400 The Movie','2019-08-12','2019-10-12'),('EZ Theater Company','Star Movies','4400 The Movie','2019-08-12','2019-08-12'),('AI Theater Company','ML Movies','Calculus Returns: A ML Story','2019-09-19','2019-10-10'),('AI Theater Company','ML Movies','Calculus Returns: A ML Story','2019-09-19','2019-12-30'),('4400 Theater Company','Cinema Star','George P Burdell\'s Life Story','1927-08-12','2010-05-20'),('EZ Theater Company','Main Movies','George P Burdell\'s Life Story','1927-08-12','2019-07-14'),('EZ Theater Company','Main Movies','George P Burdell\'s Life Story','1927-08-12','2019-10-22'),('4400 Theater Company','Cinema Star','Georgia Tech The Movie','1985-08-13','2019-09-30'),('Awesome Theater Company','ABC Theater','Georgia Tech The Movie','1985-08-13','1985-08-13'),('4400 Theater Company','Cinema Star','How to Train Your Dragon','2010-03-21','2010-04-02'),('EZ Theater Company','Main Movies','How to Train Your Dragon','2010-03-21','2010-03-22'),('EZ Theater Company','Main Movies','How to Train Your Dragon','2010-03-21','2010-03-23'),('EZ Theater Company','Star Movies','How to Train Your Dragon','2010-03-21','2010-03-25'),('4400 Theater Company','Cinema Star','Spaceballs','1987-06-24','2000-02-02'),('AI Theater Company','ML Movies','Spaceballs','1987-06-24','2010-04-02'),('AI Theater Company','ML Movies','Spaceballs','1987-06-24','2023-01-23'),('EZ Theater Company','Main Movies','Spaceballs','1987-06-24','1999-06-24'),('AI Theater Company','ML Movies','Spider-Man: Into the Spider-Verse','2018-12-01','2019-09-30'),('Awesome Theater Company','ABC Theater','The First Pokemon Movie','1998-07-19','2018-07-19'),('4400 Theater Company','Cinema Star','The King\'s Speech','2010-11-26','2019-12-20'),('EZ Theater Company','Main Movies','The King\'s Speech','2010-11-26','2019-12-20');
/*!40000 ALTER TABLE `movie_play` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `state`
--

DROP TABLE IF EXISTS `state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `state` (
  `postal_code` char(2) NOT NULL,
  `state_name` varchar(50) NOT NULL,
  PRIMARY KEY (`postal_code`),
  UNIQUE KEY `state_name` (`state_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `state`
--

LOCK TABLES `state` WRITE;
/*!40000 ALTER TABLE `state` DISABLE KEYS */;
INSERT INTO `state` VALUES ('AL','Alabama'),('AK','Alaska'),('AZ','Arizona'),('AR','Arkansas'),('CA','California'),('CO','Colorado'),('CT','Connecticut'),('DE','Delaware'),('FL','Florida'),('GA','Georgia'),('HI','Hawaii'),('ID','Idaho'),('IL','Illinois'),('IN','Indiana'),('IA','Iowa'),('KS','Kansas'),('KY','Kentucky'),('LA','Louisiana'),('ME','Maine'),('MD','Maryland'),('MA','Massachusetts'),('MI','Michigan'),('MN','Minnesota'),('MS','Mississippi'),('MO','Missouri'),('MT','Montana'),('NE','Nebraska'),('NV','Nevada'),('NH','New Hampshire'),('NJ','New Jersey'),('NM','New Mexico'),('NY','New York'),('NC','North Carolina'),('ND','North Dakota'),('OH','Ohio'),('OK','Oklahoma'),('OR','Oregon'),('PA','Pennsylvania'),('RI','Rhode Island'),('SC','South Carolina'),('SD','South Dakota'),('TN','Tennessee'),('TX','Texas'),('UT','Utah'),('VT','Vermont'),('VA','Virginia'),('WA','Washington'),('WV','West Virginia'),('WI','Wisconsin'),('','Wyoming');
/*!40000 ALTER TABLE `state` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `theater`
--

DROP TABLE IF EXISTS `theater`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `theater` (
  `theater_name` varchar(50) NOT NULL,
  `company_name` varchar(50) NOT NULL,
  `manager` varchar(50) NOT NULL,
  `zipcode` char(5) NOT NULL,
  `street` varchar(50) NOT NULL,
  `city` varchar(50) NOT NULL,
  `state` char(2) NOT NULL,
  `capacity` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY (`theater_name`,`company_name`),
  UNIQUE KEY `manager` (`manager`),
  KEY `company_name` (`company_name`),
  KEY `state` (`state`),
  CONSTRAINT `theater_ibfk_1` FOREIGN KEY (`company_name`) REFERENCES `company` (`company_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `theater_ibfk_2` FOREIGN KEY (`manager`) REFERENCES `manager` (`username`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `theater_ibfk_3` FOREIGN KEY (`state`) REFERENCES `state` (`postal_code`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `theater`
--

LOCK TABLES `theater` WRITE;
/*!40000 ALTER TABLE `theater` DISABLE KEYS */;
INSERT INTO `theater` VALUES ('ABC Theater','Awesome Theater Company','imbatman','73301','880 Color Dr','Austin','TX',5),('Cinema Star','4400 Theater Company','entropyRox','94016','100 Cool Place','San Francisco','CA',4),('Jonathan\'s Movies','4400 Theater Company','georgep','98101','67 Pearl Dr','Seattle','WA',2),('Main Movies','EZ Theater Company','fatherAI','10001','123 Main St','New York','NY',3),('ML Movies','AI Theater Company','ghcghc','31415','314 Pi St','Pallet Town','KS',3),('Star Movies','4400 Theater Company','radioactivePoRa','80301','4400 Rocks Ave','Boulder','CA',5),('Star Movies','EZ Theater Company','calcultron','30332','745 GT St','Atlanta','GA',2);
/*!40000 ALTER TABLE `theater` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(50) NOT NULL,
  `user_password` char(32) NOT NULL,
  `user_type` enum('Admin','CustomerAdmin','Customer','Manager','CustomerManager','User') NOT NULL,
  `user_status` enum('Approved','Declined','Pending') NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('calcultron','77c9749b451ab8c713c48037ddfbb2c4','CustomerManager','Approved','Dwight','Schrute'),('calcultron2','8792b8cf71d27dc96173b2ac79b96e0d','Customer','Approved','Jim','Halpert'),('calcwizard','0d777e9e30b918e9034ab610712c90cf','Customer','Approved','Issac','Newton'),('clarinetbeast','c8c605999f3d8352d7bb792cf3fdb25b','Customer','Declined','Squidward','Tentacles'),('cool_class4400','77c9749b451ab8c713c48037ddfbb2c4','CustomerAdmin','Approved','A. TA','Washere'),('DNAhelix','ca94efe2a58c27168edf3d35102dbb6d','Customer','Approved','Rosalind','Franklin'),('does2Much','00cedcf91beffa9ee69f6cfe23a4602d','Customer','Approved','Carl','Gauss'),('eeqmcsquare','7c5858f7fcf63ec268f42565be3abb95','Customer','Approved','Albert','Einstein'),('entropyRox','c8c605999f3d8352d7bb792cf3fdb25b','CustomerManager','Approved','Claude','Shannon'),('fatherAI','0d777e9e30b918e9034ab610712c90cf','Manager','Approved','Alan','Turing'),('fullMetal','d009d70ae4164e8989725e828db8c7c2','Customer','Approved','Edward','Elric'),('gdanger','3665a76e271ada5a75368b99f774e404','User','Declined','Gary','Danger'),('georgep','bbb8aae57c104cda40c93843ad5e6db8','CustomerManager','Approved','George P.','Burdell'),('ghcghc','9f0863dd5f0256b0f586a7b523f8cfe8','Manager','Approved','Grace','Hopper'),('ilikemoney$$','7c5858f7fcf63ec268f42565be3abb95','Customer','Approved','Eugene','Krabs'),('imbatman','9f0863dd5f0256b0f586a7b523f8cfe8','Manager','Approved','Bruce','Wayne'),('imready','ca94efe2a58c27168edf3d35102dbb6d','Customer','Approved','Spongebob','Squarepants'),('isthisthekrustykrab','134fb0bf3bdd54ee9098f4cbc4351b9a','Customer','Approved','Patrick','Star'),('manager1','e58cce4fab03d2aea056398750dee16b','Manager','Approved','Manager','One'),('manager2','ba9485f02fc98cdbd2edadb0aa8f6390','Manager','Approved','Manager','Two'),('manager3','6e4fb18b49aa3219bef65195dac7be8c','Manager','Approved','Three','Three'),('manager4','d61dfee83aa2a6f9e32f268d60e789f5','Manager','Approved','Four','Four'),('notFullMetal','d009d70ae4164e8989725e828db8c7c2','Customer','Approved','Alphonse','Elric'),('programerAAL','ba9485f02fc98cdbd2edadb0aa8f6390','Customer','Approved','Ada','Lovelace'),('radioactivePoRa','e5d4b739db1226088177e6f8b70c3a6f','Manager','Approved','Marie','Curie'),('RitzLover28','8792b8cf71d27dc96173b2ac79b96e0d','Customer','Approved','Abby','Normal'),('smith_j','77c9749b451ab8c713c48037ddfbb2c4','User','Pending','John','Smith'),('texasStarKarate','7c5858f7fcf63ec268f42565be3abb95','User','Declined','Sandy','Cheeks'),('thePiGuy3.14','e11170b8cbd2d74102651cb967fa28e5','Customer','Approved','Archimedes','Syracuse'),('theScienceGuy','c8c605999f3d8352d7bb792cf3fdb25b','Customer','Approved','Bill','Nye');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `visit`
--

DROP TABLE IF EXISTS `visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `visit` (
  `visit_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `visit_date` date NOT NULL,
  `username` varchar(50) NOT NULL,
  `theater_name` varchar(50) NOT NULL,
  `company_name` varchar(50) NOT NULL,
  PRIMARY KEY (`visit_id`),
  KEY `username` (`username`),
  KEY `theater_name` (`theater_name`,`company_name`),
  CONSTRAINT `visit_ibfk_1` FOREIGN KEY (`username`) REFERENCES `user` (`username`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `visit_ibfk_2` FOREIGN KEY (`theater_name`, `company_name`) REFERENCES `theater` (`theater_name`, `company_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `visit`
--

LOCK TABLES `visit` WRITE;
/*!40000 ALTER TABLE `visit` DISABLE KEYS */;
INSERT INTO `visit` VALUES (1,'2010-03-22','georgep','Main Movies','EZ Theater Company'),(2,'2010-03-22','calcwizard','Main Movies','EZ Theater Company'),(3,'2010-03-25','calcwizard','Star Movies','EZ Theater Company'),(4,'2010-03-25','imready','Star Movies','EZ Theater Company'),(5,'2010-03-20','calcwizard','ML Movies','AI Theater Company');
/*!40000 ALTER TABLE `visit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'team84'
--

--
-- Dumping routines for database 'team84'
--
/*!50003 DROP PROCEDURE IF EXISTS `admin_approve_user` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `admin_approve_user`(IN i_username VARCHAR(50))
BEGIN
	IF (SELECT user_status from user where username = i_username) in ('Pending', 'Declined') THEN
        UPDATE user
        SET
            user_status = 'Approved'
        WHERE
            username = i_username;
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `admin_create_mov` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `admin_create_mov`(IN i_movName VARCHAR(50), IN i_movDuration INT, IN i_movReleaseDate DATE)
BEGIN
        INSERT INTO movie (movie_name, release_date, duration) VALUES (i_movName, i_movReleaseDate, i_movDuration);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `admin_create_theater` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `admin_create_theater`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_thStreet VARCHAR(50), IN i_thCity VARCHAR(50), IN i_thState CHAR(2), IN i_thZipcode CHAR(5), IN i_capacity INT, IN i_managerUsername VARCHAR(50))
BEGIN
	IF (NOT EXISTS (SELECT * from theater where manager = i_managerUsername) and i_comName = (SELECT company from manager where manager.username = i_managerUsername)) THEN
        INSERT INTO theater(theater_name, company_name, manager, zipcode, street, city, state, capacity) VALUES (i_thName, i_comName, i_managerUsername, i_thZipcode, i_thStreet, i_thCity, i_thState, i_capacity);
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `admin_decline_user` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `admin_decline_user`(IN i_username VARCHAR(50))
BEGIN
	IF 'Pending' = (SELECT user_status from user where username = i_username) THEN
        UPDATE user
        SET
            user_status = 'Declined'
        WHERE
            username = i_username;
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `admin_filter_company` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `admin_filter_company`(IN i_comName VARCHAR(50), IN i_minCity INT, IN i_maxCity INT, IN i_minTheater INT, IN i_maxTheater INT, IN i_minEmployee INT, IN i_maxEmployee INT, IN i_sortBy VARCHAR(50), IN i_sortDirection VARCHAR(50))
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `admin_filter_user` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `admin_filter_user`(IN i_username VARCHAR(50), IN i_status VARCHAR(50), IN i_sortBy VARCHAR(50), IN i_sortDirection VARCHAR(50))
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `admin_view_comDetail_emp` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `admin_view_comDetail_emp`(IN i_comName VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS AdComDetailEmp;
    CREATE TABLE AdComDetailEmp
    SELECT firstname as empFirstName, lastname as empLastName
    FROM user
    WHERE user.username in (SELECT manager.username FROM manager WHERE company = i_comName);

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `admin_view_comDetail_th` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `admin_view_comDetail_th`(IN i_comName VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS AdComDetailTh;
    CREATE TABLE AdComDetailTh
    SELECT theater_name as thName, manager as thManagerUsername, city as thCity, state as thState, capacity as thCapacity
    FROM theater
    WHERE theater.company_name = i_comName;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `customer_add_creditcard` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `customer_add_creditcard`(IN i_username VARCHAR(50), IN i_creditCardNum CHAR(16))
BEGIN
	DROP TABLE IF EXISTS AddCreditCardHelper;
    CREATE TABLE AddCreditCardHelper
    SELECT username as username, count(*) as credit_card_count FROM credit_card GROUP BY username;
	
    IF 	(SELECT credit_card_count from AddCreditCardHelper where username = i_username) < 5 
			and LENGTH(i_creditCardNum) = 16 THEN
        INSERT INTO credit_card (credit_card_num, username) VALUES (i_creditCardNum, i_username);
	END IF;
    
    DROP TABLE IF EXISTS AddCreditCardHelper;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `customer_filter_mov` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `customer_filter_mov`(IN i_movName VARCHAR(50), IN i_comName VARCHAR(50), IN i_city VARCHAR(50), IN i_state VARCHAR(50), IN i_minMovPlayDate DATE,  IN i_maxMovPlayDate DATE)
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
        
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `customer_only_register` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `customer_only_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50))
BEGIN
        INSERT INTO user (username, user_password, firstname, lastname, user_type, user_status) VALUES (i_username, MD5(i_password), i_firstname, i_lastname, 'Customer', 'Pending');
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `customer_view_history` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `customer_view_history`(IN i_cusUsername VARCHAR(50))
BEGIN
    DROP TABLE IF EXISTS CosViewHistory;
    CREATE TABLE CosViewHistory
    SELECT movie_name as movName, theater_name as thName, company_name as comName, credit_card_num as creditCardNum, movie_play_date as movPlayDate
    FROM credit_card_payment
    WHERE credit_card_payment.credit_card_num IN (SELECT credit_card.credit_card_num FROM credit_card WHERE credit_card.username = i_cusUsername or i_cusUsername = '');
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `customer_view_mov` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `customer_view_mov`(IN i_creditCardNum CHAR(16), IN i_movName VARCHAR(50), IN i_movReleaseDate DATE, IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_movPlayDate DATE)
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `manager_customer_add_creditcard` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `manager_customer_add_creditcard`(IN i_username VARCHAR(50), IN i_creditCardNum CHAR(16))
BEGIN
	DROP TABLE IF EXISTS AddCreditCardHelper2;
    CREATE TABLE AddCreditCardHelper2
    SELECT username as username, count(*) as credit_card_count FROM credit_card GROUP BY username;
	
    IF (SELECT credit_card_count from AddCreditCardHelper2 where username = i_username) < 5 THEN
        INSERT INTO credit_card (credit_card_num, username) VALUES (i_creditCardNum, i_username);
	END IF;
    
    DROP TABLE IF EXISTS AddCreditCardHelper2;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `manager_customer_register` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `manager_customer_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50), IN i_comName VARCHAR(50), IN i_empStreet VARCHAR(50), IN i_empCity VARCHAR(50), IN i_empState CHAR(2), IN i_empZipcode CHAR(5))
BEGIN
        INSERT INTO user (username, user_password, firstname, lastname, user_type, user_status) VALUES (i_username, MD5(i_password), i_firstname, i_lastname, 'CustomerManager', 'Pending');
        INSERT INTO manager (username, zipcode, street, city, state, company) VALUES (i_username, i_empZipcode, i_empStreet, i_empCity, i_empState, i_comName);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `manager_filter_th` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `manager_filter_th`(IN i_manUsername VARCHAR(50), IN i_movName VARCHAR(50), IN i_minMovDuration INT, IN i_maxMovDuration INT, IN i_minMovReleaseDate DATE,  IN i_maxMovReleaseDate DATE, IN i_minMovPlayDate DATE,  IN i_maxMovPlayDate DATE, IN i_includeNotPlayed BOOLEAN)
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `manager_only_register` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `manager_only_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50), IN i_comName VARCHAR(50), IN i_empStreet VARCHAR(50), IN i_empCity VARCHAR(50), IN i_empState CHAR(2), IN i_empZipcode CHAR(5))
BEGIN
        INSERT INTO user (username, user_password, firstname, lastname, user_type, user_status) VALUES (i_username, MD5(i_password), i_firstname, i_lastname, 'Manager', 'Pending');
        INSERT INTO manager (username, zipcode, street, city, state, company) VALUES (i_username, i_empZipcode, i_empStreet, i_empCity, i_empState, i_comName);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `manager_schedule_mov` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `manager_schedule_mov`(IN i_manUsername VARCHAR(50), IN i_movName VARCHAR(50), IN i_movReleaseDate DATE, IN i_movPlayDate DATE)
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `user_filter_th` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `user_filter_th`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_city VARCHAR(50), IN i_state VARCHAR(3))
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `user_filter_visitHistory` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `user_filter_visitHistory`(IN i_username VARCHAR(50), IN i_minVisitDate DATE, IN i_maxVisitDate DATE)
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `user_login` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `user_login`(IN i_username VARCHAR(50), IN i_password VARCHAR(50))
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `user_register` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `user_register`(IN i_username VARCHAR(50), IN i_password VARCHAR(50), IN i_firstname VARCHAR(50), IN i_lastname VARCHAR(50))
BEGIN
		INSERT INTO user (username, user_password, firstname, lastname, user_type, user_status) VALUES (i_username, MD5(i_password), i_firstname, i_lastname, 'User', 'Pending');
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `user_visit_th` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `user_visit_th`(IN i_thName VARCHAR(50), IN i_comName VARCHAR(50), IN i_visitDate DATE, IN i_username VARCHAR(50))
BEGIN
    INSERT INTO visit (theater_name, company_name, visit_date, username)
    VALUES (i_thName, i_comName, i_visitDate, i_username);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-26 17:03:19
