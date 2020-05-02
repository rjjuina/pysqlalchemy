CREATE TABLE user(
	id int NOT NULL AUTO_INCREMENT,
    name varchar(50),
    age int,
    address varchar(200),
    email varchar(80),
    PRIMARY KEY (id)
);

INSERT INTO user(name, age, address, email) VALUES("ROY", 30, "SINGAPORE", "roy.jia@outlook.com");


select * from user;