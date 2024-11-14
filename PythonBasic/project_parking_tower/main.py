# 주차타워 (엘레베이터)
# - 1~5층(1층당 1대만 주차)
# - 차량번호 : 정수숫자 4자리만 입력

# 기능
# 1. 차량입고
# 2. 차량출고
# 3. 차량조회
# 4. 프로그램 종료

# 1. 공통 설정
max_car = 5  # 최대 주차 5대
cnt_car = 0  # 현재 주차 대수(count)

# 2. 주차 타워 생성 -> list 
# 방법1 : 하드코딩(절대 지양)
# tower = ["","","","",""] 

# 방법2 : for문 활용
# tower = []
# for i in range(max_car):
#     tower.append("")
    
# 방법3 : List Comprehension 활용
tower = ["" for i in range(max_car)]  
# 방법2와 방법3은 동일한 기능의 코드
# 방법3을 사용하면 좀더 효율적으로 코드 개발 가능
# 모든 for문을 "List Comprehension"으로 변경 불가
# (심플한 for문만 가능)

# 3. 주차타워 메뉴 출력
while True:
    print("=" * 50)
    print("== 주차 타워 시스템 ver1.1 ==")
    print("=" * 50)
    print("1. 입고")
    print("2. 출고")
    print("3. 조회")
    print("4. 종료")
    print("=" * 50)
    
    while True:
        select_num = int(input(">> 번호: "))
        if 4 >= select_num >= 1:
            break
        else:
            print(">> MSG: 올바른 번호를 입력해주세요.")
            
    if select_num == 1:  # 입고
        # 도메인 지식 -> 비지니스 고직
    
        # 1. 주차타워 만차 여부 확인
        if cnt_car < max_car:
            # - 만차X : 다음 단계 이동
            # 2. 주차번호(4자리) 입력
            # + 유효성 체크(숫자만 입력, 4자리 입력)
            car_num = input(">> 차량번호: ")
            
            # 3. 주차타워 입고 -> tower[] 저장
            for i, car in enumerate(tower):
                if car == "":  # 빈 주차공간
                    tower[i] = car_num
                    # 4. 현재 주차 차량 최신화 -> cnt_car + 1
                    cnt_car += 1
                    break
            # tower.insert(index, car_num)
            
            
        else:
            print(">> MSG: 만차입니다. 다음에 이용해주세요.")
        # - 만차 : 죄송합니다.
        
      
        
    elif select_num == 2:  # 출고
        pass
        # 1. 차량번호 입력(출고)
        # 2. 주차타워 주차여부 확인
        # y: 다음단계
        # n: "주차 되지 않으 차량입니다"
        # 3. 차량 출고 -> tower -> "" 변경
        # 4. 현재 차량 수 -1
    elif select_num == 3:  # 조회
        print("■"*20)
        for i in range(len(tower)):
            print(f"■■{i+1}층: {tower[i]}")
        print("■" * 20)
    elif select_num == 4:
        print(">> MSG: 프로그램을 종료합니다.")
        exit()
    
    
        
        
