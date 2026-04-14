class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap! for O(n) approach
        # brute force is a nested for loop. for O(n^2) approach

        # for loop
        # if key already in numsMap, return true
        # if we reach the end of the loop and it's not there, return false
        numsMap = {}
        for num in nums:
            if num not in numsMap:
                numsMap[num] = 1
            else:
                return True
        return False
