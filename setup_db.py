import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Jantyking@1',
        port=3306
    )
    cursor = conn.cursor()
    cursor.execute("DROP DATABASE IF EXISTS edutrackx")
    conn.commit()
    print("Dropped database")
    
    with open('database.sql', 'r') as f:
        sql = f.read()
    
    statements = sql.split(';')
    for stmt in statements:
        if stmt.strip():
            cursor.execute(stmt)
    conn.commit()
    print("Database recreated successfully.")
except Exception as e:
    print(f"Error: {e}")
