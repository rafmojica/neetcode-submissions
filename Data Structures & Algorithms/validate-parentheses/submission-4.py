class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack, to track inner most open parenthesis,
        # ensuring it gets closed first
        stack = []
        parenthesis = {')': '(', ']': '[', '}': '{' }

        for char in s:
            if char in parenthesis:
                if stack and stack[-1] == parenthesis[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        return False