import os
import pymysql
from decouple import config  # If using env vars

# Connect to MySQL (without specifying a database)
connection = pymysql.connect(
  host=config('DB_HOST', default='localhost'),
  user=config('DB_USER', default='root'),
  password=config('DB_PASSWORD'),
)
cursor = connection.cursor()

# Create database if it doesn't exist
db_name = config('DB_NAME', default='dapurku_db')
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
print(f"Database '{db_name}' is ready.")

cursor.close()
connection.close()