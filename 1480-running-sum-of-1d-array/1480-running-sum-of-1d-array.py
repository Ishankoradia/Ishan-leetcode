class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum1 = 0
        for i in range(len(nums)):
            sum1 += nums[i]
            nums[i] = sum1
        return nums