# -*- coding: utf-8 -*-
import sys

import fileinput
import codecs
import csv


def   MakeOvlBat( inputfile  ):
     ln = 0


     with open( inputfile, mode="r", encoding='shift_jis' ) as fp:

         cin = csv.reader(fp)
         
         
         for row in cin:
         
             num = row[0]
             shape = row[1]
             
             tgp = "G:/work/NHK_kumamoto/dataTypechecker/clip2/cp" + num + ".csv"
             
             #print( num )
             #print( tgp )
             #print( shape )
             
             with open(  tgp, mode="r" ,encoding='shift_jis' ) as np:
             
                   ncnin = csv.reader(np )
                   
                   for nrow in ncnin:
                        
                       if nrow[1] != "code":
                 
                 
                 
                            result_f =  "rf" + num + "_" + nrow[1] + ".csv" 
                            
                            cmd_str = "qgis_process-qgis run qgis:clip -- INPUT=\"" + "G:/work/NHK_kumamoto/mesh/gpkg/" + nrow[1] + ".gpkg|layername=" + nrow[1] + "\" OUTPUT=\"G:/work/NHK_kumamoto/dataTypechecker/clip5/" + result_f + "\"  OVERLAY=\"" + shape + "\" "
                            #cmdstr = shape + " " + result_f
             
                            print( cmd_str )



if __name__ == "__main__":
    import makeovlschemes

    #print("initializing...")

    args =  makeovlschemes.ARGSCHEME.parse_args()

    input_file = args.inputfile

    MakeOvlBat( input_file )

