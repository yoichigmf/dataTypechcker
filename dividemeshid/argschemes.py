# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='divide 25m mesh id to 5m mesh id ')
#ARGSCHEME.add_argument('inputfile', help='input file name')

ARGSCHEME.add_argument('-i', '--input_file', help='input file name (option)')
ARGSCHEME.add_argument('-o', '--output_file', help='output  file name (option)')
