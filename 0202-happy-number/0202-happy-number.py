class Solution:
    def isHappy(self, n: int) -> bool:
        
        sum = 0

        while(n > 0):

            digit = n % 10
            sum += digit * digit
            n //= 10

        if(sum == 1):
            return True
        
        if(sum == 4):
            return False
        
        return self.isHappy(sum)

            

        