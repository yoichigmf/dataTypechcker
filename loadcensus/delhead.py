#import doovl
#import jismesh.utils as ju

#import numpy

import sys
import os
#import subprocess
import glob
import json
import csv
#from osgeo import ogr

def  filtercsv( input, output ):

    #print ( input )
    #print( output )

    with open( input, "r", encoding='cp932') as ip:
        csvreader = csv.reader( ip )


        with open( output, "w", encoding='cp932') as op:

            lp = 0

            for s_line in csvreader:

                if lp > 1:
                    key_code = s_line[0]
                    pop = s_line[4]

                    print( key_code + "," + pop, file=op)
                lp = lp + 1
            



def  delhead( ifolder, schema,  tablename,  dbhost, dbname, dbuser, dbpasswd, workfolder,  filename ):

#def create4thmesh( thirdmesh, schema,  tablename, dbhost, dbname, dbuser, dbpasswd, workfolder, outputfolder, filename  ):
 #   driver = ogr.GetDriverByName('GPKG')
 #   dataSource = driver.Open(thirdmesh, 0)

  #  if dataSource is None:
  #      print ('Could not open %s' % (thirdmesh))
  #  else:
                          #print( 'Opened %s' % (ifname))

        # folder が無ければ作成

            
    if not os.path.exists( workfolder ):
        os.mkdir( workfolder )

        #ofp.write(sctr)


    if filename is None:
        of = sys.stdout    
    else:
        of = open( filename, "w")

    #  table create sql


    ntablename = schema + "." + tablename

    sqlstr = "create schema if not exists " + schema + ";"

    print( sqlstr, file=of)

    const_name = "const_key_" + tablename

    sqlstr = "drop table if exists  " + ntablename  + ";"

    print( sqlstr, file=of)   


    sqlstr = "create table " + ntablename
    print( sqlstr, file=of)  

    sqlstr = "("
    print( sqlstr, file=of)  
    sqlstr = "key_code text COLLATE pg_catalog.\"default\" NOT NULL,"
    print( sqlstr, file=of)  

    sqlstr = "jinko bigint,"
    print( sqlstr, file=of)  
    sqlstr = "CONSTRAINT " + const_name + " PRIMARY KEY (key_code)"
    print( sqlstr, file=of)  
    sqlstr =");"
    print( sqlstr, file=of)  


    # list of csv files
    files = glob.glob(ifolder + "/*.txt")
    for file in files:
        csvfname = os.path.basename( file )
        file_name =os.path.splitext( csvfname)[0]


        nfile_name = workfolder + "/nc" + file_name

        filtercsv( file , nfile_name )
    

        print( "\copy " + ntablename + " from \'" + nfile_name + "\' CSV ;", file=of)
    
      
    if filename is not None:
        of.close()



if __name__ == "__main__":
    import delheadschemems

    #print("initializing...")

    args = delheadschemems.ARGSCHEME.parse_args()

    #csv_path = args.csvpath

    ifolder = args.inputfilefolder

    schema = args.schema

    workfolder = args.workfolder

    #outputfolder = args.outputfolder

    tablename = args.tablename

    filename = args.filename


    #output_field = args.field


#    input_path =  './workfiles/ovlinput/'
#    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'

#    ovlsep  = './workfiles/ovlsplit/'

         
    if workfolder is None:
         workfolder = './workfiles/census'
    
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
         schema = "census2015"

    if tablename  is None:
        tablename = "stat"


    #if filename is None:
    #    filename = "4themesh.gpkg"
    #file = sys.stdout
    #if outputfile is not None:
    #    ofile = open( outputfile, "w", encoding="cp932")
         

    
    attrflag = True


    #  db 関係パラメータを渡す必要
    #  host  db  user  passwd  


    #doovl.cnvpostgis_gpkg( thirdmesh, schema,  dbhost, dbname, dbuser, dbpasswd,outputfolder )
    delhead( ifolder, schema,  tablename,  dbhost, dbname, dbuser, dbpasswd, workfolder,  filename )
    #print( dbhost)
    #print(dbname)

