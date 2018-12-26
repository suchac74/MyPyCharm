"""all combinations"""
import math


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


r = '''\
all possible queens combinations
'''
print(r)
print(nCr(64, 8))


"""all permutations"""
from math import factorial


def number_permutations(n, k):
    return factorial(n) / factorial(n - k)


q = '''\

How many ways can 8 queens on a chessboard
be positioned?
'''
print(q)
print(number_permutations(8, 8))
