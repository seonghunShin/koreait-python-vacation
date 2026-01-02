print("hello")
print() # enter키가 자동 포함
print("world")
print("hello", end=" ") # 출력 끝에 enter 대신 " "가 포함

print()

nums = [0, 1, 2, 3, 4]
for num in nums:
    print(num, end=" ")

print()

# range(a, b) -> a이상 b미만 []
# ex) range(1, 5) -> [1, 2, 3, 4]
# range(n) == range(0, n) -> 0이상 n미만
nums = list(range(5)) # 리스트로 쓰려면 형변환
print(nums)

for num in range(10):
    print(num, end=" ")

for _ in range(5): # 요소가 필요없으면 "_"로 표현(관행)
    print("hello world")

# 1 ~ 50까지 홀수끼리, 짝수끼리 나누어 담아보자
odds, evens = [], [] # 튜플 언패킹
for num in range(1, 51):
    if num % 2 == 0:
        num = evens.append(num) # evens 리스트에 num 추가
    elif num % 2 == 1:
        num = odds.append(num)
print(odds)
print(evens)

# 1 ~ 50까지 홀수는 홀수끼리, 짝수는 짝수끼리
# 더하여서 각각 출력하시오
odds = 0 # 누적변수에 초기값 대입
evens = 0 # 누적변수에 초기값 대입
for num in range(1, 51):
    if num % 2 == 0:
        evens += num
    elif num % 2 == 1:
        odds += num

print(f"짝수합: {evens}, 홀수합: {odds}\n")

names = ["김지수", "김길동", "박철호", "박화목", "최영희"]
# 박 성씨인 이름들만 모아주세요
parks = []
count = 0
for name in names:
    # 내부적으로 name = names[0]
    # name = names[1] ...
    # if name[0] == "박":
    #     parks.append(name)
    if name.startswith("박"):
        parks.append(name)
        count += 1
print(parks)
# 박 성씨인 이름이 몇개인지 출력
print(count)

files = ["report.pdf", "ad.exe", "setup.bat", "memo.txt"]
# for 문으로 파일명을 확인하면서
# .exe 파일로 끝나는 파일이 있으면, "위험한 파일입니다!" 출력

for file in files:
    if file.endswith(".exe"):
        print(f"{file}파일은 위험한 파일입니다.\n")

# banned_files에 기록되어있는 확장자로 끝나면 "위험한 파일입니다!" 출력
banned_files = [".exe", ".bat"]
for ban in banned_files:
    for file in files:
        if file.endswith(ban):
            print(f"{file}파일은 위험한 파일입니다.")
print()

for file in files:
    # "."의 index를 찾는다
    dot_idx = file.index(".")
    # .부터 끝까지 슬라이싱
    ext = file[dot_idx:]
    if ext in banned_files:
        print(f"{file}파일은 위험한 파일입니다.")
    # in 연산자로 banned_files에 있는지 확인
    # 있으면 출력

# 2중 for문
# 바깥 반복 한번당 안쪽반복 전체가 도는 구조

# 일주일
for day in range(1, 8):
    print(f"{day}일 살았습니다!", end=" ")

for week in range(1, 5):
    print(f"{week}주 시작") # 4번
    # 일주일 4번
    for day in range(1, 8):
        print(f"{day}일 살았습니다!", end=" ") # 4 * 7번
    print() # enter
    print(f"{week}주 끝") # 4번

# 구구단 (2단 ~ 9단)
"""
2단시작!
2 x 1 = 2
2 x 2 = 4
...
2 x 9 = 18
2단 끝!
3단 시작!
3 x 1 = 3...
3단 끝!
.. 9단 끝!
"""
for i in range(2, 10):
    print(f"{i}단 시작!")
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")
    print(f"{i}단 끝!\n")

