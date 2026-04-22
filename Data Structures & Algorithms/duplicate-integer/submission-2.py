class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashmap
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        for k, v in freq.items():
            if v > 1:
                return True
        
        return False