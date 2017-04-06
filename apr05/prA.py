def int2base(x,b,alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
    'convert an integer to its string representation in a given base'
    if b<2 or b>len(alphabet):
        if b==64: # assume base64 rather than raise error
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        else:
            raise AssertionError("int2base base out of range")
    if isinstance(x,complex): # return a tuple
        return ( int2base(x.real,b,alphabet) , int2base(x.imag,b,alphabet) )
    if x<=0:
        if x==0:
            return alphabet[0]
        else:
            return  '-' + int2base(-x,b,alphabet)
    # else x is non-negative real
    rets=''
    while x>0:
        x,idx = divmod(x,b)
        rets = alphabet[idx] + rets
    return rets

if __name__ == '__main__':
    base, length = map(int, input().split(' '))
    formatter = '%0' + str(length) + 'd'
    i = 0
    while(True):
        out = int2base(i, base)
        if len(out) > length:
            exit()
        print(formatter % (int(out)))
        i += 1