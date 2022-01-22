class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        result = ""
        digits = "0123456789"
        ans = "0"
        read = True
        s = s.strip() + "z"
        for i in range(len(s)):
            if read == False:
                break

            if s[i] == '-' or s[i] == '+':
                if i < len(s) -1 and s[i+1] in digits:
                    ans = s[i] + ans
                    continue
                else:
                    read = False
            elif s[i] in digits and read:
                ans += s[i]
                if i < len(s) and s[i+1] in digits:
                    continue
                else:
                    read = False
            else:
                read = False

        ans = int(ans)

        if ans < INT_MIN:
            return INT_MIN
        elif ans > INT_MAX:
            return INT_MAX
        else:
            return ans
        
        
                
            
        