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
import json

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

         
         meshstr2 = "qgis_process-qgis-ltr run qgis:extractbylocation -- INPUT=\"" + work_path + "/mesh2nd.gpkg|layername=mesh2nd\" PREDICATE=0,1,4,5 INTERSECT=\"" + admfilename + "\" OUTPUT=\"" + outputfname + "\""
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


def  Create5mand2ndMesh( param, output_file  ):

     basedir = param["BASEDIR"]
     dbname = param["DBNAME"]

     prefname = param["PREFNAME"]
     prefname_j = param["PREFNAME_J"]

     dbname = param["DBNAME"]
     dbuser = param["DBUSER"]
     dbpassword = param["DBPASSWD"]

     root = basedir + "/" + prefname
     Adm = root + "/" +"Adm"

         #  2nd mesh geopackage and geojson
     secondMesh = root + "/" + "2ndmesh"

     second_md = secondMesh + "/mesh2nd.gpkg"

     conn = ogr.Open(second_md )

     outputdir = root + "/workfiles/2nd/"

     lyr = conn.GetLayer( "mesh2nd" )

     if lyr is None:
        print >> sys.stderr, '[ ERROR ]: layer name = "%s" could not be found in database "%s"' % ( "mesh2nd", second_md )
        sys.exit( 1 )


     toolstr =  basedir + "/hazard_tools/japan-mesh-tool/python/japanmesh/"
  
     if output_file  is  None:
        outf = sys.stdout
     else:
        outf = open(output_file , mode='w',  encoding='sjis' )


     for feature in lyr:
        geom = feature.GetGeometryRef()
        extent = geom.GetEnvelope()

        code = feature["code"]

        outputstr = outputdir + str(code) + ".gojsonl"
        cmdstr = "python " + toolstr + "main.py 10  -e " + str(extent[0]) + "," + str(extent[2]) + " " + str(extent[1]) + "," + str(extent[3]) + " -o " + outputstr 
        #print( str(feature.GetField("code")) + "," + str(extent[0]) + "," + str(extent[2]) + " " + str(extent[1]) + "," + str(extent[3]))
        print( cmdstr , file=outf)

        ogrstr = "ogr2ogr -f \"GPKG\" -nln " + str(code) + " " + secondMesh + "/"  + str(code) + ".gpkg " + outputstr 
        print( ogrstr , file=outf)


        ogpgstr = "ogr2ogr -f \"PostgreSQL\" PG:\"host=localhost user=" + dbuser + "password=" + dbpassword + "dbname=" + dbname + "\" " + outputstr + " -nln mesh." + str(code) + " -append"
     #featureCount = lyr.GetFeatureCount()
        print( ogpgstr , file=outf)
     #print("feature count " + str(featureCount))

     print (basedir )
     print( dbname )

     print( second_md )
     
def  getLayers( dbfile ):


     conn = ogr.Open( dbfile )
     
     layec = conn.GetLayerCount()
     
     
     print( "number of layer " + str(layec ))
     
     layer = conn.GetLayerByIndex(0)
     
     print( str(layer.GetGeomType()) )
     
     geomtype = layer.GetGeomType()
     
     

          
    
     
     for feature in layer:
     
          geom = feature.GetGeometryRef()
              # polygon
          if geomtype == 3:
          
              #xmin, ymin, xmax, ymax = getext( geom )
              #for ring in geom:
              #    points = ring.GetPointCount()
                   
              #     print("points in ring " + str(points ))
              print( geom.ExportToWkt())
              geom_poly_envelope = geom.GetEnvelope()
              print(str( geom_poly_envelope[0] ) + " " + str(geom_poly_envelope[2] ) + " " + str(geom_poly_envelope[1] ) + " " + str(geom_poly_envelope[3] ))
          else:    
              

         
              print( "pointc " + str(geom.GetPointCount()))
              for i in range(0, geom.GetPointCount()):
                   pt = geom.GetPoint(i)
              
                   print("point " + str(i ) + " [" + str(pt[0] ) + "," + str(pt[1] ) + "]" )
              print( geom.ExportToWkt())
     
     #inLayer = conn.GetLayer( layername )
     #extent = inLayer.GetExtent()
     
     #print( extent )
     
     #return extent
     
def getext( geom ):

     valueset = False
     
     xmin = 0.0
     ymin = 0.0
     xmax = 0.0
     ymax = 0.0
     
     
     for ring in geom:
          points = ring.GetPointCount()
          
          for p in xrange(points):
          #pcnt+=1
               lon,lat, z = ring.GetPoint(p)
          #zval = get_zval(feat,zfield)
          
               if not valueset:
                    xmin = lon
                    xmax = lon
                    ymin = lat
                    ymax = lat
               
               if zval != None:
                    z = zval.strip()
               outstr = "%s,%s,%s\n" % (lon,lat,z)
               print(outstr)
                   
         # print("points in ring " + str(points ))
     return xmin, ymin, xmax, ymax

def  createstat2( result_json ):

     with open( result_json , 'r') as jf: 

          jld = json.load( jf )

          results = jld["results"]
          print( results )

          invarid = int(results["INVALID_COUNT"])
          errord = int( results["ERROR_COUNT"])

          #nc = invarid + errord + 3
          print( nc )

          sys.exit( nc )

#   
def createalltb( input_file ):


    
    pref_filename = input_file
    with open(pref_filename, mode='r',  encoding='sjis' ) as f: 
    
         head_read = False
         tsv_reader = csv.reader(f, delimiter=',')
         for row in tsv_reader:
         
              if head_read:
              
                   #print( row[1])
                   output_sql( row[1] )
              else:
                   head_read = True
                   
              #if prefname == row[2]:
              #     return row[0], row[1]
              #print( row )
         
    #return  "0", "undefined"
    
def  output_sql( secondmesh ):

     firstmesh  = secondmesh[0:4]
     print("-- ")
     #print("drop view  if EXISTS  \"4thmesh\".\"" + secondmesh + "\";" )


     print ("insert into  \"result\".\"kumamoto_test\" (  wkb_geometry , code, d5mmesh , dratio ,jinko , soutei_jinko ) ")
     print ("select  wkb_geometry , code, d5mmesh , dratio ,jinko , soutei_jinko from \"4thmesh\".\"" + secondmesh + "\" ; " )


 

if __name__ == "__main__":
    import createalltbschema

    #print("initializing...")

    args = createalltbschema.ARGSCHEME.parse_args()


    input_file = args.inputfile

    

    if input_file  is  None:
        print( "input file miss" )
        exit()
 
    #print(input_file )

    createalltb( input_file )
    


    #getLayers( input_file )
    
    #param =  args.param

    #command_str = args.command

    #print( prefname )
    
    #if int(pref_code) > 0 :
    #     MakeFolders(  prefname, basedir, pref_code, pref_name_j, test_mode  )
    #else:
    #     print("prefecture name error  " + prefname )
    #     print("you must type prefcture name such as  aichiken   hokkaido ")