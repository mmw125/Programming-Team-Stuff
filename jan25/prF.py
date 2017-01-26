if __name__ == '__main__':
    out_num = 0
    num_inputs = input()
    inputs = set([int(i) for i in input().split(' ')])
    for i in inputs:
        if 12345 - i in inputs:
            out_num += 1
    print(int(out_num / 2))
