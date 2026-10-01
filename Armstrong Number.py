n = int(input())
temp = n
c = 0
while n>0:
    a = n%10
    c += a**3
    n//=10
if c==temp:
    print("Armstong Number")
else:
    print("Not Armstrong")
