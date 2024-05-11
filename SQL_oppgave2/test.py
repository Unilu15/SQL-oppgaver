import sqlite3

# Connect to the database
conn = sqlite3.connect('Random.db')

# Create a cursor object
cur = conn.cursor()

# Define your query with a WHERE clause
query = 'SELECT * FROM zero WHERE number2= ?'

# Define the value for the placeholder (?)
value = ('1',)

# Execute the query with the provided value
cur.execute(query, value)

# Fetch data
data = cur.fetchall()

# Do something with the data
for row in data:
    print(row)

# Close the cursor and the connection
cur.close()
conn.close()
