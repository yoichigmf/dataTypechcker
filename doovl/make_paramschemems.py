# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='create sql script for load 5m mesh data to tbl  ')
ARGSCHEME.add_argument('listfile', help='listfilename name')


ARGSCHEME.add_argument('-p', '--paramfilename', help='parameter file name')

