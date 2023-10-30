#min이나 sort메소드 사용하지 않고 s_list 내의 문자열 항목 중 가장 길이가 짧은 문자열 출력
#2개 이상일 경우 먼저 나타나는 문자열 출력

s_list = ['abc','bcdefg','abba','cddc','opq']

string_lengh = 10

for i in range(len(s_list)):  #list 길이 만큼 반복문
    l = len(s_list[i])
    if l < string_lengh:      #저장된 최소길이 보다 더 짧을 때
        string = s_list[i]    
        string_lengh = l      #최소길이 저장
    
print(string)