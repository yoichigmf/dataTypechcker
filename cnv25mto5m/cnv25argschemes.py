# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='script convert 25m mesh id to 5m mesh id  ')
#ARGSCHEME.add_argument('inputfile', help='input file name')

ARGSCHEME.add_argument('-i', '--inputfile', help='input file name  (option)')
ARGSCHEME.add_argument('-o', '--outputfile', help='output  file name (option)')
