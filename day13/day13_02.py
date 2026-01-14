# 클래스 변수
# 클래스 내부에도 데이터를 저장할 수 있음
# 해당 클래스 객체들은 다 공유

class Student:
    # 클래스 변수
    school_name = "파이썬 고등학교"
    count = 0

    def __init__(self, name):
        # 객체(인스턴스) 변수
        self.name = name
        Student.count += 1
        # 정원 100명만 받겠다
        if Student.count > 100:
            print("정원 초과! 현재 100명")
            # 예외(에러)를 고의로 일으켜야한다.

st1 = Student("김학생")
st2 = Student("박학생")
print(st1.name)
print(st1.school_name) # 클래스 변수 접근"만" 가능
print(st2.school_name) # 동일한 변수에 접근"만" 가능

# 데이터의 실제 메모리 주소
id_1 = id(st1.school_name)
print(id_1)
id_2 = id(st2.school_name)
print(id_2)

# 객체로 접근하여서 클래스변수 "변경"은 안됨
st1.name = "김학생아님" # 필드값 변경
print(st1.name)

# 클래스 변수 변경이 아니라
# st1에 school_name이라는
# 필드를 추가하는 것으로 파이썬이 해석
st1.school_name = "파이썬 대학교"
print(st2.school_name)
print(st1.school_name)

# 클래스 이름으로 접근해야 변경 가능
Student.school_name = "파이썬 대학교"
print(st2.school_name)
print(st1.count)

print("\n")

class Wallet:
    # 공용 돈 -> 클래스변수
    total_money = 100000
    def __init__(self, name):
        self.name = name
        self.money = 0 # 지갑 생성시 0원

    def __str__(self):
        return f"{self.name}의 소지금: {self.money} 남은 공용 돈: {self.total_money}"

    def take_money(self, amount):
        if not isinstance(amount, int):
            print("숫자를 입력해주세요.")
            return
        # 공용돈을 내 지갑(money필드)에
        # 옮기는 코드 작성
        # 남은 공용돈보다 더 많은 금액을 가져갈 수는 없음

        # 대소비교, 동일비교 -> 읽기
        # 객체로 접근해도 동일하게 동작
        if amount > Wallet.total_money:
            print("공용 돈이 모자랍니다.")
            return
        # 클래스변수 변경? 클래스. 으로 접근
        Wallet.total_money -= amount
        self.money += amount
        return

p1 = Wallet("사람1")
p2 = Wallet("사람2")

p1.take_money(30000)
print(p1)
p2.take_money(55000)
print(p2)
p1.take_money(16000)
print(p1)