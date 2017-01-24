import sys

if __name__  == "__main__":
    i = 0
    for c in input():
       if c == "(":
            i += 1
       else:
            i -= 1
            if i < 0:
                break
    print('Balanced' if i == 0 else 'Unbalanced')
