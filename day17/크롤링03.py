import requests
from bs4 import BeautifulSoup
import time

# 여러페이지 -> 여러개의 url에 요청/응답 반복
# https://quotes.toscrape.com/page/2/ -> 2페이지
# https://quotes.toscrape.com/page/3/ -> 3페이지

root_url = "https://quotes.toscrape.com"

# num에 5를 넘기면 1 ~ 5페이지를 모두 크롤링
def crawl_multi_page(num):
    # 모든 데이터를 저장할 리스트
    all_data = []

    # num에 5를 넘기면 [1, 2, 3, 4, 5]
    for page in range(1, num + 1):
        target_url = f"{root_url}/page/{page}/"
        print(f"현재 크롤링 페이지: {page}페이지")

        # 요청 / 응답
        response = requests.get(target_url)
        # 파이썬 객체화
        soup = BeautifulSoup(response.text, "html.parser")

        quote_tags = soup.find_all("div", class_="quote")
        for quote_tag in quote_tags:
            text_tag = quote_tag.find("span", class_="text")
            text = text_tag.text
            author_tag = quote_tag.find("small", class_="author")
            author = author_tag.text
            print(f"{author}: {text[:60]}")
            data = {
                "author": author,
                "quote": text,
            }
            all_data.append(data)
        # 1초 정지 -> 너무 빠르면 서버 부하 -> 밴먹음
        time.sleep(1)

    return all_data


if __name__ == "__main__":
    crawl_multi_page(10)