import doovl





if __name__ == "__main__":
    import fixfilesschemems

    #print("initializing...")

    args = fixfilesschemems.ARGSCHEME.parse_args()

    param_file = args.paramfile
    workfolder = args.workfolder
    #schema = args.schema
    logfile = args.logfile

    input_path =  './workfiles/ovlinput/'
    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'

    if workfolder is not None:
        input_path = workfolder + "/ovlinput/"
        ovl3rdpath = workfolder + "/ovl3rd/"


    logfp = None

    if logfile is not None:
        logfp = open( logfile, mode="a")

    attrflag = True
    # 3次メッシュとのIntersect
    #doovl.dummy( param_file, input_path )
    doovl.make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag , logfp )

    if logfile is not None: 
        logfp.close()



