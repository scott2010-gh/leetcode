class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        import math
        check = [0]*5
        o = list("balon")
        l = list(text)
        
        for i in l:
            if i in o:
                check[o.index(i)]+=1
        
        check[2]/=2
        check[3]/=2
        a = min(check)
        if a<1:
            return 0
        else:
            return math.floor(a)
        