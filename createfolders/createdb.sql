-- Database: postgis_31_sample

--- DROP DATABASE "02hokkaido";

CREATE DATABASE "02aomori"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Japanese_Japan.932'
    LC_CTYPE = 'Japanese_Japan.932'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

\c  02aomori;


CREATE EXTENSION postgis
    SCHEMA public
    ;
    
CREATE EXTENSION postgis_topology
    SCHEMA topology
  ;

CREATE EXTENSION ogr_fdw
    SCHEMA public
   ;

    
CREATE SCHEMA "census2015"
    AUTHORIZATION postgres;
    
    
CREATE SCHEMA "L2mesh"
    AUTHORIZATION postgres;   
    
CREATE SCHEMA "joins"
    AUTHORIZATION postgres;
    
    
CREATE SCHEMA  "groupstats"
    AUTHORIZATION postgres;
    
CREATE SCHEMA  "mesh"
    AUTHORIZATION postgres;
    
CREATE SCHEMA  "5mmesh"
    AUTHORIZATION postgres;
    
CREATE SCHEMA  "5mmeshin4th"
    AUTHORIZATION postgres;
    