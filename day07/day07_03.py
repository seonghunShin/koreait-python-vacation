import random

# 미니 로또
# 6개 중복없는 랜덤 숫자
# 6: 1등, 5:2등, 4:3등, 꽝

# 1. 당첨번호 뽑기
winning_nums = []
while True:
    random_num = random.randint(1, 45)
    # 이미 뽑힌 번호라면
    if random_num in winning_nums:
        continue # 중복 때문에 for 대신 while 사용

    winning_nums.append(random_num)
    # 6개 뽑으면 탈출
    if len(winning_nums) == 6:
        break

print(f"이번 회차 당첨번호: {winning_nums}\n")

# 2. 번호 6개 찍기
my_nums = []
while True:
    input_my_num = input("로또 번호를 입력하여주세요: ")
    if not input_my_num.isdecimal():
        print("숫자를 입력하세요")
        continue
    input_my_num = int(input_my_num)
    if not 1 <= input_my_num <= 45:
        print("1 ~ 45 사이의 숫자를 입력하세요")
        continue
    # 중복 아니면 추가
    if input_my_num not in my_nums:
        my_nums.append(input_my_num)
    # 6개 찍으면 탈출
    if len(my_nums) == 6:
        print(f"내 번호: {my_nums}")
        break

# 3. 두 개 비교하기
# 맞춘 횟수 변수를 만들어서 두 리스트 비교해서
# 같은 값이 있으면 + 1
winning_count = 0
# my_nums = set(my_nums)
# winning_nums = set(winning_nums)
# for my_nums in winning_nums:
#     if my_nums & winning_nums:
#         winning_count += len(my_nums & winning_nums)
#     if winning_count == 6:
#         print("1등")
#         break
#     elif winning_count == 5:
#         print("2등")
#         break
#     elif winning_count == 4:
#         print("3등")
#         break
#     else:
#         print("꽝")
#         break
for my_num in my_nums:
    if my_num in winning_nums:
        winning_count += 1

if winning_count == 6:
    print("1등")
elif winning_count == 5:
    print("2등")
elif winning_count == 4:
    print("3등")
else:
    print("꽝")