# Problem Link: https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        
        for x in strs:
            lst=[0]*26
            for c in x:
                i=ord(c)-ord('a')
                lst[i]+=1
            
            t=tuple(lst)
            if(t in mp):
                mp[t].append(x)
            else:
                mp[t]=[x]
        
        return list(mp.values())
