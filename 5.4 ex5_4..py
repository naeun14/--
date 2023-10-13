a = [2, 3, 4, 5, 6]
reversed_a = []

for i in range(len(a)):
    element = a.pop()  # 리스트 a의 마지막 요소를 꺼내어
    reversed_a.append(element)  # 새로운 리스트에 추가

print(reversed_a)
