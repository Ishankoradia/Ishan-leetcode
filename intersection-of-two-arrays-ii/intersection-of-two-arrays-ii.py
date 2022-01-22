class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = {}
        n2 = {}
        inter = []
        for i in nums1:
            if i in n1.keys():
                n1[i] += 1
            else:
                n1[i] = 1
        
        for i in nums2:
            if i in n2.keys():
                n2[i] += 1
            else:
                n2[i] = 1
                
        for k in n1.keys():
            if k in n2.keys():
                for _ in range(min(n1[k], n2[k])):
                    inter.append(k)
                    
        return inter