class Solution:
    def __init__(self):
        self.c = []
    def return_same(self,l1,l2):
        ans = 0
        l1.sort()
        l2.sort()
        for a in l1:
            if a in l2:
                ans+=1
        return ans
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        for a in range(len(A)):
            self.c.append(self.return_same(A[:a+1],B[:a+1]))
        return self.c