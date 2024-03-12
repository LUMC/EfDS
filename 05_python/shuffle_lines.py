from random import *   
import sys


def shuffle_lines(fileread,filewrite):                    # Note: write this file first with one of the writing examples
    with open(file=fileread, mode="r") as f:     # Note: now mode="r" for reading access!!!
        lines = f.readlines()                    # Texts from all lines of the file will be read and returned as a list
    copiedlines = lines.copy()  
    shuffle(copiedlines)
    for i in range(len(copiedlines)):
        print( " ".join( copiedlines ) )
    with open(file=filewrite, mode="w") as g:
        for l in copiedlines:
            g.write( l )                         # Let's use the write method of f, instead of the print command 
            
if __name__ == "__main__":                  # a suggested way to define the main part of a script
    print( "Hello, world!" )
    if len(sys.argv) != 3:
        raise Exception("Number of argument not 2")
    fileread,filewrite = sys.argv[1:]
    print(fileread,filewrite)
    shuffle_lines(fileread,filewrite)