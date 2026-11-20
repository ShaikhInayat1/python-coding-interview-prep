class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:

        ans = k * threshold

        windowSum = 0
        count = 0

        for i in range(k):

            windowSum += arr[i]

        if(windowSum >= ans):

            count += 1

        for i in range(1, len(arr) - k + 1):

            windowSum = windowSum - arr[i - 1] + arr[i + k - 1]

            if(windowSum >= ans):

                count += 1

        
        return count


        