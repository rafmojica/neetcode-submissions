class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted list
        # if l + r < target, move l
        # if l + r > target, move r
        l, r = 0, len(numbers) - 1
        myList = []

        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1

        myList.append(l+1)
        myList.append(r+1)

        return myList