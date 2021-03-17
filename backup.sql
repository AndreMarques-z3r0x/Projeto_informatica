-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: informatica
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `stores`
--

DROP TABLE IF EXISTS `stores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stores` (
  `piece` varchar(3) NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`piece`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stores`
--

LOCK TABLES `stores` WRITE;
/*!40000 ALTER TABLE `stores` DISABLE KEYS */;
INSERT INTO `stores` VALUES ('P1',30),('P12',86),('P2',30),('P3',40),('P4',45),('P5',20),('P6',24),('P7',61),('P8',85),('P9',66);
/*!40000 ALTER TABLE `stores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transform`
--

DROP TABLE IF EXISTS `transform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transform` (
  `nnn` int NOT NULL,
  `from` varchar(3) NOT NULL,
  `to` varchar(3) NOT NULL,
  `quantity` int NOT NULL,
  `time` int NOT NULL,
  `max_delay` int NOT NULL,
  `penalty` int NOT NULL,
  `quantity1` int NOT NULL,
  `quantity2` int NOT NULL,
  `quantity3` int NOT NULL,
  PRIMARY KEY (`nnn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transform`
--

LOCK TABLES `transform` WRITE;
/*!40000 ALTER TABLE `transform` DISABLE KEYS */;
INSERT INTO `transform` VALUES (1,'P1','P2',30,1500,1500,0,0,0,0),(2,'P5','P6',15,0,224,0,0,0,0),(3,'P2','P7',55,0,117,0,0,0,0),(4,'P2','P3',69,0,6969,0,0,0,0),(5,'P2','P3',69,0,6969,0,0,0,0),(6,'P2','P3',69,0,6969,0,0,0,0),(7,'P2','P3',80,0,9999,0,0,0,0);
/*!40000 ALTER TABLE `transform` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unload`
--

DROP TABLE IF EXISTS `unload`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unload` (
  `nnn` int NOT NULL,
  `type` varchar(3) NOT NULL,
  `destination` varchar(3) NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`nnn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unload`
--

LOCK TABLES `unload` WRITE;
/*!40000 ALTER TABLE `unload` DISABLE KEYS */;
/*!40000 ALTER TABLE `unload` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-17 12:27:39
