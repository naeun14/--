a = int(input("1부터 9까지의 수를 입력하세요: "))
while a > 9 or a < 1:
    a = int(input("1에서 9까지의 수를 다시 입력하세요: "))

i = 1
while(i<10):
    print("{} * {} = {}".format(a,i,a*i,))
    i += 1
    