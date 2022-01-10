import doovl





if __name__ == "__main__":
    import fixfilesschemems

    #print("initializing...")

    args = fixfilesschemems.ARGSCHEME.parse_args()

    param_file = args.paramfile

    input_path =  './workfiles/ovlinput/'

    # ジオメトリ修復
    #doovl.dummy( param_file, input_path )
    doovl.make_fix( param_file, input_path )
