print("맛나 식당에 오신것을 환영합니다. 메뉴는 다음과 같습니다")
print("1) 햄버거\n2) 치킨\n3) 피자")
select = int(input("1에서 3까지의 메뉴를 선택하세요 : "))

while select > 3 or select < 1:
    select = int(input("메뉴를 다시 입력하세요: "))

if select == 1:
    print("햄버거를 선택하였습니다.")
elif select == 2:
    print("치킨 선택하였습니다.")
else:
    print("피자를 선택하였습니다.")