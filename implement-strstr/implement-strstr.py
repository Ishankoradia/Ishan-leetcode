class Solution:
    def strStr(self, haystack: str, needle: str) -> int:  
        if len(needle) <= 0:
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        
        N = len(haystack)
        M = len(needle)
        lps_arr = [0] * M
                
        def computeLPS(needle, M, lps_arr):
            j = 0
            i = 1
            lps_arr[0] = 0
            while i < M:
                if needle[i] == needle[j]:
                    j += 1
                    lps_arr[i] = j
                    i += 1
                else:
                    if j != 0:
                        j = lps_arr[j-1]
                    else: 
                        lps_arr[i] = 0
                        i += 1
                        
        
        
        
        
        computeLPS(needle, M, lps_arr)
        i = 0
        j = 0
        idx = -1
        while i < N:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps_arr[j-1]
                else:
                    i += 1
            
            if j == M:
                return (i-j)
            
        return idx
                