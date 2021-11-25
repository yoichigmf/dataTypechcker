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
    print( "type  13to15list.txt | python filt2ndmesh\\filter2m.py     -o  result13\\" + fname + ".txt " + fname )

         
    ln = ln + 1
    
#print("]\n")s