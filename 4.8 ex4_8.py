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
        
        
def mean6(a,b,c,d,e,f):
    return (mean3(a,b,c)+mean3(d,e,f))/2

def max6(a,b,c,d,e,f):
    x = max3(a,b,c)
    y = max3(d,e,f)
    if x>y:
        return x
    else:
        return y

def min6(a,b,c,d,e,f):
    x = min3(a,b,c)
    y = min3(d,e,f)
    if x<y:
        return x
    else:
        return y
    
a,b,c,d,e,f = input('여섯 개의 수를 입력하시오: ').split()


#4-7의 과제에서 문자열을 실수형으로 바꿔 정수인지 확인하는 조건문을 예시로 보임
#인터넷검색으로 찾아본 isdecimal() 사용하기 
while not a.isdecimal() or not b.isdecimal() or not c.isdecimal() or not d.isdecimal() or not e.isdecimal() or not f.isdecimal():
    a,b,c,d,e,f = input('정수인 여섯 개의 수를  다시 입력하시오: ').split()
    
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)   

print("평균값은 ",mean6(a,b,c,d,e,f))
print("최댓값은 ",max6(a,b,c,d,e,f))
print("최솟값은 ",min6(a,b,c,d,e,f))