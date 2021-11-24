# coding: UTF-8
#
#   csvfilter
#
#

import os
import sys
from osgeo import ogr


def   FilterValue( filter_value,  inputfile, outputfile   ):

    ofile = sys.stdout
    ifile = sys.stdin

    if outputfile  is not None:
        ofile = open( outputfile, mode="w")

    if inputfile is not None:
        ifile = open( inputfile, mode="r")


    for s_line in ifile:

        if s_line.startswith( filter_value ):
             ofile.write(s_line)
        #lsp = s_line.split(',')

        #if lsp[0] == filter_value:
        #    ofile.write(s_line)

    if outputfile  is not None:
        ofile.close()

    if inputfile is not None:
        ifile.close()




if __name__ == "__main__":
    import flt2argschemes

    #print("initializing...")

    args = flt2argschemes.ARGSCHEME.parse_args()

    input_file = args.inputfile

    output_file = args.outputfile

    filter_value = args.value

    FilterValue( filter_value, input_file, output_file  )

