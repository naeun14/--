import numpy as np

# 4.1 데이터 생성
# 0과 1을 가지는 임의의 데이터 배열 생성 
data = np.random.randint(0, 2, size=10**7)

print("배열 'data'의 첫 30개의 값:",end = ' ')
for i in range(0,30):
    print(data[i], end = ' ')
    

print("\n배열 'data'의 크기:",data.size)

# 4.2 변조
# 0을 -1 V로, 1을 1 V로 변조
x = 2 * data - 1  

print("배열 'x'의 첫 30개의 값:",end = ' ')
for i in range(0,30):
    print(x[i], end = ' ')

# 4.3 잡음 (noise) 생성
n = np.random.randn(10**7) 

print("\n배열 'n'의 첫 30개의 값:",end = ' ')
for i in range(0,30):
    print("{0:.4f}".format(n[i]), end = ' ')

# 4.4 수신 신호 계산
r = x + n

print("\n배열 'r'의 첫 30개의 값:",end = ' ')
for i in range(0,30):
    print("{0:.4f}".format(r[i]), end = ' ')
    
# 4.5 복조
y = np.where(r > 0, 1, 0)

print("\n배열 'y'의 첫 30개의 값:",end = ' ')
for i in range(0,30):
    print(y[i], end = ' ')
    
# 4.6 에러 확률 계산
check = np.where(y == data, 1,0)
count_check = np.count_nonzero(check == 1) # 바르게 복조한 비트 

print("\n배열 'check'의 첫 30개의 값:",end = ' ')
for i in range(0,30):
    print(check[i], end = ' ')
print("\n수신기가 바르게 복조한 비트의 개수:",count_check);
print("에러 확률:",(data.size-count_check)/data.size, '\n')  # (전체비트-바르게 복조한 비트) / 전체비트


# 4.7 다양한 잡음 세기에 따른 에러 확률 계산
num_of_times = np.round(np.arange(0,3.0,0.1),1)       #arange함수를 이용해 0부터 3미만까지 0.1씩 증가하여 저장
                                                      #0.3333과 0.6666 등의 출력때문에 round함수 사용하여 소수 첫째자리로 맞춤
                                                      
error_rate = np.empty(num_of_times.shape)             #error_rate 을 num_of_times 만큼의 크기를 가지는 빈 배열 생성

for i, data_num in enumerate(num_of_times):              #송신데이터와 잡음을 매 실행마다 생성함
    original_data = np.random.randint(0, 2, size=10**7)  #송신데이터 생성
    noise = np.random.randn(10**7) * data_num            #잡음 생성 (가우시안 분포, 평균이 0이고 표준편차 1) * 표준편차 변수
    
    Modulated_data = 2 * original_data - 1                   #변조된 data
    incoming_signal = Modulated_data + noise                 #수신 신호
    demodulation = np.where(incoming_signal > 0, 1, 0)       #복조
    
    error_bit = np.where(demodulation == original_data, 0,1)         #송신 데이터와 수신데이터가 다를 때(에러) 1 입력된 배열 생성
    Number_of_errors = np.count_nonzero( error_bit == 1)             #에러 비트개수
    

    error_rate[i] = Number_of_errors/original_data.size              #에러 확률 배열에 저장
    
for i in range(0,30):       #error_rate 배열 출력
    print(i+1,"{0:.6f}".format(error_rate[i]))
    
    
    
    