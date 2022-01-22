import doovl
import sys
import json

def  make_thirdmesh_tables( thirdmesh, schema ):

    print(schema )



if __name__ == "__main__":
    import creategeotiffschemems

    #print("initializing...")

    args = creategeotiffschemems.ARGSCHEME.parse_args()

    #csv_path = args.csvpath

    schema = args.schema

    workfolder = args.workfolder

    outputfolder = args.outputfolder


    output_field = args.field


#    input_path =  './workfiles/ovlinput/'
#    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'

#    ovlsep  = './workfiles/ovlsplit/'

    if outputfolder is None:
         outputfolder= './workfiles/geotiff'

   

    if output_field is None:
         output_field = "SSS_RANK"

    field_type = args.type

    if field_type is None:
         field_type = "Int32"

         # Int32 or Float32
    
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
         schema = "mesh5m"

    #file = sys.stdout
    #if outputfile is not None:
    #    ofile = open( outputfile, "w", encoding="cp932")
         

    
    attrflag = True


    #  db 関係パラメータを渡す必要
    #  host  db  user  passwd  


    doovl.create_geotiff( thirdmesh, schema, output_field, field_type,  dbhost, dbname, dbuser, dbpasswd,outputfolder )

    #print( dbhost)
    #print(dbname)

