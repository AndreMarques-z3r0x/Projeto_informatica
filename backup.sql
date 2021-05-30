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
-- Table structure for table `estatisticas`
--

DROP TABLE IF EXISTS `estatisticas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estatisticas` (
  `P1` int NOT NULL,
  `P2` int NOT NULL,
  `P3` int NOT NULL,
  `P4` int NOT NULL,
  `P5` int NOT NULL,
  `P6` int NOT NULL,
  `maq` int NOT NULL,
  PRIMARY KEY (`maq`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estatisticas`
--

LOCK TABLES `estatisticas` WRITE;
/*!40000 ALTER TABLE `estatisticas` DISABLE KEYS */;
INSERT INTO `estatisticas` VALUES (0,0,0,0,0,0,1),(0,0,0,0,0,0,2),(0,0,0,0,0,0,3),(0,0,0,0,0,0,4),(0,0,0,0,0,0,5),(0,0,0,0,0,0,6);
/*!40000 ALTER TABLE `estatisticas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `piece` int NOT NULL,
  `quantity` int NOT NULL,
  PRIMARY KEY (`piece`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (12,0),(23,0),(34,0),(45,0),(56,0),(59,0),(67,0),(68,0),(99,1);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

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
INSERT INTO `stores` VALUES ('P1',339),('P2',67),('P3',18),('P4',23),('P5',13),('P6',15),('P7',30),('P8',2),('P9',0);
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
  `falta` json NOT NULL,
  `falta_mesmo` json NOT NULL,
  `time1` int NOT NULL,
  `start` int NOT NULL,
  `end` int NOT NULL,
  `penalty_incurred` int NOT NULL,
  `estado` int NOT NULL,
  PRIMARY KEY (`nnn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transform`
--

LOCK TABLES `transform` WRITE;
/*!40000 ALTER TABLE `transform` DISABLE KEYS */;
INSERT INTO `transform` VALUES (101,'P1','P5',15,100,250,100,60,0,0,'[0, 0, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622390939,1622391016,1622391744,1200,2),(102,'P5','P6',16,100,300,100,16,0,0,'[0, 0, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622390939,1622391213,1622391478,500,2),(103,'P6','P7',16,100,300,100,16,0,0,'[0, 0, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622390939,1622391071,1622391373,300,2),(104,'P1','P5',15,100,300,100,37,23,23,'[0, 0, 3, 0, 0, 0, 0, 0, 0]','[0, 0, 1, 10, 12, 0, 0, 0, 0]',1622391145,1622391422,0,700,1),(105,'P5','P6',16,100,295,110,16,0,0,'[0, 0, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622391145,1622391414,1622391685,550,2),(106,'P6','P7',16,100,290,120,16,0,0,'[0, 0, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622391145,1622391317,1622391650,600,2),(111,'P1','P2',2,3,50,100,2,0,0,'[0, 1, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622390943,1622391015,1622391016,100,2),(112,'P1','P2',4,3,50,100,4,0,0,'[0, 3, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622390943,1622391015,1622391017,100,2),(113,'P2','P3',1,3,50,100,1,0,0,'[0, 0, 1, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622390943,1622390944,1622390980,0,2),(114,'P3','P4',1,3,50,100,1,0,0,'[0, 0, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622390943,1622390944,1622390978,0,2),(115,'P1','P3',2,3,150,100,4,0,0,'[0, 0, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622391162,1622391316,1622391505,400,2),(116,'P1','P2',4,3,160,150,4,0,0,'[0, 0, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622391162,1622391315,1622391435,450,2),(117,'P2','P3',1,3,145,100,1,0,0,'[0, 0, 1, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622391162,1622391314,1622391320,100,2),(118,'P3','P4',1,3,100,110,1,0,0,'[0, 0, 0, 1, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622391162,1622391214,1622391219,0,2),(201,'P6','P8',2,0,50,1000,2,0,0,'[0, 0, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622390994,1622391015,1622391075,1000,2),(202,'P1','P2',4,0,50,1000,4,0,0,'[0, 0, 0, 0, 0, 0, 0, 0, 0]','[0, 0, 0, 0, 0, 0, 0, 0, 0]',1622390994,1622391016,1622391037,0,2);
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
  `estado` int NOT NULL,
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

--
-- Table structure for table `unload_plc`
--

DROP TABLE IF EXISTS `unload_plc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unload_plc` (
  `destination` int NOT NULL,
  `quantity` int NOT NULL,
  `type` int NOT NULL,
  `99` int NOT NULL,
  PRIMARY KEY (`destination`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unload_plc`
--

LOCK TABLES `unload_plc` WRITE;
/*!40000 ALTER TABLE `unload_plc` DISABLE KEYS */;
INSERT INTO `unload_plc` VALUES (1,0,1,0),(2,0,3,0),(3,0,3,0);
/*!40000 ALTER TABLE `unload_plc` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-30 17:31:01
