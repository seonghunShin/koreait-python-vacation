#day08_01.py
"""
변수 ? 데이터 재사용
함수 ? 코드를 재사용

함수정의
def 함수이름(매개변수1, 매개변수2...):
    코드 작성

    return 데이터

- 매개변수와 리턴은 선택사항
- 헷갈리는 부분 정리
함수 정의와 함수 호출은 서로 다른 것
"""

# 매개변수 x, 리턴 x
def hello():
    # 호출되면 아래의 코드를 실행하시오.
    print("안녕하세요")
    print("반갑습니다")

# 함수 호출 -> 함수가 가지고 있던 코드가 실제 실행
hello()
hello()

his_name = "최길동"

# 매개변수 o, 리턴 x
def hello_name(name):
    # 매개변수: 함수가 호출될 떄 외부에서 전달받는 값을 저장
    # 생존범위가 존재한다
    # 함수 안에서만 유효
    print(f"{name}님 안녕하세요")
    print(f"{name}님 반갑습니다")
    # print(f"{his_name}") 일반 변수는 함수 내에서 사용 가능

# print(name) name은 함수 안에서만 생존
hello_name("홍길동")
hello_name("박길동")
my_name = "박화목"
hello_name(my_name)

# introduce라는 함수
# name과 age를 전달 받아서,
# 안녕하세요. 저는 ~ 이고, ~ 살 입니다.

def introduce(name, age):
    print(f"안녕하세요. 저는 {name}이고, {age}살 입니다.")
# input_name = input("이름: ")
# input_name = input_name.strip()
# input_age = input("나이: ")
# input_age = input_age.strip()
# introduce(input_name, input_age)
introduce("홍길동", 25)

# 매개변수 x, 리턴 o
def get_100():
    print("get_100 호출되었습니다.")
    return 100 # return을 읽으면 함수가 즉시 종료
    print("아무거나")

return_value = get_100()
print(f"리턴 받은 값: {return_value}")

# 매개변수 o, 리턴 o
def add(x, y):
    sum = x + y
    return sum

# 호출 결과가 값이면 값,
# 특별한 자료형 데이터라면 그 데이터처럼 다룰 수 있다.
result = add(10, 20)
print(result)
# f(g()) -> g()호출/실행 -> f()호출/실행
result2 = add(add(10, 20), add(10, 20))
print(result2)

score_list1 = [55, 70, 100]

def calc_avg(score_list):
    score_sum = 0
    for score in score_list:
        score_sum += score

    avg = score_sum / len(score_list)
    return avg

score_sum = 0
for score in score_list1:
    score_sum += score

score_list2 = [60, 70, 100]
score_list3 = [70, 80, 90]

print(calc_avg(score_list1))
print(calc_avg(score_list2))
print(calc_avg(score_list3))

# 주민등록번호를 매개변수로 전달 받아서,
# "991122-1122334"
# "-" 빼고 13자리인지?
# 숫자인지?
# 모두 충족되면 True 리턴, 하나라도 안되면 False 리턴

def validate_pn(pn):
    pn = pn.replace("-", "")
    # if pn.isdecimal() or len(pn) == 13:
    #     return True # 얼리 리턴
    # return False
    if not len(pn) == 13:
        return False
    if not pn.isdecimal():
        return False
    # 월 검사
    # "9911221122334"
    month = pn[2:4]
    month = int(month)
    if not (1 <= month <= 12):
        return False
    day = pn[4:6]
    day = int(day)
    if not (1 <= day <= 31):
        return False
    return True
my_pn = "991122-1122334"
result = validate_pn(my_pn)
print(result)

# 주민 번호를 받아서 남자인지 여자인지 리턴
def get_gender(pn):
    # 전달 받은 주민번호가 타당하지 않으면
    if not validate_pn(pn):
        return "유효하지 않은 주민번호 입니다."

    # 991122-3344556
    gender_digit = pn[7]
    gender_digit = int(gender_digit)

    # 1, 3이면 "남자" 리턴
    # 2, 4이면 "여자" 리턴
    # 그 외는 "외국인" 리턴

    if gender_digit in [1, 3]:
        return "남자"
    elif gender_digit in [2, 4]:
        return "여자"
    else:
        return "외국인"

test_pn = "991122-3344556"
result = get_gender(test_pn)
print(result)

# print() 매개변수 갯수가 변한다.
print("안녕하세요", "반갑습니다")
# 입력한 데이터 끝에 엔터가 자동추가
print("안녕하세요", end="..")

# 매개변수에 기본값을 저장할 수 있다.
def print_info(name, age, nationality="대한민국"):
    print(f"이름: {name}, 나이{age}, 국적: {nationality}")

# 기본 값 설정이 되면, 호출 시 매개변수 생략해도
# 기본 값 사용된다.
print_info("홍길동", 30)