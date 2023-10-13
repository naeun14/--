def sort3(sorting):
    sorting = sorted(sorting)
        
    print("정렬된 리스트는 다음과 같습니다: {} {} {}".format(sorting[0],sorting[1],sorting[2]))
    
        
sorting = []
print("세 수를 입력하세요:")
for i in range(3):
    num = int(input())
    sorting.append(num)
    
sorted_numbers = sort3(sorting)
