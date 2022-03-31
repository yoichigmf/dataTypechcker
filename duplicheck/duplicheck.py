#import doovl
#import jismesh.utils as ju

#import numpy

import sys
import os
import subprocess

import json
from osgeo import ogr



def checkdupli( thirdmesh, schema,  tablename, dbhost, dbname, dbuser, dbpasswd, filename  ):
    driver = ogr.GetDriverByName('GPKG')
    dataSource = driver.Open(thirdmesh, 0)

    if dataSource is None:
        print ('Could not open %s' % (thirdmesh))
    else:
                          #print( 'Opened %s' % (ifname))

    
        #gpkg =  outputfolder + "/" + filename
        
        with open( filename , mode="w", encoding="UTF-8" ) as gsl:
        
        
            jstr = "CREATE SCHEMA " + schema +";"
            print( jstr,file=gsl )
            print( jstr )  
             

            jstr = "create table \"" +  schema + "\".\"" +  tablename + "\" ( "
            print( jstr,file=gsl )
            print( jstr )  
                         
             
            jstr = " code  varchar(18), dcount  integer );"
             
            print( jstr,file=gsl )
            print( jstr )  
                                     

        

            layer = dataSource.GetLayer()


            
            for feature in layer:
                code = feature.GetField("code")
                
                jstr = "insert into \"" + schema + "\".\"" + tablename +"\" (code, dcount )" 
                
                print( jstr,file=gsl )
                print( jstr )
                
                 
                jstr = "select  '" + code + "' code , count(* ) dcount from   \"mesh\".\"" + code + "\" t1 " 
  
  
                print( jstr,file=gsl )
                print( jstr )
                              
                jstr = "where exists(select * from \"mesh\".\"" + code + "\"  t2 "  
                              
                print( jstr,file=gsl )
                print( jstr )               
                              
                jstr = " where t2.code=t1.code and t2.ctid > t1.ctid ); "
                
                                
                print( jstr,file=gsl )
                print( jstr )                         
            
 


if __name__ == "__main__":
    import duplicheckschemems

    #print("initializing...")

    args = duplicheckschemems.ARGSCHEME.parse_args()

    #csv_path = args.csvpath

    schema = args.schema

    #workfolder = args.workfolder

    #outputfolder = args.outputfolder

    tablename = args.tablename

    filename = args.filename


    #output_field = args.field


#    input_path =  './workfiles/ovlinput/'
#    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'

#    ovlsep  = './workfiles/ovlsplit/'

    
    #schema = 'tdmesh'

    config_file_name = "./config/config.json"

    json_open = open(config_file_name, 'r')


    if json_open is None:
         print("error config file open error " + config_file_name )
         exit()

    json_load = json.load(json_open)

    dbhost = json_load["DBHOST"]
    dbname  = json_load["DBNAME"]
    dbuser  = json_load["DBUSER"]
    dbpasswd  = json_load["DBPASSWD"]

    if schema  is None:
         schema = "check_s"

    if tablename  is None:
        tablename = "check_dupli"


    if filename is None:
        filename = "4themesh.gpkg"
    #file = sys.stdout
    #if outputfile is not None:
    #    ofile = open( outputfile, "w", encoding="cp932")
         

    
    attrflag = True


    #  db 関係パラメータを渡す必要
    #  host  db  user  passwd  


    #doovl.cnvpostgis_gpkg( thirdmesh, schema,  dbhost, dbname, dbuser, dbpasswd,outputfolder )
    checkdupli( thirdmesh, schema,  tablename,  dbhost, dbname, dbuser, dbpasswd, filename )
    #print( dbhost)
    #print(dbname)

