class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        start = 1
        end = num
        ans = 0

        while(start <= end):

            mid = start + (end - start) // 2

            if(mid * mid == num):

                return True
            
            if(mid * mid < num):

                start = mid + 1

            else: 

                end = mid - 1

        return False
        