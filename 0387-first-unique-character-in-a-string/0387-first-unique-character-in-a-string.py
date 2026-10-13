class Solution:
    def firstUniqChar(self, s: str) -> int:

        arr = {}

        for ch in s:

            if(ch in arr):

                arr[ch] += 1

            else:

                arr[ch] = 1

        for i in range(len(s)):

            if(arr[s[i]] == 1):

                return i

        return -1
        