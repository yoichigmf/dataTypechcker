# -*- coding: utf-8 -*-
import sys

import fileinput
import csv

ln = 0

cin = csv.reader(sys.stdin) # 補足: 開く対象がファイルのときは newline='' をパラメータに追加



schema = "\"groupstats\""


for row in cin:

    if ln > 0:
        meshname = row[1]
    
        fmesh = meshname[0:4]
        
        gviewname = schema + ".\"gv" + meshname + "\""
    
        jointbl = "\"groupstats\".\"" + meshname + "\""
    
        censustbl = "\"census2015\".\"" + fmesh + "\""
        nviewname = schema + ".\"nv" + meshname + "\"" 
        
        cviewname = schema + ".\"cv" + meshname + "\"" 
        
        print("drop view if exists " + cviewname + ";" )        
        
        print("drop view if exists " + nviewname + ";" ) 

        print("drop view if exists " + gviewname + ";" )
    
    
        print("create view " + gviewname + " as ")
        print("select m4.id, m4.geom  ,text(m4.code) as code , COALESCE(gs.count, 0)  count , ")
        print("COALESCE(gs.count, 0.0)  / 10000.0  ratio   from " + jointbl + " gs "  )
        print(" left join  base_mesh.mesh_4 m4    on  gs.fcode = text(m4.code) ;")
 
    
        print("create view " + cviewname + " as ")
        print(" select  ces.key_code,  COALESCE(ces.sousu, 0) jinko  ")
        print("   from " + censustbl + " ces ")  
        print(" where ces.key_code like \'" + meshname + "%\';" )    
        
        
    
        print("create view " + nviewname + " as ")
        print(" select  cv.key_code,  gs.geom,  COALESCE(gs.count,0) count  ,COALESCE(gs.ratio,0.0) ratio ,cv.jinko,  ")
        print("  COALESCE(cv.jinko, 0) * COALESCE(gs.ratio,0.0)   kasojinko   from " + cviewname + " cv ")
        print(" left join " + gviewname + " gs on  cv.key_code=gs.code ; ")
        
         
    ln = ln + 1
    
#print("]\n")