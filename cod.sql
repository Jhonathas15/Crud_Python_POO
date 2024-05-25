create database banco;
create table cliente(
	id int primary key auto_increment,
    nome varchar(100), 
    senha varchar(20),
    email varchar(50)
);