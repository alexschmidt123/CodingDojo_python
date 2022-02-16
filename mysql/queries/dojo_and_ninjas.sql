-- Query: Create 3 new dojos 
INSERT INTO `dojos_and_ninjas_schema`.`dojos` (`id`, `name`) VALUES ('1', 'Persistence Dojo.');
INSERT INTO `dojos_and_ninjas_schema`.`dojos` (`id`, `name`) VALUES ('2', 'Smooth Moves Dojo');
INSERT INTO `dojos_and_ninjas_schema`.`dojos` (`id`, `name`) VALUES ('3', 'Master Kickers Karate');
 
--  Query: Delete the 3 dojos you just created
DELETE FROM `dojos_and_ninjas_schema`.`dojos` 
WHERE (`id` = '1');
DELETE FROM `dojos_and_ninjas_schema`.`dojos` 
WHERE (`id` = '2');
DELETE FROM `dojos_and_ninjas_schema`.`dojos` 
WHERE (`id` = '3');
  
 --  Query: Create 3 more dojos
 INSERT INTO `dojos_and_ninjas_schema`.`dojos` (`id`, `name`) 
 VALUES ('1', 'Persistence Dojo.');
 INSERT INTO `dojos_and_ninjas_schema`.`dojos` (`id`, `name`) 
 VALUES ('2', 'Smooth Moves Dojo');
 INSERT INTO `dojos_and_ninjas_schema`.`dojos` (`id`, `name`) 
 VALUES ('3', 'Master Kickers Karate');
 
--  Query: Create 3 ninjas that belong to the first dojo
INSERT INTO `dojos_and_ninjas_schema`.`ninjas` (`id`, `first_name`,`last_name`, `age`, `dojo_id`) 
VALUES ('101', 'Joseph', 'Schmidt', '25', '1');
INSERT INTO `dojos_and_ninjas_schema`.`ninjas` (`id`, `first_name`,`last_name`, `age`, `dojo_id`) 
VALUES ('102', 'Micheal', 'James', '31', '1');
INSERT INTO `dojos_and_ninjas_schema`.`ninjas` (`id`, `first_name`,`last_name`, `age`, `dojo_id`) 
VALUES ('103', 'Peter', 'Adam', '45', '1');

-- Query: Create 3 ninjas that belong to the second dojo
INSERT INTO `dojos_and_ninjas_schema`.`ninjas` (`id`, `first_name`,`last_name`, `age`, `dojo_id`) 
VALUES ('201', 'Justin', 'Pie', '36', '2');
INSERT INTO `dojos_and_ninjas_schema`.`ninjas` (`id`, `first_name`,`last_name`, `age`, `dojo_id`) 
VALUES ('202', 'Kobe', 'Anna', '19', '2');
INSERT INTO `dojos_and_ninjas_schema`.`ninjas` (`id`, `first_name`,`last_name`, `age`, `dojo_id`) 
VALUES ('203', 'Sakura', 'Toi', '55', '2');

-- Query: Create 3 ninjas that belong to the third dojo
INSERT INTO `dojos_and_ninjas_schema`.`ninjas` (`id`, `first_name`,`last_name`, `age`, `dojo_id`) 
VALUES ('301', 'Pan', 'Xue', '28', '3');
INSERT INTO `dojos_and_ninjas_schema`.`ninjas` (`id`, `first_name`,`last_name`, `age`, `dojo_id`) 
VALUES ('302', 'Mike', 'Jimmy', '37', '3');
INSERT INTO `dojos_and_ninjas_schema`.`ninjas` (`id`, `first_name`,`last_name`, `age`, `dojo_id`) 
VALUES ('303', 'Duke', 'Uman', '66', '3');

-- Query: Retrieve all the ninjas from the first dojo
SELECT * 
FROM dojos_and_ninjas_schema.ninjas 
WHERE `dojo_id`='1';

-- Query: Retrieve all the ninjas from the last dojo
SELECT * 
FROM dojos_and_ninjas_schema.ninjas 
WHERE `dojo_id`='3';

-- Query: Retrieve the last ninja's dojo
SELECT dojos.id, dojos.name, dojos.created_at,dojos.updated_at
FROM dojos_and_ninjas_schema.ninjas
LEFT JOIN dojos_and_ninjas_schema.dojos
ON ninjas.dojo_id = dojos.id
WHERE ninjas.id = '303'; /* the last ninja's id*/