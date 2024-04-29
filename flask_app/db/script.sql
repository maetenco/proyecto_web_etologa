-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: esquema_etologia
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `adquisiciones`
--

DROP TABLE IF EXISTS `adquisiciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `adquisiciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `edad_adopcion` varchar(255) DEFAULT NULL,
  `donde_adquisicion` varchar(255) DEFAULT NULL,
  `tiempo_con_madre_hrnos` varchar(255) DEFAULT NULL,
  `momento_salida_a_calle` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_adquisiciones_mascotas1_idx` (`mascota_id`),
  CONSTRAINT `fk_adquisiciones_mascotas1` FOREIGN KEY (`mascota_id`) REFERENCES `mascotas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `agenda`
--

DROP TABLE IF EXISTS `agenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agenda` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fecha_inicio` datetime DEFAULT NULL,
  `fecha_final` datetime DEFAULT NULL,
  `evento` varchar(50) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `alimentaciones`
--

DROP TABLE IF EXISTS `alimentaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alimentaciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo_alimentacion` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascotas_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_alimentaciones_mascotas1_idx` (`mascotas_id`),
  CONSTRAINT `fk_alimentaciones_mascotas1` FOREIGN KEY (`mascotas_id`) REFERENCES `mascotas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `antecedentes`
--

DROP TABLE IF EXISTS `antecedentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `antecedentes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre_mas` varchar(255) DEFAULT NULL,
  `dog_or_cat` tinyint DEFAULT NULL,
  `raza` varchar(255) DEFAULT NULL,
  `fecha_nac` datetime DEFAULT NULL,
  `edad` varchar(100) DEFAULT NULL,
  `peso` varchar(100) DEFAULT NULL,
  `sexo` tinyint DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_antecedentes_mascotas1_idx` (`mascota_id`),
  CONSTRAINT `fk_antecedentes_mascotas1` FOREIGN KEY (`mascota_id`) REFERENCES `mascotas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `castraciones`
--

DROP TABLE IF EXISTS `castraciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `castraciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `castracion` tinyint DEFAULT NULL,
  `fecha_castracion` datetime DEFAULT NULL,
  `motivo_castracion` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_castraciones_mascotas1_idx` (`mascota_id`),
  CONSTRAINT `fk_castraciones_mascotas1` FOREIGN KEY (`mascota_id`) REFERENCES `mascotas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `derivaciones`
--

DROP TABLE IF EXISTS `derivaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `derivaciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `derivacion` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_derivaciones_mascotas1_idx` (`mascota_id`),
  CONSTRAINT `fk_derivaciones_mascotas1` FOREIGN KEY (`mascota_id`) REFERENCES `mascotas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `diagn_previo`
--

DROP TABLE IF EXISTS `diagn_previo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diagn_previo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `diagnostico` varchar(255) DEFAULT NULL,
  `esta_en_tto` tinyint DEFAULT NULL,
  `problema_fisico` varchar(255) DEFAULT NULL,
  `medicamentos` text,
  `examenes` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_diagn_previo_mascotas1_idx` (`mascota_id`),
  CONSTRAINT `fk_diagn_previo_mascotas1` FOREIGN KEY (`mascota_id`) REFERENCES `mascotas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `entrenamientos`
--

DROP TABLE IF EXISTS `entrenamientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `entrenamientos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tuvo_entrenamiento` tinyint DEFAULT NULL,
  `motivo_entrenamiento` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_entrenamientos_mascotas1_idx` (`mascota_id`),
  CONSTRAINT `fk_entrenamientos_mascotas1` FOREIGN KEY (`mascota_id`) REFERENCES `mascotas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `examenes`
--

DROP TABLE IF EXISTS `examenes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `examenes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `examen` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_examenes_mascotas1_idx` (`mascota_id`),
  CONSTRAINT `fk_examenes_mascotas1` FOREIGN KEY (`mascota_id`) REFERENCES `mascotas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `mascotas`
--

DROP TABLE IF EXISTS `mascotas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mascotas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tutor_id` int NOT NULL,
  `veterinario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_mascotas_tutores_idx` (`tutor_id`),
  KEY `fk_mascotas_veterinarios1_idx` (`veterinario_id`),
  CONSTRAINT `fk_mascotas_tutores` FOREIGN KEY (`tutor_id`) REFERENCES `tutores` (`id`),
  CONSTRAINT `fk_mascotas_veterinarios1` FOREIGN KEY (`veterinario_id`) REFERENCES `veterinarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `motivos`
--

DROP TABLE IF EXISTS `motivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `motivos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `motivo_consulta` text,
  `gatos_mas` int DEFAULT NULL,
  `perros_mas` int DEFAULT NULL,
  `otro_animal` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_motivos_mascotas1_idx` (`mascota_id`),
  CONSTRAINT `fk_motivos_mascotas1` FOREIGN KEY (`mascota_id`) REFERENCES `mascotas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tutores`
--

DROP TABLE IF EXISTS `tutores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tutores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `apellido` varchar(100) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `vacunas`
--

DROP TABLE IF EXISTS `vacunas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vacunas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom_fecha_ultima_vac` text,
  `nom_fecha_antiparasitario` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_vacunas_mascotas1_idx` (`mascota_id`),
  CONSTRAINT `fk_vacunas_mascotas1` FOREIGN KEY (`mascota_id`) REFERENCES `mascotas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `veterinarios`
--

DROP TABLE IF EXISTS `veterinarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veterinarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-27 22:16:18
