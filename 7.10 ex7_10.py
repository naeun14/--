import random as ran
count = 0
x = ran.randrange(1,21)
while(1):
    a = int(input("1~20까지 중 하나의 숫자를 입력하세요: "))
    count += 1
    if a > x:
        print("입력된 숫자가 생성된 숫자보다 큽니다.")
    elif a < x:
        print("입력된 숫자가 생성된 숫자보다 작습니다.")
    else:
        break
print("사용자가 시도한 횟수: {}".format(count))