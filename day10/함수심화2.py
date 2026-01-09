# 함수 심화2
# 람다함수
# def로 정의해줘야하는데, 그럴 필요 없이 단순한 함수면
# 람다함수를 사용한다.
# 성능차이 x, 간결하게 작성이 되지 않으면 def 쓰는 것을 권장

def multiply(num1,num2):
    return num1 * num2

lambda_multi = lambda num1, num2: num1 * num2

print(multiply(5,5))
print(lambda_multi(5,5))

# 함수를 받는 함수: 고차함수
# 함수를 매개변수로 전달받아 호출하는 함수
def calc(num1,num2, fx):
    result = fx(num1,num2)
    return result

# 콜백함수: 전달되는 함수
def plus(num1,num2):
    return num1 + num2

calc_result = calc(10, 5, plus)
print(calc_result)
calc_result2 = calc(10,5,
                    lambda num1, num2: num1 * num2)
print(calc_result2)

# 람다함수와 자주 쓰이는 내장함수
# 1. filter(): 함수 결과가 true인 요소들만 남겨주는 함수
# filter(함수 , 리스트)
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda n: n % 2 == 0, nums))
# filter 결과는 list로 형변환해야 리스트처럼 사용가능
print(result)

nums = [1, 5, 10, 30, 60, 100]
# filter를 사용해서
# 10 ~ 60 사이 숫자들만 리스트로 모아서 출력
result = list(filter(lambda n: 10 <= n <= 60, nums))
print(result)

names = ["김철수", "박철수", "김길동", "최영희"]
# filter를 사용해서
# 김씨만 리스트로 모아서 출력