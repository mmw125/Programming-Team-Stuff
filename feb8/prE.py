if __name__ == '__main__':
    counts = {}
    outputs = {}
    while True:
        args = [int(i) for i in input().split(' ')]
        if args == [0, 0, 0]:
            exit(0)
        L, H, X = args
        out = 0
        for i in range(L, H + 1):
            def bit_count(num, times=1):
                if num in outputs:
                    return outputs[num] + times - 1
                count = bin(num).count("1")
                if count == 1:
                    return times
                times = bit_count(count, times + 1)
                outputs[num] = times
                return times
            count = bit_count(i)
            if count == X:
                out += 1
        print(out)