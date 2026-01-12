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
result = list(filter(lambda name: name.startswith("김"), names))
print(result)

# 2. map(리스트 요소를 조작하는 함수, 리스트)
nums = [1, 2, 3, 4]
result = list(map(lambda n: n ** 2, nums))
print(result)

# foods에서 (상함)이 붙은 데이터를 (상함)을 떼주세요
foods = ["계란", "우유(상함)", "사과", "치즈(상함)"]
result = map(lambda food: food[: -4] if "(상함)" in food else food, foods)
result = list(result)
print(result)

# map()을 사용해서, 이름 뒤에 ~고객님이라고 문자열을 모두 수정해주세요.
# ["철수고객님", "영희고객님"..., "병철고객님"
names = ["철수", "영희", "민수", "병철"]
result = list(map(lambda name: name+"고객님", names))
print(result)

# 3. sorted - 정렬
nums = [30, 55, 1, 4, 11]
# 숫자 리스트는 오름차순 정렬된 결과를 리턴
sorted_nums = sorted(nums)
print(sorted_nums)

words = ["banana", "kiwi", "apple"]
sorted_words = sorted(words)
# 사전순으로 정렬된 결과를 리턴
print(sorted_words)

# sorted에 key라는 매개변수에 함수를 전달할 수 있음
# key로 넘겨준 함수결과로 정렬
sorted_words_by_len = sorted(words, key=lambda word: -1 * len(word))
print(sorted_words_by_len)
# -1을 곱하면 내림차순으로 할 수도 있음
# reverse = True로 내림차순으로 할 수 있음

nums = [30, 55, 1, 4, 11]
# 내림차순?
desc_nums = sorted(nums, key=lambda n: -n)
print(desc_nums)

# max(), min(): key함수 결과로 최대, 최소 연산
nums = [30, 55, 1, 4, 11]
print(max(nums))
print(min(nums))
print(max(1, 5, 3, 30, 100))# *args 패킹

names = ["Kim", "Park", "Lee"]
# 이름이 가장 긴걸 찾을 때
longest_name = max(names, key=lambda name: len(name))
print(longest_name)

# 짧은 이름을 찾는데 함수결과가 동률인 경우
# 사전순으로 빠른걸 찾겠다
# 리턴값에 튜플로 적용될 값의 우선순위를 지정할 수 있다.
shortest_name = min(names, key=lambda name: (len(name), name))
print(shortest_name)

scores = [
    {"name": "홍길동1", "score": 80},
    {"name": "홍길동2", "score": 50},
    {"name": "홍길동3", "score": 90}
]
highest = max(scores, key=lambda data: data["score"])
print(highest["name"])

# max()를 사용하여서 가격이 가장 비싼 과일
# 가격이 동률이면, 무게가 많이 나가는걸 찾아주세요.
fruits = [
    {"name": "apple", "price": 1200, "weight": 100},
    {"name": "banana", "price": 800, "weight": 100},
    {"name": "grape", "price": 2500, "weight": 70},
    {"name": "peach", "price": 2500, "weight": 120},
]
expensive_fruit = max(fruits, key=lambda fruit: (fruit["price"], fruit["weight"]))
print(expensive_fruit["name"])