import numpy as np
import os
import queue as Q

#0 -> blockage
#1 -> allowed path
#2 -> source vertex
#3 -> visited vertex
#4 -> A* path traversed
#5 -> destination

n=8

#for storing the 0,1 matrix to indicate positions where there is path or blockage
A=np.ndarray((n,n))  
L=np.ndarray((n,n))  
#dictionary to store G-cost, H-cost(heuristic cost), VisitedList             
G={}
H={}
V={}
#for storing the priority queue
PQ=Q.PriorityQueue(n*n+1)

def initialize_visited():
	for i in range(n):
		for j in range(n):
			V[(i,j)]=0

def h(dx,dy):
	for i in range(n):
		for j in range(n):
			H[(i,j)]=(dx-i)*(dx-i)+(dy-j)*(dy-j)

def a_star(A,sx,sy,dx,dy):
	A[sx][sy]=2
	A[dx][dy]=5
	h(dx,dy)
	x,y=sx,sy
	PQ.put((0,sx,sy))
	G[(sx,sy)]=0
	V[(sx,sy)]=1
	os.system("clear")
	print(A)
	os.system("sleep 0.5")     
	
	while(x!=dx or y!=dy):
		if (x!=0 and y!=0 and A[x-1][y-1]!=0 and V[(x-1,y-1)]==0):
			G[(x-1,y-1)]=G[(x,y)]+1
			PQ.put((G[(x-1,y-1)]+H[(x-1,y-1)],x-1,y-1))
			V[(x-1,y-1)]=1
			A[x-1][y-1]=3
		if (x!=0 and A[x-1][y]!=0 and V[(x-1,y)]==0):
			G[(x-1,y)]=G[(x,y)]+1
			PQ.put((G[(x-1,y)]+H[(x-1,y)],x-1,y))
			V[(x-1,y)]=1
			A[x-1][y]=3
		if (x!=0 and y!=n-1 and A[x-1][y+1]!=0 and V[(x-1,y+1)]==0):
			G[(x-1,y+1)]=G[(x,y)]+1
			PQ.put((G[(x-1,y+1)]+H[(x-1,y+1)],x-1,y+1))
			V[(x-1,y+1)]=1
			A[x-1][y+1]=3
		if (y!=0 and A[x][y-1]!=0 and V[(x,y-1)]==0):
			G[(x,y-1)]=G[(x,y)]+1
			PQ.put((G[(x,y-1)]+H[(x,y-1)],x,y-1))
			V[(x,y-1)]=1
			A[x][y-1]=3
		if (y!=n-1 and A[x][y+1]!=0 and V[(x,y+1)]==0):
			G[(x,y+1)]=G[(x,y)]+1
			PQ.put((G[(x,y+1)]+H[(x,y+1)],x,y+1))
			V[(x,y+1)]=1
			A[x][y+1]=3
		if (x!=n-1 and y!=0 and A[x+1][y-1]!=0 and V[(x+1,y-1)]==0):
			G[(x+1,y-1)]=G[(x,y)]+1
			PQ.put((G[(x+1,y-1)]+H[(x+1,y-1)],x+1,y-1))
			V[(x+1,y-1)]=1
			A[x+1][y-1]=3
		if (x!=n-1 and A[x+1][y]!=0 and V[(x+1,y)]==0):
			G[(x+1,y)]=G[(x,y)]+1
			PQ.put((G[(x+1,y)]+H[(x+1,y)],x+1,y))
			V[(x+1,y)]=1
			A[x+1][y]=3
		if (x!=n-1 and y!=n-1 and A[x+1][y+1]!=0 and V[(x+1,y+1)]==0):
			G[(x+1,y+1)]=G[(x,y)]+1
			PQ.put((G[(x+1,y+1)]+H[(x+1,y+1)],x+1,y+1))			        
			V[(x+1,y+1)]=1
			A[x+1][y+1]=3
			
		os.system("clear")
		print(A)
		os.system("sleep 0.5")  
           		
		no=PQ.qsize()
		if(no==0):
			os.system("clear")
			print("Destination can't be reached!")
			os.system("sleep 0.5") 
			break
		f,x,y=PQ.get(no-1)

		if(x==dx and y==dy):
			os.system("clear")
			A[dx][dy]=5
			print("Destination reached!")
			print(A)
			os.system("sleep 0.5")	
			break 
		else:
			A[x][y]=4          

#change address to the required text file address containing input A matrix
def data_read():
	data=open("/home/devansh/Downloads/lab8/t","r") 
	i=0
	for line in data:
		word=line.split()
		for j in range(n):
			A[i][j]=word[j]
		i+=1
		
#-------------------------- Main function ------------------------------
initialize_visited()
data_read() 
dx=3
dy=4 
h(dx,dy)
if(A[0][0]!=0 and A[dx][dy]!=0):
	a_star(A,0,0,dx,dy)
else:
	os.system("clear")
	print("Destination can't be reached!")
	os.system("sleep 0.5") 
