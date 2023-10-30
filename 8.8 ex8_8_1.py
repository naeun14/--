import random    #random.randint 사용하기 위해 선언

fw = open("random_numbers.txt",'w')         #파일 열기
for i in range(10):
    random_num = random.randint(1,1000)     #랜덤 숫자 저장
    fw.write(str(random_num)+' ')

fw.close()

