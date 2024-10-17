######################################################
## 프로젝트 : kiosk_ice
## 작성자 : Park05
## 최초생성 : 2024년 10월 14일
## 마지막 수정 : 2024년 10월 14일
## 내용 : 아이스크림을 판매하는 키오스크의 메인 프로그램
## + 회사명
## + 라이센스

from service_kiosk import print_sub_menu, input_menu_num

##########################
## 1. 메뉴와 가격표 생성 ##
##########################
# Dict타입생성 -> 향후 "데이터베이스"사용!
# - 메인 메뉴
main_menu={
    1:"아이스크림",
    2:"음료",
    3:"디저트"
}
# - 서브 메뉴
icecream_menu={
    1:"딸기",
    2:"바닐라",
    3:"초코"
}
icecream_price={
    1:4000,
    2:3500,
    3:4500
}
drink_menu={
    1:"아메리카노",
    2:"복숭아 아이스티",
    3:"딸기스무디"
}
drink_price={
    1:5000,
    2:3500,
    3:4000
}
desert_menu={
    1:"마카롱",
    2:"샌드위치",
    3:"조각 케이크"
}
desert_price={
    1:6000,
    2:6500,
    3:5500
}
# 사용자가 주문한 메뉴 목록
order_list = []





######################
## 2. 메인 메뉴 출력 ##
######################
while True:
    print("*"*50)
    print("** == 베스킨 조선 ==")
    print("** 1. 아이스크림")
    print("** 2. 음료")
    print("** 3. 디저트")
    print(">> MSG: 메뉴를 선택해주세요.")

    order = input_menu_num(3)  
        
    if order ==1 : # 서브 : 아이스크림
        print_sub_menu(icecream_menu, icecream_price, 3)
        sub_order = input_menu_num(3)
        # ["딸기", 4000]
        order_list.append([icecream_menu[sub_order],icecream_price[sub_order]])
        
    elif order ==2 : # 서브 : 음료
        print_sub_menu(drink_menu, drink_price, 3)
        sub_order = input_menu_num(3)
        order_list.append([drink_menu[sub_order],drink_price[sub_order]])
        
    elif order ==3:  # 서브 : 디저트
        print_sub_menu(desert_menu, desert_price, 3)
        sub_order = input_menu_num(3)
        order_list.append([desert_menu[sub_order],desert_price[sub_order]])
     
     # 추가 주문할거냐? 
     # input() y/n : yes or no
     # y: 추가주문
     # n: 결제하는 곳으로 가기!(X)
     # if 주문
     # else:
     
    print(">> MSG: 추가 주문하시겠습니까?")
    while True: 
        yn = input("y/n: ").lower()
        if yn =="y":
            break
        elif yn =="n":
            break
        else:
            print(">> WARNING: 올바른 값을 입력하세요")
            
    if yn == "y":
        continue
    elif yn == "n":
        # 주문내역을 출력
        print("*"*50)
        print(f"== 주문 메뉴 ==")
        # order_list = [[이름, 가격],[이름, 가격]...]
        total = 0
        for i,item in enumerate(order_list):  # item = [이름, 가격]
            print(f"{i+1}.{item[0]}({item[1]}원)")
            total += item[1]
        print(f"고객님이 주문하신 메뉴는 총 {len(order_list)}건으로 ")
        print(f"결제금액은 {total}원 입니다.")
        print(f"이용해주셔서 감사합니다.")
     
    
     # 사용자가 주문한 메뉴 출력   
    # for item in order_list:
    #     print(item)