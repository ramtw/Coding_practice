# Problem Link: https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/?envType=daily-question&envId=2025-10-13


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        c=1
        f=0
        i=1
        
        while i<len(nums):
            # print(i)
            if(nums[i]>nums[i-1]):
                c+=1
                if(c==2*k):
                    return True
                if(f==1 and c==k):
                    return True
            else:
                if(f==0):
                    if(c>=k):
                        c=1
                        f=1
                        if(c>=k and f==1):
                            return True
                    else:
                        c=1
                        f=0
                else:
                    c=1
                    f=0
            i+=1
        
        if(c>=k and f==1):
            return True

        return False
                
