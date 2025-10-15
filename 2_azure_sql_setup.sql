-- azure_sql_setup.sql
CREATE TABLE Customers (
  customer_id INT PRIMARY KEY,
  name NVARCHAR(100),
  age INT,
  gender NVARCHAR(10),
  location NVARCHAR(100)
);

CREATE TABLE Products (
  product_id INT PRIMARY KEY,
  product_name NVARCHAR(100),
  category NVARCHAR(100),
  price DECIMAL(10,2)
);

CREATE TABLE Transactions (
  transaction_id INT PRIMARY KEY,
  customer_id INT FOREIGN KEY REFERENCES Customers(customer_id),
  product_id INT FOREIGN KEY REFERENCES Products(product_id),
  purchase_date DATETIME,
  quantity INT,
  price DECIMAL(10,2),
  total_amount AS (quantity * price) PERSISTED
);
