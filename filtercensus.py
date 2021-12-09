# -*- coding: utf-8 -*-
import sys

import fileinput
import csv

ln = 0

cin = csv.reader(sys.stdin) # 補足: 開く対象がファイルのときは newline='' をパラメータに追加

#print("[\n")


for row in cin:

    key_code = row[0]
    
    sousuu =  row[4]
    male = row[5]
    fem = row[6]
    
    fori = row[25]
    fori_m = row[26]
    fori_f = row[27]
    setai = row[28]
    
    # output_str = key_code + "," + sousuu + "," + male + "," + fem + "," + fori + "," + fori_m + "," + fori_f + "," + setai
  
    output_str = key_code + "," + sousuu 
    
    if ln > 1:
    
         print(output_str)

    
    #table = mid[0:4]
    #table = mid

    #if ln > 0 :
    #print( "type  15list.txt | python filt2ndmesh\\filter2m.py     -o  result\\" + fname + ".txt " + fname )

    #print("copy \"5mmesh\".\"" + fname + "\" (mid) FROM \'g:/work/NHK_kumamoto/dataTypechecker/result13/" + fname + ".txt\' CSV  ;")
  
    
         
    ln = ln + 1
    
#print("]\n")s