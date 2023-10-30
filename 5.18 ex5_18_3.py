#예제 18-1에서 'abc' 'bcd' 'opq' 와 같이 길이가 같을 경우 가장 짧은 문자열 3개를 모두 출력

s_list = ['abc','bcdefg','abba','cddc','opq']
string_list = []

s_list.sort(key=len)
    
for i in range(len(s_list)):
    if len(s_list[0]) != len(s_list[i]):
        break
    string_list.append(s_list[i])   #리스트에 저장

print(string_list)
