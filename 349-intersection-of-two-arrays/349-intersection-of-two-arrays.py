class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in nums1:
            d[i] = 1
        for j in nums2:
            if d.get(j) is not None:
                d[j] += d[j] + 1
        return [i for i in d.keys() if d[i] > 1]