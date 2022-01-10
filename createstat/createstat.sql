-- 
drop view  if EXISTS  "4thmesh"."482917";
create view "4thmesh"."482917"
as
select  "L2mesh"."482917".ogc_fid,
"L2mesh"."482917".wkb_geometry, "L2mesh"."482917".code  ,
 coalesce("groupstats"."482917".count , 0 )  d5mmesh,
coalesce("groupstats"."482917".count,0)/10000.0 dratio  , 
coalesce("census2015"."4829".sousu,0) as jinko, 
coalesce("census2015"."4829".sousu,0) * coalesce("groupstats"."482917".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."482917" left outer  join  "groupstats"."482917" 
on  "L2mesh"."482917".code =  to_number("groupstats"."482917".fcode, '999999999') 
left outer join  "census2015"."4829" on 
"L2mesh"."482917".code =  to_number("census2015"."4829".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."482927";
create view "4thmesh"."482927"
as
select  "L2mesh"."482927".ogc_fid,
"L2mesh"."482927".wkb_geometry, "L2mesh"."482927".code  ,
 coalesce("groupstats"."482927".count , 0 )  d5mmesh,
coalesce("groupstats"."482927".count,0)/10000.0 dratio  , 
coalesce("census2015"."4829".sousu,0) as jinko, 
coalesce("census2015"."4829".sousu,0) * coalesce("groupstats"."482927".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."482927" left outer  join  "groupstats"."482927" 
on  "L2mesh"."482927".code =  to_number("groupstats"."482927".fcode, '999999999') 
left outer join  "census2015"."4829" on 
"L2mesh"."482927".code =  to_number("census2015"."4829".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."482937";
create view "4thmesh"."482937"
as
select  "L2mesh"."482937".ogc_fid,
"L2mesh"."482937".wkb_geometry, "L2mesh"."482937".code  ,
 coalesce("groupstats"."482937".count , 0 )  d5mmesh,
coalesce("groupstats"."482937".count,0)/10000.0 dratio  , 
coalesce("census2015"."4829".sousu,0) as jinko, 
coalesce("census2015"."4829".sousu,0) * coalesce("groupstats"."482937".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."482937" left outer  join  "groupstats"."482937" 
on  "L2mesh"."482937".code =  to_number("groupstats"."482937".fcode, '999999999') 
left outer join  "census2015"."4829" on 
"L2mesh"."482937".code =  to_number("census2015"."4829".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."482947";
create view "4thmesh"."482947"
as
select  "L2mesh"."482947".ogc_fid,
"L2mesh"."482947".wkb_geometry, "L2mesh"."482947".code  ,
 coalesce("groupstats"."482947".count , 0 )  d5mmesh,
coalesce("groupstats"."482947".count,0)/10000.0 dratio  , 
coalesce("census2015"."4829".sousu,0) as jinko, 
coalesce("census2015"."4829".sousu,0) * coalesce("groupstats"."482947".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."482947" left outer  join  "groupstats"."482947" 
on  "L2mesh"."482947".code =  to_number("groupstats"."482947".fcode, '999999999') 
left outer join  "census2015"."4829" on 
"L2mesh"."482947".code =  to_number("census2015"."4829".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483010";
create view "4thmesh"."483010"
as
select  "L2mesh"."483010".ogc_fid,
"L2mesh"."483010".wkb_geometry, "L2mesh"."483010".code  ,
 coalesce("groupstats"."483010".count , 0 )  d5mmesh,
coalesce("groupstats"."483010".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483010".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483010" left outer  join  "groupstats"."483010" 
on  "L2mesh"."483010".code =  to_number("groupstats"."483010".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483010".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483012";
create view "4thmesh"."483012"
as
select  "L2mesh"."483012".ogc_fid,
"L2mesh"."483012".wkb_geometry, "L2mesh"."483012".code  ,
 coalesce("groupstats"."483012".count , 0 )  d5mmesh,
coalesce("groupstats"."483012".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483012".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483012" left outer  join  "groupstats"."483012" 
on  "L2mesh"."483012".code =  to_number("groupstats"."483012".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483012".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483013";
create view "4thmesh"."483013"
as
select  "L2mesh"."483013".ogc_fid,
"L2mesh"."483013".wkb_geometry, "L2mesh"."483013".code  ,
 coalesce("groupstats"."483013".count , 0 )  d5mmesh,
coalesce("groupstats"."483013".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483013".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483013" left outer  join  "groupstats"."483013" 
on  "L2mesh"."483013".code =  to_number("groupstats"."483013".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483013".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483014";
create view "4thmesh"."483014"
as
select  "L2mesh"."483014".ogc_fid,
"L2mesh"."483014".wkb_geometry, "L2mesh"."483014".code  ,
 coalesce("groupstats"."483014".count , 0 )  d5mmesh,
coalesce("groupstats"."483014".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483014".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483014" left outer  join  "groupstats"."483014" 
on  "L2mesh"."483014".code =  to_number("groupstats"."483014".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483014".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483015";
create view "4thmesh"."483015"
as
select  "L2mesh"."483015".ogc_fid,
"L2mesh"."483015".wkb_geometry, "L2mesh"."483015".code  ,
 coalesce("groupstats"."483015".count , 0 )  d5mmesh,
coalesce("groupstats"."483015".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483015".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483015" left outer  join  "groupstats"."483015" 
on  "L2mesh"."483015".code =  to_number("groupstats"."483015".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483015".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483016";
create view "4thmesh"."483016"
as
select  "L2mesh"."483016".ogc_fid,
"L2mesh"."483016".wkb_geometry, "L2mesh"."483016".code  ,
 coalesce("groupstats"."483016".count , 0 )  d5mmesh,
coalesce("groupstats"."483016".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483016".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483016" left outer  join  "groupstats"."483016" 
on  "L2mesh"."483016".code =  to_number("groupstats"."483016".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483016".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483017";
create view "4thmesh"."483017"
as
select  "L2mesh"."483017".ogc_fid,
"L2mesh"."483017".wkb_geometry, "L2mesh"."483017".code  ,
 coalesce("groupstats"."483017".count , 0 )  d5mmesh,
coalesce("groupstats"."483017".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483017".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483017" left outer  join  "groupstats"."483017" 
on  "L2mesh"."483017".code =  to_number("groupstats"."483017".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483017".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483020";
create view "4thmesh"."483020"
as
select  "L2mesh"."483020".ogc_fid,
"L2mesh"."483020".wkb_geometry, "L2mesh"."483020".code  ,
 coalesce("groupstats"."483020".count , 0 )  d5mmesh,
coalesce("groupstats"."483020".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483020".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483020" left outer  join  "groupstats"."483020" 
on  "L2mesh"."483020".code =  to_number("groupstats"."483020".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483020".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483021";
create view "4thmesh"."483021"
as
select  "L2mesh"."483021".ogc_fid,
"L2mesh"."483021".wkb_geometry, "L2mesh"."483021".code  ,
 coalesce("groupstats"."483021".count , 0 )  d5mmesh,
coalesce("groupstats"."483021".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483021".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483021" left outer  join  "groupstats"."483021" 
on  "L2mesh"."483021".code =  to_number("groupstats"."483021".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483021".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483022";
create view "4thmesh"."483022"
as
select  "L2mesh"."483022".ogc_fid,
"L2mesh"."483022".wkb_geometry, "L2mesh"."483022".code  ,
 coalesce("groupstats"."483022".count , 0 )  d5mmesh,
coalesce("groupstats"."483022".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483022".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483022" left outer  join  "groupstats"."483022" 
on  "L2mesh"."483022".code =  to_number("groupstats"."483022".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483022".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483023";
create view "4thmesh"."483023"
as
select  "L2mesh"."483023".ogc_fid,
"L2mesh"."483023".wkb_geometry, "L2mesh"."483023".code  ,
 coalesce("groupstats"."483023".count , 0 )  d5mmesh,
coalesce("groupstats"."483023".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483023".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483023" left outer  join  "groupstats"."483023" 
on  "L2mesh"."483023".code =  to_number("groupstats"."483023".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483023".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483024";
create view "4thmesh"."483024"
as
select  "L2mesh"."483024".ogc_fid,
"L2mesh"."483024".wkb_geometry, "L2mesh"."483024".code  ,
 coalesce("groupstats"."483024".count , 0 )  d5mmesh,
coalesce("groupstats"."483024".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483024".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483024" left outer  join  "groupstats"."483024" 
on  "L2mesh"."483024".code =  to_number("groupstats"."483024".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483024".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483025";
create view "4thmesh"."483025"
as
select  "L2mesh"."483025".ogc_fid,
"L2mesh"."483025".wkb_geometry, "L2mesh"."483025".code  ,
 coalesce("groupstats"."483025".count , 0 )  d5mmesh,
coalesce("groupstats"."483025".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483025".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483025" left outer  join  "groupstats"."483025" 
on  "L2mesh"."483025".code =  to_number("groupstats"."483025".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483025".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483026";
create view "4thmesh"."483026"
as
select  "L2mesh"."483026".ogc_fid,
"L2mesh"."483026".wkb_geometry, "L2mesh"."483026".code  ,
 coalesce("groupstats"."483026".count , 0 )  d5mmesh,
coalesce("groupstats"."483026".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483026".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483026" left outer  join  "groupstats"."483026" 
on  "L2mesh"."483026".code =  to_number("groupstats"."483026".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483026".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483027";
create view "4thmesh"."483027"
as
select  "L2mesh"."483027".ogc_fid,
"L2mesh"."483027".wkb_geometry, "L2mesh"."483027".code  ,
 coalesce("groupstats"."483027".count , 0 )  d5mmesh,
coalesce("groupstats"."483027".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483027".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483027" left outer  join  "groupstats"."483027" 
on  "L2mesh"."483027".code =  to_number("groupstats"."483027".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483027".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483030";
create view "4thmesh"."483030"
as
select  "L2mesh"."483030".ogc_fid,
"L2mesh"."483030".wkb_geometry, "L2mesh"."483030".code  ,
 coalesce("groupstats"."483030".count , 0 )  d5mmesh,
coalesce("groupstats"."483030".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483030".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483030" left outer  join  "groupstats"."483030" 
on  "L2mesh"."483030".code =  to_number("groupstats"."483030".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483030".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483031";
create view "4thmesh"."483031"
as
select  "L2mesh"."483031".ogc_fid,
"L2mesh"."483031".wkb_geometry, "L2mesh"."483031".code  ,
 coalesce("groupstats"."483031".count , 0 )  d5mmesh,
coalesce("groupstats"."483031".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483031".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483031" left outer  join  "groupstats"."483031" 
on  "L2mesh"."483031".code =  to_number("groupstats"."483031".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483031".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483032";
create view "4thmesh"."483032"
as
select  "L2mesh"."483032".ogc_fid,
"L2mesh"."483032".wkb_geometry, "L2mesh"."483032".code  ,
 coalesce("groupstats"."483032".count , 0 )  d5mmesh,
coalesce("groupstats"."483032".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483032".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483032" left outer  join  "groupstats"."483032" 
on  "L2mesh"."483032".code =  to_number("groupstats"."483032".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483032".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483033";
create view "4thmesh"."483033"
as
select  "L2mesh"."483033".ogc_fid,
"L2mesh"."483033".wkb_geometry, "L2mesh"."483033".code  ,
 coalesce("groupstats"."483033".count , 0 )  d5mmesh,
coalesce("groupstats"."483033".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483033".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483033" left outer  join  "groupstats"."483033" 
on  "L2mesh"."483033".code =  to_number("groupstats"."483033".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483033".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483034";
create view "4thmesh"."483034"
as
select  "L2mesh"."483034".ogc_fid,
"L2mesh"."483034".wkb_geometry, "L2mesh"."483034".code  ,
 coalesce("groupstats"."483034".count , 0 )  d5mmesh,
coalesce("groupstats"."483034".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483034".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483034" left outer  join  "groupstats"."483034" 
on  "L2mesh"."483034".code =  to_number("groupstats"."483034".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483034".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483035";
create view "4thmesh"."483035"
as
select  "L2mesh"."483035".ogc_fid,
"L2mesh"."483035".wkb_geometry, "L2mesh"."483035".code  ,
 coalesce("groupstats"."483035".count , 0 )  d5mmesh,
coalesce("groupstats"."483035".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483035".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483035" left outer  join  "groupstats"."483035" 
on  "L2mesh"."483035".code =  to_number("groupstats"."483035".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483035".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483036";
create view "4thmesh"."483036"
as
select  "L2mesh"."483036".ogc_fid,
"L2mesh"."483036".wkb_geometry, "L2mesh"."483036".code  ,
 coalesce("groupstats"."483036".count , 0 )  d5mmesh,
coalesce("groupstats"."483036".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483036".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483036" left outer  join  "groupstats"."483036" 
on  "L2mesh"."483036".code =  to_number("groupstats"."483036".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483036".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483037";
create view "4thmesh"."483037"
as
select  "L2mesh"."483037".ogc_fid,
"L2mesh"."483037".wkb_geometry, "L2mesh"."483037".code  ,
 coalesce("groupstats"."483037".count , 0 )  d5mmesh,
coalesce("groupstats"."483037".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483037".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483037" left outer  join  "groupstats"."483037" 
on  "L2mesh"."483037".code =  to_number("groupstats"."483037".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483037".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483040";
create view "4thmesh"."483040"
as
select  "L2mesh"."483040".ogc_fid,
"L2mesh"."483040".wkb_geometry, "L2mesh"."483040".code  ,
 coalesce("groupstats"."483040".count , 0 )  d5mmesh,
coalesce("groupstats"."483040".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483040".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483040" left outer  join  "groupstats"."483040" 
on  "L2mesh"."483040".code =  to_number("groupstats"."483040".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483040".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483041";
create view "4thmesh"."483041"
as
select  "L2mesh"."483041".ogc_fid,
"L2mesh"."483041".wkb_geometry, "L2mesh"."483041".code  ,
 coalesce("groupstats"."483041".count , 0 )  d5mmesh,
coalesce("groupstats"."483041".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483041".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483041" left outer  join  "groupstats"."483041" 
on  "L2mesh"."483041".code =  to_number("groupstats"."483041".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483041".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483042";
create view "4thmesh"."483042"
as
select  "L2mesh"."483042".ogc_fid,
"L2mesh"."483042".wkb_geometry, "L2mesh"."483042".code  ,
 coalesce("groupstats"."483042".count , 0 )  d5mmesh,
coalesce("groupstats"."483042".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483042".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483042" left outer  join  "groupstats"."483042" 
on  "L2mesh"."483042".code =  to_number("groupstats"."483042".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483042".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483043";
create view "4thmesh"."483043"
as
select  "L2mesh"."483043".ogc_fid,
"L2mesh"."483043".wkb_geometry, "L2mesh"."483043".code  ,
 coalesce("groupstats"."483043".count , 0 )  d5mmesh,
coalesce("groupstats"."483043".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483043".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483043" left outer  join  "groupstats"."483043" 
on  "L2mesh"."483043".code =  to_number("groupstats"."483043".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483043".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483044";
create view "4thmesh"."483044"
as
select  "L2mesh"."483044".ogc_fid,
"L2mesh"."483044".wkb_geometry, "L2mesh"."483044".code  ,
 coalesce("groupstats"."483044".count , 0 )  d5mmesh,
coalesce("groupstats"."483044".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483044".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483044" left outer  join  "groupstats"."483044" 
on  "L2mesh"."483044".code =  to_number("groupstats"."483044".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483044".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483045";
create view "4thmesh"."483045"
as
select  "L2mesh"."483045".ogc_fid,
"L2mesh"."483045".wkb_geometry, "L2mesh"."483045".code  ,
 coalesce("groupstats"."483045".count , 0 )  d5mmesh,
coalesce("groupstats"."483045".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483045".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483045" left outer  join  "groupstats"."483045" 
on  "L2mesh"."483045".code =  to_number("groupstats"."483045".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483045".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483046";
create view "4thmesh"."483046"
as
select  "L2mesh"."483046".ogc_fid,
"L2mesh"."483046".wkb_geometry, "L2mesh"."483046".code  ,
 coalesce("groupstats"."483046".count , 0 )  d5mmesh,
coalesce("groupstats"."483046".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483046".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483046" left outer  join  "groupstats"."483046" 
on  "L2mesh"."483046".code =  to_number("groupstats"."483046".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483046".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483047";
create view "4thmesh"."483047"
as
select  "L2mesh"."483047".ogc_fid,
"L2mesh"."483047".wkb_geometry, "L2mesh"."483047".code  ,
 coalesce("groupstats"."483047".count , 0 )  d5mmesh,
coalesce("groupstats"."483047".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483047".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483047" left outer  join  "groupstats"."483047" 
on  "L2mesh"."483047".code =  to_number("groupstats"."483047".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483047".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483050";
create view "4thmesh"."483050"
as
select  "L2mesh"."483050".ogc_fid,
"L2mesh"."483050".wkb_geometry, "L2mesh"."483050".code  ,
 coalesce("groupstats"."483050".count , 0 )  d5mmesh,
coalesce("groupstats"."483050".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483050".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483050" left outer  join  "groupstats"."483050" 
on  "L2mesh"."483050".code =  to_number("groupstats"."483050".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483050".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483051";
create view "4thmesh"."483051"
as
select  "L2mesh"."483051".ogc_fid,
"L2mesh"."483051".wkb_geometry, "L2mesh"."483051".code  ,
 coalesce("groupstats"."483051".count , 0 )  d5mmesh,
coalesce("groupstats"."483051".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483051".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483051" left outer  join  "groupstats"."483051" 
on  "L2mesh"."483051".code =  to_number("groupstats"."483051".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483051".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483052";
create view "4thmesh"."483052"
as
select  "L2mesh"."483052".ogc_fid,
"L2mesh"."483052".wkb_geometry, "L2mesh"."483052".code  ,
 coalesce("groupstats"."483052".count , 0 )  d5mmesh,
coalesce("groupstats"."483052".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483052".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483052" left outer  join  "groupstats"."483052" 
on  "L2mesh"."483052".code =  to_number("groupstats"."483052".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483052".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483053";
create view "4thmesh"."483053"
as
select  "L2mesh"."483053".ogc_fid,
"L2mesh"."483053".wkb_geometry, "L2mesh"."483053".code  ,
 coalesce("groupstats"."483053".count , 0 )  d5mmesh,
coalesce("groupstats"."483053".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483053".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483053" left outer  join  "groupstats"."483053" 
on  "L2mesh"."483053".code =  to_number("groupstats"."483053".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483053".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483054";
create view "4thmesh"."483054"
as
select  "L2mesh"."483054".ogc_fid,
"L2mesh"."483054".wkb_geometry, "L2mesh"."483054".code  ,
 coalesce("groupstats"."483054".count , 0 )  d5mmesh,
coalesce("groupstats"."483054".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483054".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483054" left outer  join  "groupstats"."483054" 
on  "L2mesh"."483054".code =  to_number("groupstats"."483054".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483054".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483055";
create view "4thmesh"."483055"
as
select  "L2mesh"."483055".ogc_fid,
"L2mesh"."483055".wkb_geometry, "L2mesh"."483055".code  ,
 coalesce("groupstats"."483055".count , 0 )  d5mmesh,
coalesce("groupstats"."483055".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483055".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483055" left outer  join  "groupstats"."483055" 
on  "L2mesh"."483055".code =  to_number("groupstats"."483055".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483055".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483056";
create view "4thmesh"."483056"
as
select  "L2mesh"."483056".ogc_fid,
"L2mesh"."483056".wkb_geometry, "L2mesh"."483056".code  ,
 coalesce("groupstats"."483056".count , 0 )  d5mmesh,
coalesce("groupstats"."483056".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483056".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483056" left outer  join  "groupstats"."483056" 
on  "L2mesh"."483056".code =  to_number("groupstats"."483056".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483056".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483057";
create view "4thmesh"."483057"
as
select  "L2mesh"."483057".ogc_fid,
"L2mesh"."483057".wkb_geometry, "L2mesh"."483057".code  ,
 coalesce("groupstats"."483057".count , 0 )  d5mmesh,
coalesce("groupstats"."483057".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483057".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483057" left outer  join  "groupstats"."483057" 
on  "L2mesh"."483057".code =  to_number("groupstats"."483057".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483057".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483060";
create view "4thmesh"."483060"
as
select  "L2mesh"."483060".ogc_fid,
"L2mesh"."483060".wkb_geometry, "L2mesh"."483060".code  ,
 coalesce("groupstats"."483060".count , 0 )  d5mmesh,
coalesce("groupstats"."483060".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483060".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483060" left outer  join  "groupstats"."483060" 
on  "L2mesh"."483060".code =  to_number("groupstats"."483060".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483060".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483061";
create view "4thmesh"."483061"
as
select  "L2mesh"."483061".ogc_fid,
"L2mesh"."483061".wkb_geometry, "L2mesh"."483061".code  ,
 coalesce("groupstats"."483061".count , 0 )  d5mmesh,
coalesce("groupstats"."483061".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483061".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483061" left outer  join  "groupstats"."483061" 
on  "L2mesh"."483061".code =  to_number("groupstats"."483061".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483061".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483062";
create view "4thmesh"."483062"
as
select  "L2mesh"."483062".ogc_fid,
"L2mesh"."483062".wkb_geometry, "L2mesh"."483062".code  ,
 coalesce("groupstats"."483062".count , 0 )  d5mmesh,
coalesce("groupstats"."483062".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483062".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483062" left outer  join  "groupstats"."483062" 
on  "L2mesh"."483062".code =  to_number("groupstats"."483062".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483062".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483063";
create view "4thmesh"."483063"
as
select  "L2mesh"."483063".ogc_fid,
"L2mesh"."483063".wkb_geometry, "L2mesh"."483063".code  ,
 coalesce("groupstats"."483063".count , 0 )  d5mmesh,
coalesce("groupstats"."483063".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483063".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483063" left outer  join  "groupstats"."483063" 
on  "L2mesh"."483063".code =  to_number("groupstats"."483063".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483063".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483064";
create view "4thmesh"."483064"
as
select  "L2mesh"."483064".ogc_fid,
"L2mesh"."483064".wkb_geometry, "L2mesh"."483064".code  ,
 coalesce("groupstats"."483064".count , 0 )  d5mmesh,
coalesce("groupstats"."483064".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483064".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483064" left outer  join  "groupstats"."483064" 
on  "L2mesh"."483064".code =  to_number("groupstats"."483064".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483064".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483065";
create view "4thmesh"."483065"
as
select  "L2mesh"."483065".ogc_fid,
"L2mesh"."483065".wkb_geometry, "L2mesh"."483065".code  ,
 coalesce("groupstats"."483065".count , 0 )  d5mmesh,
coalesce("groupstats"."483065".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483065".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483065" left outer  join  "groupstats"."483065" 
on  "L2mesh"."483065".code =  to_number("groupstats"."483065".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483065".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483066";
create view "4thmesh"."483066"
as
select  "L2mesh"."483066".ogc_fid,
"L2mesh"."483066".wkb_geometry, "L2mesh"."483066".code  ,
 coalesce("groupstats"."483066".count , 0 )  d5mmesh,
coalesce("groupstats"."483066".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483066".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483066" left outer  join  "groupstats"."483066" 
on  "L2mesh"."483066".code =  to_number("groupstats"."483066".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483066".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483067";
create view "4thmesh"."483067"
as
select  "L2mesh"."483067".ogc_fid,
"L2mesh"."483067".wkb_geometry, "L2mesh"."483067".code  ,
 coalesce("groupstats"."483067".count , 0 )  d5mmesh,
coalesce("groupstats"."483067".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483067".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483067" left outer  join  "groupstats"."483067" 
on  "L2mesh"."483067".code =  to_number("groupstats"."483067".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483067".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483072";
create view "4thmesh"."483072"
as
select  "L2mesh"."483072".ogc_fid,
"L2mesh"."483072".wkb_geometry, "L2mesh"."483072".code  ,
 coalesce("groupstats"."483072".count , 0 )  d5mmesh,
coalesce("groupstats"."483072".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483072".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483072" left outer  join  "groupstats"."483072" 
on  "L2mesh"."483072".code =  to_number("groupstats"."483072".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483072".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483073";
create view "4thmesh"."483073"
as
select  "L2mesh"."483073".ogc_fid,
"L2mesh"."483073".wkb_geometry, "L2mesh"."483073".code  ,
 coalesce("groupstats"."483073".count , 0 )  d5mmesh,
coalesce("groupstats"."483073".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483073".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483073" left outer  join  "groupstats"."483073" 
on  "L2mesh"."483073".code =  to_number("groupstats"."483073".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483073".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483074";
create view "4thmesh"."483074"
as
select  "L2mesh"."483074".ogc_fid,
"L2mesh"."483074".wkb_geometry, "L2mesh"."483074".code  ,
 coalesce("groupstats"."483074".count , 0 )  d5mmesh,
coalesce("groupstats"."483074".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483074".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483074" left outer  join  "groupstats"."483074" 
on  "L2mesh"."483074".code =  to_number("groupstats"."483074".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483074".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483075";
create view "4thmesh"."483075"
as
select  "L2mesh"."483075".ogc_fid,
"L2mesh"."483075".wkb_geometry, "L2mesh"."483075".code  ,
 coalesce("groupstats"."483075".count , 0 )  d5mmesh,
coalesce("groupstats"."483075".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483075".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483075" left outer  join  "groupstats"."483075" 
on  "L2mesh"."483075".code =  to_number("groupstats"."483075".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483075".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483076";
create view "4thmesh"."483076"
as
select  "L2mesh"."483076".ogc_fid,
"L2mesh"."483076".wkb_geometry, "L2mesh"."483076".code  ,
 coalesce("groupstats"."483076".count , 0 )  d5mmesh,
coalesce("groupstats"."483076".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483076".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483076" left outer  join  "groupstats"."483076" 
on  "L2mesh"."483076".code =  to_number("groupstats"."483076".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483076".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483077";
create view "4thmesh"."483077"
as
select  "L2mesh"."483077".ogc_fid,
"L2mesh"."483077".wkb_geometry, "L2mesh"."483077".code  ,
 coalesce("groupstats"."483077".count , 0 )  d5mmesh,
coalesce("groupstats"."483077".count,0)/10000.0 dratio  , 
coalesce("census2015"."4830".sousu,0) as jinko, 
coalesce("census2015"."4830".sousu,0) * coalesce("groupstats"."483077".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483077" left outer  join  "groupstats"."483077" 
on  "L2mesh"."483077".code =  to_number("groupstats"."483077".fcode, '999999999') 
left outer join  "census2015"."4830" on 
"L2mesh"."483077".code =  to_number("census2015"."4830".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483110";
create view "4thmesh"."483110"
as
select  "L2mesh"."483110".ogc_fid,
"L2mesh"."483110".wkb_geometry, "L2mesh"."483110".code  ,
 coalesce("groupstats"."483110".count , 0 )  d5mmesh,
coalesce("groupstats"."483110".count,0)/10000.0 dratio  , 
coalesce("census2015"."4831".sousu,0) as jinko, 
coalesce("census2015"."4831".sousu,0) * coalesce("groupstats"."483110".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483110" left outer  join  "groupstats"."483110" 
on  "L2mesh"."483110".code =  to_number("groupstats"."483110".fcode, '999999999') 
left outer join  "census2015"."4831" on 
"L2mesh"."483110".code =  to_number("census2015"."4831".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483120";
create view "4thmesh"."483120"
as
select  "L2mesh"."483120".ogc_fid,
"L2mesh"."483120".wkb_geometry, "L2mesh"."483120".code  ,
 coalesce("groupstats"."483120".count , 0 )  d5mmesh,
coalesce("groupstats"."483120".count,0)/10000.0 dratio  , 
coalesce("census2015"."4831".sousu,0) as jinko, 
coalesce("census2015"."4831".sousu,0) * coalesce("groupstats"."483120".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483120" left outer  join  "groupstats"."483120" 
on  "L2mesh"."483120".code =  to_number("groupstats"."483120".fcode, '999999999') 
left outer join  "census2015"."4831" on 
"L2mesh"."483120".code =  to_number("census2015"."4831".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483130";
create view "4thmesh"."483130"
as
select  "L2mesh"."483130".ogc_fid,
"L2mesh"."483130".wkb_geometry, "L2mesh"."483130".code  ,
 coalesce("groupstats"."483130".count , 0 )  d5mmesh,
coalesce("groupstats"."483130".count,0)/10000.0 dratio  , 
coalesce("census2015"."4831".sousu,0) as jinko, 
coalesce("census2015"."4831".sousu,0) * coalesce("groupstats"."483130".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483130" left outer  join  "groupstats"."483130" 
on  "L2mesh"."483130".code =  to_number("groupstats"."483130".fcode, '999999999') 
left outer join  "census2015"."4831" on 
"L2mesh"."483130".code =  to_number("census2015"."4831".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483140";
create view "4thmesh"."483140"
as
select  "L2mesh"."483140".ogc_fid,
"L2mesh"."483140".wkb_geometry, "L2mesh"."483140".code  ,
 coalesce("groupstats"."483140".count , 0 )  d5mmesh,
coalesce("groupstats"."483140".count,0)/10000.0 dratio  , 
coalesce("census2015"."4831".sousu,0) as jinko, 
coalesce("census2015"."4831".sousu,0) * coalesce("groupstats"."483140".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483140" left outer  join  "groupstats"."483140" 
on  "L2mesh"."483140".code =  to_number("groupstats"."483140".fcode, '999999999') 
left outer join  "census2015"."4831" on 
"L2mesh"."483140".code =  to_number("census2015"."4831".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483150";
create view "4thmesh"."483150"
as
select  "L2mesh"."483150".ogc_fid,
"L2mesh"."483150".wkb_geometry, "L2mesh"."483150".code  ,
 coalesce("groupstats"."483150".count , 0 )  d5mmesh,
coalesce("groupstats"."483150".count,0)/10000.0 dratio  , 
coalesce("census2015"."4831".sousu,0) as jinko, 
coalesce("census2015"."4831".sousu,0) * coalesce("groupstats"."483150".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483150" left outer  join  "groupstats"."483150" 
on  "L2mesh"."483150".code =  to_number("groupstats"."483150".fcode, '999999999') 
left outer join  "census2015"."4831" on 
"L2mesh"."483150".code =  to_number("census2015"."4831".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483160";
create view "4thmesh"."483160"
as
select  "L2mesh"."483160".ogc_fid,
"L2mesh"."483160".wkb_geometry, "L2mesh"."483160".code  ,
 coalesce("groupstats"."483160".count , 0 )  d5mmesh,
coalesce("groupstats"."483160".count,0)/10000.0 dratio  , 
coalesce("census2015"."4831".sousu,0) as jinko, 
coalesce("census2015"."4831".sousu,0) * coalesce("groupstats"."483160".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483160" left outer  join  "groupstats"."483160" 
on  "L2mesh"."483160".code =  to_number("groupstats"."483160".fcode, '999999999') 
left outer join  "census2015"."4831" on 
"L2mesh"."483160".code =  to_number("census2015"."4831".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483170";
create view "4thmesh"."483170"
as
select  "L2mesh"."483170".ogc_fid,
"L2mesh"."483170".wkb_geometry, "L2mesh"."483170".code  ,
 coalesce("groupstats"."483170".count , 0 )  d5mmesh,
coalesce("groupstats"."483170".count,0)/10000.0 dratio  , 
coalesce("census2015"."4831".sousu,0) as jinko, 
coalesce("census2015"."4831".sousu,0) * coalesce("groupstats"."483170".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483170" left outer  join  "groupstats"."483170" 
on  "L2mesh"."483170".code =  to_number("groupstats"."483170".fcode, '999999999') 
left outer join  "census2015"."4831" on 
"L2mesh"."483170".code =  to_number("census2015"."4831".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."483171";
create view "4thmesh"."483171"
as
select  "L2mesh"."483171".ogc_fid,
"L2mesh"."483171".wkb_geometry, "L2mesh"."483171".code  ,
 coalesce("groupstats"."483171".count , 0 )  d5mmesh,
coalesce("groupstats"."483171".count,0)/10000.0 dratio  , 
coalesce("census2015"."4831".sousu,0) as jinko, 
coalesce("census2015"."4831".sousu,0) * coalesce("groupstats"."483171".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."483171" left outer  join  "groupstats"."483171" 
on  "L2mesh"."483171".code =  to_number("groupstats"."483171".fcode, '999999999') 
left outer join  "census2015"."4831" on 
"L2mesh"."483171".code =  to_number("census2015"."4831".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493004";
create view "4thmesh"."493004"
as
select  "L2mesh"."493004".ogc_fid,
"L2mesh"."493004".wkb_geometry, "L2mesh"."493004".code  ,
 coalesce("groupstats"."493004".count , 0 )  d5mmesh,
coalesce("groupstats"."493004".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493004".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493004" left outer  join  "groupstats"."493004" 
on  "L2mesh"."493004".code =  to_number("groupstats"."493004".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493004".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493005";
create view "4thmesh"."493005"
as
select  "L2mesh"."493005".ogc_fid,
"L2mesh"."493005".wkb_geometry, "L2mesh"."493005".code  ,
 coalesce("groupstats"."493005".count , 0 )  d5mmesh,
coalesce("groupstats"."493005".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493005".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493005" left outer  join  "groupstats"."493005" 
on  "L2mesh"."493005".code =  to_number("groupstats"."493005".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493005".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493006";
create view "4thmesh"."493006"
as
select  "L2mesh"."493006".ogc_fid,
"L2mesh"."493006".wkb_geometry, "L2mesh"."493006".code  ,
 coalesce("groupstats"."493006".count , 0 )  d5mmesh,
coalesce("groupstats"."493006".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493006".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493006" left outer  join  "groupstats"."493006" 
on  "L2mesh"."493006".code =  to_number("groupstats"."493006".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493006".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493007";
create view "4thmesh"."493007"
as
select  "L2mesh"."493007".ogc_fid,
"L2mesh"."493007".wkb_geometry, "L2mesh"."493007".code  ,
 coalesce("groupstats"."493007".count , 0 )  d5mmesh,
coalesce("groupstats"."493007".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493007".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493007" left outer  join  "groupstats"."493007" 
on  "L2mesh"."493007".code =  to_number("groupstats"."493007".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493007".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493014";
create view "4thmesh"."493014"
as
select  "L2mesh"."493014".ogc_fid,
"L2mesh"."493014".wkb_geometry, "L2mesh"."493014".code  ,
 coalesce("groupstats"."493014".count , 0 )  d5mmesh,
coalesce("groupstats"."493014".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493014".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493014" left outer  join  "groupstats"."493014" 
on  "L2mesh"."493014".code =  to_number("groupstats"."493014".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493014".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493015";
create view "4thmesh"."493015"
as
select  "L2mesh"."493015".ogc_fid,
"L2mesh"."493015".wkb_geometry, "L2mesh"."493015".code  ,
 coalesce("groupstats"."493015".count , 0 )  d5mmesh,
coalesce("groupstats"."493015".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493015".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493015" left outer  join  "groupstats"."493015" 
on  "L2mesh"."493015".code =  to_number("groupstats"."493015".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493015".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493016";
create view "4thmesh"."493016"
as
select  "L2mesh"."493016".ogc_fid,
"L2mesh"."493016".wkb_geometry, "L2mesh"."493016".code  ,
 coalesce("groupstats"."493016".count , 0 )  d5mmesh,
coalesce("groupstats"."493016".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493016".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493016" left outer  join  "groupstats"."493016" 
on  "L2mesh"."493016".code =  to_number("groupstats"."493016".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493016".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493017";
create view "4thmesh"."493017"
as
select  "L2mesh"."493017".ogc_fid,
"L2mesh"."493017".wkb_geometry, "L2mesh"."493017".code  ,
 coalesce("groupstats"."493017".count , 0 )  d5mmesh,
coalesce("groupstats"."493017".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493017".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493017" left outer  join  "groupstats"."493017" 
on  "L2mesh"."493017".code =  to_number("groupstats"."493017".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493017".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493023";
create view "4thmesh"."493023"
as
select  "L2mesh"."493023".ogc_fid,
"L2mesh"."493023".wkb_geometry, "L2mesh"."493023".code  ,
 coalesce("groupstats"."493023".count , 0 )  d5mmesh,
coalesce("groupstats"."493023".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493023".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493023" left outer  join  "groupstats"."493023" 
on  "L2mesh"."493023".code =  to_number("groupstats"."493023".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493023".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493024";
create view "4thmesh"."493024"
as
select  "L2mesh"."493024".ogc_fid,
"L2mesh"."493024".wkb_geometry, "L2mesh"."493024".code  ,
 coalesce("groupstats"."493024".count , 0 )  d5mmesh,
coalesce("groupstats"."493024".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493024".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493024" left outer  join  "groupstats"."493024" 
on  "L2mesh"."493024".code =  to_number("groupstats"."493024".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493024".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493025";
create view "4thmesh"."493025"
as
select  "L2mesh"."493025".ogc_fid,
"L2mesh"."493025".wkb_geometry, "L2mesh"."493025".code  ,
 coalesce("groupstats"."493025".count , 0 )  d5mmesh,
coalesce("groupstats"."493025".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493025".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493025" left outer  join  "groupstats"."493025" 
on  "L2mesh"."493025".code =  to_number("groupstats"."493025".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493025".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493026";
create view "4thmesh"."493026"
as
select  "L2mesh"."493026".ogc_fid,
"L2mesh"."493026".wkb_geometry, "L2mesh"."493026".code  ,
 coalesce("groupstats"."493026".count , 0 )  d5mmesh,
coalesce("groupstats"."493026".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493026".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493026" left outer  join  "groupstats"."493026" 
on  "L2mesh"."493026".code =  to_number("groupstats"."493026".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493026".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493027";
create view "4thmesh"."493027"
as
select  "L2mesh"."493027".ogc_fid,
"L2mesh"."493027".wkb_geometry, "L2mesh"."493027".code  ,
 coalesce("groupstats"."493027".count , 0 )  d5mmesh,
coalesce("groupstats"."493027".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493027".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493027" left outer  join  "groupstats"."493027" 
on  "L2mesh"."493027".code =  to_number("groupstats"."493027".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493027".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493033";
create view "4thmesh"."493033"
as
select  "L2mesh"."493033".ogc_fid,
"L2mesh"."493033".wkb_geometry, "L2mesh"."493033".code  ,
 coalesce("groupstats"."493033".count , 0 )  d5mmesh,
coalesce("groupstats"."493033".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493033".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493033" left outer  join  "groupstats"."493033" 
on  "L2mesh"."493033".code =  to_number("groupstats"."493033".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493033".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493034";
create view "4thmesh"."493034"
as
select  "L2mesh"."493034".ogc_fid,
"L2mesh"."493034".wkb_geometry, "L2mesh"."493034".code  ,
 coalesce("groupstats"."493034".count , 0 )  d5mmesh,
coalesce("groupstats"."493034".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493034".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493034" left outer  join  "groupstats"."493034" 
on  "L2mesh"."493034".code =  to_number("groupstats"."493034".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493034".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493035";
create view "4thmesh"."493035"
as
select  "L2mesh"."493035".ogc_fid,
"L2mesh"."493035".wkb_geometry, "L2mesh"."493035".code  ,
 coalesce("groupstats"."493035".count , 0 )  d5mmesh,
coalesce("groupstats"."493035".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493035".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493035" left outer  join  "groupstats"."493035" 
on  "L2mesh"."493035".code =  to_number("groupstats"."493035".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493035".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493036";
create view "4thmesh"."493036"
as
select  "L2mesh"."493036".ogc_fid,
"L2mesh"."493036".wkb_geometry, "L2mesh"."493036".code  ,
 coalesce("groupstats"."493036".count , 0 )  d5mmesh,
coalesce("groupstats"."493036".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493036".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493036" left outer  join  "groupstats"."493036" 
on  "L2mesh"."493036".code =  to_number("groupstats"."493036".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493036".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493037";
create view "4thmesh"."493037"
as
select  "L2mesh"."493037".ogc_fid,
"L2mesh"."493037".wkb_geometry, "L2mesh"."493037".code  ,
 coalesce("groupstats"."493037".count , 0 )  d5mmesh,
coalesce("groupstats"."493037".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493037".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493037" left outer  join  "groupstats"."493037" 
on  "L2mesh"."493037".code =  to_number("groupstats"."493037".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493037".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493043";
create view "4thmesh"."493043"
as
select  "L2mesh"."493043".ogc_fid,
"L2mesh"."493043".wkb_geometry, "L2mesh"."493043".code  ,
 coalesce("groupstats"."493043".count , 0 )  d5mmesh,
coalesce("groupstats"."493043".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493043".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493043" left outer  join  "groupstats"."493043" 
on  "L2mesh"."493043".code =  to_number("groupstats"."493043".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493043".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493044";
create view "4thmesh"."493044"
as
select  "L2mesh"."493044".ogc_fid,
"L2mesh"."493044".wkb_geometry, "L2mesh"."493044".code  ,
 coalesce("groupstats"."493044".count , 0 )  d5mmesh,
coalesce("groupstats"."493044".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493044".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493044" left outer  join  "groupstats"."493044" 
on  "L2mesh"."493044".code =  to_number("groupstats"."493044".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493044".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493045";
create view "4thmesh"."493045"
as
select  "L2mesh"."493045".ogc_fid,
"L2mesh"."493045".wkb_geometry, "L2mesh"."493045".code  ,
 coalesce("groupstats"."493045".count , 0 )  d5mmesh,
coalesce("groupstats"."493045".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493045".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493045" left outer  join  "groupstats"."493045" 
on  "L2mesh"."493045".code =  to_number("groupstats"."493045".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493045".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493046";
create view "4thmesh"."493046"
as
select  "L2mesh"."493046".ogc_fid,
"L2mesh"."493046".wkb_geometry, "L2mesh"."493046".code  ,
 coalesce("groupstats"."493046".count , 0 )  d5mmesh,
coalesce("groupstats"."493046".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493046".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493046" left outer  join  "groupstats"."493046" 
on  "L2mesh"."493046".code =  to_number("groupstats"."493046".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493046".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493047";
create view "4thmesh"."493047"
as
select  "L2mesh"."493047".ogc_fid,
"L2mesh"."493047".wkb_geometry, "L2mesh"."493047".code  ,
 coalesce("groupstats"."493047".count , 0 )  d5mmesh,
coalesce("groupstats"."493047".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493047".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493047" left outer  join  "groupstats"."493047" 
on  "L2mesh"."493047".code =  to_number("groupstats"."493047".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493047".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493054";
create view "4thmesh"."493054"
as
select  "L2mesh"."493054".ogc_fid,
"L2mesh"."493054".wkb_geometry, "L2mesh"."493054".code  ,
 coalesce("groupstats"."493054".count , 0 )  d5mmesh,
coalesce("groupstats"."493054".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493054".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493054" left outer  join  "groupstats"."493054" 
on  "L2mesh"."493054".code =  to_number("groupstats"."493054".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493054".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493055";
create view "4thmesh"."493055"
as
select  "L2mesh"."493055".ogc_fid,
"L2mesh"."493055".wkb_geometry, "L2mesh"."493055".code  ,
 coalesce("groupstats"."493055".count , 0 )  d5mmesh,
coalesce("groupstats"."493055".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493055".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493055" left outer  join  "groupstats"."493055" 
on  "L2mesh"."493055".code =  to_number("groupstats"."493055".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493055".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493056";
create view "4thmesh"."493056"
as
select  "L2mesh"."493056".ogc_fid,
"L2mesh"."493056".wkb_geometry, "L2mesh"."493056".code  ,
 coalesce("groupstats"."493056".count , 0 )  d5mmesh,
coalesce("groupstats"."493056".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493056".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493056" left outer  join  "groupstats"."493056" 
on  "L2mesh"."493056".code =  to_number("groupstats"."493056".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493056".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493057";
create view "4thmesh"."493057"
as
select  "L2mesh"."493057".ogc_fid,
"L2mesh"."493057".wkb_geometry, "L2mesh"."493057".code  ,
 coalesce("groupstats"."493057".count , 0 )  d5mmesh,
coalesce("groupstats"."493057".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493057".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493057" left outer  join  "groupstats"."493057" 
on  "L2mesh"."493057".code =  to_number("groupstats"."493057".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493057".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493065";
create view "4thmesh"."493065"
as
select  "L2mesh"."493065".ogc_fid,
"L2mesh"."493065".wkb_geometry, "L2mesh"."493065".code  ,
 coalesce("groupstats"."493065".count , 0 )  d5mmesh,
coalesce("groupstats"."493065".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493065".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493065" left outer  join  "groupstats"."493065" 
on  "L2mesh"."493065".code =  to_number("groupstats"."493065".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493065".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493067";
create view "4thmesh"."493067"
as
select  "L2mesh"."493067".ogc_fid,
"L2mesh"."493067".wkb_geometry, "L2mesh"."493067".code  ,
 coalesce("groupstats"."493067".count , 0 )  d5mmesh,
coalesce("groupstats"."493067".count,0)/10000.0 dratio  , 
coalesce("census2015"."4930".sousu,0) as jinko, 
coalesce("census2015"."4930".sousu,0) * coalesce("groupstats"."493067".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493067" left outer  join  "groupstats"."493067" 
on  "L2mesh"."493067".code =  to_number("groupstats"."493067".fcode, '999999999') 
left outer join  "census2015"."4930" on 
"L2mesh"."493067".code =  to_number("census2015"."4930".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493100";
create view "4thmesh"."493100"
as
select  "L2mesh"."493100".ogc_fid,
"L2mesh"."493100".wkb_geometry, "L2mesh"."493100".code  ,
 coalesce("groupstats"."493100".count , 0 )  d5mmesh,
coalesce("groupstats"."493100".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493100".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493100" left outer  join  "groupstats"."493100" 
on  "L2mesh"."493100".code =  to_number("groupstats"."493100".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493100".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493101";
create view "4thmesh"."493101"
as
select  "L2mesh"."493101".ogc_fid,
"L2mesh"."493101".wkb_geometry, "L2mesh"."493101".code  ,
 coalesce("groupstats"."493101".count , 0 )  d5mmesh,
coalesce("groupstats"."493101".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493101".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493101" left outer  join  "groupstats"."493101" 
on  "L2mesh"."493101".code =  to_number("groupstats"."493101".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493101".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493110";
create view "4thmesh"."493110"
as
select  "L2mesh"."493110".ogc_fid,
"L2mesh"."493110".wkb_geometry, "L2mesh"."493110".code  ,
 coalesce("groupstats"."493110".count , 0 )  d5mmesh,
coalesce("groupstats"."493110".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493110".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493110" left outer  join  "groupstats"."493110" 
on  "L2mesh"."493110".code =  to_number("groupstats"."493110".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493110".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493111";
create view "4thmesh"."493111"
as
select  "L2mesh"."493111".ogc_fid,
"L2mesh"."493111".wkb_geometry, "L2mesh"."493111".code  ,
 coalesce("groupstats"."493111".count , 0 )  d5mmesh,
coalesce("groupstats"."493111".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493111".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493111" left outer  join  "groupstats"."493111" 
on  "L2mesh"."493111".code =  to_number("groupstats"."493111".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493111".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493112";
create view "4thmesh"."493112"
as
select  "L2mesh"."493112".ogc_fid,
"L2mesh"."493112".wkb_geometry, "L2mesh"."493112".code  ,
 coalesce("groupstats"."493112".count , 0 )  d5mmesh,
coalesce("groupstats"."493112".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493112".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493112" left outer  join  "groupstats"."493112" 
on  "L2mesh"."493112".code =  to_number("groupstats"."493112".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493112".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493120";
create view "4thmesh"."493120"
as
select  "L2mesh"."493120".ogc_fid,
"L2mesh"."493120".wkb_geometry, "L2mesh"."493120".code  ,
 coalesce("groupstats"."493120".count , 0 )  d5mmesh,
coalesce("groupstats"."493120".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493120".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493120" left outer  join  "groupstats"."493120" 
on  "L2mesh"."493120".code =  to_number("groupstats"."493120".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493120".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493121";
create view "4thmesh"."493121"
as
select  "L2mesh"."493121".ogc_fid,
"L2mesh"."493121".wkb_geometry, "L2mesh"."493121".code  ,
 coalesce("groupstats"."493121".count , 0 )  d5mmesh,
coalesce("groupstats"."493121".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493121".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493121" left outer  join  "groupstats"."493121" 
on  "L2mesh"."493121".code =  to_number("groupstats"."493121".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493121".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493122";
create view "4thmesh"."493122"
as
select  "L2mesh"."493122".ogc_fid,
"L2mesh"."493122".wkb_geometry, "L2mesh"."493122".code  ,
 coalesce("groupstats"."493122".count , 0 )  d5mmesh,
coalesce("groupstats"."493122".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493122".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493122" left outer  join  "groupstats"."493122" 
on  "L2mesh"."493122".code =  to_number("groupstats"."493122".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493122".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493130";
create view "4thmesh"."493130"
as
select  "L2mesh"."493130".ogc_fid,
"L2mesh"."493130".wkb_geometry, "L2mesh"."493130".code  ,
 coalesce("groupstats"."493130".count , 0 )  d5mmesh,
coalesce("groupstats"."493130".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493130".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493130" left outer  join  "groupstats"."493130" 
on  "L2mesh"."493130".code =  to_number("groupstats"."493130".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493130".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493131";
create view "4thmesh"."493131"
as
select  "L2mesh"."493131".ogc_fid,
"L2mesh"."493131".wkb_geometry, "L2mesh"."493131".code  ,
 coalesce("groupstats"."493131".count , 0 )  d5mmesh,
coalesce("groupstats"."493131".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493131".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493131" left outer  join  "groupstats"."493131" 
on  "L2mesh"."493131".code =  to_number("groupstats"."493131".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493131".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493132";
create view "4thmesh"."493132"
as
select  "L2mesh"."493132".ogc_fid,
"L2mesh"."493132".wkb_geometry, "L2mesh"."493132".code  ,
 coalesce("groupstats"."493132".count , 0 )  d5mmesh,
coalesce("groupstats"."493132".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493132".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493132" left outer  join  "groupstats"."493132" 
on  "L2mesh"."493132".code =  to_number("groupstats"."493132".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493132".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493140";
create view "4thmesh"."493140"
as
select  "L2mesh"."493140".ogc_fid,
"L2mesh"."493140".wkb_geometry, "L2mesh"."493140".code  ,
 coalesce("groupstats"."493140".count , 0 )  d5mmesh,
coalesce("groupstats"."493140".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493140".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493140" left outer  join  "groupstats"."493140" 
on  "L2mesh"."493140".code =  to_number("groupstats"."493140".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493140".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493141";
create view "4thmesh"."493141"
as
select  "L2mesh"."493141".ogc_fid,
"L2mesh"."493141".wkb_geometry, "L2mesh"."493141".code  ,
 coalesce("groupstats"."493141".count , 0 )  d5mmesh,
coalesce("groupstats"."493141".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493141".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493141" left outer  join  "groupstats"."493141" 
on  "L2mesh"."493141".code =  to_number("groupstats"."493141".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493141".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493150";
create view "4thmesh"."493150"
as
select  "L2mesh"."493150".ogc_fid,
"L2mesh"."493150".wkb_geometry, "L2mesh"."493150".code  ,
 coalesce("groupstats"."493150".count , 0 )  d5mmesh,
coalesce("groupstats"."493150".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493150".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493150" left outer  join  "groupstats"."493150" 
on  "L2mesh"."493150".code =  to_number("groupstats"."493150".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493150".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493151";
create view "4thmesh"."493151"
as
select  "L2mesh"."493151".ogc_fid,
"L2mesh"."493151".wkb_geometry, "L2mesh"."493151".code  ,
 coalesce("groupstats"."493151".count , 0 )  d5mmesh,
coalesce("groupstats"."493151".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493151".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493151" left outer  join  "groupstats"."493151" 
on  "L2mesh"."493151".code =  to_number("groupstats"."493151".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493151".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493160";
create view "4thmesh"."493160"
as
select  "L2mesh"."493160".ogc_fid,
"L2mesh"."493160".wkb_geometry, "L2mesh"."493160".code  ,
 coalesce("groupstats"."493160".count , 0 )  d5mmesh,
coalesce("groupstats"."493160".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493160".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493160" left outer  join  "groupstats"."493160" 
on  "L2mesh"."493160".code =  to_number("groupstats"."493160".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493160".code =  to_number("census2015"."4931".key_code, '999999999') ;
-- 
drop view  if EXISTS  "4thmesh"."493161";
create view "4thmesh"."493161"
as
select  "L2mesh"."493161".ogc_fid,
"L2mesh"."493161".wkb_geometry, "L2mesh"."493161".code  ,
 coalesce("groupstats"."493161".count , 0 )  d5mmesh,
coalesce("groupstats"."493161".count,0)/10000.0 dratio  , 
coalesce("census2015"."4931".sousu,0) as jinko, 
coalesce("census2015"."4931".sousu,0) * coalesce("groupstats"."493161".count,0)/10000.0 soutei_jinko 
from    "L2mesh"."493161" left outer  join  "groupstats"."493161" 
on  "L2mesh"."493161".code =  to_number("groupstats"."493161".fcode, '999999999') 
left outer join  "census2015"."4931" on 
"L2mesh"."493161".code =  to_number("census2015"."4931".key_code, '999999999') ;
