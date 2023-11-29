import random as ran
lo = ran.randrange(1,7)
jul = ran.randrange(1,7)
print("로미오의 주사위 숫자는 {} 입니다.".format(lo))
print("줄리엣의 주사위 숫자는 {} 입니다.".format(jul))
if lo < jul:
    print("줄리엣이 이겼습니다.")
elif lo > jul:
    print("로미오가 이겼습니다.")
else: 
    print("비겼습니다.")
    