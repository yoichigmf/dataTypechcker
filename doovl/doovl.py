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


       

#  指定オーバーレイ結果ファイルのレコード数チェック
#     レコード数 0 の場合指定領域外
#     　　パラメータファイルノ書き直し   範囲外データを除去する
#

     
def chk_area( param_file,  ovl3rdpath,  newparam,   attrflag ):

    with open( param_file , mode="r", encoding='cp932' ) as prmf:


         count = 0
    
         with open( newparam, mode="w", encoding='cp932' ) as newp:

                 csvreader = csv.reader( prmf )

                 driver = ogr.GetDriverByName('GPKG')
                 for  s_line in csvreader:

                     fname = s_line[0]
                     ifname = ovl3rdpath + "/" + fname + ".gpkg"

                     dataSource = driver.Open(ifname, 0)

                     if dataSource is None:
                          print ('Could not open %s' % (ifname))
                     else:
                          #print( 'Opened %s' % (ifname))
                          layer = dataSource.GetLayer()
                          featureCount = layer.GetFeatureCount()
                          print ("Number of features in %s: %d" % (ifname,featureCount))

                          if featureCount > 0:
                               count = count + 1

                    # layer = dataSource.GetLayer()
                    # print( ifname )

         print( "Number of data contain  %d" % (count))
           # cmd_str = "qgis_process-qgis-ltr run native:fixgeometries  -- INPUT=\"" + tgfname + "\" OUTPUT=\"" + input_path + fname + "\"" 


#  指定オーバーレイ結果ファイルのレコード数チェック
#     レコード数 0 の場合指定領域外
#     　　パラメータファイルノ書き直し   範囲外データを除去する
#

     
def chk_extent( param_file,  input_path,  newparam,   attrflag ):

    with open( param_file , mode="r", encoding='cp932' ) as prmf:


         count = 0
    
         with open( newparam, mode="w", encoding='cp932' ) as newp:

                 csvreader = csv.reader( prmf )

                 driver = ogr.GetDriverByName('GPKG')
                 for  s_line in csvreader:

                     fname = s_line[0]
                     ifname = input_path + "/" + fname + ".gpkg"

                     dataSource = driver.Open(ifname, 0)

                     if dataSource is None:
                          print ('Could not open %s' % (ifname))
                     else:
                          #print( 'Opened %s' % (ifname))
                          layer = dataSource.GetLayer()
                          featureCount = layer.GetFeatureCount()
                          extent = layer.GetExtent()
                          spatialRef = layer.GetSpatialRef()
                          spatialRef.AutoIdentifyEPSG()

                          feature = layer.GetNextFeature()
                          geometry = feature.GetGeometryRef()





                          print ("Number of features in %s: %d  %f %f %f %f %s %s" % (ifname,featureCount,extent[0],extent[1],extent[2],extent[3], spatialRef.GetName(),geometry.GetGeometryName()))

                          if featureCount > 0:
                               count = count + 1

                    # layer = dataSource.GetLayer()
                    # print( ifname )

         print( "Number of data contain  %d" % (count))
           # cmd_str = "qgis_process-qgis-ltr run native:fixgeometries  -- INPUT=\"" + tgfname + "\" OUTPUT=\"" + input_path + fname + "\"" 



def  make_paramfile( inputfile, paramfile ):


    #sys.stdin  = codecs.getreader('shift_jis')(sys.stdin)
    #ifile = sys.stdin

 
    prmfile = open( paramfile , mode="w", encoding='cp932' )

    
    ifile = open( inputfile, mode="r", encoding='cp932' )


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

    with open( param_file , mode="r", encoding='cp932' ) as prmfile:

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

    with open( param_file , mode="r", encoding='cp932' ) as prmfile:

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

    with open( param_file , mode="r", encoding='cp932' ) as prmfile:

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

    with open( param_file , mode="r", encoding='cp932' ) as prmfile:

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


