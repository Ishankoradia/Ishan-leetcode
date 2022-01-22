class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_count = 0
        for i in range(len(nums)):
            if nums[i] != nums[unique_count]:
                unique_count += 1
                nums[unique_count] = nums[i]
        return (unique_count + 1)