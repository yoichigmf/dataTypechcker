# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='filterling csv file using first value ')
ARGSCHEME.add_argument('value', help='filterling value')

ARGSCHEME.add_argument('-i', '--inputfile', help='input file name (option)')
ARGSCHEME.add_argument('-o', '--outputfile', help='output  file name (option)')
