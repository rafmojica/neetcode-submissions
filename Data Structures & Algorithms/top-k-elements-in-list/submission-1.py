class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HASHMAP
        freq = {}
        maxFreq = []
        pair = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, val in freq.items():
            pair.append([key, val])
            
        pair.sort(key=lambda x: x[1], reverse=True) # sort by descending value

        for i in range(k):
            maxFreq.append(pair[i][0])

        return maxFreq
