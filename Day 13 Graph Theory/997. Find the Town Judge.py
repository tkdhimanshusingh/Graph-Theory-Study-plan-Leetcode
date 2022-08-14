class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dp=[0 for _ in range(n+1)]
        for i,j in trust:
            dp[i]-=1
            dp[j]+=1
        for i in range(1,len(dp)):
            if dp[i]==n-1:
                return i
        return -1