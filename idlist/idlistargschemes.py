# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='dump specified field value from vector layer')
ARGSCHEME.add_argument('inputfile', help='input file name')


ARGSCHEME.add_argument('-o', '--outputfile', help='output log file name (option)')
ARGSCHEME.add_argument('-f', '--fieldname', help='dump field name (option)')
