#진약수 구하는 함수
def is_perfect_num(n):
    div_num = []
    for i in range(1,n):
        if n % i == 0:
            div_num.append(i)
            
    n1 = sum(div_num) #약수의 합
    #완전수 일 경우 정보 출력
    if n1 == n: 
        print("{}은 완전수 입니다".format(n))
        print("{}의 약수 : {}, 약수의 합 = {}".format(n, div_num, n1))
    

start_num = 1
end_num = 10001
for i in range(start_num, end_num):
    is_perfect_num(i)