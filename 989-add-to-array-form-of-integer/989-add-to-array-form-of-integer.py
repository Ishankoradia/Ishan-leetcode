class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_s = ''
        for i in num:
            num_s += str(i)
        k += int(num_s)
        result = []
        for i in str(k):
            result.append(i)
        return result
        