import sys
sys.setrecursionlimit(100000)

a, b = raw_input(), raw_input()
arr = [[None for __ in a] for _ in b]

def lcs(i, j):
    if i >= len(a) or j >= len(b):
        return 0
    if arr[j][i] is None:
        arr[j][i] = max(lcs(i + 1, j), lcs(i, j + 1), int(a[i] == b[j]) + lcs(i + 1, j + 1))
    return arr[j][i]

print(lcs(0, 0))