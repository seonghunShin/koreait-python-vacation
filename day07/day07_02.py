import random # 외부에서 random.py 코드를 빌려오는 것.

# random.randint(1, 6) -> 1 ~ 6 사이 난수 생성
my_random_num = random.randint(1, 6)
fruits = ["사과", "바나나", "포도", "배"]
random_fruit = random.choice(fruits) # 리스트 중 무작위 값 하나 선택

# 업다운게임
answer_num = random.randint(1, 100)

while True:
    my_guess = input("1 ~ 100 사이 숫자를 입력: ")

    # 문자열.isdecimal(): 0 ~ 9 문자로 이루어졌는가?
    if not my_guess.isdecimal():
        print("숫자만 입력하세요")
        continue

    my_guess = int(my_guess)
    # my_guess가 answer보다 크면 "다운!" 출력
    # my_guess가 answer보다 작으면 "업!" 출력
    # my_guess가 answer과 같으면 정답:{번호} 탈출! 출력
    if my_guess < 1 or my_guess > 100:
        print("1 ~ 100사이 숫자를 입력하세요")
        continue
    if my_guess > answer_num:
        print(f"입력한 숫자: {my_guess} 난수: {answer_num}\n다운!")
        break
    elif my_guess < answer_num:
        print(f"입력한 숫자: {my_guess} 난수: {answer_num}\n업!")
        break
    else:
        print(f"정답: {my_guess} 탈출!")
        break

# 가위 바위 보
# 3판 2선
# 사용자 점수, 컴퓨터 점수가 있고 먼저 2점을 획득하면 승리
rsp_game = ["가위", "바위", "보"]
my_choice = ""
com_choice = ""
my_score = 0
com_score = 0
while True:
    my_choice = input("가위, 바위, 보 중 하나를 입력해 주세요: ")
    my_choice = my_choice.strip() # 공백 제거

    # 입력값 검증
    if my_choice not in rsp_game:
        print("다시 입력하세요")
        continue

    com_choice = random.choice(rsp_game)

    win1 = my_choice == "가위" and com_choice == "보"
    win2 = my_choice == "바위" and com_choice == "가위"
    win3 = my_choice == "보" and com_choice == "바위"
    wins = [win1, win2, win3]

    if my_choice == com_choice:
        print(f"컴퓨터: {com_choice}\n무승부, 내 점수: {my_score} 컴퓨터 점수: {com_score}\n")
        continue
    elif True in wins:
        my_score += 1
        print(f"컴퓨터: {com_choice}\n승리!, 내 점수: {my_score} 컴퓨터 점수: {com_score}\n")
        if my_score == 2:
            print("최종결과: 승리!")
            break
    else:
        com_score += 1
        print(f"컴퓨터: {com_choice}\n패배.., 내 점수: {my_score} 컴퓨터 점수: {com_score}\n")
        if com_score == 2:
            print("최종결과: 패배..")
            break
print("게임 종료")

