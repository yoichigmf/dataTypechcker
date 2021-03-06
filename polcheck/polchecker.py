# coding: UTF-8
#
#    shape file data checker
#
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


def   checkPolygonFiles( inputfile  , outputfile, resultfile):

    #daShapefile = r"G:\work\NHK_kumamoto\210909HDD\kumamoto\430005kumamotoken\その1\1 筑後川\L1\MAXALL.SHP"
    #daShapefile = r"C:\Temp\Voting_Centers_and_Ballot_Sites.shp"
    #daShapefile = unicode(inputfile, 'cp932') 
    
    daShapefile = toUnicode(inputfile) 
    driver = ogr.GetDriverByName('ESRI Shapefile')

    dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

    ofile = sys.stdout
   


# Check to see if shapefile is found.
    if dataSource is None:
        print( 'Could not open ' + inputfile)
        print ('could not open  %s' % (daShapefile), file=sys.stderr)
    else:
        print ('Opened %s' % (daShapefile))
        print ('Opened %s' % (daShapefile), file=sys.stderr)
        layer = dataSource.GetLayer()
        featureCount = layer.GetFeatureCount()
        #print "Number of features in %s: %d" % (os.path.basename(daShapefile),featureCount)

        layer_defn = layer.GetLayerDefn()

        fcount = layer_defn.GetFieldCount()
        #  field 数取得

        if fcount > 0:
        #if 
               keyname = layer_defn.GetFieldDefn(0).GetName()
        #print(keyname )
               layer.ResetReading()

               for feature in layer:
                    tgdata = feature. GetField(keyname)
            #print( feature. GetField(keyname))
                    tgeometry = feature.GetGeometryRef()

                    geomname =  tgeometry.GetGeometryName()
            
                    if geomname != "POLYGON" and geomname != "MULTIPOLYGON" :

                        output_str = "-2," + toUnicode(inputfile) + "," + geomname + "\n"

                        if outputfile is not None:
                            with open(toUnicode(outputfile), "a") as of:
                                of.write(output_str)
                        else:
                            print(output_str)



                        result_str =  "-2," + toUnicode(inputfile) +  "," + " " + "," + geomname + " \n"

                        if resultfile is not None:
                            with open(toUnicode(resultfile), "a") as rf:
                                rf.write(result_str )
                        else:
                            print(result_str)
            
                        break


                    if isinstance(tgdata, int):
                        tglength = len(str(tgdata))
                          
                        if tglength != 13 and  tglength != 15 :
                            tglength = -1 

                        output_str = str(tglength)+ "," + toUnicode(inputfile) + "\n"

                        if outputfile is not None:
                            with open(toUnicode(outputfile), "a") as of:
                                of.write(output_str)
                        else:
                            print(output_str)

                        result_str =  str(tglength)+ "," + toUnicode(inputfile) +  "," + " " + ","+ str(tgdata) + "\n"

                        if resultfile is not None:
                            with open(toUnicode(resultfile), "a") as rf:
                                rf.write(result_str )
                        else:
                            print(result_str)
            
                        break
                    elif isinstance(tgdata, str):
                        tglength = len(tgdata)

                        if tglength != 13 and  tglength != 15 :
                            tglength = -1 

                        output_str = str(tglength)+ "," + toUnicode(inputfile) + "\n"

                        if outputfile is not None:
                            with open(toUnicode(outputfile), "a") as of:
                                of.write(output_str)
                        else:
                            print(output_str)

                        result_str =  str(tglength)+ "," + toUnicode(inputfile) +  "," + " " + ","+ str(tgdata) + ",string \n"

                        if resultfile is not None:
                            with open(toUnicode(resultfile), "a") as rf:
                                rf.write(result_str )
                        else:
                            print(result_str)

                        break
                    elif isinstance(tgdata, float):
                        tglength  = -1
                        output_str = str(tglength)+ "," + toUnicode(inputfile) + "\n"

                        if outputfile is not None:
                            with open(toUnicode(outputfile), "a") as of:
                                of.write(output_str)
                        else:
                            print(output_str)

                        #result_str =  str(tglength)+ "," + toUnicode(inputfile) +  "," +toUnicode( keyname ) + ",,type float \n"


                        result_str =  str(tglength)+ "," + toUnicode(inputfile) +  "," +"   " + ",,type float \n"

                        if resultfile is not None:
                            with open(resultfile, "a") as rf:
                                #print(result_str)
                                rf.write(result_str )
                        else:
                            print(result_str)

                        break


                    else:
                        tglength  = -1
                        output_str = str(tglength)+ "," + toUnicode(inputfile) + "\n"

                        if outputfile is not None:
                            with open(toUnicode(outputfile), "a") as of:
                                of.write(output_str)
                        else:
                            print(output_str)

                        result_str =  str(tglength)+ "," + toUnicode(inputfile) +  "," + " "+ ","+ str(tgdata) + ",type unknown \n"

                        if resultfile is not None:
                            with open(toUnicode(resultfile), "a") as rf:
                                rf.write(result_str )
                        else:
                            print(result_str)

                        break
        else:
            tglength  = -1
            output_str = str(tglength)+ "," + toUnicode(inputfile) + "\n"

            if outputfile is not None:
                with open(toUnicode(outputfile), "a") as of:
                     of.write(output_str)
            else:
                print(output_str)

            result_str =  str(tglength)+ "," +toUnicode(inputfile) +  "," + "  " + ",,no field \n"

            if resultfile is not None:
                with open(toUnicode(resultfile), "a") as rf:
                    rf.write(result_str )
            else:
                print(result_str)

       





if __name__ == "__main__":
    import polchkargschemes

    #print("initializing...")

    args = polchkargschemes.ARGSCHEME.parse_args()

    input_file = args.inputfile
    output_file  = args.output_file
    result_file  = args.result

    checkPolygonFiles( input_file, output_file, result_file  )

