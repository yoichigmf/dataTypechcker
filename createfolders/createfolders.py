# coding: UTF-8
#
#   csvfilter
#
#

import os
import sys
import csv
import pathlib
import shutil

from osgeo import ogr


def   MakeFolders(  prefname, basedir, pref_code, prefname_j, test_mode  ):


    
    if basedir  is  None:
        basedir ="."
        
    print( prefname )
    
    
   
    root = basedir + "/" + prefname
    
    my_makedirs( root )
    print( root )
    
    
    
    # geopackage
    
    mesh5m = root + "/" + "5mmesh"
    
    my_makedirs( mesh5m )
    
    wk = mesh5m + "/" + "2nd"
    
    my_makedirs( wk )
    
    wk = mesh5m + "/" + "3rd"   
    my_makedirs( wk )   
    
    
    #  admin boudary
    
    Adm = root + "/" +"Adm"
    my_makedirs( Adm )       
    
    #  2nd mesh geopackage and geojson
    secondMesh = root + "/" + "2ndmesh"
    
    my_makedirs( secondMesh )    
    
    #   geojson  work files
    workfiles = root + "/" + "workfiles"   
    
    my_makedirs( workfiles )     
    
    wk = workfiles + "/" + "2nd"
    
    my_makedirs( wk )     
    
    wk = workfiles + "/" + "3rd"     

    my_makedirs( wk )         
    
    scripts = root + "/" + "scripts"   
    
    my_makedirs( scripts )      
    
    config =   root + "/" + "config"   
    
    my_makedirs( config )      
    
    admfile , admtable = copy_admfile( Adm, prefname_j )
    
    print( admfile + " layer=" + admtable )
    
    
    layerdesc = admfile + "|layer=" + admtable
    ext = getExtent( admfile, admtable )
    
    config_file_name = config + "/config.json"
    
    with open(config_file_name, 'w') as f: 
         db_name = format(int(pref_code), '02d' ) +prefname
         
         p = pathlib.Path( basedir )
         
         basedirname = basedir
         if p.is_absolute():
              basedirname = basedir
         else:
              prel = p.resolve()
              basedirname = prel.as_posix()
     
       
         #print( basedirname )
         
         

         #print( "db=" + db_name )
         f.write("{\n" )
         f.write("\"DBNAME\":\"" + db_name + "\"\n")
         f.write(",\"BASEDIR\":\"" + basedirname + "\"\n" )
         f.write(",\"PREFNAME\":\"" +  prefname + "\"\n" )
         f.write(",\"PREFNAME_J\":\"" +  prefname_j + "\"\n" )     
         f.write(",\"ADMFILE\":\"" +  admfile + "\"\n" )           
         f.write(",\"ADMLAYER\":\"" +  admtable + "\"\n" )    
         f.write(",\"EXTENT\":\"" +  str(ext[0]) + "," +str(ext[2]) + " " + str(ext[1]) + "," + str(ext[3]) + "\"\n" )               
         f.write(",\"DBUSER\":\"postgres\"\n")
         f.write(",\"DBPASSWD\":\"disastNHK\"\n")
         f.write("}\n" )
         
         
    
    create_dbcreatesql( scripts, db_name )
    
    create2ndMeshall(  root , basedir, secondMesh, workfiles,  ext, scripts, prefname_j )




