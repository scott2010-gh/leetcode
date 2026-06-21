class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = list(s)
        f = list(t)
        ans = ""
        for i in f:
            print(i in d)
            if not i in d:
                ans=i
            elif i in d:
                d.remove(i)
        return ans