# DAO(Data Access Object)
# - 실제 Database와 연결하고 작업하는 내용(CRUD)

from connection import connection

def insert_news(data:dict):
    # 1. DB와 Python의 Connection 생성
    conn = connection()
    
    try:
        # 2. DB관련 일꾼 Cursor 생성
        curs = conn.cursor()
        # 3. 일을 생성(SQL 작성)
        sql = f'''
            INSERT INTO tbl_news(title, writer, content, regdate) 
            VALUES(%(title)s, %(writer)s, %(content)s, %(regdate)s);
        '''
        # 4. 실행(Cursor -> SQL)
        curs.execute(sql,data)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:  # 자원 반납
        # 5. 자원반납(Cursor, Connection)
        if curs:
            curs.close()
        if conn and conn.open:
            conn.close()