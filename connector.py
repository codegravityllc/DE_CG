import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="127.0.0.1",        # e.g., "localhost"
    user="root",    # e.g., "root"
    password="CLFA568d0d!2",
    database="CG" # e.g., "test_db"
)

# Check connection
if conn.is_connected():
    print("Connected to MySQL database")

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT DATABASE();")
record = cursor.fetchone()
print("You're connected to database:", record)

# Close the connection
cursor.close()
conn.close()