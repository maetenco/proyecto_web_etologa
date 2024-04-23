-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema esquema_etologia
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `esquema_etologia` ;

-- -----------------------------------------------------
-- Schema esquema_etologia
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `esquema_etologia` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema new_schema1
-- -----------------------------------------------------
USE `esquema_etologia` ;

-- -----------------------------------------------------
-- Table `esquema_etologia`.`veterinarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`veterinarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(100) NULL,
  `last_name` VARCHAR(100) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`tutores`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`tutores` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL,
  `apellido` VARCHAR(100) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`mascotas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`mascotas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `tutor_id` INT NOT NULL,
  `veterinario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_mascotas_tutores_idx` (`tutor_id` ASC) VISIBLE,
  INDEX `fk_mascotas_veterinarios1_idx` (`veterinario_id` ASC) VISIBLE,
  CONSTRAINT `fk_mascotas_tutores`
    FOREIGN KEY (`tutor_id`)
    REFERENCES `esquema_etologia`.`tutores` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_mascotas_veterinarios1`
    FOREIGN KEY (`veterinario_id`)
    REFERENCES `esquema_etologia`.`veterinarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`antecedentes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`antecedentes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre_mas` VARCHAR(255) NULL,
  `dog_or_cat` TINYINT NULL,
  `raza` VARCHAR(255) NULL,
  `fecha_nac` DATETIME NULL,
  `edad` VARCHAR(100) NULL,
  `peso` VARCHAR(100) NULL,
  `sexo` TINYINT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_antecedentes_mascotas1_idx` (`mascota_id` ASC) VISIBLE,
  CONSTRAINT `fk_antecedentes_mascotas1`
    FOREIGN KEY (`mascota_id`)
    REFERENCES `esquema_etologia`.`mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`castraciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`castraciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `castracion` TINYINT NULL,
  `fecha_castracion` DATETIME NULL,
  `motivo_castracion` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_castraciones_mascotas1_idx` (`mascota_id` ASC) VISIBLE,
  CONSTRAINT `fk_castraciones_mascotas1`
    FOREIGN KEY (`mascota_id`)
    REFERENCES `esquema_etologia`.`mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`adquisiciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`adquisiciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `edad_adopcion` VARCHAR(255) NULL,
  `donde_adquisicion` VARCHAR(255) NULL,
  `tiempo_con_madre_hrnos` VARCHAR(255) NULL,
  `momento_salida_a_calle` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_adquisiciones_mascotas1_idx` (`mascota_id` ASC) VISIBLE,
  CONSTRAINT `fk_adquisiciones_mascotas1`
    FOREIGN KEY (`mascota_id`)
    REFERENCES `esquema_etologia`.`mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`entrenamientos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`entrenamientos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tuvo_entrenamiento` TINYINT NULL,
  `motivo_entrenamiento` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_entrenamientos_mascotas1_idx` (`mascota_id` ASC) VISIBLE,
  CONSTRAINT `fk_entrenamientos_mascotas1`
    FOREIGN KEY (`mascota_id`)
    REFERENCES `esquema_etologia`.`mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`alimentaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`alimentaciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo_alimentacion` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascotas_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_alimentaciones_mascotas1_idx` (`mascotas_id` ASC) VISIBLE,
  CONSTRAINT `fk_alimentaciones_mascotas1`
    FOREIGN KEY (`mascotas_id`)
    REFERENCES `esquema_etologia`.`mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`diagn_previo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`diagn_previo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `diagnostico` VARCHAR(255) NULL,
  `esta_en_tto` TINYINT NULL,
  `problema_fisico` VARCHAR(255) NULL,
  `medicamentos` TEXT NULL,
  `examenes` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_diagn_previo_mascotas1_idx` (`mascota_id` ASC) VISIBLE,
  CONSTRAINT `fk_diagn_previo_mascotas1`
    FOREIGN KEY (`mascota_id`)
    REFERENCES `esquema_etologia`.`mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`vacunas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`vacunas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nom_fecha_ultima_vac` TEXT NULL,
  `nom_fecha_antiparasitario` TEXT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_vacunas_mascotas1_idx` (`mascota_id` ASC) VISIBLE,
  CONSTRAINT `fk_vacunas_mascotas1`
    FOREIGN KEY (`mascota_id`)
    REFERENCES `esquema_etologia`.`mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`motivos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`motivos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `motivo_consulta` TEXT NULL,
  `gatos_mas` INT NULL,
  `perros_mas` INT NULL,
  `otro_animal` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_motivos_mascotas1_idx` (`mascota_id` ASC) VISIBLE,
  CONSTRAINT `fk_motivos_mascotas1`
    FOREIGN KEY (`mascota_id`)
    REFERENCES `esquema_etologia`.`mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`examenes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`examenes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `examen` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_examenes_mascotas1_idx` (`mascota_id` ASC) VISIBLE,
  CONSTRAINT `fk_examenes_mascotas1`
    FOREIGN KEY (`mascota_id`)
    REFERENCES `esquema_etologia`.`mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `esquema_etologia`.`derivaciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `esquema_etologia`.`derivaciones` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `derivacion` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `mascota_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_derivaciones_mascotas1_idx` (`mascota_id` ASC) VISIBLE,
  CONSTRAINT `fk_derivaciones_mascotas1`
    FOREIGN KEY (`mascota_id`)
    REFERENCES `esquema_etologia`.`mascotas` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
