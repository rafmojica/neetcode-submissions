class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l, r = 0, len(heights) - 1

        while l < r:
            length = r - l
            if heights[l] > heights[r]:
                ans = max(ans, length * heights[r])
                r -= 1
            elif heights[r] > heights[l]:
                ans = max(ans, length * heights[l])
                l += 1
            elif heights[r] == heights[l]:
                ans = max(ans, length * heights[l])
                l += 1
                r -= 1

        return ans
