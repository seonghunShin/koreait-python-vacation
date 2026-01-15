# 예외 - error
# 예외도 객체다.
# 에러가 발생 -> 예외클래스의 객체가 생성
# 인터프리터는 "즉시" 해석을 멈추고,
# 에러메세지를 콘솔에 출력

# 예외 처리
"""
---- 필수 ----
try:
    예외가 발생할 것 같은 코드
except(예외종류1, 예외종류2):
    예외 발생 시 실행 할 코드
---- 필수 ----
---- 선택 ----
else:
    예외 없이 성공했을때 실행될 코드
finally:
    예외 여부랑 상관없이 마지막에 실행할 코드
---- 선택 ----
"""

# print(1)
# print(2 / 0) # 예외발생! -> 코드해석 멈춤
# print(3)

# 예외 종류
# 1. SyntaxError - 문법에러(코드아래 빨간줄)
# 2. TypeError - 타입이 맞지않는 '연산'시 발생
try:
    a = "홍길동"
    b = 20
    print(a + b) # 에러생성!
    print("아자쓰") # 실행안됨
except TypeError as e: # 에러객체가 e라는 변수에 담김
    print("타입에러!")
    print(f"에러내용: {e}") # 에러객체의 __str__호출

# 3.NameError: 변수 선언 전에 읽을 때
# print(name)
# name = "홍길동"

# 4. IndexError: 인덱스 범위를 벗어날 때
my_list = [1, 2, 3]
# print(my_list[100]) 범위초과

# 5. keyError: dict에 없는키로 접근할 때
# 6. ValueError: 타입은 맞는데, 값이 이상한 경우
try:
    sample = "abc"
    int(sample)
    # int(): 문자열은 맞는데, 값이 숫자처럼 생겨야 함.
    names = ["철수", "영희"]
    names.remove("병철")
    # 문자열은 맞는데, 리스트에 있는 문자열이어야 함.
except ValueError as e:
    print("밸류 에러!")

# 7. ImportError: 없는 모듈 import할 때
# 8. IndentationError: 들여쓰기 실수
# 9. ZeroDivisionError: 0으로 나올 때

try:
    num = input("숫자를 입력: ")
    int_num = int(num)
    result = 100 / int_num
    print(result)
except (ValueError, ZeroDivisionError) as e:
    print("정상적인 값을 입력하세요")

# except ValueError as e:
#     print("숫자 입력하세요")
# except ZeroDivisionError as e:
#     print("무한대")

# else: 예외 없이 성공시
try:
    num = "10살"
    age = int(num) # 예외발생 -> age에는 아무것도 안담김
except ValueError as e:
    print("숫자가 아니에요")
else:
    if age > 19: # NameError 발생
        print("성인!")
    else:
        print("미성년자!")


file = None
try:
    file = open("./hi.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("hi.txt파일이 없습다.")
finally:
    # 예외와 상관없이 항상 실행될 코드
    # 주로 자원반납
    file.close()