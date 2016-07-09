
def judge(x,y,p):
    if ( (bd[0][0] == bd[1][1] == bd[2][2] == p) or\
         (bd[2][0] == bd[1][1] == bd[0][2] == p) ):
        print("Player %d is winner?"%(bd[1][1]))
        return bd[1][1]
    
    elif ( bd[y]==[p,p,p] or\
           (bd[0][x],bd[1][x],bd[2][x]) == (p,p,p)):
        print("Player %d is winner"%(p))
        return p
    
    else:
        return 2
    
bd =[[2,2,2],
     [2,2,2],
     [2,2,2]]

p=0

while(True):
    print("Player %d's turn."%(p))
    x=int(input()) -1
    y=int(input()) -1
    if(bd[y][x] !=2):
        print("Cannot!")
        continue
    bd[y][x] =p
    if(judge(x,y,p) !=2 ): break
    print(bd[0])
    print(bd[1])
    print(bd[2])
    print("")
    p = (p+1)%2


