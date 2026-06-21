class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans=0
        co = costs
        co.sort()
        using=co[0]
        coi = coins
        
        while len(co)>=1:
            if coi-using>=0:
                coi-=using
                ans+=1
            co.pop(0)
            if len(co)==0:
                return ans
            else:
                using = co[0]
        return ans