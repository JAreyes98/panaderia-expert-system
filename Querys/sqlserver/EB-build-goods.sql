use Pastelerķa;
go

create table goods(
id int primary key not null,
flavour varchar(20),
dish varchar(15),
price float,
typeDish varchar(15)
);
go

insert into goods values (0,'Chocolate','Cake',8.95,'Food');
insert into goods values (1,'Lemon','Cake',8.95,'Food');
insert into goods values (2,'Casino','Cake',15.95,'Food');
insert into goods values (3,'Opera','Cake',15.95,'Food');
insert into goods values (4,'Strawberry','Cake',11.95,'Food');
insert into goods values (5,'Truffle','Cake',15.95,'Food');
insert into goods values (6,'Chocolate','Eclair',3.25,'Food');
insert into goods values (7,'Coffee','Eclair',3.5,'Food');
insert into goods values (8,'Vanilla','Eclair',3.25,'Food');
insert into goods values (9,'Napoleon','Cake',13.49,'Food');
insert into goods values (10,'Almond','Tart',3.75,'Food');
insert into goods values (11,'Apple','Pie',5.25,'Food');
insert into goods values (12,'Apple','Tart',3.25,'Food');
insert into goods values (13,'Apricot','Tart',3.25,'Food');
insert into goods values (14,'Berry','Tart',3.25,'Food');
insert into goods values (15,'Blackberry','Tart',3.25,'Food');
insert into goods values (16,'Blueberry','Tart',3.25,'Food');
insert into goods values (17,'Chocolate','Tart',3.75,'Food');
insert into goods values (18,'Cherry','Tart',3.25,'Food');
insert into goods values (19,'Lemon','Tart',3.25,'Food');
insert into goods values (20,'Pecan','Tart',3.75,'Food');
insert into goods values (21,'Ganache','Cookie',1.15,'Food');
insert into goods values (22,'Gongolais','Cookie',1.15,'Food');
insert into goods values (23,'Raspberry','Cookie',1.09,'Food');
insert into goods values (24,'Lemon','Cookie',0.79,'Food');
insert into goods values (25,'Chocolate','Meringue',1.25,'Food');
insert into goods values (26,'Vanilla','Meringue',1.15,'Food');
insert into goods values (27,'Marzipan','Cookie',1.25,'Food');
insert into goods values (28,'Tuile','Cookie',1.25,'Food');
insert into goods values (29,'Walnut','Cookie',0.79,'Food');
insert into goods values (30,'Almond','Croissant',1.45,'Food');
insert into goods values (31,'Apple','Croissant',1.45,'Food');
insert into goods values (32,'Apricot','Croissant',1.45,'Food');
insert into goods values (33,'Cheese','Croissant',1.75,'Food');
insert into goods values (34,'Chocolate','Croissant',1.75,'Food');
insert into goods values (35,'Apricot','Danish',1.15,'Food');
insert into goods values (36,'Apple','Danish',1.15,'Food');
insert into goods values (37,'Almond','Twist',1.15,'Food');
insert into goods values (38,'Almond','Bear Claw',1.95,'Food');
insert into goods values (39,'Blueberry','Danish',1.15,'Food');
insert into goods values (40,'Lemon','Lemonade',3.25,'Drink');
insert into goods values (41,'Raspberry','Lemonade',3.25,'Drink');
insert into goods values (42,'Orange','Juice',2.75,'Drink');
insert into goods values (43,'Green','Tea',1.85,'Drink');
insert into goods values (44,'Bottled','Water',1.80,'Drink');
insert into goods values (45,'Hot','Coffee',2.15,'Drink');
insert into goods values (46,'Chocolate','Coffee',2.45,'Drink');
insert into goods values (47,'Vanilla','Frappuccino',3.85,'Drink');
insert into goods values (48,'Cherry','Soda',1.29,'Drink');
insert into goods values (49,'Single','Espresso',1.85,'Drink');
