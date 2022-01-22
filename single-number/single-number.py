class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # while True:
        #     ele = nums.pop(0)
        #     if ele in nums:
        #         nums.remove(ele)
        #     else:
        #         return ele
        ele=nums[0]
        for i in range(1,len(nums)): 
            ele ^= nums[i]
        return ele