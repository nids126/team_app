CREATE SCHEMA `team_app` ;
USE team_app;

CREATE TABLE `team_members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) NOT NULL,
  `last_name` varchar(45) NOT NULL,
  `phone_number` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `role` enum('ADMIN','REGULAR') NOT NULL DEFAULT 'REGULAR',
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone_number_UNIQUE` (`phone_number`),
  UNIQUE KEY `email_UNIQUE` (`email`)
);

INSERT INTO `team_app`.`team_members` (`first_name`, `last_name`, `phone_number`, `email`, `role`) VALUES ('Nidhi', 'Sahu', '9005798121', 'sahu.nidhi1892@gmail.com', 'ADMIN');

INSERT INTO `team_app`.`team_members` (`first_name`, `last_name`, `phone_number`, `email`) VALUES ('Sample', 'User', '9898989898', 'xyz123@gmail.com');



