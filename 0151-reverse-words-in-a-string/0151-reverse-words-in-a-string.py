class Solution:
    def reverseWords(self, s: str) -> str:

        word = s.split()

        start = 0
        end = len(word) - 1

        while(start < end):

            temp = word[start]
            word[start] = word[end]
            word[end] = temp

            start += 1
            end -= 1

        return" ".join(word)
        