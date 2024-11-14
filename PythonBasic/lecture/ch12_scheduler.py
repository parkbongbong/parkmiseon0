# 스케쥴러(Scheduler)
# - 일정시간에 반복적으로 동작해야하는 작업
#  ex) 12시간에 한번씩
#       5분에 한번씩

# Python은 유명한 스케쥴러 라이브러리 2개
# 1. Scheduler
#   - 매우 쉽고, 매우 기능이 약함
# 2. ApSchduler
#   - 매우 쉽고, 기능이 강함

# ** ApScheduler
# 1. BlockingScheduler -> 내가 메인, 나만 동작!
# 2. BackgroundScheduler -> 난 서브, 뒤에서 동작!

# ** ApScheduler 사용방법
import time
# 1. 스케쥴러 생성
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
sched = BackgroundScheduler()

# 백그라운드 스케쥴러는 반드시 메인 프로그램이 동작 중이어야만 동작함!


# 2. Job 생성 (함수)
def print_hello():
    print("Hello")
    
# 3. 스케쥴러에 Job 등록
# - CRON 표기법 : 날짜 또는 특정시간 표기법(구글 검색)
sched.add_job(print_hello,"cron",hour="12",minute = "35", id = "chosun")

# 4. 스케쥴러 실행
sched.start()
while True:
    time.sleep(1)