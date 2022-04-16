class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        def swap(nums,a,b):
            x=nums[a]
            nums[a]=nums[b]
            nums[b]=x
            return nums
        
        os=0
        oe=len(nums)-1
        mid=0
        
        while(mid<=oe):
            if nums[mid]==0:
                nums=swap(nums,mid,os)
                os+=1
                if nums[mid]==1 or nums[mid]==0:
                    mid+=1
                
            elif nums[mid]==1:
                mid+=1
            else :
                nums=swap(nums,mid,oe)
                oe-=1
                
                if nums[mid]==1:
                    mid+=1
                
                
                
        return nums
                
        
