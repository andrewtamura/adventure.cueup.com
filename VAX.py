'''
Cue Adventure
http://adventure.cueup.com/

Andrew Tamura
March 15, 2013

'''

import math

def main():
    initial_seed = 6
    for i in range(10):
        result = VAXrand(initial_seed)
        print "x_%d: %d. Seed: %d" % (i+1, result%36, initial_seed)
        initial_seed = result

def VAXrand(seed):
    num = (69069*seed + 1) % math.pow(2,32)
    return int(num)

if __name__ == "__main__":
    main()
