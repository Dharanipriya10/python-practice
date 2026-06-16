class Solution:
    def processStr(self, s: str) -> str:
        result=""
        for ch in s:
            if ch in "abcdefghijklmnopqrstuvwxyz":
                result+=ch
            elif ch == '#':
                result*=2
            elif ch =='%':
                result=result[::-1]
            elif ch == '*':
                result=result[:-1]
        return result
