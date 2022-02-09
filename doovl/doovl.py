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

import datetime
import tempfile
import shutil


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
#     　
#

     
def chk_extent( param_file,  input_path,    attrflag ):

    with open( param_file , mode="r", encoding='cp932' ) as prmf:


        count = 0
    
         #with open( newparam, mode="w", encoding='cp932' ) as newp:

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





                print (" %s: %d  %f %f %f %f %s %s" % (ifname,featureCount,extent[0],extent[1],extent[2],extent[3], spatialRef.GetName(),geometry.GetGeometryName()))

                if featureCount > 0:
                    count = count + 1

                    # layer = dataSource.GetLayer()
                    # print( ifname )

        print( "Number of data contain  %d" % (count))
           # cmd_str = "qgis_process-qgis-ltr run native:fixgeometries  -- INPUT=\"" + tgfname + "\" OUTPUT=\"" + input_path + fname + "\"" 



def  make_paramfile( inputfile, paramfile , csvpos):


    #sys.stdin  = codecs.getreader('shift_jis')(sys.stdin)
    #ifile = sys.stdin

 
    prmfile = open( paramfile , mode="w", encoding='cp932' )

    
    ifile = open( inputfile, mode="r", encoding='cp932' )


    csvreader = csv.reader( ifile )
    

    fid = 1
    for s_line in csvreader:



        mstr = f'{fid:05}'
        
        outstr = 'f' + mstr + "," + s_line[csvpos]
        
        #print( outstr )
        
        print( outstr, file=prmfile)
            
        fid = fid + 1
        
    prmfile.close()

    if inputfile is not None:
        ifile.close()


def isNumeric(parameter):
    if not parameter.isdecimal():
        try:
            float(parameter)
            return True
        except ValueError:
            return False
    else:
        return True

def  csv_mod( csvfile ):


    #sys.stdin  = codecs.getreader('shift_jis')(sys.stdin)
    #ifile = sys.stdin

 
    #prmfile = open( paramfile , mode="w", encoding='cp932' )
    fp = tempfile.NamedTemporaryFile(mode='w', encoding='cp932', delete=False)
    
    fname = fp.name

    with open( csvfile , mode="r", encoding='cp932' ) as  ifile:


    #csvreader = csv.reader( ifile )
    

        iflag = False
        
        fid = 0
        for s_line in ifile:

            
            if fid > 0 :

                sl = s_line.split(',')

                ns=sl[1].replace('"','')

                
                if not isNumeric(ns):
                    #print( "not numeric" )
                    #print( ns )
                    n_line = sl[0]+ ",\"0\","+ sl[2] 

                    iflag = True
                    fp.write( n_line )

                else:
                    fp.write( s_line )
            else:
                fp.write( s_line )

            fid = fid + 1

        #print( fname )
        fp.close()
        if iflag:

            nfname = csvfile  + ".csv"
            shutil.copy(fname, csvfile )
        #os.rename( fname, "sample.csv")


            #print( s_line )

        #print( s_line[1])
        #mstr = f'{fid:05}'
        
        #outstr = 'f' + mstr + "," + s_line[csvpos]
        

def   FilterCSV( folder   ):

          
    files = glob.glob( folder + "/*.csv")
    for file in files:

        csvfname = os.path.basename( file )
        file_name =os.path.splitext( csvfname)[0]

        csv_mod( file )

        #print( file )


def make_fix( param_file , input_path, logfilename ):


    #  フォルダが無ければ作る

    if not os.path.exists(input_path ):
        os.mkdir(input_path)

    logf = None
    if logfilename  is not None:
        logf = open( logfilename, mode="a" )


    with open( param_file , mode="r", encoding='cp932' ) as prmfile:

        csvreader = csv.reader( prmfile )

        for  s_line in csvreader:

            fname = s_line[0]
            tgfname = s_line[1]

            cmd_str = "qgis_process-qgis-ltr run native:fixgeometries  -- INPUT=\"" + tgfname + "\" OUTPUT=\"" + input_path + fname + "\"" 

            #print( cmd_str )
            #res = subprocess.run(cmd_str, shell=True, capture_output=True, text=True)
            res = subprocess.run(cmd_str, shell=True, text=True)
            if res.returncode == 0:   
                if logf is not None:
                    put_log( logf, fname, tgfname, "fixgeometries",  "OK" )
            else:
                    put_log( logf, fname, tgfname, "fixgeometries",  "ERROR" )           

    if logf is not None:
        logf.close()


