class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset (only stores unique elements)
        return len(set(nums)) < len(nums)
