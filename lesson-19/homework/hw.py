import pandas as pd

sales = pd.read_csv(r'C:\Users\hp\Desktop\python homeworks\hw_19\sales_data.csv')

sales.head()
total = sales.groupby('Category').agg(
  quantity_count = ('Quantity', 'count'), 
  avg_price = ("Price", "mean"),
  max_quant = ("Quantity", "max"),
  )
total
grouped = sales.groupby(['Category', 'Product'])['Quantity'].sum().reset_index()
top = grouped.sort_values(['Category', 'Quantity'], ascending=[True, False]).drop_duplicates(subset='Category', keep='first')
top
sales['Revenue'] = sales['Quantity'] * sales['Price']

grouped_second = sales.groupby('Date')['Revenue'].max()

grouped_second.idxmax()
customers = pd.read_csv(r'C:\Users\hp\Desktop\python homeworks\hw_19\customer_orders.csv')
customers
order_counts = customers.groupby('CustomerID').size().reset_index(name='OrderCount')
filtered_customers = order_counts[order_counts['OrderCount'] >= 20]
result = customers[customers['CustomerID'].isin(filtered_customers['CustomerID'])]
avg_price = customers.groupby('CustomerID')['Price'].mean()
gr_120 = avg_price[avg_price > 120]
gr_120
product_sum = customers.groupby('Product').agg(
  total_quan = ('Quantity', 'sum'),
  total_price = ('Price', 'sum')
).reset_index()

product_sum[product_sum['total_quan'] >= 5]
populations = pd.read_excel(r'C:\Users\hp\Desktop\python homeworks\hw_19\population_salary_analysis.xlsx')

populations
import sqlite3
conn = sqlite3.connect(r'C:\Users\hp\Desktop\python homeworks\hw_19\population.db')


count = populations['Salary Band'].value_counts().sort_index()
count
count = populations['Salary Band'].value_counts().sort_index()
average_salary = populations.groupby('Salary Band')['Salary'].mean()
median_salary = populations.groupby('Salary Band')['Salary'].median()
total = len(populations)
percentage = (count / total) * 100

