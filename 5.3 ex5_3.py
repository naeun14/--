list1 = [3,5,7]
list2 = [2,3,4,5,6]

for num1 in list1:
    for num2 in list2:
        result = num1 * num2
        print("{} * {} = {}".format(num1,num2,result))