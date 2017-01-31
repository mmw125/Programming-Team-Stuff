import collections

if __name__ == '__main__':
    can, sup = [int(i) for i in input().split(' ')]
    write_ins = collections.OrderedDict()
    nones = []
    candidates = collections.OrderedDict()
    for i in range(can):
        candidates[input()] = []
    for i in range(sup):
        str_in = input()
        if ' ' in str_in:
            person, can = str_in.split(' ')
            if can in candidates:
                candidates[can].append(person)
            else:
                arr = write_ins.get(can, [])
                arr.append(person)
                write_ins[can] = arr
        else:
            nones.append(str_in)
    for key in candidates:
        for value in candidates[key]:
            print(value)
    for key in write_ins:
        for value in write_ins[key]:
            print(value)
    for none in nones:
        print(none)