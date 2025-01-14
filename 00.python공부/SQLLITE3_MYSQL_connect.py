# pip install mysql-connector-python
# pip install mysql-connector-python-rf


import sqlite3
import mysql.connector
from mysql.connector import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def create_mysql_connection(host_name, user_name, user_password, db_name):
    """ create a database connection to a MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(
            host     = host_name,
            user     = user_name,
            password = user_password,
            database = db_name
        )
        if conn.is_connected():
            print(f"Connected to MySQL database: {db_name}")
    except Error as e:
        print(e)
    return conn

if __name__ == '__main__':
    # SQLite 데이터베이스 연결 (파일 기반)
    conn = create_connection(r"example.db")
    
    # 커서 객체 생성
    cur = conn.cursor()

    # 테이블 생성
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    ''')
    
    # 데이터 삽입
    cur.execute('''
        INSERT INTO users (name, age) VALUES (?, ?)
        ''', ('Alice', 30)
    )

    # 여러 데이터 삽입
    users = [
        ('Bob', 25),
        ('Charlie', 35)
    ]
    
    cur.executemany('''
        INSERT INTO users (name, age) VALUES (?, ?)
        ''', users
    )

    # 데이터 조회
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
    # 데이터 업데이트
    cur.execute('''
        UPDATE users SET age = ? WHERE name = ?
        ''', (31, 'Alice')
    )

    # 데이터 삭제
    cur.execute('''
        DELETE FROM users WHERE name = ?
        ''', ('Bob',)
    )


    # 변경 사항 저장
    conn.commit()

    # 연결 종료
    conn.close()
    
    
    # MySQL 데이터베이스 연결
    mysql_conn = create_mysql_connection("localhost", "root", "password", "test_db")
    
    if mysql_conn:
        # 커서 객체 생성
        cur = mysql_conn.cursor()

        # 테이블 생성
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT
            )
        ''')
        
        # 데이터 삽입
        cur.execute('''
            INSERT INTO users (name, age) VALUES (%s, %s)
            ''', ('Alice', 30)
        )

        # 여러 데이터 삽입
        users = [
            ('Bob', 25),
            ('Charlie', 35)
        ]
        
        cur.executemany('''
            INSERT INTO users (name, age) VALUES (%s, %s)
            ''', users
        )

        # 데이터 조회
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()
        for row in rows:
            print(row)
            
        # 데이터 업데이트
        cur.execute('''
            UPDATE users SET age = %s WHERE name = %s
            ''', (31, 'Alice')
        )

        # 데이터 삭제
        cur.execute('''
            DELETE FROM users WHERE name = %s
            ''', ('Bob',)
        )

        # 변경 사항 저장
        mysql_conn.commit()

        # 연결 종료
        mysql_conn.close()
        