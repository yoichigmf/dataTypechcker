# coding: UTF-8
#
#    shape file data checker
#
#

import os
from osgeo import ogr


def   checkShapeFile( inputfile  ):

    #daShapefile = r"G:\work\NHK_kumamoto\210909HDD\kumamoto\430005kumamotoken\その1\1 筑後川\L1\MAXALL.SHP"
    #daShapefile = r"C:\Temp\Voting_Centers_and_Ballot_Sites.shp"
    daShapefile = unicode(inputfile, 'cp932') 
    driver = ogr.GetDriverByName('ESRI Shapefile')

    dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

# Check to see if shapefile is found.
    if dataSource is None:
        print 'Could not open %s' % (daShapefile)
    else:
        print 'Opened %s' % (daShapefile)
        layer = dataSource.GetLayer()
        featureCount = layer.GetFeatureCount()
        print "Number of features in %s: %d" % (os.path.basename(daShapefile),featureCount)

        layer_defn = layer.GetLayerDefn()

        keyname = layer_defn.GetFieldDefn(0).GetName()
        print(keyname )
        layer.ResetReading()

        for feature in layer:
            tgdata = feature. GetField(keyname)
            #print( feature. GetField(keyname))

            if isinstance(tgdata, long):
                print(len(str(tgdata)))
            #print( type(tgdata) )
            #print('Feature ID:', feature.GetFID())
        # get a metadata field with GetField('fieldname'/fieldindex)
            #print('Feature Metadata Keys:', feature.keys())
            #print('Feature Metadata Dict:', feature.items())
            #print('Feature Geometry:', feature.geometry())





if __name__ == "__main__":
    import argschemes

    print("initializing...")

    args = argschemes.ARGSCHEME.parse_args()

    input_file = args.inputfile

    checkShapeFile( input_file )

