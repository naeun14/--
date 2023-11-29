import random as ran
import numpy as np
a = []
for _ in range(10):
    a.append(ran.random())

print("a = [ ",end="")
for i in range(10):
    print("{:.8f}".format(a[i]),end=" ")
print("]")
print("최댓값: {:.15f}".format(np.max(a)))
print("최솟값: {:.15f}".format(np.min(a)))
print("평균값: {:.15f}".format(np.mean(a)))