
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from collect_dao import insert_news
import requests


options = Options()
options.add_experimental_option("detach",True)  
options.add_argument("disable-blink-features=AutomationControlled")
options.add_experimental_option("useAutomationExtension",False)
options.add_experimental_option("excludeSwitches",["enable-automation"])



def collect_news():
    
    driver = webdriver.Chrome(options=options)
    url = "https://news.daum.net/home" 
    driver.get(url)
    time.sleep(1)

    count = 0
    result = driver.page_source  # 현재 페이지 소스코드 GET
    
    for i in range(2):
        doc = BeautifulSoup(result,"html.parser")
        
        # link_list -> 현재 페이지의 수집할 기사 링크(9개)
        # - 현재 페이지 수집 완료! -> link 목록을 저장!
        
        # if 현재 link가 link목록에 있는지 물어보기
        # -> 있으면: 중복, 수집 멈춤
        # -> 없으면: 수집!

        link_list = doc.select("article.content-article ul.list_newsheadline2 a.item_newsheadline2")
        print(link_list)
            
        for link in (link_list):
            print(f"{count} ==================================================================")
            get_news_info(link["href"])
            count += 1
            # 다음 뉴스 버튼 클릭 이벤트
        driver.find_element(By.XPATH,'//*[@id="58d84141-b8dd-413c-9500-447b39ec29b9"]/div[2]/a').click()
        time.sleep(1)
        result = driver.page_source
            
   
        

def get_news_info(url: str): 
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    contents = doc.select("section > p")
    content = ""
    for text in contents:
        content += (text.get_text())
        
    writer_list = doc.select("span.txt_info")
    if len(writer_list) < 2:
        writer = ""
    else:
        writer = writer_list[0].get_text()
        
    # writer = doc.select("span.txt_info")[0].get_text()
    reg_date = doc.select("span.num_date")[0].get_text()
    split_list =  reg_date.split(".")
    split_date = list(map(lambda x: x.strip(), split_list))
    reg_date = split_list[0].strip() + split_list[1].strip() + split_list[2].strip()

    print(reg_date.split("."))
    print(f"뉴스 제목 : {title}")
    print(f"뉴스 본문: {content}")
    print(f"기자 : {writer}")
    print(f"날짜 : {reg_date}")
    
    # DB에 저장
    
    data = {
        "title":title,
        "writer":writer,
        "content":content,
        "regdate":reg_date
    }
    
    # insert_news(data)
    
collect_news()