# coding: UTF-8
#
#    doovl.py
#
#    do overlay using 3rd mesh
#
#     2022.1.6  Y.Kayama
#
import sys
import os
import unicodedata
import csv
import glob
import subprocess

import uuid

import codecs
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


       

     

def  make_paramfile( inputfile, paramfile ):


    #sys.stdin  = codecs.getreader('shift_jis')(sys.stdin)
    #ifile = sys.stdin

 
    prmfile = open( paramfile , mode="w", encoding='shift_jisx0213' )

    
    ifile = open( inputfile, mode="r", encoding='shift_jisx0213' )


    csvreader = csv.reader( ifile )
    

    fid = 1
    for s_line in csvreader:



        mstr = f'{fid:05}'
        
        outstr = 'f' + mstr + "," + s_line[1]
        
        #print( outstr )
        
        print( outstr, file=prmfile)
            
        fid = fid + 1
        
    prmfile.close()

    if inputfile is not None:
        ifile.close()


def make_fix( param_file , input_path):


    #  フォルダが無ければ作る

    if not os.path.exists(input_path ):
        os.mkdir(input_path)

    with open( param_file , mode="r", encoding='shift_jis' ) as prmfile:

        csvreader = csv.reader( prmfile )

        for  s_line in csvreader:

            fname = s_line[0]
            tgfname = s_line[1]

            cmd_str = "qgis_process-qgis-ltr run native:fixgeometries  -- INPUT=\"" + tgfname + "\" OUTPUT=\"" + input_path + fname + "\"" 

            #print( cmd_str )
            subprocess.run(cmd_str, shell=True)


def make_intersect3rd( param_file , input_path, ovl3rdpath, thirdmesh ,attrflag):


    #  フォルダが無ければ作る

    if not os.path.exists(ovl3rdpath ):
        os.mkdir(ovl3rdpath)

    with open( param_file , mode="r", encoding='shift_jis' ) as prmfile:

        csvreader = csv.reader( prmfile )

        for  s_line in csvreader:
            fname0 = s_line[0] 
            fname = s_line[0] + ".gpkg"
            #tgfname = s_line[1]

            cmd_str = "qgis_process-qgis-ltr run qgis:intersection    -- INPUT=\"" + thirdmesh  + "\" OVERLAY=\"" + input_path + fname + "\" INPUT_FIELDS=code OUTPUT=\""  + ovl3rdpath + fname0 + "\""

            if attrflag:
                cmd_str = cmd_str + " OVERLAY_FIELDS=SSS;SSS_Rank OVERLAY_FIELDS_PREFIX="
                #cmd_str = cmd_str + " OVERLAY_FIELDS= OVERLAY_FIELDS_PREFIX="
            else:
                cmd_str = cmd_str + " OVERLAY_FIELDS=None OVERLAY_FIELDS_PREFIX="

            #print( cmd_str )
            subprocess.run(cmd_str, shell=True)


def make_split( param_file,  ovl3rdpath, ovlsep, attrflag ):


    #  フォルダが無ければ作る

    if not os.path.exists(ovlsep ):
        os.mkdir(ovlsep)

    with open( param_file , mode="r", encoding='shift_jis' ) as prmfile:

        csvreader = csv.reader( prmfile )

        for  s_line in csvreader:
            fname0 = s_line[0] 

            tgpath = ovlsep + fname0
            if not os.path.exists( tgpath ):
                 os.mkdir(tgpath)

            fname = s_line[0] + ".gpkg"
            #tgfname = s_line[1]

            cmd_str = "qgis_process-qgis-ltr run  native:splitvectorlayer    -- INPUT=\"" + ovl3rdpath + fname  + "\" FIELD=code FILE_TYPE=0 OUTPUT=\""  + tgpath + "\""



            #print( cmd_str )
            subprocess.run(cmd_str, shell=True)


