import doovl
import sys

def  make_thirdmesh_tables( thirdmesh, schema ):

    print(schema )



if __name__ == "__main__":
    import create5msqlschemems

    #print("initializing...")

    args = create5msqlschemems.ARGSCHEME.parse_args()

    #csv_path = args.csvpath

    schema = args.schema

    workfolder = args.workfolder

    outputfile = args.outputfile

    #csvpath =  args.csvpath 



    input_path =  './workfiles/ovlinput/'
    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'

    ovlsep  = './workfiles/ovlsplit/'

    #schema = 'tdmesh'

    if schema  is None:
       schema = "mesh5m"

    ofile = sys.stdout
    if outputfile is not None:
        ofile = open( outputfile, "w", encoding="cp932")
         

    
    attrflag = True
    # 3次メッシュとのIntersect
    #doovl.dummy( param_file, input_path )

    # create mesh id table script
    #doovl.make_thirdmesh_tables( thirdmesh, schema, ofile )

    #  load  csv to table script
    #doovl.load_csv_tables( csvpath, schema, ofile )
    
    forth = False

    doovl.create_5msql( thirdmesh, schema, ofile, forth )

    if outputfile is not None:
        ofile.close()
    #doovl.make_split( param_file,  ovl3rdpath, ovlsep, attrflag )
    #doovl.make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag )
