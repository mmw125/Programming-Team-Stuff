
if __name__ == "__main__":
    num = input()
    strs = []
    for i in range(int(num)):
        str = input()
        rev = ''.join(reversed(str))
        strs.append(rev if str < rev else str)
