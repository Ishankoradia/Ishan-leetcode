class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        
        maximum = max(nums)
        
        if len(nums) < 3:
            return maximum
        
        nums.remove(maximum)
        maximum = max(nums)
        nums.remove(maximum)
        return max(nums)
        
        