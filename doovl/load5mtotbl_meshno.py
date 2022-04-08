import doovl
import sys

def  make_thirdmesh_tables( thirdmesh, schema ):

    print(schema )



if __name__ == "__main__":
    import load5mtotbl_meshnoschemems

    #print("initializing...")

    args = load5mtotbl_meshnoschemems.ARGSCHEME.parse_args()

    csv_folder = args.csvfolder

    schema = args.schema

    workfolder = args.workfolder

    outputfile = args.outputfile

    

    meshnof = args.meshnofile

    logfile = args.logfile
    #header = args.createschema



    input_path =  './workfiles/ovlinput/'
    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'

   
    #ovlsep  = './workfiles/ovlsplit/'

    #schema = 'tdmesh'

    if meshnof = is None:
         print("no mesh number file")
         exit()

    if schema  is None:
         print("no schema")
         exit()
       #schema = "mesh5m"

    ofile = sys.stdout
    if outputfile is not None:
        ofile = open( outputfile, "w", encoding="cp932")

    
         
    csvpath = './workfiles/ovlresult/'
    if workfolder is not None:
        csvpath = workfolder + '/ovlresult/'

 


    log = None

    if logfile is not None:
        log = open(logfile, mode="a", encoding="cp932")
    
    attrflag = True
    # 3次メッシュとのIntersect
    #doovl.dummy( param_file, input_path )

    # create mesh id table script

    #   header parameter が 0 より大きい場合スキーマを作成する
    #if header  is not None:
     #   if int(header) > 0:
     #       doovl.make_thirdmesh_tables( thirdmesh, schema, ofile )

    #  load  csv to table script
    doovl.load_csv_tables_meshno( csvpath, meshnof , schema, ofile, log )

    if outputfile is not None:
        ofile.close()

    if logfile is not None:
        log.close()

    #doovl.make_split( param_file,  ovl3rdpath, ovlsep, attrflag )
    #doovl.make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag )
