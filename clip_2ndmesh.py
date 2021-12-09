# -*- coding: utf-8 -*-
import sys

import fileinput
import csv

ln = 0

cin = csv.reader(sys.stdin) # 補足: 開く対象がファイルのときは newline='' をパラメータに追加

#print("[\n")
fd = open("l2nlist.csv", "w")

tid = 0

for row in cin:

    fname = row[1]

    
    #table = mid[0:4]
    #table = mid

    ofname = "G:/work/NHK_kumamoto/dataTypechecker/clip2/cp" + str(tid ) + ".csv"
    #if ln > 0 :
    #print( "type  15list.txt | python filt2ndmesh\\filter2m.py     -o  result\\" + fname + ".txt " + fname )

    print("qgis_process-qgis run qgis:clip -- INPUT=\"G:/work/NHK_kumamoto/workdata/l2mesh.gpkg|layername=l2mesh\" OUTPUT=\"" + ofname + "\" OVERLAY=\"" + fname + "\"")
  
    print( str(tid) + "," + fname ,file=fd )

    #qgis_process-qgis run qgis:clip -- INPUT="G:/work/NHK_kumamoto/workdata/l2mesh.gpkg|layername=l2mesh" OUTPUT="G:/work/NHK_kumamoto/dataTypechecker/clip/clip8.csv" OVERLAY="G:/work/NHK_kumamoto/210909HDD/kumamoto/430005kumamotoken/その2/15 白川/白川上流/河岸浸食/白川上流家屋倒壊（河岸侵食）.shp" 
         
    tid = tid + 1
    
fd.close()

#print("]\n")s