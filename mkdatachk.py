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

#    print( "python dataTypechecker\dataTypechecker.py  \"g:\\work\\NHK_kumamoto\\" + fname + "\" -o output.csv  -r result.csv" )

    #if ln > 0 :
    print( "python G:/work/NHK_kumamoto/dataTypechecker/dataTypechecker\dataTypechecker.py  \"" + fname + "\" -o output.csv  -r result.csv" )
         #print("{ \"PARAMETERS\": {\"EXTENT\":\"\'" + dxmin + "," + dxmax +"," + dymin+"," + dymax +" [EPSG:6668]\'\",\"LEVEL\": \"9\"}, \"OUTPUTS\": {\"OUTPUT\":\"F:/work/NHK_kumamoto/mesh/mesh/" + mid + ".geojson\"}}")
         #print(row[1])  # または print(line.rstrip())
         #print("}")
         
    ln = ln + 1
    
#print("]\n")s