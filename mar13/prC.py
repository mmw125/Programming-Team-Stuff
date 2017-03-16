
if __name__ == '__main__':
    n_lines = int(raw_input())
    lines = [[int(s) for s in raw_input().split(' ') if s] for _ in xrange(n_lines)]
    sum_lines = []
    for y in xrange(n_lines):
        sum_lines.append([])
        for x in xrange(n_lines):
            up = sum_lines[y - 1][x] if y != 0 else 0
            left = sum_lines[y][x - 1] if x != 0 else 0
            up_left = sum_lines[y - 1][x - 1] if y != 0 and x != 0 else 0
            sum_lines[y].append(up + left - up_left + lines[y][x])
    best = sum_lines[0][0]
    for x0 in xrange(n_lines):
        for y0 in xrange(n_lines):
            for x1 in xrange(x0 + 1):
                for y1 in xrange(y0 + 1):
                    large_box = sum_lines[y0][x0]
                    up = sum_lines[y1 - 1][x0] if y1 != 0 else 0
                    left = sum_lines[y0][x1 - 1] if x1 != 0 else 0
                    up_left = sum_lines[y1 - 1][x1 - 1] if y1 != 0 and x1 != 0 else 0
                    sum = large_box - up - left + up_left
                    if sum > best:
                        best = sum
    print(best)