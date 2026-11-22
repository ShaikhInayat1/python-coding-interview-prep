class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:

        k = len(p)

        if(len(s) < k):

            return []

        result = []
        s_arr = [0] * 26
        p_arr = [0] * 26

        for i in range(k):

            s_arr[ord(s[i]) - 97] += 1
            p_arr[ord(p[i]) - 97] += 1

        if(s_arr == p_arr):
            result.append(0)

        for i in range(1, len(s) - k + 1):

            s_arr[ord(s[i - 1]) - 97] -= 1
            s_arr[ord(s[i + k - 1]) - 97] += 1

            if(s_arr == p_arr):

                result.append(i)

        return result
        
        