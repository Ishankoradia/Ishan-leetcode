class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            beg = s[i]
            end = s[len(s) - i - 1]
            s[i] = end
            s[len(s) - i - 1] = beg