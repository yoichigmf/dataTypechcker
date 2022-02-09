import doovl





if __name__ == "__main__":
    import make4thsqlschemems

    #print("initializing...")

    args = make4thsqlschemems.ARGSCHEME.parse_args()

    ischema = args.ischema

 
    schema = args.schema

    outputfile = args.output

    tablename = args.tablename

  
    thirdmesh = './3rdmesh/mesh3.gpkg'


#  db parameter

    doovl.make_4thesql( ischema,  schema,  tablename, outputfile,  thirdmesh )
    #doovl.make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag )

 

