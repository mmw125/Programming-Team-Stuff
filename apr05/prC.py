import operator as op
import functools


def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = functools.reduce(op.mul, range(n, n-r, -1))
    denom = functools.reduce(op.mul, range(1, r+1))
    return numer//denom


if __name__ == '__main__':
    width, height = map(int, input().split(' '))
    print(int(ncr(width + height, width)) % (10 ** 9 + 7))
