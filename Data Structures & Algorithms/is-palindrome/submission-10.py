class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = re.sub(r'[^a-zA-Z0-9]+', '', s)
        s_new = s_new.lower()

        if len(s_new) < 2:
            return True

        lpointer, rpointer = 0, len(s_new) - 1
        while lpointer < rpointer:
            if s_new[lpointer] == s_new[rpointer]:
                lpointer, rpointer = lpointer + 1, rpointer - 1
            else:
                return False
        return True