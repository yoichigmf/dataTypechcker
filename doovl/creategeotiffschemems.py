# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='create sql script for load 5m mesh data to tbl  ')
ARGSCHEME.add_argument('schema', help='database schema name')

ARGSCHEME.add_argument('-t', '--type', help='field type')
ARGSCHEME.add_argument('-f', '--field', help='attribute field name ')
ARGSCHEME.add_argument('-w', '--workfolder', help='work folder name (option)')
ARGSCHEME.add_argument('-o', '--outputfolder', help='output folder name (option)')
