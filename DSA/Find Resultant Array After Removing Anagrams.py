# Problem Link: https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/?envType=daily-question&envId=2025-10-13

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans=[words[0]]
        la=sorted(words[0])
        # print(la)

        for w in words:
            s=sorted(w)
            if(s!=la):
                ans.append(w)
                la=s

        return ans
