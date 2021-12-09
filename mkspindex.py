# -*- coding: utf-8 -*-
import sys

import fileinput
import codecs


def   Make2ndBat( inputfile  ):
     ln = 0



#fp = sys.stdin
     with open( inputfile, mode="r", encoding='shift_jis' ) as fp:
     
#print("[\n")
#fd = open("l2nlist.csv", "w")

         tid = 0

         while True:
             s_line = fp.readline()
             #print(s_line)
             if not s_line:
                 break

        
    
             
             fname =  "G:\\work\\NHK_kumamoto\\dataTypechecker\\crtspindex\\c" + str(tid) + ".bat"
        #pf = open( fname , "w" )
             with open(fname, 'w', encoding='shift_jis') as f:
                    f.write( s_line)
        #print(datal,file=pf)

             tid = tid + 1
    
  
        #pf.close
  


#print("]\n")s



if __name__ == "__main__":
    import clip_2ndbatschemes

    #print("initializing...")

    args =  clip_2ndbatschemes.ARGSCHEME.parse_args()

    input_file = args.inputfile

    Make2ndBat( input_file )

