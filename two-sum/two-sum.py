class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = {}
#         for i in range(len(nums)):
#             n[i] = nums[i]

#         for k1, v1 in n.items():
#             for k2, v2 in n.items():
#                 if (k1 != k2):
#                     if (v1 + v2 == target):
#                         return [k1, k2]

        answer = []
        n = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in n.keys():
                answer.append(n.get(diff))
                answer.append(i)
            else:
                n[nums[i]] = i
        
        return answer