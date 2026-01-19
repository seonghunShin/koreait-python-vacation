# 모듈: .py파일, 함수 or 클래스 정의만 있음
# 패키지: 모듈들을 묶어놓은 폴더
# __init__.py는
# 해당 폴더를 파이썬이 패키지로 인식

# random.py파일의 코드를 복붙한 것
import random # 라이브러리는 from 생략 ok
from a import a
from b import b

# a.py안에 있는 add함수 as 별명
from a.a import add as 더하기함수
from b.b import Person

더하기함수(1, 2)

p1 = Person("길동이", 20)
p1.print_person()