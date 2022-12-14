class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0]*(n+1)
        for i in range(len(trust)):
            count[trust[i][1]] += 1
            count[trust[i][0]] -= 1
        for i in range(1,len(count)):
            if count[i] == n-1:
                return i
        return -1