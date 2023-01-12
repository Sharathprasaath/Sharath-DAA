import numpy as np
a='agcacaca'
b='acacacta'
n=len(a)+1
m=len(b)+1
mat=np.zeros((n,m))
for i in range(n - 1):
    for j in range(m - 1):
        if(a[i]==b[j]):
            mat[i+1][j+1]=mat[i][j]+2
        else:
            x=max(mat[i][j],mat[i+1][j],mat[i][j+1])
            mat[i+1][j+1]=x - 1
print(mat)
arr=[]
c=[]
def back(mat,arr,x,y):
    if(x==1 and y==1):
        return arr
    elif(mat[x,y]==(mat[x-1,y-1] - 1) or mat[x,y]==(mat[x-1,y-1]+2)):
        arr.append([x-1,y-1])
        return back(mat,arr,x-1,y-1)
    elif(mat[x,y]==(mat[x-1,y] - 1)):
        arr.append([x-1,y])
        return back(mat,arr,x-1,y)
    elif(mat[x,y]==(mat[x,y-1] - 1)):
        arr.append([x,y - 1])
        return back(mat,arr,x,y - 1)
back(mat,arr,n-1,m-1)
print(arr)