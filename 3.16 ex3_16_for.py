a = int(input("1부터 9까지의 수를 입력하세요: "))
for i in range(1000):
    a = int(input("1에서 9까지의 수를 다시 입력하세요: "))
    if 0 < a < 10:
        break
for i in range(1,10):
    print("{} * {} = {}".format(a,i,a*i,))
    