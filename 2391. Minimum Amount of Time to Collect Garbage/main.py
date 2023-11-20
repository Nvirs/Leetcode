class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0

        for g in garbage:
            res += len(g)
        g,p,m = False,False,False

        for i in range(len(travel),0,-1):
            m = m or 'M' in garbage[i]
            p = p or 'P' in garbage[i]
            g = g or 'G' in garbage[i]

            res += travel[i-1]*(m+p+g)
        
        return res
        print(i)
