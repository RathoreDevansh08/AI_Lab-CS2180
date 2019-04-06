import numpy as np
import matplotlib.pyplot as plt

velL=[-0.07,0.07]
posL=[-1.2,0.5]
A=[-1,0,1]

gamma=0.9
psize=100
vsize=100

posUnit=(posL[1]-posL[0])/(psize-1)
velUnit=(velL[1]-velL[0])/(vsize-1)

def update(pos,vel,a):
    v=vel+0.001*a-0.0025*np.cos(3*pos)
    p=pos+vel
    v=min(velL[1],max(v,velL[0]))
    p=min(posL[1],max(p,posL[0]))
    if(p==posL[0]):
        v=0
    return p,v

def reward(p,v):
    if(p==posL[1]):
        return 50
    else: 
        return -10

def repeat(TV, OP):  
    for p in range(psize):
        for v in range(vsize):
            maxv=-10000
            op=0
            t=0
            for a in A:
                Pos=posL[0]+(p*posUnit)
                Vel=velL[0]+(v*velUnit)
                
                newP, newV = update(Pos, Vel, a)
                npi=(newP-posL[0])/posUnit
                nvi=(newV-velL[0])/velUnit
                npi=int(np.ceil(npi))
                nvi=int(np.ceil(nvi))
                
                t=reward(newP,newV)+gamma*(TV[npi][nvi])
                
                if(maxv<t):
                    maxv=t
                    op=a
                
            TV[p][v]=maxv
            OP[p][v]=op
    return TV,OP

def Value_iteration(it=300):
    TV=np.zeros((psize,vsize))
    OP=np.zeros((psize,vsize))
    for i in range(it):
        if(i%50==0):
        	print("iteration: "+ str(i))
        TV,OP=repeat(TV,OP)
    return TV,OP


#------------------------ Main Program ----------------------------

TV,OP=Value_iteration()

plt.imshow(TV, interpolation="nearest")
plt.show()

np.savetxt("V.txt", TV, fmt = "%i")
np.savetxt("P.txt", OP, fmt = "%i")

