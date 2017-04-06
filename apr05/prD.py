
def fact(n, modulus):
    ans=1
    if n <= modulus//2:
        #calculate the factorial normally (right argument of range() is exclusive)
        for i in range(1,n+1):
            ans = (ans * i) % modulus
    return ans % modulus

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

mod = 1000000007
width, height = map(int, input().split(' '))
print(fact(width + height, mod) * modinv(fact(width, mod) * fact(height, mod), mod) % mod)
