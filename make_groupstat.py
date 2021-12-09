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


    print("drop table if EXISTS \"groupstats\".\"" + fname + "\";")
   
    print(" ")
    
    print("create table \"groupstats\".\"" + fname + "\" as " )
    print(" select fcode, count(*) from \"joins\".\"" + fname + "\" group by fcode ;")

    
      

    print("ALTER TABLE \"groupstats\".\"" + fname + "\"" )
    print("OWNER to postgres;")
    print(" " )
  
         
    ln = ln + 1
    
