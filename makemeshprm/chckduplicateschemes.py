# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='make mesh parameter from mesh vector')

ARGSCHEME.add_argument('-c', '--configfile', help='config file name (option)')

ARGSCHEME.add_argument('-b', '--basedir', help='base folder  (option)')

ARGSCHEME.add_argument('-o', '--outputfile', help='outpu file name  (option)')
ARGSCHEME.add_argument('-t', '--testmode', help='execute in test mode (option)')

