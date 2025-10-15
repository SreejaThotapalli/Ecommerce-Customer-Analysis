# data_extraction.py
import pandas as pd
import pyodbc

# Update with your actual Azure SQL details
SERVER = 'your_server.database.windows.net'
DATABASE = 'your_database'
USERNAME = 'your_username'
PASSWORD = 'your_password'

# Connection string
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    f"Server={SERVER};Database={DATABASE};UID={USERNAME};PWD={PASSWORD};"
)

# Query transaction data
query = "SELECT * FROM Transactions"
transactions_df = pd.read_sql(query, conn)
conn.close()

# Data cleaning
transactions_df['purchase_date'] = pd.to_datetime(transactions_df['purchase_date'])
transactions_df['total_purchase_value'] = transactions_df['quantity'] * transactions_df['price']

# Feature engineering
transactions_df['year'] = transactions_df['purchase_date'].dt.year
transactions_df['month'] = transactions_df['purchase_date'].dt.month

# Save cleaned data
transactions_df.to_csv('cleaned_transactions.csv', index=False)
print("✅ Data cleaned and saved as cleaned_transactions.csv")
