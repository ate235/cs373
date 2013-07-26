/*
CS373: Quiz #16 (10 pts)
*/

/* -----------------------------------------------------------------------
1. What is the output of the following?
   (9 pts)

A   B
1   1
2   1
1   2
2   2

A   B
1   1
2   1
1   2
2   2

A   A
1   8
2   8
1   9
2   9

<empty>

A   A
1   1
2   1
1   2
2   2

A
1
2
*/

use downing_test;

drop table if exists R;
drop table if exists S;
drop table if exists T;

create table R (A int);
create table S (B int);
create table T (A int);

insert into R values (1);
insert into R values (2);

insert into S values (1);
insert into S values (2);

insert into T values (8);
insert into T values (9);

select * from R cross   join S;
select * from R natural join S;

select * from R cross   join T;
select * from R natural join T;

select * from R as R1 cross   join R as R2;
select * from R as R1 natural join R as R2;

drop table if exists R;
drop table if exists S;
drop table if exists T;

exit
