#t= (tuple(map(int,input().split())))  #입력받는다면
t = (4,5,2,3,8,1,9,0)
for i in range(len(t),0,-1):
    print(t[:i])
    