def make_intersect3rd( param_file , input_path, ovl3rdpath, thirdmesh ,attrflag, logfp):


    #  フォルダが無ければ作る

    if not os.path.exists(ovl3rdpath ):
        os.mkdir(ovl3rdpath)

    with open( param_file , mode="r", encoding='cp932' ) as prmfile:

        csvreader = csv.reader( prmfile )

        for  s_line in csvreader:
            fname0 = s_line[0] 
            fname = s_line[0] + ".gpkg"
            tgfname = s_line[1]

            cmd_str = "qgis_process-qgis-ltr run qgis:intersection    -- INPUT=\"" + thirdmesh  + "\" OVERLAY=\"" + input_path + fname + "\" INPUT_FIELDS=code OUTPUT=\""  + ovl3rdpath + fname0 + "\""

            if attrflag:
                cmd_str = cmd_str + " OVERLAY_FIELDS=SSS;SSS_Rank OVERLAY_FIELDS_PREFIX="
                #cmd_str = cmd_str + " OVERLAY_FIELDS= OVERLAY_FIELDS_PREFIX="
            else:
                cmd_str = cmd_str + " OVERLAY_FIELDS=None OVERLAY_FIELDS_PREFIX="

            #print( cmd_str )
            res = subprocess.run(cmd_str, shell=True,  text=True)

            if logfp is not None:
                if res.returncode == 0:  
                    put_log( logfp, fname0, tgfname, "intersect3rd",  "OK" )
                else: 

                    put_log( logfp, fname0, tgfname, "intersect3rd",  "ERROR"  )              


def make_split( param_file,  ovl3rdpath, ovlsep, attrflag, logfp ):


    #  フォルダが無ければ作る

    if not os.path.exists(ovlsep ):
        os.mkdir(ovlsep)

    with open( param_file , mode="r", encoding='cp932' ) as prmfile:

        csvreader = csv.reader( prmfile )

        for  s_line in csvreader:
            fname0 = s_line[0] 

            tgfname = s_line[1]

            tgpath = ovlsep + fname0
            if not os.path.exists( tgpath ):
                 os.mkdir(tgpath)

            fname = s_line[0] + ".gpkg"
            #tgfname = s_line[1]

            cmd_str = "qgis_process-qgis-ltr run  native:splitvectorlayer    -- INPUT=\"" + ovl3rdpath + fname  + "\" FIELD=code FILE_TYPE=0 OUTPUT=\""  + tgpath + "\""



            #print( cmd_str )
            res =  subprocess.run(cmd_str, shell=True,  text=True)

            if logfp is not None:
                if res.returncode == 0:  
                    put_log( logfp, fname0, tgfname, "split",  "OK" )
                else: 

                    put_log( logfp, fname0, tgfname, "split",  "ERROR"  )    





def make_5m( param_file,  ovlresult, ovlsep, thirdpath,  attrflag, logfp  ):


    #  フォルダが無ければ作る

    if not os.path.exists(ovlresult):
        os.mkdir(ovlresult)

    with open( param_file , mode="r", encoding='cp932' ) as prmfile:

        csvreader = csv.reader( prmfile )

        for  s_line in csvreader:
            fname0 = s_line[0] 

            tgfname = s_line[1]
            tgpath = ovlsep + fname0
            #if not os.path.exists( tgpath ):
            #     os.mkdir(tgpath)


            result_path =  ovlresult + fname0

            fname = s_line[0] + ".gpkg"
          
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


                 res = subprocess.run(cmd_str, shell=True,  text=True)

                 
                 if logfp is not None:
                   if res.returncode == 0:  
                       put_log( logfp, output_f, tgfname, "5movl",  "OK" )
                   else: 

                       put_log( logfp, output_f, tgfname, "5movl",  "ERROR"  )    

