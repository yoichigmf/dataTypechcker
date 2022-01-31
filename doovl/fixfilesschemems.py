# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='create overlay script  ')
ARGSCHEME.add_argument('paramfile', help='parameter file name')

ARGSCHEME.add_argument('-w', '--workfolder', help='work folder name ')
ARGSCHEME.add_argument('-l', '--logfilename', help='log file name (option)')
