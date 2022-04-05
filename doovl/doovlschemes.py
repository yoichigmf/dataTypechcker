# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='create overlay script  ')
ARGSCHEME.add_argument('paramfile', help='parameter file name')

ARGSCHEME.add_argument('-w', '--workfolder', help='work folder name ')
ARGSCHEME.add_argument('-t', '--thirdmesh', help='sthier mesh file ( option) ')
ARGSCHEME.add_argument('-A', '--ATTRIBUTE', help='output attribute name ')
ARGSCHEME.add_argument('-l', '--logfile', help='logfile name ')
