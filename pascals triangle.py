class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        array=[]
        
        for i in range(numRows):
            arr=[]
            for j in range(0,i+1):
                if i==0:
                    arr.append(1)
                    
                elif(j==0) or j==i:
                    arr.append(1)
                else:
                    arr.append(array[i-1][j-1]+array[i-1][j])
            array.append(arr)
                    
                
            
        return array
     
        
