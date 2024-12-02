# 도서 관리 시스템
# 1. 도서 기능 한정적으로 개발
# 2. CRUD 개발 학습

# 프로그래밍 언어 + Database
# Create  : 데이터 저장
# Read    : 데이터 조회
# Update  : 데이터 수정
# Delete  : 데이터 삭제

# streamlit run project_lms/main.py

import streamlit as st
import pandas as pd
from service import book_service

##########################
## 1. 프로그램 초기 설정 ##
#########################
st.set_page_config(
    page_title="도서관리 시스템",
    page_icon=""  # favicon
    
)

# 1-1. Stramlit 세션 상태에서 현재 페이지를 추적하기 위한 초기 설정
# session_state: 웹사이트의 현재 상태값을 저장
# -> session_state값에 Page가 없으면
#    기본적으로 main을 저장
#    = Main 페이지 실행
if "page" not in st.session_state:
    st.session_state["page"] = "main"
    
# 1-2. 다른 페이지로 이동하는 함수
def navigate_to(page):
    st.session_state["page"]=page
    st.rerun()
    
# 1-3. 기본 디자인 작업(CSS)
st.markdown("""
    <style>
        .block-container {
            padding-top: 2rem;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 55rem !important;
        }
        
        hr {
            margin: 0;
            padding: 0;
        }

        .stButton>button {
            width: 5rem;
            padding: 0;
            margin: 0;
            text-align: center;
            font-size: 16px;
            cursor: pointer;
        }

        .stColumns {
            gap: 0px; /* 열 간의 기본 간격을 없애기 */
        }

    </style>

""", unsafe_allow_html=True)


###############
## 2. HEADER ##
###############

st.title("도서관리 시스템")
st.markdown("<hr>",unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("HOME"):
        navigate_to("main")
with col2:
    if st.button("등록"):
        navigate_to("insert")
st.markdown("<hr>",unsafe_allow_html=True)

#############
## 3. BODY ##
#############

def main_page():  # 조회, 검색, 삭제
    # DB에서 도서 데이터 가져오기
    rows = book_service.get_books()
    event = st.dataframe(rows,
                         on_select="rerun",
                         selection_mode="single-row",
                         use_container_width=True,
                         hide_index=True)
    
def insert_page():  # 등록
    pass
def update_page():  # 수정
    pass

if st.session_state["page"] == "main":
    main_page()
elif st.session_state["page"] == "insert":
    insert_page()
elif st.session_state["page"] == "update":
    update_page()

    