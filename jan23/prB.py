
if __name__  == "__main__":
    num = input()
    strs = []
    for i in range(int(num)):
        str = input()
        rev = ''.join(reversed(str))
        strs.append(rev if str < rev else str)
    fin = ''.join(reversed(sorted(strs))).title()
    print(fin if fin > 'Acorn' else 'Acorn')
