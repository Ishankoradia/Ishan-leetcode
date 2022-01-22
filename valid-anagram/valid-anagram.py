class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        for i in s:
            s1[i] = s1.get(i, 0) + 1
        
        t1 = {}
        for i in t:
            t1[i] = t1.get(i, 0) + 1
            
        
        if s1 != t1:
            return False
        return True