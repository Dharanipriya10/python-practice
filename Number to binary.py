def binary(a):  # use bin() for built-in function
    s=""
    while a>0:
        rem = a%2 # 10%2=0 2%2=0
        s+=str(rem)
        a//=2 # 10//2=5

    return s

a = int(input())
print(binary(a))
