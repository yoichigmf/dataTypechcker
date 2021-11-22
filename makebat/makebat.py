# coding: UTF-8
#
#   csvfilter
#
#

import os
import sys
from osgeo import ogr


def   MakeBat( param,  command_str,  inputfile, outputfile   ):

    ofile = sys.stdout
    ifile = sys.stdin

    if outputfile  is not None:
        ofile = open( outputfile, mode="w")

    if inputfile is not None:
        ifile = open( inputfile, mode="r")


    for s_line in ifile:
        lsp = s_line.split(',')

        cmdstr = "python idlist/idlist.py -o 15list.txt \"" +  lsp[1] + "\"\n"
        #if lsp[0] == filter_value:

        ofile.write( cmdstr )

    if outputfile  is not None:
        ofile.close()

    if inputfile is not None:
        ifile.close()




if __name__ == "__main__":
    import makebatschemes

    #print("initializing...")

    args = makebatschemes.ARGSCHEME.parse_args()

    input_file = args.inputfile

    output_file = args.outputfile

    param =  args.param

    command_str = args.command

    MakeBat( param, command_str, input_file, output_file  )

