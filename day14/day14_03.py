colors = ["빨강", "파랑", "노랑", "블랙", "화이트"]

# 아래의 코드에서 예외가 발생 경우의 수를 고려하여
# 예외 처리를 작성해주세요!
# 정상적이면 result 출력!, 언제나 "안녕히가세요" 출력!
try:
    my_idx = input("번호 입력: ")
    my_idx = int(my_idx)
    result = colors[my_idx]
except (ValueError, IndexError) as e:
    print(e)
else:
    print(result)
finally:
    print("안녕히가세요")


# raise: 예외를 의도적으로 생성하는 문법
try:
    raise ValueError("저는 님이 만든 에러입니다.")
except ValueError as e:
    # e의 메세지
    print(e)

# 커스텀(비즈니스)에러
# Exception을 상속받으면 된다.
# Exception -> 모든 에러의 부모클래스
class NegativeScoreError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message

try:
    score = input("점수를 입력하세요")
    score = int(score)
    if score < 0:
        raise NegativeScoreError("점수는 음수일 수 없습니다.")
except NegativeScoreError as e:
    print(e)

# 사용자에게 이메일 주소를 입력받고,
# 에러메세지: "유효하지 않은 이메일 형식"
# "@", ".com" 이 없으면 InvalidEmailError 예외를 발생
# 올바르지 않으면 -> 에러 메시지 출력
# 올바르다면 -> 올바른 이메일 형식입니다. 출력
class InvalidEmailError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message

try:
    email = input("이메일을 입력하여 주세요")
    email = email.strip()
    if "@" not in email or ".com" not in email:
        raise InvalidEmailError("유효하지 않은 이메일 형식.")
except InvalidEmailError as e:
    print(e)
else:
    print("올바른 이메일 형식입니다.")

"""
시스템이 복잡해지면 f(f(f(f(f())))) 복잡도 상승
return으로는 한계가 존재한다.
즉시 멈추고 바로 탈출할 수 있는 문법이 필요하다!
"""