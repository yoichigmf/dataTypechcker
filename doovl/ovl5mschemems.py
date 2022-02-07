# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='create overlay script  ')
ARGSCHEME.add_argument('paramfile', help='parameter file name')

ARGSCHEME.add_argument('-w', '--workfolder', help='workfolder name ')
ARGSCHEME.add_argument('-l', '--logfile', help='logfile  file name (option)')
