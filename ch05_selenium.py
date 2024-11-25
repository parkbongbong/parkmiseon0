# SELENIUM 
# - 설치 : pip install selenium
#         pip install webdriver_manager
# - 웹 크롤링(정적, 동적 모두 가능) -> 자동화
# - 자신만의 웹브라우저를 통해서 동작

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 1. Selenium에 제어하는 Chrome 웹 브라우저 설정
options = Options()
# - SELENIUM 동작 후 웹브라우저 종료(Default) -> 끄기
options.add_experimental_option("detach",True)  # 배포시 제거할것!

# 2. Selenium이 제어하는 Chrome 웹 브라우저 설치
# - 오류1: 사용하고 있는 Chrome 웹브라우저의 버전을 최신 업데이트
# - 오류2: 웹브라우저 불러오기 경로 문제!(경로 관련 문제 해결)
# ※ 최신버전에서는 ChromeDriver 설치하지 않아도 됨
#     "service=service" 삭제 가능
service = Service(ChromeDriverManager().install())

# 3. Selenium이 제어하는 Chrome 웹브라우저 생성 
driver = webdriver.Chrome(options=options)

# 4. 웹브라우저 명령
driver.get("https://www.naver.com")
time.sleep(1)

search = driver.find_element(By.ID,'query')
search.send_keys("정우성")
search.send_keys(Keys.ENTER)
time.sleep(1)

# 5. 전체 소스코드
print(driver.page_source)