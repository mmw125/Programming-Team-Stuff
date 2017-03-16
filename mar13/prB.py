
if __name__ == '__main__':
    num_flow, subs = map(int, input().split(' '))
    flowers = list(map(int, input().split(' ')))
    pflo = []
    for i in range(len(flowers)):
        pflo.append((pflo[i - 1] + flowers[i]) if i != 0 else flowers[0])
    sum = 0
    for i in range(subs):
        x, y = map(int, input().split(' '))
        hap = pflo[y - 1] - (pflo[x - 2] if x != 1 else 0)
        if 0 < hap:
            sum += hap
    print(sum)