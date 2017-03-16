import bisect

if __name__ == '__main__':
    input()
    prices = sorted(map(int, input().split(' ')))
    to_buy = int(input())
    for i in range(to_buy):
        print(bisect.bisect(prices, int(input())))