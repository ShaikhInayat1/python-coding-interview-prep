class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        
        n = len(nums)
        result = [0] * n
        start = 0
        end = n - 1
        pos = n - 1

        while(start <= end):

            s_square = nums[start] * nums[start]
            e_square = nums[end] * nums[end]

            if(s_square < e_square):

                result[pos] = e_square
                end -= 1
            
            else:

                result[pos] = s_square
                start += 1

            pos -= 1

        return result

        
        