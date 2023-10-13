for i in range(2,13):
    prime = True
    for j in range(2,i):
        if i % j == 0:
            prime = False
            break
    if(prime):
        print(i,": 소수")
    else:
        print(i,": 합성수")