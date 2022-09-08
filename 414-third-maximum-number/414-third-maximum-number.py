class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = sorted(set(nums))
        if len(a) >= 3:
            return a[-3]
        else:
            return a[-1]
            
            