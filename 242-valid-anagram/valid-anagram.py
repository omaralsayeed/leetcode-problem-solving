from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s) == len(t) and Counter(list(s)) == Counter(list(t))
        