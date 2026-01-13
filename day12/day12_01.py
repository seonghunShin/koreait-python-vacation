# 상속
# 두 개 이상의 클래스가 공통코드가 많을 때
# 이를 상위클래스를 정의해서 묶어 줄 수 있음

class Pet:
    def __init__(self, name, age):
        print("부모클래스 생성자 호출!")
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}가 밥을 먹습니다.")

class Dog(Pet):
    def sound(self):
        print(f"{self.name}이 짖습니다. 멍멍")

class Cat(Pet):
    def sound(self):
        print(f"{self.name}이 말합니다. 야옹")

    # 부모의 함수를 재정의: 오버라이딩(overwriting)
    def eat(self):
        print("캣잎주세요.")

# __init__정의 안했음
# Dog와 Cat의 생성자를 호출했지만,
# 부모클래스의 __init__이 호출 됨
dog = Dog("뽀삐", 5)
cat = Cat("호피", 5)
dog.eat() # 부모클래스 eat
cat.eat()

# MRO(method resolution order)
# 자식 클래스에 호출한 함수가 없으면
# 파이썬은 부모클래스에 해당 함수를 찾으러 간다.
# 있으면 부모것을 호출
print("")
# 오버라이딩 활용
class Car:
    def __init__(self, name, model):
        print("부모클래스 생성자 호출!")
        self.name = name
        self.model = model

    def drive(self):
        print(f"{self.name}이 주행을 시작합니다.")

# 상속받은 자식 객체는 super(부모) 객체의 데이터 영역이
# 구분되어 있다.
# 단, self의 데이터 영역은 super 객체의 데이터 영역을 포함한다.
class ElectricCar(Car):
    # __init__을 재정의
    # super().__init__()이 호출 되어야 함.
    def __init__(self, name, model, battery):
        super().__init__(name, model)
        # super(): 부모의 함수를 연결해주는 함수
        self.battery = battery

    # 오버라이딩
    def drive(self):
        super().drive() # 부모의 drive 호출
        print("전기로!!")

class GasCar(Car):
    # __init__을 재정의
    # super().__init__()이 호출 되어야 함.
    def __init__(self, name, model, gas):
        super().__init__(name, model)
        # super(): 부모의 함수를 연결해주는 함수
        self.gas = gas

    # 오버라이딩
    def drive(self):
        super().drive() # 부모의 drive 호출
        print("휘발유로!!")

# 호출된 test_car는 같은 코드
# 동작이 달라진다.
def test_car(car):
    # 검증코드 필요
    # 매개변수로 들어온 car가
    # drive() 함수를 반드시 가지고 있길 바람
    # drive는 오버라이딩된 함수임.
    # -> Car를 상속받은 객체인지만 확인하면 되겠다.
    is_car_instance = isinstance(car, Car)
    if not is_car_instance:
        print("자동차가 아닙니다.")
        return

    car.drive() # 같은 함수 호출 중
    # drive라는 같은 함수 -> 다른 동작
    # : 다형성

e_car = ElectricCar("모델y", "tesla", 100)
g_car = GasCar("x3", "bmw", 100)

test_car(g_car)
test_car(e_car)


class Payment:
    def __init__(self):
        print("결제시스템 초기화")

    # pass - 나중에 구현하겠다. 에러방지
    # 상속받은 자식 클래스에서 오버라이딩하면
    # 호출안됨
    def pay(self, price):
        pass

# KakaoPayment - pay오버라이딩 15000원 이상 결제시 5%할인
# NaverPayment - pqy오버라이딩 20000원 이상 결제시 2000할인

# class KakaoPayment(Payment):
#     def __init__(self, price):
#         super().__init__()
#         self.price = price
#
#     def pay(self):
#         if self.price >= 15000:
#             print(self.price * 0.95)
#             return
#         print(self.price)
#
# class NaverPayment(Payment):
#     def __init__(self, price):
#         super().__init__()
#         self.price = price
#
#     def pay(self):
#         if self.price >= 20000:
#             print(self.price - 2000)
#             return
#         print(self.price)
#
# def test_payment(payment):
#     payment.pay()
#
# k_pay = KakaoPayment(15000)
# n_pay = NaverPayment(20000)
# test_payment(k_pay)
# test_payment(n_pay)

class KakaoPayment(Payment):
    # 생성자 생략 - 생성자를 오버라이딩할때는
    # super().__init__() 필요
    def pay(self, price):
        # super().pay() 오버라이딩 시 필수 아님
        if price >= 15000:
            return price * 0.95
        return price

class NaverPayment(Payment):
    def pay(self, price):
        if price >= 20000:
            return price - 2000
        return price

def order(payment, price):
    is_payment = isinstance(payment, Payment)
    if not is_payment:
        print("올바른 결제방식을 선택하세요")
        return

    total_price = payment.pay(price)
    print(f"총 결제금액: {int(total_price)}원")

food_menu = {
    "피자": 25000,
    "치킨": 20000,
    "참치김밥": 5000,
    "라면": 4000,
    "제로콜라": 1500
}

# [{피자: 2}, {라면: 1}.. {}]
# 위의 리스트를 받아서 결제 총금액을 리턴
def accept(menus):
    # 메뉴들에서 메뉴들을 골라 옴
    price_sum = 0
    for menu in menus:
        # menu -> {메뉴이름: 갯수}
        # menu.items -> [(메뉴이름, 갯수)]
        # menu.items()[0] -> (메뉴이름, 갯수)
        for item_name, item_count in menu.items():
            price = food_menu[item_name]
            price_sum += price * item_count

    return price_sum

cart = []
while(True):
    food_list = list(food_menu.keys())
    print(food_list)
    menu_name = input("담으실 메뉴를 입력하세요: ")
    count = int(input("몇개 담으시겠습니까: "))

    cart_item = { menu_name: count }
    cart.append(cart_item)

    confirm = input("주문을 마치시겠습니까? (y/n): ")
    if confirm.lower() == "y":
        break

total_price = accept(cart)

kakao = KakaoPayment()
naver = NaverPayment()

order(kakao, total_price)
order(naver, total_price)