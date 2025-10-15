from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sLetters = Counter(list(s))
        tLetters = Counter(list(t))
        # print(list(tLetters.difference(sLetters)))
        return list(tLetters - sLetters)[0]
