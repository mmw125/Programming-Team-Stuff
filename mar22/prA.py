

# if __name__ == '__main__':
#     num_nodes, num_edges = map(int, input().split(' '))
#     edges = num_edges * [num_edges * [None]]
#     for _ in range(num_edges):
#         s, e, d = map(int, input().split(' '))
#         edges[s][e] = d
#         edges[e][s] = d
#     nodes = num_nodes * [9999999999999999999999999, None]

import heapq
import collections
import sys
dist = collections.defaultdict(lambda : sys.maxsize)
pred = {}
queue = []
start = 0
adj = collections.defaultdict(list)
goal = -1
sweat_if_we_walk = 0

def put_on_queue(node_dist):
   heapq.heappush(queue, node_dist)

def remove_from_queue():
    return heapq.heappop(queue)

def get_neighbors(node):
    return adj[node]


def read_input():
    global end
    global goal
    global start
    global fact_map
    global initial
    global adj
    global queue
    global dist
    import sys
    global pred
    queue = []
    adj = collections.defaultdict(list)
    n = int(raw_input())
    points = {}
    start = n
    goal = n + 1
    dist = [sys.maxint for _ in range(n+2)]
    pred = [sys.maxint for _ in range(n+2)]
    for idx in xrange(n + 2):
        (x,y) = map(int, raw_input().split())
        points[idx] = (x,y)
        adj[idx] = []
        for idx2 in adj.keys():
            if idx == idx2:
                continue
            otherx, othery = points[idx2]
            import math
            sq_dist = (x-otherx)**2 + (y-othery)**2
            adj[idx2].append((idx,sq_dist))
            adj[idx].append((idx2,sq_dist))
    global sweat_if_we_walk
    sweat_if_we_walk = 0
    for neighbor in adj[start]:
        if neighbor[0] == goal:
            sweat_if_we_walk = neighbor[1]
            break

def main():
    read_input()
    put_on_queue((0, start))
    dist[start] = 0
    while len(queue) > 0:
        (cur_dist, node) = remove_from_queue()
        if node == goal:
            path = []
            while node != start:
                path.append(node)
                node = pred[node]
            path = path[1:]
            if len(path) == 0:
                print('-')
            else:
                for p in reversed(path):
                    print(p)
            return
        if dist[node] < cur_dist:
            continue
        if cur_dist > sweat_if_we_walk:
            continue
        for (neighbor, edge) in get_neighbors(node):
            if dist[neighbor] > cur_dist + edge:
                dist[neighbor] = cur_dist + edge
                pred[neighbor] = node
                put_on_queue((cur_dist + edge, neighbor))
    print('invalid!!!')

main()