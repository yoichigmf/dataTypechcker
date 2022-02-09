# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='create overlay script  ')
ARGSCHEME.add_argument('ischema', help='input view schema name')

ARGSCHEME.add_argument('-o', '--output', help='output file name ')
ARGSCHEME.add_argument('-s', '--schema', help='schema name ')
ARGSCHEME.add_argument('-t', '--tablename', help='output table name ')
#ARGSCHEME.add_argument('-l', '--logfile', help='logfile  file name (option)')
