from datetime import datetime, timedelta

# 날짜 포맷팅
# now_date = datetime.now() 출력 : 2024-10-10 12:05:22.313027
now_date = datetime.now().strftime("%Y.%m.%d.%H:%M") #2024.10.10.12:08
print(now_date)  # 현재날짜 및 시간 출력

# 날짜 계산
# ex) 현재 시간에서 13시간 빼기
now = datetime.now() # 현재 시간
before_time = (now-timedelta(hours=13)).strftime("%Y%m%d %H:%M")
print(before_time)
