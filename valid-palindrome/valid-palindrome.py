class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_filtered = ""
        alph_num = "abcdefghijklmnopqrstuvwxyz0123456789"
        for i in s:
            if i.lower() in alph_num:
                s_filtered += i.lower()
        
        for i in range(len(s_filtered)//2):
            if s_filtered[i] != s_filtered[len(s_filtered) - i -1]:
                return False
            
        return True