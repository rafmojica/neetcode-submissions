class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a hashmap to count each character in string and compare
        if len(s) != len(t):
            return False

        sCount = {}
        tCount = {}
        for c in range(len(s)):
            sCount[s[c]] = sCount.get(s[c], 0) + 1
            tCount[t[c]] = tCount.get(t[c], 0) + 1

        return True if sCount == tCount else False
