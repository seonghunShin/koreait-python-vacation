coords = [
    (3, -3),
    (2, 3),
    (1, -2),
    (5, 6)
]
my_coords = []
# 좌표들 중 1사분면에 해당하는 좌표만 모아주세요.
# coord = (3, -3) -> (2, 3).... (5, 6)
for coord in coords:
    x, y = coord # x, y = (3, -3)
    if x > 0 and y > 0:
        my_coords.append(coord)
print(my_coords)

scores = {
    "김철수": 90,
    "김영희": 80,
    "김민수": 100,
    "박철수": 50,
    "박영희": 45
}
# value들만 모아서 리스트로 가져다줄 수 있음.
score_nums = scores.values()
# 평균 점수 구하기
score_sum = 0
for score in score_nums:
    score_sum += score # 누적합

score_avg = score_sum / len(score_nums)
print(score_avg)

# 60점 이상 학생들의 평균점수
# len() x
score_sum = 0
count_over_60 = 0
# dict에서 value를 점수만 추출
score_nums = scores.values()
for score in score_nums:
    if score >= 60:
        score_sum += score
        count_over_60 += 1

score_avg_over_60 = score_sum / count_over_60
print(score_avg_over_60)

score_over_60s = []
score_sum = 0
for score in score_nums:
    if score >= 60:
        score_over_60s.append(score)
        score_sum += score

length_over_60 = len(score_over_60s)
score_avg_over_60 = score_sum / length_over_60

# scores에서 60점 이상인 학생들의 이름을 출력해주세요
# dict -> {이름: 점수}
# [("김철수", 90), ("김영희", 80), .....]
score_items = scores.items()

for item in score_items:
    name, score = item # 튜플 언패킹
    if score >= 60:
        print(f"{name}님 합격입니다!")


tele_book = {
    "김철수": "01011111111",
    "박철수": "01022222222",
    "최철수": "01033333333",
    "이철수": "01044444444",
}

target_number = input("찾으시는 전화번호를 - 빼고 입력: ")
# target_number가 dict에 value로 존재한다면, 이름을 출력
# 없다면, "발신자 알 수 없음" 출력
tele_items = tele_book.items()
is_exist_number = False # flag 찾으면, True로 업데이트
for item in tele_items:
    name, tele_num = item # 튜플 언패킹
    if tele_num == target_number:
        print(f"{name}님의 전화 입니다.")
        is_exist_number = True
        break

# 반복을 다 돌았지만, 여전히 False -> 없는 전화번호
if not is_exist_number:
    print("발신자 알 수 없음.")
