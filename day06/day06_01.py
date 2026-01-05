# day06_01

a = ["Seoul", "Kyeonggi", "Incheon", "Daejun", "Daegu", "Pusan"]
str = "S"

for i in a:
	str = str + i[1]

print(str)

# 이중 for 문 = 비교
s1 = ["a", "b", "c"]
s2  = ["com", "b", "d", "p", "c"]
# s1과 s2 배열의 유사도를 출력

count = 0
for x in s1:
    for y in s2:
        if x == y:
            print(f"{x}와 동일한 데이터 {y}발견")
            count += 1

print(count)

# break & continue

# break를 읽으면 반복문을 한 번 탈출
for num in range(10):
    # 10번 반복 중 num이 5가 되면 탈출
    if num == 5:
        print("5가 되었습니다. 탈출!")
        break

    print(num)

# continue를 읽으면 다음 반복을 즉시 실행
for num in range(10):
    # 10번 반복 중 num이 5가 되면 다음 반복 실행
    if num == 5:
        print("5가 되었습니다. 스킵!")
        continue

    print(num) # num이 5면 실행되지 않음

# 짝수만 출력!
for num in range(10):
    if num % 2 != 0: # 홀수면
        continue # 다음 반복

    print(num)

foods = ["계란", "우유(상함)",
         "사과", "김치", "수박(상함)"]

# "(상함)"이 포함되지 않은 음식만 출력

for food in foods:
    if "(상함)" in food:
        continue
    print(food)
print()

for food in foods:
    # food는 대입받는 변수이지 원본이 x
    if "(상함)" in food:
        food = food[:-4] # 대입받는 변수를 수정한 것
        print(food)

print(foods)

# 원본을 수정하려면? 인덱스 정보가 필요하다.
# enumerate(): 리스트 데이터를 (인덱스, 데이터) 튜플 형태로 만들어 준다.
# foods = ["계란", "우유(상함)", "사과", "김치", "수박(상함)"]
# [(0, "계란"), (1, "우유(상함)"), (...), (...), (4, "수박(상함)")]

samples = enumerate(foods)
# idx, food = (0, "계란")
for idx, food in samples: # 튜플 언패킹
    print(f"{idx}: {food}")

for idx, food in enumerate(foods):
    # "(상함)"
    if "(상함)" in food:
        # 원본 수정
        foods[idx] = food[:-4]
        # foods[idx] = food.replace("상함", "") 으로 대체 가능
print(foods) # 원본 수정됨.

fruits = ["사과", "바나나", "체리", "포도", "망고"]
# 홀수 인덱스에 있는 것만 출력해 주세요!
# enumerate -> [(0, "사과"), (1, "바나나"), ...(4, "망고")]
# continue 사용, enumerate() 사용

# idx, fruit = (0, "사과)
for idx, fruit in enumerate(fruits):
    if idx % 2 == 0: # 짝수 인덱스면
        continue # 스킵(다음 반복)

    print(f"{idx}: {fruit}")