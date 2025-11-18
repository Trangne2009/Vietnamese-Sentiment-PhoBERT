import sqlite3 
import datetime 
import pandas as pd

DB_NAME = "sentiment_history.db"

def init_db(): 
    conn = None 
    try:
        conn = sqlite3.connect(DB_NAME) 
        cursor = conn.cursor() 
        
    # Tạo bảng sentiments   
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sentiments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL, 
                sentiment TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )           
                    """)
        conn.commit() 
    except sqlite3.Error as e: 
        print(f"Lỗi SQLite khi khởi tạo DB: {e}")
    finally:
        if conn: 
            conn.close() 
            
def save_history(text: str, sentiment: str): 
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = None
    
    try: 
        conn = sqlite3.connect(DB_NAME) 
        cursor = conn.cursor() 
        
        query = "INSERT INTO sentiments (text, sentiment, timestamp) VALUES (?, ?, ?)"
        cursor.execute(query, (text, sentiment, now)) 
        
        conn.commit() 
    except sqlite3.Error as e: 
        print(f"Lỗi SQLite khi lưu lịch sử: {e}")
    finally:
        if conn:
            conn.close() 
            
def load_history(limit: int = 50) -> pd.DataFrame:
    conn = None 
    try: 
        conn = sqlite3.connect(DB_NAME) 
        query = f"SELECT timestamp, text, sentiment FROM sentiments ORDER BY timestamp DESC LIMIT {limit}"
        df = pd.read_sql_query(query, conn) 
        return df
    except sqlite3.Error as e:
        print(f"Lỗi SQLite khi tải lịch sử: {e}")
        return pd.DataFrame() 
    finally:
        if conn:
            conn.close() 
            
init_db() 
    
