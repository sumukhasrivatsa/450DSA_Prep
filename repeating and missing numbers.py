def repeatedNumber(A):
        
        B=[]
        for j in range(len(A)):
            B.append(0)
        print(B)
        
        for i in range(len(A)):
            B[A[i]-1]+=1
        print(B)
        for i in range(len(A)):
            if B[i]==0:
                z=i+1
            elif B[i]==2:
                r=i+1
        return [r,z]

s=repeatedNumber([3,1,2,5 ,3])
print(s)
