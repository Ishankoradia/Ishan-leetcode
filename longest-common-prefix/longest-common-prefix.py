class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPrefix(left, right):
            min_length = min(len(left), len(right))
            for i in range(min_length):
                if left[i] != right[i]:
                    return left[0:i]
                
            return left[0: min_length]
        
        
        def LCP(strs, l, r):
            if l == r:
                return strs[l]
            else:
                mid = (l + r) // 2
                lcp_left = LCP(strs, l, mid)
                lcp_right = LCP(strs, mid+1, r)
                return commonPrefix(lcp_left, lcp_right)
            
            
        
        return LCP(strs, 0, len(strs)-1)
        
        
                  
            