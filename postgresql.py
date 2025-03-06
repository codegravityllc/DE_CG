import psycopg2

# Connect to PostgresSQL
conn = psycopg2.connect(
    host="localhost",
    port = 5432,
    database="Cgdb",
    user="postgres",
    password="Password")



# Create a cursor
cur = conn.cursor()

# Execute a query
cur.execute("SELECT version();")

# Fetch and print results
print(cur.fetchone())

# Close the connection
cur.close()
conn.close()
