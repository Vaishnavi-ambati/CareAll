CREATE DATABASE careallDB;
SHOW DATABASES;
# drop table young_champs;
CREATE TABLE young_champs (
    username varchar(255), 
    pass varchar(255), 
    income_earned bigint, 
    contact bigint, 
    address varchar(255), 
    id_proof varchar(255), 
    no_of_oldies bigint, 
    rating integer,
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

alter table young_champs CHANGE COLUMN pass passwd varchar(255)

INSERT INTO young_champs (username, passwd , income_earned, contact, address, id_proof, no_of_oldies, rating)
VALUES ("name1","123",1000,74563561230,"pune","aadhar",2,5);

INSERT INTO young_champs (username, passwd , income_earned, contact, address, id_proof, no_of_oldies, rating)
VALUES ("name2","456",2000,5634561230,"pune","aadhar",3,4);

INSERT INTO young_champs (username, passwd , income_earned, contact, address, id_proof, no_of_oldies, rating)
VALUES ("name3","789",4000,5684561230,"pune","aadhar",4,5);

INSERT INTO young_champs (username, passwd , income_earned, contact, address, id_proof, no_of_oldies, rating)
VALUES ("name4","147",1000,56710561230,"pune","aadhar",1,4);


select * from young_champs
##############################################################################################################################################

# drop table adults;

CREATE TABLE adults (
    username varchar(255), 
    pass varchar(255), 
    contact bigint, 
    address varchar(255), 
    id_proof varchar(255), 
    oldies_name varchar(255),
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

INSERT INTO adults (username, pass, contact, address, id_proof, oldies_name)
VALUES ("adult1","12345",6334561230,"pune","aadhar","oldie1");

INSERT INTO adults (username, pass, contact, address, id_proof, oldies_name)
VALUES ("adult2","5698",2308561230,"pune","aadhar","oldie3,oldie4");

select * from adults
##############################################################################################################################################

CREATE TABLE oldies (
    username varchar(255), 
    adult_name varchar(255), 
    contact bigint, 
    address varchar(255), 
    id_proof varchar(255), 
    assigned_champ bigint,
    sickness varchar(255),
    any_cmnts varchar(255), 
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY
);

INSERT INTO oldies (username, adult_name, contact, address, id_proof, assigned_champ, sickness, any_cmnts)
VALUES ("oldie1","adult1",6334561230,"pune","aadhar",1,"sugar","NA");

INSERT INTO oldies (username, adult_name, contact, address, id_proof, assigned_champ, sickness, any_cmnts)
VALUES ("oldie2","adult1",6334561230,"pune","aadhar",1,"High BP","NA");

INSERT INTO oldies (username, adult_name, contact, address, id_proof, assigned_champ, sickness, any_cmnts)
VALUES ("oldie3","adult2",2308561230,"pune","aadhar",4,"Cholestrol","NA");

INSERT INTO oldies (username, adult_name, contact, address, id_proof, assigned_champ, sickness, any_cmnts)
VALUES ("oldie4","adult2",2308561230,"pune","aadhar",4,"Cholestrol and Sugar","NA");

select * from oldies;

##############################################################################################################################################


DELIMITER //
CREATE PROCEDURE SelectAllOldies(IN champ_id BIGINT)
BEGIN
	SELECT oldies.username as oldie_name, oldies.ID as oldieID, oldies.assigned_champ as assignedChamp, young_champs.username as champ_name 
    FROM oldies INNER JOIN young_champs ON oldies.assigned_champ = young_champs.ID where oldies.assigned_champ = champ_id;
END //

DELIMITER ;

	
CALL SelectAllOldies(1);
##############################################################################################################################################

DELIMITER //
CREATE PROCEDURE SelectAllchamps(IN oldie_id BIGINT)
BEGIN
	SELECT oldies.username as oldie_name, oldies.ID as oldieID, oldies.assigned_champ as assignedChamp, young_champs.username as champ_name, young_champs.contact
    FROM oldies INNER JOIN young_champs ON oldies.assigned_champ = young_champs.ID where oldies.ID = oldie_id;
END //

DELIMITER ;

	
CALL SelectAllchamps(3);








