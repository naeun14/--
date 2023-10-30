fr = open("random_numbers.txt",'r')         #파일 열기
num = fr.read().rstrip().split(' ')         #파일의 마지막 문자 공백을 제외한 문자열을 공백으로 분리하여 num 리스트에 저장
fr.close()

fw = open("randoo_even.txt",'w')            
for i in range(len(num)):                   #파일 크기만큼 반복
    if(int(num[i]) % 2 == 0):               #짝수 값이라면
        fw.write(num[i]+' ')                #파일에 저장
    
fw.close()