def make_thirdmesh_tables( thirdmesh, schema , ofp ):

    driver = ogr.GetDriverByName('GPKG')
    dataSource = driver.Open(thirdmesh, 0)

    if dataSource is None:
        print ('Could not open %s' % (ifname))
    else:
                          #print( 'Opened %s' % (ifname))

        cstr = "drop schema  if exists \"" + schema + "\"  cascade;\n"
        ofp.write(cstr )

        sctr = "create schema \"" + schema + "\";\n" 

        ofp.write(sctr)

        layer = dataSource.GetLayer()
        #featureCount = layer.GetFeatureCount()
        #extent = layer.GetExtent()
        #spatialRef = layer.GetSpatialRef()
        for feature in layer:
            code = feature.GetField("code")

            tablename = "\"" + schema + "\".\"" + code + "\""

            dropstr = "drop table if exists " + tablename + ";\n"
            ofp.write( dropstr )

            ofp.write("create table if not exists " + tablename + "\n" )
            ofp.write( "(\n")
            ofp.write( "ogc_fid serial,\n")
            ofp.write( "code character varying COLLATE pg_catalog.\"default\",\n")
            #ofp.write( "code character ,\n")
            ofp.write( "SSS real ,\n")
            ofp.write( "SSS_RANK  integer ,\n")
            ofp.write( "primary key( ogc_fid)\n")            
            ofp.write( ");\n\n")




        #print( str(featureCount))


def create_5msql( thirdmesh, schema , ofp ):
    driver = ogr.GetDriverByName('GPKG')
    dataSource = driver.Open(thirdmesh, 0)

    if dataSource is None:
        print ('Could not open %s' % (ifname))
    else:
                          #print( 'Opened %s' % (ifname))


        #ofp.write(sctr)

        layer = dataSource.GetLayer()

        for feature in layer:
            code = feature.GetField("code")
            tablename = "\"" + schema + "\".\"" + code + "\""

            view1name = "\"" + schema + "\".\"mv" + code + "\""
        
            view2name = "\"" + schema + "\".\"map" + code + "\""

            dropindex2 = "drop index if exists  idx_map_" + code + " ;\n"

            ofp.write( dropindex2  )

            dropstr2 = "drop view if exists " + view2name + ";\n"
            ofp.write( dropstr2 )       


            dropindex = "drop index if exists  idx_mv_" + code + " ;\n"

            ofp.write( dropindex  )

            dropstr = "drop view if exists " + view1name + ";\n"
            ofp.write( dropstr )

            cstr = "create  MATERIALIZED VIEW " + view1name + " as\n" 
            dstr = " select code, max(SSS) SSS,max(SSS_Rank) SSS_Rank FROM " + tablename + " group by code;\n"

  

            ofp.write( cstr )
            ofp.write( dstr )  

            # index

            
            indexstr = "create unique index idx_mv_" + code + " \n"
            indexstr2 = "on  " + view1name + " (code) ;\n"
          

            ofp.write( indexstr )
            ofp.write( indexstr2 )

            cstr1 = "create  MATERIALIZED VIEW " + view2name + " as\n" 
            cstr2 = "select t1.ogc_fid, t1.code, t1.fcode, v1.SSS, v1.SSS_Rank, t1.wkb_geometry \n"

            cstr3 = "  from \"mesh\".\"" + code + "\" t1," + view1name +  " v1 \n"
            cstr4 = "    where  t1.code = v1.code; \n"
            ofp.write( cstr1 )
            ofp.write( cstr2 )
            ofp.write( cstr3 )
            ofp.write( cstr4 )

            indexstr = "create unique index idx_map_" + code + " \n"
            indexstr2 = "on  " + view2name + " (ogc_fid) ;\n"
            
            ofp.write( indexstr )
            ofp.write( indexstr2 )
            ofp.write( " \n" )

            
  


        

        

def load_csv_tables( csv_path, schema, ofp ):

    #print(csv_path) 

    files = glob.glob( csv_path + "/*.csv")
    for file in files:
         basename = os.path.basename(file)
         #print(basename)
         meshno = basename[7:15]
        # print( meshno )
         #nfile = file
         nfile =  file.replace("\\", "/")

         istr = "\\copy \"" + schema + "\".\"" + meshno + "\" (code,SSS,SSS_Rank) from " + "\'" + nfile + "\'  WITH CSV HEADER;\n"

         ofp.write( istr )
         #print( istr )

def dummy( param_file , input_path):
    print( param_file )
       #  フォルダが無ければ作る

    #if not os.path.exists(input_path ):
    #    os.mkdir(input_path)

    with open( param_file , mode="r", encoding='cp932' ) as prmfile:

        csvreader = csv.reader( prmfile )

        for  s_line in csvreader:

            fname = s_line[0]
            tgfname = s_line[1]

            cmd_str = "qgis_process-qgis-ltr run native:fixgeometries  -- INPUT=\"" + tgfname + "\" OUTPUT=\"" + input_path + fname + "\"" 

            print( cmd_str )
            #subprocess.run(cmd_str, shell=True)


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

