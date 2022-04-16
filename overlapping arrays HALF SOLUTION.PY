class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ptr=0
        i=0
        j=0
        newarr=[]
        newarr.append(intervals[0])
        while(i!=len(intervals)-1):
            if intervals[i][1]>=intervals[i+1][0]:
                newarr[j][1]=intervals[i+1][1]
                i+=1
                
            else:
                newarr.append(intervals[i+1])
                i=i+1
                j=j+1
                
        return newarr
            
                
            
            
            
            
