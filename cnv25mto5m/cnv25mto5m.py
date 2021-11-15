# coding: UTF-8
#
#    cnv25mto5m
#
#    convert 25m mesh code to 5m codes
#
#     2021.11.15  Y.Kayama
#
import sys
import os
import unicodedata
from osgeo import ogr

def toUnicode(encodedStr):
    '''
    :return: an unicode-str.
    '''
    if isinstance(encodedStr, str):
        return encodedStr

    for charset in [u'cp932', u'utf-8', u'euc-jp', u'shift-jis', u'iso2022-jp']:
        try:
            return encodedStr.decode(charset)
        except:
            pass


def   changecode( inputcode  ):



    thirdm = inputcode[0:8]

    df = inputcode[8:9]

    yp = inputcode[9:11]
    xp = inputcode[11:13]

    #print(thirdm) 
    #print(df)
    #print(yp)
    #print(xp)

    basex = int(xp) * 8
    basey = int(yp) * 8

    div2 = "2"

    ret_list = list(range(64))

    idx = 0
    for iy in range(8):
        for ix in range(8):
            yyp = basey + iy
            xxp = basex + ix
      
            #print( yyp )
            #print( xxp )

            sty = '{:0=3}'.format( yyp)
            stx = '{:0=3}'.format( xxp)

            #print( sty )
            #print( stx )
            ncode = thirdm + div2 + sty + stx

            ret_list[idx] = ncode
            idx = idx + 1
            # print( ncode )

            #print( iy )
            #print( ix )
            #print( idx )

    return ret_list


       





if __name__ == "__main__":
    #import argschemes

    #print("initializing...")

    #args = argschemes.ARGSCHEME.parse_args()

    #input_file = args.inputfile
    #output_file  = args.output_file
    #result_file  = args.result

    inputcode = "4931506430123"

    ret_list = changecode( inputcode )

    print(ret_list)

