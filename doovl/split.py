import doovl





if __name__ == "__main__":
    import splitschemems

    #print("initializing...")

    args = splitschemems.ARGSCHEME.parse_args()

    param_file = args.paramfile
    workfolder = args.workfolder
    #schema = args.schema
    logfile = args.logfile

    input_path =  './workfiles/ovlinput/'
    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'

    ovlsep  = './workfiles/ovlsplit/'

    if workfolder is not None:
        input_path = workfolder + "/ovlinput/"
        ovl3rdpath = workfolder + "/ovl3rd/"
        ovlsep  =  workfolder +  '/ovlsplit/'


    logfp = None

    if logfile is not None:
        logfp = open( logfile, mode="a")

    
    attrflag = True
    # 3次メッシュとのIntersect
    #doovl.dummy( param_file, input_path )

    doovl.make_split( param_file,  ovl3rdpath, ovlsep, attrflag , logfp )
    #doovl.make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag )

    
    if logfile is not None: 
        logfp.close()

