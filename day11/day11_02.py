# 객체지향 프로그래밍
# 검증된 값들과 동작을 묶고 싶다.

# 은행계좌 클래스
class BankAccount:
    def __init__(self, name):
        # 검증하는 코드 작성 가능
        self.name = name
        self.balance = 0 # 계좌 개설시 무조건 0원

    def check_balance(self):
        print(f"{self.name}님의 잔액: {self.balance}")

    # 예금
    def deposit(self, amount):
        # amount가 숫자인지 검증
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액 부족")
            return

        # 검증 이후에 객체에 담긴 데이터를 조작할 수 있다.
        # 객체에 담긴 데이터는 언제나  신뢰가능하다.
        self.balance -= amount

acc1 = BankAccount("홍길동")
acc2 = BankAccount("김길동")

acc1.deposit(10000)
acc2.deposit(5000)

acc1.withdraw(6000)
acc2.withdraw(6000)

acc1.check_balance()
acc2.check_balance()

print()
# Cup 클래스
# 필드: size(최대용량), water(현재물의양) - 생성시 0
# 함수: fill(self, amount) - size를 넘어가면 안됨
# drink(self, amount) - water를 넘어가면 안됨
# check(self) - 현재 물의 양 출력

class Cup:
    def __init__(self, size):
        self.size = size
        self.water = 0

    def fill(self, amount):
        if amount > self.size - self.water:
            print("컴의 용량을 넘어섭니다.")
            return
        self.water += amount

    def drink(self, amount):
        if amount > self.water:
            print("현재 물의 양을 넘어갑니다.")
            return
        self.water -= amount

    def check(self):
        print(f"현재 물의 양: {self.water}ml")

cup1 = Cup(100)
cup1.fill(30)
cup1.drink(20)
cup1.check()