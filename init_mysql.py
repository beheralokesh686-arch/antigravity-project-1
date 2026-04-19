
import mysql.connector
from config import active_config

def init_db():
    try:
        # Connect to MySQL without database first to create it
        conn = mysql.connector.connect(
            host=active_config.MYSQL_HOST,
            user=active_config.MYSQL_USER,
            password=active_config.MYSQL_PASSWORD
        )
        cursor = conn.cursor()
        
        # Create database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {active_config.MYSQL_DATABASE}")
        cursor.execute(f"USE {active_config.MYSQL_DATABASE}")
        
        # Create tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            roll_no VARCHAR(30) NOT NULL UNIQUE,
            class VARCHAR(50) NOT NULL,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS marks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT NOT NULL,
            subject VARCHAR(100) NOT NULL,
            marks INT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
            UNIQUE KEY unique_student_subject (student_id, subject)
        )
        """)
        
        # Add default admin
        from werkzeug.security import generate_password_hash
        cursor.execute("SELECT * FROM admin WHERE username = 'admin'")
        if not cursor.fetchone():
            hashed_pw = generate_password_hash('admin123')
            cursor.execute("INSERT INTO admin (username, password) VALUES (%s, %s)", ('admin', hashed_pw))
            conn.commit()
            print("Admin created: admin / admin123")
            
        print("Database initialized successfully.")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    init_db()
