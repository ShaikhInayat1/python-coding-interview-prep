class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()

        rev_words = []

        for word in words:

            rev_words.append(word[::-1])

        result = " ".join(rev_words)

        return result


        