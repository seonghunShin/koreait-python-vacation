# 클래스메서드 / 정적메서드

class Person:
    # 클래스 변수
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    # 인스턴스 메서드
    # self를 매개변수로 받고있다. -> 객체가 아니면 호출x
    # 객체.메서드() 호출
    def print_person(self):
        print(f"{self.name}입니다.")

    # 클래스메서드
    # 클래스 이름으로 호출 가능
    # 객체로도 호출 가능
    @classmethod # @: 어노테이션
    def print_population(cls):
        print(f"현재 인구수: {cls.population}")

    # 클래스로 부터 생성된 객체들이
    # 자주 사용할 것 같은 일반 메서드 -> 정적 메서드
    @staticmethod
    def is_adult(age):
        return age > 19

    # 인스턴스 메서드
    def is_adult2(self):
        return self.age > 19

    # __init__을 간접적으로 호출해서
    # 객체를 생성하는 방법
    @classmethod
    def from_dict(cls, data):
        # dict에 담긴 정보로
        # Person 객체를 만들어보자.
        return Person(data["name"], data["age"])




p1 = Person("홍길동", 10)
p2 = Person("길동이동생", 8)
p1.print_person()
p2.print_person()

p1.print_population()
Person.print_population()

p1.is_adult(p1.age)
p1.is_adult2()

dict_person = {
    "name": "김철수",
    "age": 25,
}
p3 = Person(dict_person["name"], dict_person["age"])
p4 = Person.from_dict(dict_person)

"""
1. 인스턴스 메서드 -> self -> 필드값 조작 or 활용할 때 사용
2. 클래스 메서드 -> cls -> 클래스변수, 객체생성.. 사용
3. 정적 메서드 -> 일반함수 -> 일반함수가 자주쓰이면 묶어줌
"""