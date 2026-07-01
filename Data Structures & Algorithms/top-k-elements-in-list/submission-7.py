from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        count = [[] for i in range(len(nums) + 1)]

        for num in nums:
            freq[num] += 1

        # stored in ascending order to most elements
        for num, cnt in freq.items():
            count[cnt].append(num)

        res = []
        for i in range(len(count) - 1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res
