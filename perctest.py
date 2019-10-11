from random import choices
npart=1
side=5  #Should be an odd number
maxsteps=1000
perc=0
time = 0
choice=[1]
density=[(input("enter a number between 0 and 1="))]
steps = [(1,0),(-1,0),(0,1),(0,-1)]
for iside in range(side):
    grid=[[0 for x in range(side)] for y in range(side)]
    time=0
    perc=0
    for ipart in range(npart):
        grid=[[choices(choice,density) for x in range(side)] for y in range(side)]    
        x,y = side//2, side//2
        counter=0
print(grid)
