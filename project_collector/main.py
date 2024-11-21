# 다음 뉴스 수집기

# 웹사이트 
#     - 화면 : 뉴스 카테고리를 선택(streamlit)
#     - 수집 : 뉴스 수집(requests, beautifulsoup)
#     - 화면 : 출력, 엑셀(다운로드)(streamlit, pandas)
#     - 저장 : 데이터베이스 저장(pymysql + MariaDB)

import streamlit as st
from fnc_news import collect_news
import re  # 정규식

# README.md -> md(Markdown) 문서
#   ㄴ emoji(아이콘) -> https://snskeyboard.com/emoji/
# Streamlit Doc -> https://docs.streamlit.io/

# streamlit run project_collector/main.py

category = "digital"
def main():
    st.set_page_config(
        page_title="뉴스 수집기",                         # 웹사이트 제목
        page_icon="project_collector/img/favicon.png"    # 웹사이트 파비콘
    )
    st.title("NEWS: :blue[Collector]")
    st.text("DAUM 뉴스를 수집합니다.")
    
    with st.form(key="form"):
        # 1. 정규식 -> 문자만 추출(숫자, 특수문자 제거!)
        # 2. 수집 데이터를 엑셀로 다운로드
        # 3. README.md 작성! -> 프로젝트 정리(Github)
        
        
        # 사용자가 수집버튼을 클릭하면 -> 클릭 이벤트
        submitted = st.form_submit_button("수집")
        if submitted:
            collect_news()
           
    
if __name__ == "__main__":
    main()
