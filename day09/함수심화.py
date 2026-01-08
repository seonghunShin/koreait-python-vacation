# 매개변수의 기본값 설정
def hello(name, nationality="대한민국"):
    print(f"[{nationality}] {name}님 안녕하세요")

hello("홍길동")
hello("김길동", "미국")

# 기본값 설정이 안되어있는 매개변수는
# 기본값 설정이 되어있는 매개변수 뒤에 올 수 없다.
# def hello(nationality="대한민국", name):
#     print(f"[{nationality}] {name}님 안녕하세요")

# 파이썬은 매개변수를 들어오는 데이터의 순서로 기억
# 기본값 설정이 되어있는게 나중 순서로 와야 명확하게 데이터를 할당가능


# *args 패킹
# 여러개로 들어온 매개변수들은 tuple에 담아서 하나로 가져온다.
print("어쩌고", "저쩌고", "이러쿵", "저러쿵")

# 매개변수명이 *args가 아님
# 매개변수명은 args임
def args_fx(*args):
    # 매개변수의 갯수와 무관하게 모두 tuple 하나로
    # 포장해서 들어온다.
    print(type(args)) # tuple
    print(args)

args_fx(1, 2, 3)

def calc_sum(*numbers):
    number_sum = 0
    for num in numbers:
        number_sum += num
    return number_sum

result = calc_sum(10, 20, 30)
print(result)

# 권장) *args 패킹을 쓸 때는 가장 뒷쪽 매개변수로 설계하자

# **kwargs 패킹
# 여러값을 하나의 dict로 묶어서 전달

# 매개변수 이름이 **details가 아님
# 매개변수 이름은 details임
def make_user(name, **details):
    print(type(details))
    print(details)
    user = {
        "name": name,
    }
    # {"age": 20, "hobby": "축구"}
    user.update(details)
    return user

# key=데이터 형식으로 kwargs를 전달해야한다.
user1 = make_user("홍길동", age=20, hobby="축구")
print(user1)

# **kwargs 언패킹

def print_user(**user):
    print(user)

print_user(name="홍길동", age=20) # kwargs 패킹
other_data = {
    "name": "김길동",
    "age": 22,
    "address": "부산"
}
# kwargs 언패킹
# 이미 dict로 포장되어있으니, 또 포장하지마세요
print_user(**other_data)