class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        def criteria(a, b):
            # return True if a < b based on the criteria
            if count[a] < count[b]:
                return True
            elif count[a] == count[b]:
                return a >= b
            elif count[a] > count[b]:
                return False
        
        result = []
        for i in count.keys():
            l = len(result)
            if l > 0:
                c = 0
                while c <= l - 1:
                    if criteria(result[c], i):
                        c += count[result[c]]
                    else:
                        for _ in range(count[i]):
                            result.insert(c, i)
                        c = -1
                        break
                if c != -1:
                    for _ in range(count[i]):
                        result.append(i)
                    
            else:
                for _ in range(count[i]):
                    result.append(i)
                    
        return result
        
            
            