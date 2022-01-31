import doovl
import sys
import json

def  make_thirdmesh_tables( thirdmesh, schema ):

    print(schema )



if __name__ == "__main__":
    import make_paramschemems

    #print("initializing...")

    args = make_paramschemems.ARGSCHEME.parse_args()

    #csv_path = args.csvpath

    listfile = args.listfile

    paramfile = args.paramfilename

    #outputfolder = args.outputfolder


 

  


    csvpos = 0
    doovl.make_paramfile( listfile, paramfile , csvpos)

    #print( dbhost)
    #print(dbname)

