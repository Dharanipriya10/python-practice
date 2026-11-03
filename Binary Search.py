class Solution:
    def binarySearch(self, arr: list[int], k: int) -> int:
        # code here
        for i in range(len(arr)):
            if arr[i]==k:
                return i
        else:
            return -1
