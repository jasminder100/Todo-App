import os
from dotenv import load_dotenv
import pymysql

# Load environment variables
load_dotenv()

# Get database configuration
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = int(os.getenv('DB_PORT', '3306'))
DB_NAME = os.getenv('DB_NAME', 'todo_db')

print("=" * 50)
print("🔗 Testing MySQL Connection")
print("=" * 50)
print(f"\n📋 Configuration:")
print(f"   Host: {DB_HOST}")
print(f"   Port: {DB_PORT}")
print(f"   User: {DB_USER}")
print(f"   Database: {DB_NAME}")
print(f"   Password: {'***' if DB_PASSWORD else '(none)'}\n")

try:
    # Try to connect
    connection = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
        database=DB_NAME
    )
    
    print("✅ Connection successful!\n")
    
    # Create cursor
    cursor = connection.cursor()
    
    # Show existing tables
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    
    print("📊 Existing tables:")
    if tables:
        for table in tables:
            print(f"   - {table[0]}")
    else:
        print("   (none yet)")
    
    cursor.close()
    connection.close()
    
except Exception as e:
    print(f"❌ Connection failed!")
    print(f"\n⚠️  Error: {e}\n")
    print("Common fixes:")
    print("1. Make sure MySQL is running: mysql.server start")
    print("2. Check username in .env (usually 'root')")
    print("3. Check password in .env (may be empty)")
    print("4. Check database name in .env (should be 'todo_db')")
    print("5. Verify MySQL is listening on port 3306")
