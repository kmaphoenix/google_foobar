## SUBMITTED SOLUTION ##

"""
lucky triples (tuples)

lucky_triple = tuple (x, y, z)
x divides y, y divides z - (1, 2, 4)

If there are 5 passcodes, need to find a list with 5 "lucky triples"
(Make a list of tuples?)

l = list of positive integers
count the # of lucky triples (li, lj, lk) where i < j < k
2 < l < 2000 (inclusive)

1 < l_elements < 999999 (inclusive)

Answer should be within signed 32-bit integer
Some lists have None access codes.
If None, return 0.

Example:
[1,2,3,4,5,6] has triples [1,2,4] [1,2,6] and [1,3,6]
"""

import time
import random

def solution(l):

    length = len(l)
    if length < 3:
        print(0)
        return 0

    lucky_triples = 0
    store = [0] * length

    i = 0
    while i < length:
        j = i + 1
        while j < length:
            if l[j] % l[i] == 0:
                store[j] += 1
                lucky_triples += store[i]
            j += 1
        i += 1
    
    print(lucky_triples)

if __name__ == '__main__':
    l = sorted([random.randint(1, 1000000) for x in range(2000)]) # big test
    # l = [1,2,3,4,5,6] # base test
    n = len(l)
    stime = time.time()
    solution(l)
    etime = time.time()
    print('{} took {} seconds'.format(n,(etime-stime)))