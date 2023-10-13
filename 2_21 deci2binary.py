a = int(input("정수를 입력하세요:"))
result = bin(a)
result_not = bin(~a)
result_not_2binary = int(~a)
print(a,"의 2진수 값:" ,result)
print(a,"의 값에 대한 비트단위 부정값:",result_not)
print(a,"의 값에 대한 비트단위 부정값을 십진수로 출력 :",result_not_2binary)

