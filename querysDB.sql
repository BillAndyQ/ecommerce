CREATE TABLE producto(
	id serial primary key,
	nombre varchar(200) not null
);

INSERT INTO producto (nombre) VALUES ('Producto A');
INSERT INTO producto (nombre) VALUES ('Producto B');
INSERT INTO producto (nombre) VALUES ('Producto C');
INSERT INTO producto (nombre) VALUES ('Producto D');
INSERT INTO producto (nombre) VALUES ('Producto E');
INSERT INTO producto (nombre) VALUES ('Producto F');
INSERT INTO producto (nombre) VALUES ('Producto G');
INSERT INTO producto (nombre) VALUES ('Producto H');
INSERT INTO producto (nombre) VALUES ('Producto I');
INSERT INTO producto (nombre) VALUES ('Producto J');

select * from producto;