def make_4thesql( ischema,  schema,  tablename, outputfile,  thirdmesh ):

    driver = ogr.GetDriverByName('GPKG')
    dataSource = driver.Open(thirdmesh, 0)

    if dataSource is None:
        print ('Could not open %s' % (thirdmesh))


def make_thirdmesh_tables( thirdmesh, schema , ofp ):

    driver = ogr.GetDriverByName('GPKG')
    dataSource = driver.Open(thirdmesh, 0)

    if dataSource is None:
        print ('Could not open %s' % (thirdmesh))
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

def cnvpostgis_gpkg( thirdmesh, schema ,  dbhost, dbname, dbuser, dbpasswd, outputfolder ):
    driver = ogr.GetDriverByName('GPKG')
    dataSource = driver.Open(thirdmesh, 0)

    if dataSource is None:
        print ('Could not open %s' % (ifname))
    else:
                          #print( 'Opened %s' % (ifname))

        # folder が無ければ作成
        if not os.path.exists(outputfolder):
            os.mkdir(outputfolder)

        #ofp.write(sctr)

        layer = dataSource.GetLayer()

        for feature in layer:
            code = feature.GetField("code")

            #print( code )
            #geom = feature.GetGeometryRef()
            #extent = geom.GetEnvelope()
            #print( extent )
            #print( extent[2])

            gdalstr = "ogr2ogr  -f \"GPKG\" " + outputfolder + "/" + code + ".gpkg "
          
            gdalstr = gdalstr + "\"PG:dbname=\'" + dbname +"\' host=\'" + dbhost + "' port=5432 user=\'" + dbuser + "\' password=\'" + dbpasswd + "\' sslmode=disable\" "  
            #str(extent[0]) + " " + str(extent[2]) + " " + str(extent[1]) + " " + str(extent[3] )
            #130.7125 32.741666667 130.725 32.75" 
            #gdalstr = gdalstr +  " -ot " + fieldtype + " -of GTiff \"PG:dbname=\'" + dbname + "\' host=" + dbhost + " port=5432 user=\'" + dbuser + "\' password=\'" + dbpasswd + "\' sslmode=disable\"  "
            gdalstr = gdalstr + schema + ".map" + code 
            print( gdalstr )



def create_geotiff( thirdmesh, schema , ofield, fieldtype, dbhost, dbname, dbuser, dbpasswd, outputfolder ):
    driver = ogr.GetDriverByName('GPKG')
    dataSource = driver.Open(thirdmesh, 0)

    if dataSource is None:
        print ('Could not open %s' % (ifname))
    else:
                          #print( 'Opened %s' % (ifname))

        # folder が無ければ作成
        if not os.path.exists(outputfolder):
            os.mkdir(outputfolder)

        #ofp.write(sctr)

        layer = dataSource.GetLayer()

        for feature in layer:
            code = feature.GetField("code")

            #print( code )
            geom = feature.GetGeometryRef()
            extent = geom.GetEnvelope()
            #print( extent )
            #print( extent[2])

            gdalstr = "gdal_rasterize -l " + schema + ".map" + code + " -a " + ofield +  " -ts 100.0 100.0 -a_nodata 0.0 -te " 
            gdalstr = gdalstr + str(extent[0]) + " " + str(extent[2]) + " " + str(extent[1]) + " " + str(extent[3] )
            #130.7125 32.741666667 130.725 32.75" 
            gdalstr = gdalstr +  " -ot " + fieldtype + " -of GTiff \"PG:dbname=\'" + dbname + "\' host=" + dbhost + " port=5432 user=\'" + dbuser + "\' password=\'" + dbpasswd + "\' sslmode=disable\"  "
            gdalstr = gdalstr + outputfolder + "/" + ofield + code + ".tif"
            print( gdalstr )



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

            dropindex2 = "drop index if exists \"" + schema + "\".idx_map_" + code + " ;\n"

            ofp.write( dropindex2  )

            dropstr2 = "drop MATERIALIZED view if exists " + view2name + ";\n"
            ofp.write( dropstr2 )       


            dropindex = "drop index if exists \"" + schema +  "\".idx_mv_" + code + " ;\n"

            ofp.write( dropindex  )

            dropstr = "drop MATERIALIZED view if exists " + view1name + ";\n"
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

            
  
