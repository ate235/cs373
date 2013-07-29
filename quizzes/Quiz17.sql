/*
CS373: Quiz #17 (10 pts)
*/

/* -----------------------------------------------------------------------
1. What is the output of the following?
   (9 pts)

A	B	C
1	4	6
1	4	7

A	B	C
1	4	6
1	4	7
2	5	NULL

A	C	B
1	6	4
1	7	4
3	8	NULL
3	9	NULL
*/

use downing_test;

drop table if exists R;
drop table if exists S;

create table R (A int, B int);
create table S (A int, C int);

insert into R values (1, 4);
insert into R values (2, 5);

insert into S values (1, 6);
insert into S values (1, 7);
insert into S values (3, 8);
insert into S values (3, 9);

select * from R inner join S using (A);
select * from R left  join S using (A);
select * from R right join S using (A);

drop table if exists R;
drop table if exists S;

exit
