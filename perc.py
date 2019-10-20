import random as rd
npart=100
side=55 #Should be an odd number
maxsteps=10000
perc=0
time = 0
choice=[1,0]
density=float((input("enter a number between 0 and 1: ")))
denstot=[]
denstot.append(density)
dens1=float(1-density)
denstot.append(dens1)
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
for ipart in range(npart):
    grid=[[rd.choices(choice,denstot) for x in range(side)] for y in range(side)]    
    x,y = side//2, side//2
    counter=0
    grid[x][y]=0
    for istep in range(maxsteps):
        w=0
        z=0
        counter+=1
        sx,sy = rd.choice(steps)
        w = x+sx
        z = y+sy
        if z<0 or w<0 or w==side or z==side:
            time+=counter
            perc+=1 
            break
        if grid[w][z]==[1]:
            continue
        else:
            x += sx
            y += sy
    avetime=time/npart
print("side=%d <t>=%5.2f <t>/r2=%5.2f perc=%5.2f"%(side,avetime,avetime/(side**2),perc/npart))
