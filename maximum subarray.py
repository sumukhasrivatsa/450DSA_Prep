class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        b=0
        sums=0
        maxsum=0
        while(b<=len(nums)-1):
            sums=sums+nums[b]
            if sums<=0:
                sums=0
                b+=1
            else:
                if sums>maxsum:
                    maxsum=sums
                b+=1
                
           
        flag=0
        for i in nums:
            if i>=0:
                flag=1
        if flag==0:
            x=max(nums)
            return x
        else:
            return maxsum
        
               
        
                
                
            
