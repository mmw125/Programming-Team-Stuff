def evaluate(str, pos):
    if str[pos] != '(':
        return int(str[pos]), pos + 1
    op = str[pos + 1]
    e0 = evaluate(str, pos + 2)
    e1 = evaluate(str, e0[1])
    if op == '-':
        return e0[0] - e1[0], e1[1] + 1
    else:
        return e0[0] + e1[0], e1[1] + 1


if __name__ == '__main__':
    num_inputs = int(input())
    for i in range(num_inputs):
        print(evaluate(input().split(' '), 0)[0])
