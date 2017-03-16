
if __name__ == '__main__':
    num_orders = int(input())
    total_time = 0
    out = 0
    for order in sorted(map(int, input().split(' '))):
        total_time += order
        out += total_time
    print('%.3f' % (out / num_orders))
