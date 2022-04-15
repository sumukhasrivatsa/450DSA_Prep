class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x=len(matrix)
        y=len(matrix[0])
        a=[0 for i in range(x)]
    
        b=[0 for i in range(y)]
        
        for  i in range(x):
            for j in range(y):
                if matrix[i][j]==0:
                    a[i]=1
                    b[j]=1
        for i in range(x):
            for j in range(y):
                if a[i]==1or b[j]==1:
                    matrix[i][j]=0
        
        
            
     
        
