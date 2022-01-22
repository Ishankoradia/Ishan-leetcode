class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum1 = 0
        l1 = len(digits)
        for i in range(l1):
            sum1 += digits[i] * (10 ** (l1-i-1))
        
        sum1 += 1
        plus_one = []
        for i in str(sum1):
            plus_one.append(int(i))
            
        return plus_one