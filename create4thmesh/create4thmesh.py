#import doovl
import jismesh.utils as ju

#import numpy

import sys
import os

import json
from osgeo import ogr



def create4thmesh( thirdmesh, schema,  dbhost, dbname, dbuser, dbpasswd,outputfolder ):
    driver = ogr.GetDriverByName('GPKG')
    dataSource = driver.Open(thirdmesh, 0)

    if dataSource is None:
        print ('Could not open %s' % (ifname))
    else:
                          #print( 'Opened %s' % (ifname))

        # folder が無ければ作成
        if not os.path.exists(outputfolder):
            os.mkdir(outputfolder)

        #ofp.write(sctr)

        layer = dataSource.GetLayer()

        for feature in layer:
            code = feature.GetField("code")
            
            for ct in range(4):
            
                ncode = code + str((ct+1))

                #print(ncode)
                lat_sw, lon_sw = ju.to_meshpoint(ncode, 0, 0)
                #print(lat_sw, lon_sw)
                lat_ne, lon_ne = ju.to_meshpoint(ncode, 1, 1)
                #print(lat_ne, lon_ne)
            
            
                jstr = "{\"type\":\"Feature\",\"geometry\":{\"type\":\"Polygon\",\"coordinates\":"
                jstr = jstr + "[[[" + str(lon_sw) + ", " + str(lat_sw) + "], [" + str(lon_sw) + ", " + str(lat_ne) + "], ["
                
                jstr = jstr + str(lon_ne ) + ", " + str(lat_ne) + "], [" + str( lon_ne )+"," + str(lat_sw )  + "], [" + str(lon_sw) + ", " + str(lat_sw) + "]]]},"
                jstr = jstr + "\"properties\":{\"code\":\"" + ncode + "\"}}"

                print( jstr )
            
         #   {"type":"Feature","geometry":{"type":"Polygon","coordinates":[[[129.975, 32.141666666666666], [129.975, 32.141708333333334], [129.9750625, 32.141708333333334], [129.9750625, 32.141666666666666], [129.975, 32.141666666666666]]]},"properties":{"code":"48291778000000", "fcode":"482917781"}}

        

            #gdalstr = "ogr2ogr  -f \"GPKG\" " + outputfolder + "/" + code + ".gpkg "
          
            #gdalstr = gdalstr + "\"PG:dbname=\'" + dbname +"\' host=\'" + dbhost + "' port=5432 user=\'" + dbuser + "\' password=\'" + dbpasswd + "\' sslmode=disable\" "  
   
            #gdalstr = gdalstr + schema + ".map" + code 
            #print( gdalstr )





if __name__ == "__main__":
    import create4thmeshschemems

    #print("initializing...")

    args = create4thmeshschemems.ARGSCHEME.parse_args()

    #csv_path = args.csvpath

    schema = args.schema

    workfolder = args.workfolder

    outputfolder = args.outputfolder


    #output_field = args.field


#    input_path =  './workfiles/ovlinput/'
#    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'

#    ovlsep  = './workfiles/ovlsplit/'

    if outputfolder is None:
         outputfolder= './workfiles/4themesh'
    
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
         schema = "mesh4th"

    #file = sys.stdout
    #if outputfile is not None:
    #    ofile = open( outputfile, "w", encoding="cp932")
         

    
    attrflag = True


    #  db 関係パラメータを渡す必要
    #  host  db  user  passwd  


    #doovl.cnvpostgis_gpkg( thirdmesh, schema,  dbhost, dbname, dbuser, dbpasswd,outputfolder )
    create4thmesh( thirdmesh, schema,  dbhost, dbname, dbuser, dbpasswd,outputfolder )
    #print( dbhost)
    #print(dbname)

