import doovl





if __name__ == "__main__":
    import ovl5mschemems

    #print("initializing...")

    args = ovl5mschemems.ARGSCHEME.parse_args()

    param_file = args.paramfile

    workfolder = args.workfolder
    #schema = args.schema
    logfile = args.logfile

    input_path =  './workfiles/ovlinput/'
    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'

    ovlsep  = './workfiles/ovlsplit/'

    ovlresult  = './workfiles/ovlresult/'

    thirdpath = './3rdmesh/'


    if workfolder is not None:
        input_path = workfolder + "/ovlinput/"

        ovlsep  =  workfolder +  '/ovlsplit/'
        ovlresult  = workfolder + '/ovlresult/'

    logfp = None

    if logfile is not None:
        logfp = open( logfile, mode="a")

    
    attrflag = True
    # 3次メッシュとのIntersect
    #doovl.dummy( param_file, input_path )

    doovl.make_5m( param_file,  ovlresult, ovlsep, thirdpath,  attrflag , logfp )
    #doovl.make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag )

    if logfile is not None: 
        logfp.close()

