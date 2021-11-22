# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='make bat file using csv file')
ARGSCHEME.add_argument('inputfile', help='input file name')

ARGSCHEME.add_argument('-c', '--command', help='command string (option)')
ARGSCHEME.add_argument('-o', '--outputfile', help='output  file name (option)')
ARGSCHEME.add_argument('-p', '--param', help='parameter ponter  (option)')
