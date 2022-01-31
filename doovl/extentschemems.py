# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='check geometry files script  ')
ARGSCHEME.add_argument('paramfile', help='parameter file name')
ARGSCHEME.add_argument('-w', '--workfolder', help='work folder name ')

#ARGSCHEME.add_argument('-i', '--inputfile', help='input file name ')
#ARGSCHEME.add_argument('-o', '--outputfile', help='output  file name (option)')
