import doovl





if __name__ == "__main__":
    import extentschemems

    #print("initializing...")

    args = extentschemems.ARGSCHEME.parse_args()

    param_file = args.paramfile

    workfolder = args.workfolder

   

    input_path =  './workfiles/ovlinput/'

    if workfolder is not None:
        input_path = workfolder + "/ovlinput/"
  
    
    attrflag = True
    # 3次メッシュとのIntersect
    #doovl.dummy( param_file, input_path )

    doovl.chk_extent( param_file,  input_path,   attrflag )
    #doovl.make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag )
