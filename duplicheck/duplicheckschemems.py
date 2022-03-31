# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='create sql script for check duplicate of 5mmesh mesh record   ')

ARGSCHEME.add_argument('filename',  help='output sql file ')

ARGSCHEME.add_argument('-s', '--schema', help='output result database schema name of ')

ARGSCHEME.add_argument('-t', '--tablename', help='output result  table name (option)')
#ARGSCHEME.add_argument('-w', '--workfolder', help='work folder name (option)')
#ARGSCHEME.add_argument('-o', '--outputfolder', help='output folder name (option)')
