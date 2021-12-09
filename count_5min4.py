# -*- coding: utf-8 -*-
import sys

import fileinput
import csv

ln = 0

cin = csv.reader(sys.stdin) # 補足: 開く対象がファイルのときは newline='' をパラメータに追加

#print("[\n")


for row in cin:

    fname = row[0]



    print("drop table if EXISTS \"5mmeshin4th\".\"" + fname + "\";")
   
    print(" ")
    
    print("create table \"5mmeshin4th\".\"" + fname + "\" as " )
    print(" select distinct(\"mesh\".\"" + fname + "\".fcode),\"groupstats\".\"" + fname + "\".count " )
    print("   from \"mesh\".\"" + fname + "\" left join ")
    print("  \"groupstats\".\"" + fname + "\" on \"mesh\".\"" + fname + "\".fcode=\"groupstats\".\"" + fname + "\".fcode ;")


    
      

    print("ALTER TABLE \"5mmeshin4th\".\"" + fname + "\"" )
    print("OWNER to postgres;")
    print(" " )
  
         
    ln = ln + 1
    
