import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

# HTTP 통신 - 요청/응답
response = requests.get(url)

# 파이썬 객체화
soup = BeautifulSoup(response.text, "html.parser")

# select() / select_one()
# "CSS 선택자방식" -> 브라우저가 태그위치를 인식하는 방식

# div 태그이면서 클래스 속성값이 quote인걸 다 가져와
soup.find_all("div", class_="quote")
# select에
# 어쩌고 -> 어쩌고 태그
# .어쩌고 -> 어쩌고 클래스
# #어쩌고 -> 어쩌고 id속성값
soup.select(".quote")

# 하나의 태그는 여러개의 클래스속성을 가질 수 있음
# 띄어쓰기로 구분

# select()는 한번에 반복되는 태그를 지정할 수 있다.
# ".a .b"
# -> a클래스 태그 안쪽에 b클래스 태그가 있다.
# ".quote .author"
# -> quote 클래스 태그 안쪽에 .author 클래스 태그
author_tags = soup.select(".quote .author")
for author_tag in author_tags:
    author = author_tag.text
    print(author)

print("")
# 브라우저의 copy selector 기능을 쓰는방법
# 반복되는 태그에 copy selector를 하면 아래와 같이 표현되어있음.
# 마지막부분의 nth-child를 지운다.
# nth-child가 없다면 그대로 사용

# body > div > div:nth-child(2) > div.col-md-4.tags-box > span:nth-child(2)
# body > div > div:nth-child(2) > div.col-md-4.tags-box > span
top_ten_tags = soup.select("body > div > div:nth-child(2) > div.col-md-4.tags-box > span")
for top_ten_tag in top_ten_tags:
    tag_name = top_ten_tag.text
    tag_name = tag_name.strip() # 문자열 좌우 공백 제거
    print(tag_name)

# 명언들만 soup에서 바로 select를 사용해서
# 추출하여 주세요! - copy selector 기능 사용해봅시다.
# body > div > div:nth-child(2) > div.col-md-8 > div

# copy selector 결과에서 마지막에 등장하는 :nth-child(숫자) 지워주세요.
quote_tags = soup.select("body > div > div:nth-child(2) > div.col-md-8 > div > span.text")
for quote_tag in quote_tags:
    quote = quote_tag.text
    print(quote[:30])