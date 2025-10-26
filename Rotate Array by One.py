class Solution:
    def rotate(self, arr):
        n=arr[-1]
        arr.pop(-1)
        arr.insert(0, n)
