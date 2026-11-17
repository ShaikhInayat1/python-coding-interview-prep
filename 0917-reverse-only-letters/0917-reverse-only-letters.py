class Solution:
    def reverseOnlyLetters(self, s: str) -> str:

        s = list(s)
        start = 0
        end = len(s) - 1
        
        while(start < end):

            if(not s[start].isalpha()):

                start += 1

            elif(not s[end].isalpha()):

                end -= 1

            else:

                temp = s[start]
                s[start] = s[end]
                s[end] = temp

                start += 1
                end -= 1

        return "".join(s)    
        