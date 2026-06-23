class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        modulo = 10**9+7
        M = r-l+1
        prev = [1]*M

        #증가로 시작하는 경우만
        for i in range(1,n):
            current = [0]*M
            hap=0
            if i%2==1:
                for l in range(M):
                    current[l]=hap
                    hap=(hap+prev[l])%modulo
            
            else:
                for l in reversed(range(M)):
                    current[l]=hap
                    hap=(hap+prev[l])%modulo
            
            prev = current
        return ((sum(prev)%modulo)*2)%modulo