import requests
from bs4 import BeautifulSoup


def get_news_info(url: str): 

    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    contents = doc.select("section > p")
    content = ""
    for text in contents:
        content += text.get_text()
    writer = doc.select("span.txt_info")[0].get_text()
    reg_date = doc.select("span.num_date")[0].get_text()
    split_list = list(map(lamda x: x.strip(), split_list))
    reg_date = split_list[0].strip() + split_list[1].strip() + split_list[2].strip()
    print(f"날짜 : {reg_date}")

    print(f"뉴스 제목 : {title}")
    print(f"뉴스 본문: {content}")
    print(f"기자 : {writer}")
    print(f"날짜 : {reg_date}")