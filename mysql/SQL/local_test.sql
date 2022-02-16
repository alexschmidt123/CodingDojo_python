 CREATE DATABASE `sql_tutorial`;
 SHOW DATABASES;
 USE `sql_tutorial`;
 
 SET SQL_SAFE_UPDATES = 0;
 CREATE TABLE `student` (
       `student_id` INT, 
       `name` VARCHAR(20),
       `major` VARCHAR(20) DEFAULT '化学',
       PRIMARY KEY  (`student_id`),
       `score` INT
);

SELECT * FROM `student`;
DROP TABLE `student`;
INSERT INTO `student` VALUES(1, '小白', '英语', 50);
INSERT INTO `student` VALUES(2, '小黄', '生物', 90);
INSERT INTO `student` VALUES(3, '小绿', '历史', 70);

INSERT INTO `student` (`name`, `major`,`student_id`, `score`)  VALUES('小蓝', '英语', 4,80);
INSERT INTO `student` (`student_id`, `name`,`score`) VALUES(5, '小黑', 20);

UPDATE `student`
SET `major` = '英语文学'
WHERE `major` = '英语';


DELETE FROM `student`
WHERE `score` < 60;