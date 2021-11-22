# coding: UTF-8
#
#    shape file data checker
#
#

import os
import sys
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

def    dump_id( inputfile, output_file,  field_name ):
    
    #daShapefile = toUnicode(inputfile) 
    dataFile = toUnicode(inputfile) 
    #driver = ogr.GetDriverByName('ESRI Shapefile')

    #dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.
    dataSource = ogr.Open(dataFile ,0)
    ofile = sys.stdout
   

    if output_file is not None:
        ofile = open( output_file, mode="a")




# Check to see if shapefile is found.
    if dataSource is None:
        print( 'Could not open ' + inputfile, file=sys.stderr)
    else:
        #print ('Opened %s' % (daShapefile))
        layer = dataSource.GetLayer(0)
        featureCount = layer.GetFeatureCount()
        #print "Number of features in %s: %d" % (os.path.basename(daShapefile),featureCount)

        layer_defn = layer.GetLayerDefn()

        fcount = layer_defn.GetFieldCount()
        #  field 数取得

        if fcount > 0:
        #if 
               keyname =  field_name

               if keyname is None:
              
                    keyname = layer_defn.GetFieldDefn(0).GetName()
        #print(keyname )
               layer.ResetReading()

               for feature in layer:
                    tgdata = feature. GetField(keyname)
            #print( feature. GetField(keyname))
                    print( tgdata , file=ofile)

                    #if isinstance(tgdata, int):
                    #    tglength = len(str(tgdata))









if __name__ == "__main__":
    import idlistargschemes

    #print("initializing...")

    args = idlistargschemes.ARGSCHEME.parse_args()

    input_file = args.inputfile
    output_file  = args.outputfile
    #result_file  = args.result
    field_name   = args.fieldname

    dump_id( input_file, output_file , field_name )

