first,second,third= input("세 정수를 입력하시오 : ").split()
first = int(first)
second = int(second)
third = int(third)

if first > second:
    first,second = second,first
if second > third:
    second,third = third, second
if first > second:
    first,second = second,first

print("오름차순으로 나열: ", first,second,third)