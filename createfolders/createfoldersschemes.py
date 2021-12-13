# coding: UTF-8
import argparse

ARGSCHEME = argparse.ArgumentParser( description='make folders for calculate stat e prefecture')

ARGSCHEME.add_argument('prefname', help='<pref name>')

ARGSCHEME.add_argument('-d', '--dbhost', help='db host  (option)')
ARGSCHEME.add_argument('-b', '--basedir', help='base folder  (option)')
ARGSCHEME.add_argument('-t', '--testmode', help='execute in test mode (option)')

