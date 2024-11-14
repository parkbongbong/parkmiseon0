# 다음 뉴스 수집기

# 웹사이트 
#     - 화면 : 뉴스 카테고리를 선택(streamlit)
#     - 수집 : 뉴스 수집(requests, beautifulsoup)
#     - 화면 : 출력, 엑셀(다운로드)(streamlit, pandas)
#     - 저장 : 데이터베이스 저장(pymysql + MariaDB)


from fnc_news import collect_news

category = "digital"
def main():
    print(">> 뉴스를 수집합니다")
    collect_news(category)
    
if __name__ == "__main__":
    main()
