class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c_max = 0
        c = 0
        for i in nums:
            if i == 1:
                c += 1
            else:
                if c > c_max:
                    c_max = c
                c = 0
        return c_max if c_max > c else c