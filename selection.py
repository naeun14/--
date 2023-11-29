sorting = [5, 10, 7, 9, 3, 1, 1, 2, 5, 4, 6, 7, 12, 11, 8]
print("정렬되지 않은 배열: {}".format(sorting))

for i in range(len(sorting)) :
    test = sorting[i:]
    min_num = min(test)
    sorting[i],sorting[test.index(min_num)+i] = sorting[test.index(min_num)+i], sorting[i] 

print("select 정렬 후 배열: {}".format(sorting))
 