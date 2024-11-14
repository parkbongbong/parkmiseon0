# 절차지향 프로그래밍 언어 : C, C++
# 객체지향 프로그래밍 언어 : JAVA, Python, c#
# 함수지향 프로그래밍 언어 : Go, Rust

# 객체지향 프로그래밍 언어(OOP)
# - 객체 -> Class
#            + 변수(필드)
#            + 함수(매서드)

# 함수(Method, Function)
# - 어떤 일을 수행하는 코드 묶음
# - 반복적으로 동작해야하는 일들
# ex) 초급 개발자 -> 아침마다 퇴근 후부터 오전 9시까지 로그 데이터를 
#                   시각화하세요. (25 line)
#                   25 line -> 함수() 생성 -> 아침마다 함수 호출(1 line)
                   
# ** 함수 개발 가이드라인 **
# 1. 함수 이름 및 내용
# - 함수 이름에 함수의 역할과 의도 명확히 드러낼 것!
# - 함수 내용은 가능하면 짧게 작성 (Code line 줄이기)
 
# 2. 함수의 역할
# - 하나의 함수에 유사한 역할을 하는 코드만 포함
# - 하나의 함수는 한 가지 기능만 명확히 정의 
# - ex) 계산기(덧셈, 뺄셈, 곱셈, 나눗셈)
#     -> 함수 몇개 만들어야 할까요? 4개
#     -> 재사용성이 좋아짐!
#        예) 계산기 함수(곱셈, 나눗셈, 덧셈, 뺄셈)
#            제곱 기능(곱셈 2번) -> 곱셈() 2번 호출, 제곱

# 3. 함수를 만들어야 하는 경우
# - 공통적으로 사용되는 코드는 함수로 생성
# - 복잡한 로직이 사용되는 경우 식별 가능한 이름의 함수 생성

# ** 함수의 종류 **
# 1. 내장 함수 (built-in function)
# - 프로그래밍 언어를 설치하면 내부적으로 제공하는 기본 함수들
#    print(), type(), range(), ...

# 2. 외장 함수
# - 라이브러리 : 다른 사람들이 개발한 코드 묶음
# - impor문을 통해서 라이브러리 모듈 제공
#   가. 다운로드     (ex: 아나콘다 pip install~)
#   나. import 호출 (ex: from datetime import datetime)
#   다. 사용하기    (ex: datetime.today())
#   .(참조 연산자)

# 3. 사용자 정의 함수
# - 개발자가 직접 만들어서 사용하는 함수

# ** 함수 이름 규칙 **
# - snake_case()

# post 변수(Field)
# Post  Class
# post()  Method

# ** 함수 정의 **
# 1. 기본 함수 문법
# def 함수명(parameterl1, parameterl2, ...):
#     실행문
#     return 반환값
# 2. 함수 정의시 "def" 키워드 사용(define)
# 3. 인자(argument or parameter) 정의 : 함수 입력값
# 4. return : 함수 종료 의미
# 5. return 반환값 : 함수 종료 + 호출문으로 반환값 전달(tuple)
# 6. 함수 종료: return or 블록문 끝
# 7. parameter와 return은 생략가능
#    (입력과 반환이 없는 함수도 존재 -> 순수 출력만 하는 기능들)


# ** 함수 사용법 **
# 1. 함수 정의
def sum_two_value(x, y):  # (매개변수)
    sum = x+y
    return sum  # 반환값

# 2. 함수 호출
total = sum_two_value(5, 10)
print(total)

# 3. 인자(입력 매개변수)
# - 함수에 전달되는 입력값
# - 함수 정의문과 호출문의 parameter 갯수가 동일해야함
# - paremeter로 int, str, float, boole, list 등 사용가능
# - 심지어 사용자 정의 함수를 parameter로 전달 가능
# - parameter값 2개 이상 사용 시 정의된 순서대로 전달해야 함

# 4. Default Parameter
# - 함수 호출 시 parameter를 전달받지 못한 경우 기본값 사용
# - 다수의 인자 중 끝에서부터 사용 가능
# def test(a, b, c=5):     # (O)
# def test(a, b=2, c=5):   # (O)
# def test(a=1, b=2, c=5): # (O)
# def test(a=1, b, c):     # (X)
# def test(a, b=2, c):     # (X)
# def test(a=1, b=2, c):   # (X)

# 5. return
# - 기본적으로 함수 종료 의미
# - return 반환값 : 함수 호출문으로 값 전달(tuple type)
# - return만 사용하면 함수호출문으로 None값 전달
# - return이 없는 경우 들여쓰기가 종료되면 함수 종료로 간주
# - return문 다음에 오는 코드는 실행 안됨(Error X)

# 6. 함수의 범위
# - 변수가 참조 가능한 코드상의 범위를 명시
# - 함수내의 변수는 자신이 속한 코드 블럭이 종료되면 소멸
# - 이렇게 특정 코드블록 내에서 선언된 변수를 지역변수
# - 반대로 가장 상단에 정의되어 프로그램 종료 전까지 유지되는 변수를 전역변수
# - 같은 이름의 지역변수와 전역변수 존재하는 경우
#   가까운(지역변수) 순서로 우선순위가 높음

num = 10  # 전역 변수
num1 = 20  # 전역 변수

def test(num, num1):
    num1 = 30  # 지역 변수
    return num,num1

test(num, num1)

# 함수 내에서 전역변수 값을 변경
num = 10  
num1 = 20  
def test(num, num1):
    num1 = 30  
    return num1
num1 = test(num, num1)


num = 10  
num1 = 20  
def test():
    global num1  # global 전역변수 지칭 키워드 (절대사용금지!!)
    num1 = 30  
test()

# 7. 가변길이인자(Variable length parameter)
# - *args(): tuple type
# - **kwargs(): dict type

def test(*args):
    for item in args:
        print(item)
test(10, 20, 30)
test(1, 2, 3, 4, 5)

def test2(**kwargs):
    for key, value in kwargs.item():
        print(key, value)
        
test2(a=1, b=2, c=3)

# 8. Type Hint
# - 입력매개변수와 반환값의 타입을 힌트로 미리 적어두기

def sum(a,b):
    return a+b

def sum(a: int, b: int) -> int:
    return a+b




 