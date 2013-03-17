'''
Cue Adventure
http://adventure.cueup.com/

Bonus Question:

solve for a, c, or m in the LCG that results in the following:
34, 27, 16, 1, 34, 31, 24, 17, 34, 35, 16, 13

My guess is that a is fixed to be 69069 and m is 2^32

Andrew Tamura
March 15, 2013

'''

import math

def main():
    initial_seed = 34
    for i in range(10):
        result = VAXrand(initial_seed)
        print "x_%d: %d. Seed: %d" % (i+1, result%36, initial_seed)
        initial_seed = result

def VAXrand(seed):
    num = (69069*seed + 213) % math.pow(2,32)
    return int(num)

if __name__ == "__main__":
    main()
