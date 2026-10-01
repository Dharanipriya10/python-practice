# A perfect number is a positive integer that is equal to the sum of its proper divisors

# 6 = 1, 2, 3 -> 1+2+3 = 6

n = int(input())
c=0
for i in range(1, n):
    if n%i==0:
        c+=i

if c==n:
    print("Perfect Number")
else:
    print("Not Perfect Number")
