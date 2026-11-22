class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)
        n = len(s2)

        if(n < k):

            return False

        result = []
        s_arr = [0] * 26
        p_arr = [0] * 26

        for i in range(k):

            s_arr[ord(s2[i]) - 97] += 1
            p_arr[ord(s1[i]) - 97] += 1

        if(s_arr == p_arr):

            return True
        
        for i in range(1, n - k + 1):

            # Remove Previous Element.
            s_arr[ord(s2[i - 1]) - 97] -= 1

            # Add new Element or Upcomming Element.
            s_arr[ord(s2[i + k - 1]) - 97] += 1

            if(s_arr == p_arr):

                result.append(i)
                return True
        
        return False

        