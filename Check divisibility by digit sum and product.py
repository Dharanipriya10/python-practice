class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum = 0
        product = 1
        temp = n
        while n>0:
            a=n%10
            sum+=a
            product *= a
            n=n//10
        b=sum+product
        if temp%b == 0:
            return True
        return False
