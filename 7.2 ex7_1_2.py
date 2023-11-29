import time
def sum1to1000000():
    total = 0
    for i in range(1, 1000001):
        total += i
    return total

    
start_time = time.time()
for i in range(100):
    sum = sum1to1000000()
end_time = time.time() 
t = end_time - start_time 
print('1에서 1000000까지의 합을 구하고 출력하는 시간 :{:7.4f}초'.format(t))