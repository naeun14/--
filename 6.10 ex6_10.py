t = (1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)
num  = 0
for i in t:
    if num == i:
        continue
    if t.count(num) == t.count(i) and num < i:
        num = i
    elif t.count(num) < t.count(i):
        num = i
            
print("주어진 튜플은: {}".format(t))  
print("가장 많이 나타나는 원소는: {}".format(num))