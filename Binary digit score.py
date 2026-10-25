def convert(n):
    t=0
    n=bin(n)[2:]

    for i in n:
        t+=int(i)

    return t

a=convert(int(input()))
b=convert(int(input()))

if a>=b:
    print(a*b)
else:
    print(b//a)
