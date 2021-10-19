# coding: UTF-8
#
#    shape file data checker
#
#
import sys
import os
from osgeo import ogr


def   checkShapeFile( inputfile  , outputfile, resultfile):

    #daShapefile = r"G:\work\NHK_kumamoto\210909HDD\kumamoto\430005kumamotoken\その1\1 筑後川\L1\MAXALL.SHP"
    #daShapefile = r"C:\Temp\Voting_Centers_and_Ballot_Sites.shp"
    daShapefile = unicode(inputfile, 'cp932') 
    driver = ogr.GetDriverByName('ESRI Shapefile')

    dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

    ofile = sys.stdout
   

# Check to see if shapefile is found.
    if dataSource is None:
        print 'Could not open %s' % (daShapefile)
    else:
        print 'Opened %s' % (daShapefile)
        layer = dataSource.GetLayer()
        featureCount = layer.GetFeatureCount()
        #print "Number of features in %s: %d" % (os.path.basename(daShapefile),featureCount)

        layer_defn = layer.GetLayerDefn()

        keyname = layer_defn.GetFieldDefn(0).GetName()
        #print(keyname )
        layer.ResetReading()

        for feature in layer:
            tgdata = feature. GetField(keyname)
            #print( feature. GetField(keyname))

            if isinstance(tgdata, long):
                tglength = len(str(tgdata))

                if tglength != 13 and  tglength != 15 :
                    tglength = -1 

                output_str = str(tglength)+ "," + unicode(inputfile, 'cp932') + "\n"

                if outputfile is not None:
                    with open(unicode(outputfile, 'cp932'), "a") as of:
                        of.write(output_str)
                else:
                    print(output_str)

                result_str =  str(tglength)+ "," + unicode(inputfile, 'cp932') +  "," + keyname + ","+ str(tgdata) + "\n"

                if resultfile is not None:
                    with open(unicode(resultfile, 'cp932'), "a") as rf:
                        rf.write(result_str )
                else:
                    print(result_str)
                


                break
       





if __name__ == "__main__":
    import argschemes

    #print("initializing...")

    args = argschemes.ARGSCHEME.parse_args()

    input_file = args.inputfile
    output_file  = args.output_file
    result_file  = args.result

    checkShapeFile( input_file, output_file, result_file  )

