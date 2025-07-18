import sqlite3

def execute_sql_query(db_path, query):
    #print("inside execute",query)
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        return str(e)
    