#   2次メッシュ作成スクリプト
def   create2ndMeshall( root, basedir, secondMesh, workfiles, extent, scripts, prefname_j ):

    mesh_script = scripts + "/create2ndmeshall.bat"
    
    basedirname = getabsolutepath( basedir )
    #p = pathlib.Path( basedir )
    
    #if p.is_absolute():
    #    basedirname = basedir
    #else:
    #    prel = p.resolve()
     #   basedirname = prel.as_posix()

    
    rootdirname = getabsolutepath( root )
              
    secondmesh_path = getabsolutepath( secondMesh )


    work_path = getabsolutepath( workfiles )

    admfilename = rootdirname + "/Adm/N03_001_" + prefname_j + ".gpkg|layername=N03_001_" + prefname_j
    #G:/work/NHK_hazard/fukuiken/Adm/N03_001_福井県.gpkg|layername=N03_001_福井県

    outputfname = secondmesh_path + "/mesh2nd.gpkg"
    
    with open( mesh_script, 'w', encoding="sjis") as f: 
    
         meshstr = "python "+ basedirname + "/hazard_tools/japan-mesh-tool/python/japanmesh/main.py  2 -e " + str(extent[0]) +","+ str(extent[2]) + " " + str(extent[1]) + "," + str(extent[3]) + "  -d "+ work_path + "\n"
         f.write( meshstr )

         ogrstr = "ogr2ogr  -overwrite   -f GPKG -nln  mesh2nd     " +  work_path + "/mesh2nd.gpkg  " + work_path + "/mesh_2.geojsonl\n"

         f.write( ogrstr )

         
         meshstr2 = "qgis_process-qgis run qgis:extractbylocation -- INPUT=\"" + work_path + "/mesh2nd.gpkg|layername=mesh2nd\" PREDICATE=0,1,4,5 INTERSECT=\"" + admfilename + "\" OUTPUT=\"" + outputfname + "\""
         #G:\\work\\NHK_hazard\\fukuiken\\workfiles\\mesh2ndselected.shp"

         f.write( meshstr2 )

#   ファイルの絶対パスを返す
def getabsolutepath( tgpath ):

    basedirname = tgpath
    p = pathlib.Path( tgpath )
    
    if p.is_absolute():
        basedirname = tgpath
    else:
        prel = p.resolve()
        basedirname = prel.as_posix()


    return basedirname


    
    
#  領域取得

def  getExtent( dbfile, layername ):


     conn = ogr.Open( dbfile )
     
     inLayer = conn.GetLayer( layername )
     extent = inLayer.GetExtent()
     
     #print( extent )
     
     return extent
    
# 領域ファイルコピー

def  copy_admfile( Adm, prefname_j ):
     adm_filename = "N03_001_" + prefname_j + ".gpkg"
     pbase = __file__
     dirname = os.path.dirname(pbase)
     
     srcname = dirname + "/prefareas/" + adm_filename
     distname = Adm + "/" + adm_filename
     shutil.copy( srcname ,distname)
     
     dtable = "N03_001_" + prefname_j 
     return distname, dtable

    
#   データベース作成SQL
def  create_dbcreatesql( scripts_path, dbname ):


     sql_filename = scripts_path + "/createdb.sql"
     
     print( sql_filename )
     
     with open( sql_filename, 'w' ) as sfile:
     
          sfile.write( "CREATE DATABASE \"" + dbname + "\"" )
          sqls2 = ''' 
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Japanese_Japan.932'
    LC_CTYPE = 'Japanese_Japan.932'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
    
    '''
    
     
          sfile.write( sqls2 )
          sfile.write( "\\c " + dbname + "\;\n" )
     
          sql = '''
          

CREATE EXTENSION postgis
    SCHEMA public
    ;
    
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
  
          ''';
          sfile.write( sql )
          


def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)
        

#   
def check_prefname( prefname ):

    pbase = __file__
    dirname = os.path.dirname(pbase)
    #print( pbase )
    #print(dirname )
    
    pref_filename = dirname + "/preflist.txt"
    with open(pref_filename, mode='r', newline='', encoding='utf-8' ) as f: 
         tsv_reader = csv.reader(f, delimiter='\t')
         for row in tsv_reader:
              if prefname == row[2]:
                   return row[0], row[1]
              print( row )
         
    return  "0", "undefined"


if __name__ == "__main__":
    import createfoldersschemes

    #print("initializing...")

    args = createfoldersschemes.ARGSCHEME.parse_args()

    basedir  = args.basedir


    prefname = args.prefname
    
    test_mode = args.testmode
    
    
    pref_code , pref_name_j =  check_prefname( prefname )

    #param =  args.param

    #command_str = args.command

    #print( prefname )
    
    if int(pref_code) > 0 :
         MakeFolders(  prefname, basedir, pref_code, pref_name_j, test_mode  )
    else:
         print("prefecture name error  " + prefname )
         print("you must type prefcture name such as  aichiken   hokkaido ")