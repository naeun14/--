fr = open("number1to10.txt","r")  #읽기모드로 열기
num_list = fr.read().rstrip().split("\n")  #리스트에 파일 내용을 \n으로 잘라 저장 
fr.close()

fw = open("numberby10.txt","w")         #쓰기모드로 열기
for i in range(len(num_list)):        #리스트크기 -1 만큼 반복
    write_text = int(num_list[i])*10    #파일내용*10
    fw.write(str(write_text)+'\n')      #파일에 쓰기
    
fw.close()
