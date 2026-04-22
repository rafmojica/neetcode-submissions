class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) solution
        # Hashmap
        # 1. nums[index]: index key-value pair
        # 2. if target - value exists in the hashmap, return indices
        indVal = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in indVal:
                return [indVal[diff], i]
            indVal[nums[i]] = i
        