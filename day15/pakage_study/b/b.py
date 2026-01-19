if __name__ == "__main__":
    print("b를 실행했어요")
else:
    print("b를 import했네요")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_person(self):
        print(f"이름: {self.name}, 나이: {self.age}살")