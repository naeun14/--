def mean3(a,b,c):
    return (a+b+c)/3

def max3(a,b,c):
    if(a > b):
        if(a > c):
            return a
        else:
            return c
    else:
        if(b > c):
            return b
        else:
            return c
        
def min3(a,b,c):
    if(a < b):
        if(a < c):
            return a
        else:
            return c
    else:
        if(b < c):
            return b
        else:
            return c
        
a,b,c = input('세 수를 입력하시오:').split()
a = float(a)
b = float(b)
c = float(c)

#문자열을 실수로 타입을 변환시킨 뒤 정수인지 판단
while a%1 != 0 or b%1 != 0 or c%1 != 0:
    a,b,c = input('정수인 세 수를  다시 입력하시오: ').split()
    a = float(a)
    b = float(b)
    c = float(c)
    
'''
#인터넷검색으로 찾아본 isdecimal() 사용하기
while not a.isdecimal() or not b.isdecimal() or not c.isdecimal():
    a,b,c = input('정수인 세 수를  다시 입력하시오: ').split()
'''
    
a = int(a)
b = int(b)
c = int(c)
print(a,",",b,",",c,"의 평균값은 ",mean3(a,b,c))
print(a,",",b,",",c,"의 최댓값은 ",max3(a,b,c))
print(a,",",b,",",c,"의 최솟값은 ",min3(a,b,c))