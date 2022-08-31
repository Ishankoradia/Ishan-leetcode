class Solution:
    def climbStairs(self, n: int) -> int:        
        my_cache = {}
        
        def recursive_climb(n):            
        
            if(n in my_cache):
                return my_cache[n]
        
            if(n == 1):
                result = 1
            elif(n == 2):
                result = 2
            else:
                result = recursive_climb(n-2) + recursive_climb(n-1)
        
            my_cache[n] = result
            
            return result
        
        return recursive_climb(n)