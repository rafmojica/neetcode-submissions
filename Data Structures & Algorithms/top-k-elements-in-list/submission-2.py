class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HASHMAP
        freq = {}
        pair = []
        result = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, val in freq.items():
            pair.append([val, key])
        pair.sort(reverse=True) # sort in descending order

        for i in range(k):
            result.append(pair[i][1])

        return result
