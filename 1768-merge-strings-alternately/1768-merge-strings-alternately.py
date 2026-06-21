class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = ' '.join(word1)
        w1 = list(word1)
        word2 = ' '.join(word2)
        w2 = list(word2)
        w2.insert(0,' ')
        print(w1,w2)

        ans = []
        ml = max(len(w1),len(w2))
        w1.extend([' ']*(ml-len(w1)))
        w2.extend([' ']*(ml-len(w2)))
        
        for ind in range(ml):
            ans.append(w1[ind].replace(' ','')+w2[ind].replace(' ',''))

        return ''.join(ans)
        