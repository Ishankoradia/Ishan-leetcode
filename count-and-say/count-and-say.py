class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ""
        for i in range(0, n):
            if i == 0:
                ans += "1"
            else:
                j = 0
                ii = 0
                say_ans = ""
                N = len(ans)
                #print(N)

                while ii < N:
                    count = 0
                    while ans[ii] == ans[j]:
                        count += 1
                        j += 1
                        if j > N - 1:
                            break
                    say_ans += str(count) 
                    say_ans += str(ans[ii]) 
                    ii = j
                ans = say_ans

        return ans