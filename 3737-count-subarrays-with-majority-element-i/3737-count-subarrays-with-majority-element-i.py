class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        k = len(nums)
        for m in range(k):
            count = 0
            for n in range(m,k):
                if nums[n]==target:
                    count+=1
                else:
                    count-=1
                if count>0:
                    ans+=1
        return ans
            

                
            
            