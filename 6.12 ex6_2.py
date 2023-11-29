l = [5,6,3,9,2,12,3,8,7]
print('주어진 리스트는 = {}'.format(l))

for i in range(0,len(l)-1):
    if l[i] > l[i+1]:
        l[i],l[i+1] = l[i+1],l[i]
    
print("가장 큰 수를 마지막으로 옮긴 결과: {}".format(l))