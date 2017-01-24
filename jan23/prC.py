
if __name__  == "__main__":
    width = len(input())
    height = 2
    while '|' in input():
        height += 1
    arr = []
    arr.append('-' * width)
    for h in range(height - 2):
        arr.append(''.join(('|', ' ' * (width - 2), '|')))

    arr.append('/' + '-' * (width - 1))
    for a in arr:
        print(a)
