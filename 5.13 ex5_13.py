
values_list = []
input_values = input("임의의 갯수만큼 정수를 입력하세요: ").split()

for i in input_values:
    value = int(i)
    values_list.append(value) 

value_sum = sum(values_list)

# 평균 계산
avg = sum(values_list) /  len(values_list)

# 각 값과 평균의 제곱을 합하여 분산을 계산
variance = sum((value - avg) ** 2 for value in values_list) / len(values_list)
# 표준편차 계산
std_deviation = (variance ** 0.5)

print("합: {}".format(value_sum))
print("평균: {:.1f}".format(avg))
print("표준편차: {:.2f}".format(std_deviation))
