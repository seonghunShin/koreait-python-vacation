# 실습) 주어진 coordㅈ ㅘ표가 몇사분면에 있는지 판별하여 출력!
# 원점, x축, y축 위츼 경우 고려 x

coord = (3, -3)
x, y = coord # 튜플 언패킹

if x > 0 and y > 0:
    print("1사분면")
elif x < 0 and y > 0:
    print("2사분면")
elif x < 0 and y < 0:
    print("3사분면")
else:
    print("4사분면")

# 컬렉션 자료형들 (list, tuple, set)
# 서로 형변환이 가능
example = ("데이터1", "데이터2")
list_example = list(example)
print(list_example) # 리스트
tuple_example = tuple(list_example)
print(tuple_example) # 튜플
