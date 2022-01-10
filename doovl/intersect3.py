import doovl





if __name__ == "__main__":
    import fixfilesschemems

    #print("initializing...")

    args = fixfilesschemems.ARGSCHEME.parse_args()

    param_file = args.paramfile

    input_path =  './workfiles/ovlinput/'
    ovl3rdpath = './workfiles/ovl3rd/'
    thirdmesh = './3rdmesh/mesh3.gpkg'
    attrflag = True
    # 3次メッシュとのIntersect
    #doovl.dummy( param_file, input_path )
    doovl.make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag )
