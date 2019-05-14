import numpy as np
import os

n=8
A=np.ndarray((n,n))
L=np.ndarray((n,n))

P={}
for i in range(n):
    for j in range(n):
        P[(i,j)]=(-1,-1)

def dfs(A,sx,sy,dx,dy):
    Q=[]
    Q.append((sx,sy))
    A[sx][sy]=2
    P[(sx,sy)]=(-2,-2)
    x,y = sx,sy
    while(x!=dx or y!=dy):
        (x,y)=Q[len(Q)-1]
        del Q[len(Q)-1]
        if(x==sx and y==sy):
            A[x][y]=2
        else:
            A[x][y]=3
        c1,c2,c3,c4=0,0,0,0
        if(x!=0 and A[x-1][y]==1):
            Q.append((x-1,y))
            A[x-1][y]=4
            P[(x-1,y)]=(x,y)
            c1=1
        if(y!=0 and A[x][y-1]==1):
            Q.append((x,y-1))
            A[x][y-1]=4
            P[(x,y-1)]=(x,y)
            c2=1
        if(y!=n-1 and A[x][y+1]==1):
            Q.append((x,y+1))
            A[x][y+1]=4
            P[(x,y+1)]=(x,y)
            c3=1
        if(x!=n-1 and A[x+1][y]==1):
            Q.append((x+1,y))
            A[x+1][y]=4
            P[(x+1,y)]=(x,y)
            c4=1
        if((c1+c2+c3+c4)==0 and len(Q)==0 and x!=dx and y!=dy):
            break;
        else:
            os.system("clear")
            print(A)
            print("\n")
            os.system("sleep 0.5")
        
    if(x==dx and y==dy):
        A[dx][dy]=5
        
        L=np.ndarray((n,n))
        s,t=dx,dy
        L[dx][dy]=2
        while(P[(s,t)]!=(-2,-2)):
            s,t=P[(s,t)]
            L[s][t]=2
        os.system("clear")
        print("Destination reached\n")
        print(A)
        print("\n")
        print(L)
        print("\n")
        os.system("sleep 0.5")
    else:
        os.system("clear")
        print("Destination cannot be reached\n")
        print("Final point:("+str(x)+","+str(y)+")")
        os.system("sleep 0.5")
        
data=open("/home/devansh/Downloads/lab8/t","r")

i=0
for line in data:
    word=line.split()
    for j in range(n):
        A[i][j]=word[j]
    i+=1
    
dfs(A,0,0,3,4)
