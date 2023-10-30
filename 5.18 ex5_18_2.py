#max이나 sort메소드 사용하지 않고 s_list 내의 문자열 항목 중 가장 길이가 긴 문자열 출력
#2개이상일 경우 제일 먼저 나타나는 문자열 출력

s_list = ['abc','bcdefg','abba','cddc','opq']

string_lengh = 0

for i in range(len(s_list)):
    l = len(s_list[i])
    if l > string_lengh:      #저장된 최대길이 보다 더 길 때
        string = s_list[i]
        string_lengh = l      #최대길이 변수에 저장
    
print(string)