def make_5m( param_file,  ovlresult, ovlsep, thirdpath,  attrflag ):


    #  フォルダが無ければ作る

    if not os.path.exists(ovlresult):
        os.mkdir(ovlresult)

    with open( param_file , mode="r", encoding='shift_jis' ) as prmfile:

        csvreader = csv.reader( prmfile )

        for  s_line in csvreader:
            fname0 = s_line[0] 

            tgpath = ovlsep + fname0
            #if not os.path.exists( tgpath ):
            #     os.mkdir(tgpath)


            result_path =  ovlresult + fname0

            fname = s_line[0] + ".gpkg"
            #tgfname = s_line[1]

            #cmd_str = "qgis_process-qgis-ltr run qgis:intersection    -- INPUT=\"" + thirdmesh  + "\" OVERLAY=\"" + input_path + fname + "\" INPUT_FIELDS=code OUTPUT=\""  + ovl3rdpath + fname0 + "\""

            #if attrflag:
            #    cmd_str = cmd_str + " OVERLAY_FIELDS=SSS,SSS_Rank OVERLAY_FIELDS_PREFIX="
           # else:
            #    cmd_str = cmd_str + " OVERLAY_FIELDS= OVERLAY_FIELDS_PREFIX="



            #cmd_str = "qgis_process-qgis-ltr run  native:splitvectorlayer    -- INPUT=\"" + ovl3rdpath + fname  + "\" FIELD=code FILE_TYPE=0 OUTPUT=\""  + tgpath + "\""

            files = glob.glob(tgpath + "/*.gpkg")
            for file in files:

                 ovlfname = os.path.basename( file )
                 file_name =os.path.splitext( ovlfname)[0]

                 rf = file_name.split("_")

                 thirdmesh = rf[1]

                 tmesh = thirdpath + thirdmesh + ".gpkg"

                 output_f = ovlresult + fname0 + "_" + thirdmesh + ".csv"
                 cmd_str = "qgis_process-qgis-ltr run qgis:intersection  -- INPUT=\"" +  tmesh    + "\" OVERLAY=\"" + file  + "\" INPUT_FIELDS=code OUTPUT=\""  + output_f + "\""
                 
                 if attrflag:
                      cmd_str = cmd_str + " OVERLAY_FIELDS=SSS;SSS_Rank OVERLAY_FIELDS_PREFIX="
                      #cmd_str = cmd_str + " OVERLAY_FIELDS= OVERLAY_FIELDS_PREFIX="
                 else:
                      cmd_str = cmd_str + " OVERLAY_FIELDS=None OVERLAY_FIELDS_PREFIX="

                 print( cmd_str )

                 #print(rf[1])
            #cmd_str = "dir  " + tgpath + "\*.*"
            #print( cmd_str )
                 subprocess.run(cmd_str, shell=True)



def   DoOverlay( inputfile, attrflag  ):

    #  パラメータファイル名をユニークファイル名に変更  2022/1/7
    unique_filename = str(uuid.uuid4())

    param_file = "scripts/" + unique_filename + ".csv"

    input_path =  './workfiles/ovlinput/'

    ovl3rdpath = './workfiles/ovl3rd/'

    thirdmesh = './3rdmesh/mesh3.gpkg'

    ovlsep  = './workfiles/ovlsplit/'

    thirdpath = './3rdmesh/'

    ovlresult  = './workfiles/ovlresult/'
    #  パラメータファイルの作成
    make_paramfile( inputfile, param_file )

    # ジオメトリ修復
    make_fix( param_file, input_path )

     # 3次メッシュとのIntersect

    make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag )


    #  3次メッシュコード別分割

    make_split( param_file,  ovl3rdpath, ovlsep, attrflag )

    # 5m mesh  overlay

    make_5m( param_file, ovlresult, ovlsep, thirdpath , attrflag  )



if __name__ == "__main__":
    import doovlschemes

    #print("initializing...")

    args = doovlschemes.ARGSCHEME.parse_args()

    input_file = args.inputfile

    attrflag = True
    DoOverlay( input_file , attrflag )

