import math

if __name__ == '__main__':
    while True:
        try:
            num = int(input())
        except EOFError:
            exit(0)
        out = '-'
        for i in range(num):
            out = (' '*int(math.pow(3, i))).join((out, out))
        print(out)