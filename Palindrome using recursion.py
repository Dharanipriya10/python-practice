def palindrome(a):
    if a=="" or len(a)==1:
        return True
    
    if a[0]==a[-1]: # racecar
        return palindrome(a[1:-1]) # acecar

    return False

a=input()
print(palindrome(a))
