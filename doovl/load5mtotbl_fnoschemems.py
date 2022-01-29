# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='create sql script for load 5m mesh data to tbl  ')
ARGSCHEME.add_argument('csvpath', help='result csv path')

ARGSCHEME.add_argument('-p', '--parameterfile', help='parameter file')
ARGSCHEME.add_argument('-s', '--schema', help='database schema name ')
ARGSCHEME.add_argument('-w', '--workfolder', help='work folder name (option)')
ARGSCHEME.add_argument('-o', '--outputfile', help='output file  name (option)')
ARGSCHEME.add_argument('-l', '--logfile', help='log file  name (option)')
