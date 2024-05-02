import sys
import math
from statistics import *  
from random import *   
    
def gen_norm(filename,size,mu,sd):
    try:
        size = int(size)
        mu = float(mu)
        sd = float(sd)
    except:
        print("size, mu, sd has to integer or float")
    vs = [gauss(mu=mu, sigma=sd) for i in range(size)]
    with open(file=filename, mode="w") as f:
        for l in vs:
            f.write( str(l) )                         # Let's use the write method of f, instead of the print command
            f.write( "\n" )
    print(f"Size:   {size}")
    print(f"Mean:   requested = {mu}, generated = {mean(vs)}")
    print(f"Stddev: requested = {sd}, generated = {stdev(vs)}")

if __name__ == "__main__":                  # a suggested way to define the main part of a script
    print( "Hello, world!" )
    # for a in sys.argv:                      # sys.argv contains the script name
    #     print(a)
    if len(sys.argv) != 5:
        raise Exception("Number of argument not 4")
    filename,size,mu,sd = sys.argv[1:]
    print(filename,size,mu,sd)
    print(type(size))
    gen_norm(filename,size,mu,sd)