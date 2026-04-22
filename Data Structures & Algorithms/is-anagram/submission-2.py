class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use a hashmap to count each character in string and compare
        sCount = {}
        for c in s:
            sCount[c] = sCount.get(c, 0) + 1

        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
        
        if sCount == tCount:
            return True
        return False
