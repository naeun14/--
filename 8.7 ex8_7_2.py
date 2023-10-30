fnum1 = open("number1to10.txt","r")  #읽기모드로 열기
fnum2 = open("numberby10.txt","r")  
num1_list = fnum1.read().rstrip().split("\n")  #리스트에 파일 내용을 \n으로 잘라 저장 
num2_list = fnum2.read().rstrip().split("\n") 
fnum1.close()
fnum2.close()

fw = open("merge.txt","w")         #쓰기모드로 열기
for i in range(len(num1_list)):        #리스트크기 -1 만큼 반복
    fw.write(str(num1_list[i])+" : "+str(num2_list[i])+'\n')      #파일에 쓰기
    
fw.close()
