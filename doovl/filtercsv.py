# coding: UTF-8
#
#   csvfilter
#
#

import os
import sys
import glob
import  csv

import doovl


#from osgeo import ogr





if __name__ == "__main__":
    import filtercsvschemes

    #print("initializing...")

    args = filtercsvschemes.ARGSCHEME.parse_args()

    folder = args.folder

    
    tgfolder = folder + "/ovlresult"
    doovl.FilterCSV( tgfolder   )

