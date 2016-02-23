drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  text text not null
);

sqlite> CREATE TABLE main.users(
ID integer primary key autoincrement,
username text not null,
password text not null,
spID int not null,
spUserID int not null
);

INSERT INTO main.users (ID, username, password, spID, spUserID) 
VALUES (1, 'elle', '12345', 1, 11);