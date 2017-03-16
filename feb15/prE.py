from heapq import heappush, heappop, heapify
from collections import defaultdict
import collections

def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        num_canvases = int(input())
        canvases = {}
        count = 0
        canvas_sizes = map(int, input().split(' '))
        for canvas in canvas_sizes:
            canvases[count] = canvas
            count += i
        print(canvases)
        heapify(canvases)
        print(canvases)
    # while len(canvases) > 0:



