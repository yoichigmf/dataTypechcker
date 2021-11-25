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

#     単一コードの変換
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


       
def   CnvCode( inputfile, outputfile  ):

    ofile = sys.stdout
    ifile = sys.stdin

    if outputfile  is not None:
        ofile = open( outputfile, mode="w")

    if inputfile is not None:
        ifile = open( inputfile, mode="r")


    for s_line in ifile:

        concode =  changecode(  s_line  )

        for nid in concode:
            print( nid, file=ofile)
    
    if outputfile  is not None:
        ofile.close()

    if inputfile is not None:
        ifile.close()




if __name__ == "__main__":
    import cnv25argschemes

    #print("initializing...")

    args = cnv25argschemes.ARGSCHEME.parse_args()

    input_file = args.inputfile
    output_file  = args.outputfile
    #result_file  = args.result
    CnvCode( input_file, output_file  )

    #inputcode = "4931506430123"

    #＃ret_list = changecode( inputcode )

    #print(ret_list)

