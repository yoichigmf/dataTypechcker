# -*- coding: utf-8 -*-
import sys

import fileinput
import csv

ln = 0

cin = csv.reader(sys.stdin) # 補足: 開く対象がファイルのときは newline='' をパラメータに追加

#print("[\n")


for row in cin:

    fname = row[0]

    
    #table = mid[0:4]
    #table = mid

    #if ln > 0 :
    #print( "type  15list.txt | python filt2ndmesh\\filter2m.py     -o  result\\" + fname + ".txt " + fname )


    print("CREATE SEQUENCE \"5mmesh\".\"" + fname + "_sid_seq\"")
    print("INCREMENT 1")
    print("START 1")
    print("MINVALUE 1")
    print("MAXVALUE 2147483647")
    print("CACHE 1;")
    print(" ")
    print ("ALTER SEQUENCE \"5mmesh\".\"" + fname + "_sid_seq\"" )
    print( "OWNER TO postgres;")
    
    print(" ")
    
    
    print("CREATE TABLE IF NOT EXISTS \"5mmesh\".\"" + fname + "\"")
    
    print("(" )
    print("sid integer NOT NULL DEFAULT nextval(\'\"5mmesh\".\"" + fname + "_sid_seq\"\'::regclass),")
    print("mid text COLLATE pg_catalog.\"default\",")
    print("CONSTRAINT \"" + fname +"_pkey\" PRIMARY KEY (sid)")
    print(")" )
    

    print("TABLESPACE pg_default;")

    print("ALTER TABLE \"5mmesh\".\"" + fname + "\"" )
    print("OWNER to postgres;")
    print(" " )
    
    #-- Table: 5mmesh.mesh5m
    
    
    
         
    ln = ln + 1
    
#print("]\n")s