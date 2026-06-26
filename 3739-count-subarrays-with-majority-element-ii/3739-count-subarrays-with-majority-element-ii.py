class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        n = nums
        ans=0
        pre = [None]*len(n)
        sorted_list = []
        for ind,k in enumerate(n):
            if k==target:
                n[ind]=1
            else:
                n[ind]=-1
        for ind,m in enumerate(n):
            if ind==0:
                pre[0]=m
            else:
                pre[ind]=pre[ind-1]+m
        pre.insert(0,0)
        for k in range(len(pre)):
            current = pre[k]
            smaller = bisect_left(sorted_list,current)
            ans+=smaller
            sorted_list.insert(smaller,current)
        return ans
            