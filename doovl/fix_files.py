import doovl
import sys
import os




if __name__ == "__main__":
    import fixfilesschemems

    #print("initializing...")

    args = fixfilesschemems.ARGSCHEME.parse_args()

    param_file = args.paramfile
    workfolder = args.workfolder

    logfilename = args.logfilename

    input_path =  './workfiles/ovlinput/'

    if workfolder is not None:
        input_path = workfolder + "/ovlinput/"
        if not os.path.exists(workfolder  ):
            os.mkdir(workfolder )



   

    # ジオメトリ修復
    #doovl.dummy( param_file, input_path )
    doovl.make_fix( param_file, input_path, logfilename )
