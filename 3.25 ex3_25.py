snail = 0
day = 1

while True:
    snail += 7
    print("day : {}  달팽이의 위치: {} 미터".format(day,snail))
    if(snail > 29):
        break
    snail -= 5
    day += 1

print("\n우물을 탈출하는 데 걸린 날은 {}일 입니다.".format(day))