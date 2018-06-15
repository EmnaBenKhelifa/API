--Create an empty table in mysql local server

CREATE TABLE flaskapp.users (
`user_id` BIGINT AUTO_INCREMENT,
`nom` VARCHAR(50) ,
`prenom` VARCHAR(50) ,
`birthday` VARCHAR(50) ,
PRIMARY KEY (`user_id`));

--Create property table

CREATE TABLE flaskapp.property (
`user_id` BIGINT,
`property_id` BIGINT AUTO_INCREMENT,
`property_name` VARCHAR(100) ,
`description` VARCHAR(1000) ,
`type` VARCHAR(100) ,
`city` VARCHAR(100) ,
`beds_number` VARCHAR(2) ,
`beds_description` VARCHAR(1000),
PRIMARY KEY (`property_id`));