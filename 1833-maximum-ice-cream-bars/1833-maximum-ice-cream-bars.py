class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans=0
        co = costs
        co.sort()
        using=co[0]
        coi = coins
        ind = 0
        lenco = len(co)

        while lenco-ind>=1:
            if coi-using>=0:
                coi-=using
                ans+=1
            if lenco-ind==1:
                return ans
            else:
                ind+=1
                using = co[ind]
        return ans