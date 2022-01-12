import doovl





if __name__ == "__main__":
    import extentschemems

    #print("initializing...")

    args = extentschemems.ARGSCHEME.parse_args()

    param_file = args.paramfile

    newparam = './scripts/nnparam.prm'

    input_path =  './workfiles/ovlinput/'
    ovl3rdpath = './workfiles/ovl3rd/'
    #thirdmesh = './3rdmesh/mesh3.gpkg'

    #ovlsep  = './workfiles/ovlsplit/'

    #ovlresult  = './workfiles/ovlresult/'

    thirdpath = './3rdmesh/'
    
    attrflag = True
    # 3次メッシュとのIntersect
    #doovl.dummy( param_file, input_path )

    doovl.chk_extent( param_file,  input_path,  newparam,   attrflag )
    #doovl.make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag )
