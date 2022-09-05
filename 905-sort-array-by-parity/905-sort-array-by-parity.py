class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            if i % 2 == 0:
                result.insert(0, i)
            else:
                result.append(i)
        return result