import requests
from bs4 import BeautifulSoup


# 1. URL 설정
#  -> 수집하고 싶은 웹 사이트 주소
url = "https://v.daum.net/v/20241028144248100"

# 2. URL 전체 소스코드 가져오기
result = requests.get(url)
# ※ response code
#    200: 성공
#    400, 500대: 오류
# print(result)
# print(result.text)

# 3. BS에게 전체 소스코드 전달 및 파싱
# -> BS가 수집할 수 있도록 소스코드를 변환
doc = BeautifulSoup(result.text, "html.parser")

# ※ HTML 태그로 구성 됨
# <div>안녕하세요</div>
# <a>Hi</a>

# 4. 수집
#   -> 선택자
#   1. 태그 선택자 (사용 금지)
#   2. 아이디 선택자 (#) -> 1개(유니크)
#   3. 클래스 선택자 (.) -> 복수 선택 가능
#   4. 자식 선택자 (>) -> 해당 태그의 하위 자식들 선택
#   5. 자손 선택자 ( ) -> 해당 태그의 자손들(자식+하위)
# select() -> LIST 타입
title = doc.select("h3.tit_view")[0].get_text()
print(f"뉴스 제목 : {title}")

# 본문: 여러개의 p태그로 구성
contents = doc.select("section > p")
content = ""
for text in contents:
    content += text.get_text()
print(f"뉴스 본문: {content}")

# contents -> [<p>본1</p>, <p>본2</p>, <p>본3</p>]
# text -> <p>본1</p>
# text.get_text -> 본1
# content += text -> "본1 + 본2 + 본3"