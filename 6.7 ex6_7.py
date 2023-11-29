sales = (100,121,120,130,140,120,122,123,190,125)
decrease = 0
for i in range(len(sales)):
    if i == 0:
        continue
    if sales[i] < sales[i-1]:
        decrease += 1
        
print("일일 매출 기록:  {}".format(sales))
print("지난 {}일 동안 전일 대비 매출이 감소한 날은 {}일입니다.".format(len(sales),decrease))