class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = []
        for i in range(len(arr)):
            j = i + 1
            while j < len(arr):
                stack.append(arr[j])
                j += 1
            if stack:
                arr[i] = max(stack)
                stack = []
        arr[len(arr) - 1] = -1
        return arr