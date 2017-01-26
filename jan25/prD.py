if __name__ == "__main__":
    name0 = input()
    name1 = input()
    longest = ''
    for offset in range(len(name1)):
        print('checking')
        print(name0)
        print(' '*offset + name1)
        index = 0
        length = 0
        while index < len(name1) and index + offset < len(name0):
            if name1[index] == name0[index + offset]:
                length += 1
            elif length:
                if length > len(longest):
                    longest = name1[index - length:index]
                length = 0
            index += 1
        if length and length > len(longest):
            longest = name1[index - length:index]
        length = 0
        if longest:
            print('found', longest)
    print(longest)