#   ログの出力
def  put_log( logfile, filename, rfilename, job,  message ):

    dt_now = datetime.datetime.now()

    dt_str = dt_now.isoformat()

    logfile.write( dt_str + "," + filename + "," + rfilename + "," + job + "," + message + "\n")
        

# パラメーターファイル指定  ファイル番号単位 CSV ロード        

def load_csv_tables_fileno( csv_path, pfile, schema, ofp, logf ):

    #print(csv_path) 
    
    
    with open( pfile , mode="r", encoding='cp932' ) as prmfile:

        csvreader = csv.reader( prmfile )

        for  s_line in csvreader:
            fname0 = s_line[0] 


            files = glob.glob( csv_path + "/" + fname0 + "*.csv")
            for file in files:
                 basename = os.path.basename(file)
                 #print(basename)
                 meshno = basename[7:15]
                 # print( meshno )
                 #nfile = file
                 nfile =  file.replace("\\", "/")

                 istr = "\\copy \"" + schema + "\".\"" + meshno + "\" (code,SSS,SSS_Rank) from " + "\'" + nfile + "\'  WITH CSV HEADER;\n"

                #put_log
                 ofp.write( istr )


                  #print( istr )

 
 
#  ディレクトリ指定　全ファイル用　CSVアップロードスクリプト作製       

def load_csv_tables_all( csv_path, schema, ofp ):

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


def   DoOverlay( param_file, workfolder,  logfile, attrflag   ):

    #  パラメータファイル名をユニークファイル名に変更  2022/1/7
    #unique_filename = str(uuid.uuid4())

    #param_file = "scripts/" + unique_filename + ".csv"

    input_path =  './workfiles/ovlinput/'
    ovl3rdpath = './workfiles/ovl3rd/'
    ovlsep  = './workfiles/ovlsplit/'
    ovlresult  = './workfiles/ovlresult/'

    if workfolder is not None:
        input_path = workfolder + "/ovlinput/"
        ovl3rdpath = workfolder + "/ovl3rd/"
        ovlsep = workfolder + "/ovlsplit/"
        ovlresult = workfolder + "/ovlresult/"


    thirdmesh = './3rdmesh/mesh3.gpkg'



    thirdpath = './3rdmesh/'



    csvpos = 1

    logfp = None

    if logfile is not None:
        logfp = open( logfile, mode="a")
    
    #  パラメータファイルの作成
    #make_paramfile( inputfile, param_file , csvpos)

    # ジオメトリ修復
    #make_fix( param_file, input_path )

     # 3次メッシュとのIntersect

    make_intersect3rd(  param_file, input_path, ovl3rdpath, thirdmesh, attrflag, logfp )


    #  3次メッシュコード別分割

    make_split( param_file,  ovl3rdpath, ovlsep, attrflag , logfp)

    # 5m mesh  overlay

    make_5m( param_file, ovlresult, ovlsep, thirdpath , attrflag , logfp )


    FilterCSV( ovlresult  )

    if logfile is not None: 
        logfp.close()



if __name__ == "__main__":
    import doovlschemes

    #print("initializing...")

    args = doovlschemes.ARGSCHEME.parse_args()

    paramfile = args.paramfile
    workfolder = args.workfolder
    #schema = args.schema
    logfile = args.logfile

    attrflag = True
    DoOverlay( paramfile, workfolder,  logfile, attrflag   )

