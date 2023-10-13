import numpy as np

num_of_times = np.round(np.arange(0,3.0,0.1),1)

for i, data_num in enumerate(num_of_times):
    data = np.random.randint(0, 2, size=10**7)
    x = 2 * data - 1  
    n = np.random.randn(10**7) * data_num
    r = x + n
    y = np.where(r > 0, 1, 0)
    check = np.where(y == data, 1,0)
    count_check = np.count_nonzero(check == 1) # 바르게 복조한 비트 
    print("에러 확률:",f"{(data.size-count_check)/data.size:.6f}")