# 현재시간을 다루는 모듈

from datetime import datetime, timedelta

# 현재시간
now = datetime.now()
print(f"지금: {now}") # now는 datetime 객체

# datetime객체 -> 내가 원하는 문자열포맷
# %Y: 년, %m: 월, %d: 일, %H: 시, %M: 분
my_time = now.strftime("%Y년도 %m월 %d일 %H시 %M분")
print(my_time)

# 날짜 덧셈/뺄셈
# 현재시간 + 1일
tomorrow = now + timedelta(days=1)
# 현재시간 - 1일
yesterday = now - timedelta(days=1)