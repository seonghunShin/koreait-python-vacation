from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

url = "https://www.health.kr"

# 파이썬이 내 pc를 사용해서 브라우저를 열고 행동

# 크롬 설치파일 가져오기
driver_manager = ChromeDriverManager().install()
# 셀레니움에 설치
chrome_service = Service(driver_manager)
# 인터넷창(브라우저) 생성
driver = webdriver.Chrome(service=chrome_service)

def scroll_to(tag):
    script = "arguments[0].scrollIntoView();"
    driver.execute_script(script, tag)

search_q = "아세트아미노펜"
drug_name_list = [
    "아세트아미노펜",
    "아로낙",
    "트라세트 세미정",
    "씨오엑스",
    "크리마인",
    "에페손"
]

for drug_name in drug_name_list:
    driver.get(url) # 접속
    sleep(2) # 대기

    # 태그기준으로 행동을 지정해줘야한다.
    # find_element - 하나찾기 -> 태그
    # find_elements - 여러개 찾기 -> [태그, 태그..]

    # 검색창 - 입력하는 태그(input)
    # 클릭 가능한 태그(button)

    search_input_tag = driver.find_element(By.ID, "search_word")
    # 태그.send_keys("검색어") -> 태그에 "검색어" 입력
    search_input_tag.send_keys(drug_name)
    sleep(0.5) # 입력 후 대기
    search_btn_tag = driver.find_element(By.CLASS_NAME, "search")
    print(search_btn_tag.text) # "검색" 버튼이 맞는지 확인
    search_btn_tag.click() # 새 페이지로 이동
    sleep(3)

    # 검색결과가 없을 경우 -> 예외처리 해야함
    try:
        drug_link_tag = driver.find_element(By.CSS_SELECTOR, "#tbl_proY > tbody > tr:nth-child(2) > td:nth-child(2)")
        drug_link_tag.click()
        sleep(3)
    except Exception as e:
        print("    -> 검색결과 없음")
    else:
        # efficacy_effect - 효능 효과
        effect_tag = driver.find_element(By.ID, "efficacy_effect")
        scroll_to(effect_tag)
        print(f"효능, 효과: {effect_tag.text.strip()[10:]}")
        # usage - 용법 용량
        usage_tag = driver.find_element(By.ID, "usage")
        scroll_to(usage_tag)
        print(f"용법, 용량: {usage_tag.text.strip()[10:]}\n")