import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        start = 0
        end = math.isqrt(c)

        while(start <= end):

            sum = start * start + end * end

            if(sum == c):

                return True
            
            elif(sum < c):

                start += 1
            
            else:

                end -= 1
        
        return False
