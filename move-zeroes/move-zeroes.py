class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = []
        for i in range(len(nums)):
            if nums[i] == 0:
                idx.append(i)
        
        for i in range(len(idx)):
            nums.pop(idx[i] - i)
            nums.append(0)