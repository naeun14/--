menu = {"Americano":3000, "Ice Anerocano":3500, "Cappuccino":4000, "Caffe Latte":4500, "Espresso":3600}
for key in menu:
    print("{:18s}가격 : {:,d}원".format(key,menu[key]))