x,y = input("점의 좌표 x,y를 입력하시오 : ").split()
x = int(x)
y = int(y)

if(x > 0):
    if(y > 0):
        state = 1
    else:
        state = 2
else:
    if(y < 0):
        state = 3
    else:
        state = 4

print(state,"사분면에 있음")