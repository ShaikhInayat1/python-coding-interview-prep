class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        start = 0
        end = int(c ** 0.5)

        while(start <= end):

            total = start * start + end * end

            if(total == c):

                return True
            
            elif(total > c):

                end -= 1
            
            elif(total < c):

                start += 1

        
        return False
        