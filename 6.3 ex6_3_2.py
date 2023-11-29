menu = {"Americano":3000, "Ice Anerocano":3500, "Cappuccino":4000, "Caffe Latte":4500, "Espresso":3600}
for key in menu:
    print("{:18s}가격 : {:,d}원".format(key,menu[key]))
answer = input("위의 메뉴중 하나를 선책하세요: ")
if(answer in menu):
    print("{}는 {:,}원 입니다. 결제를 부탁합니다.".format(answer,menu[answer]))
else:
    print("미안합니다. {}는 메뉴에 없습니다.".format(answer))