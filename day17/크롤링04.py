import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 도전) 아래 url 게시판의 제목들만 추출해서 출력!
url = "https://de.mofa.go.kr/de-ko/brd/m_7204/list.do"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

all_data = []

# #contents > div.board_list > table > tbody > tr:nth-child(1)

social_tags = soup.select("#contents > div.board_list > table > tbody > tr")
for social_tag in social_tags:
    # select는 언제나 리스트를 리턴
    # [태그1, 태그2...]
    # 담는 "순서"가 위에서 부터 아래로 담음
    title_tag = social_tag.select(".al div a")[0]
    title = title_tag.text
    social_data = social_tag.select("td div")
    author = social_data[2].text
    date = social_data[3].text
    # print(f"제목: {title[:10]}..., 저자: {author}, 날짜: {date}")


# 게시글 제목 말고
# 실제 게시글 내용 여러개를 크롤링
# -> url 패턴파악 먼저
# 2975116&page=1 첫번째
# 2975115&page=1 두번째
# 2975107&page=1 마지막
# 2975103&page=2 2페이지 첫번째
BASE_ID = 2975116
BASE_URL = "https://de.mofa.go.kr/de-ko/brd/m_7204/view.do?seq="
target_urls = []
for num in range(0, 10):
    print(f"{BASE_URL}{BASE_ID - num}&page=1")
    target_urls.append(f"{BASE_URL}{BASE_ID - num}&page=1")

for url in target_urls:
    response = requests.get(url)

    # 통신성공여부
    # 200이면 통신은 성공한것
    print(response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
