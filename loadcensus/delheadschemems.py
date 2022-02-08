# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='create sql script for load census data to table  ')
ARGSCHEME.add_argument('inputfilefolder', help='input file folder')

ARGSCHEME.add_argument('-f', '--filename', help='output sql file name (option)')
ARGSCHEME.add_argument('-t', '--tablename', help='output table name (option)')
ARGSCHEME.add_argument('-w', '--workfolder', help='work folder name (option)')
ARGSCHEME.add_argument('-s', '--schema', help='schema name (option)')
