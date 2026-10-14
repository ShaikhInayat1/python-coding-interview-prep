class Solution:
    def reverseVowels(self, s: str) -> str:

        s = list(s)

        vowels = "aeiouAEIOU"

        start = 0
        end = len(s) - 1

        while(start < end):

            if(s[start] not in vowels):

                start += 1

            elif(s[end] not in vowels):
                
                end -= 1

            else:
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                
                start += 1
                end -= 1

        return "".join(s)
        