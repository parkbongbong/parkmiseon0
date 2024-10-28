# 웹 크롤링 (Web Crawling)
# -> 웹 사이트에서 데이터를 수집하는 기술


# AI, 데이터분석 -> 데이터!

# 1. 클라이언트로부터 데이터 받기
# 2. 공공 데이터(검색) 찾기
# 3. kaggle, Dacon -> AI 및 데이터분석 경쟁 대회 웹 사이트
#   - 기업이 경쟁을 위해 올려둔 데이터 검색
# ★ 직접 웹 사이트로부터 데이터 수집 -> 웹 크롤링

# 웹 크롤링 -> 웹 크롤러

# 도베인 널리지 (도메인 지식) -> 웹 사이트
# 웹 브라우저 
#     -> request(https://www.naver.com)
#         -> 네이버 서버
#             -> response(naver.com에 필요한 소스)
#                  -> 웹 브라우저(랜더링) 

# *request 소스들
#  1. HTML
#  2. CSS
#  3. Javascript
#  4. 이미지 및 기타 등등
#  ※ [HTML, CSS, JS] -> 웹 표준
#  ※ 대부분의 웹 브라우저들은 웹 표의 95% 정도 지원 (크롬 100% 지원)
#  ※ 크롬, IE, 사파리, 파이어폭스, 오페라, 네이버 웨일
#  HTML: 구조 설계
#  CSS: 디자인
#  JS: 기능

# *라이브러리
# 1. requests : 해당 웹 사이트의 전체 코드 Get(정적)
# 2. Beautifulsoup : 특정 부분을 Select

# 3. selenium : 해당 웹 사이트의 전체 코드 Get(동적)
#               -> 마우스, 키보드 조작!

  