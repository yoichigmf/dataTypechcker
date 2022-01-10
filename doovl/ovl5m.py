import doovl





if __name__ == "__main__":
    import ovl5mschemems

    #print("initializing...")

    args = ovl5mschemems.ARGSCHEME.parse_args()

    param_file = args.paramfile

    input_path =  './workfiles/ovlinput/'
    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'

    ovlsep  = './workfiles/ovlsplit/'

    ovlresult  = './workfiles/ovlresult/'

    thirdpath = './3rdmesh/'
    
    attrflag = True
    # 3次メッシュとのIntersect
    #doovl.dummy( param_file, input_path )

    doovl.make_5m( param_file,  ovlresult, ovlsep, thirdpath,  attrflag )
    #doovl.make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag )
