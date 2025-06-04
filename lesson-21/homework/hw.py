import pandas as pd
import matplotlib.pyplot as plt
data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)
df1
avg_grade = df1.groupby('Student_ID')[['Math', 'English', 'Science']].mean()

avg_grade['Average'] = avg_grade.mean(axis=1)
top_student_id = avg_grade['Average'].idxmax()
top_student_info = avg_grade.loc[top_student_id]
df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
df1.set_index('Student_ID')[['Math', 'English', 'Science']].plot(kind='bar')
plt.ylabel('Scores')
plt.title('Scores by Subject and Student')
plt.show()


data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)
df2[['Product_A', 'Product_B', 'Product_C']].max()
row_idx = df2[['Product_A', 'Product_B', 'Product_C']].values.max() 
mask = df2[['Product_A', 'Product_B', 'Product_C']] == row_idx
row_index = mask.any(axis=1).idxmax()
max_date = df2.loc[row_index, 'Date']
print(max_date)
df2
df2['Date'] = pd.to_datetime(df2['Date'])
df2['product_a_change'] = df2['Product_A'].pct_change() * 100
df2['product_b_change'] = df2['Product_B'].pct_change() * 100
df2['product_c_change'] = df2['Product_C'].pct_change() * 100

df2[['product_a_change', 'product_b_change', 'product_c_change']] = df2[['product_a_change', 'product_b_change', 'product_c_change']].fillna(0).round(2)
df2[['product_a_change', 'product_b_change', 'product_c_change']]
plt.figure(figsize=(10, 6)) 

plt.plot(df2['Date'], df2['Product_A'], label='Product A', marker='o')
plt.plot(df2['Date'], df2['Product_B'], label='Product B', marker='s')
plt.plot(df2['Date'], df2['Product_C'], label='Product C', marker='^')


plt.title('Sales Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

df3
avg_sal = df3.groupby('Department')['Salary'].mean().round(2)
avg_sal
max_exp = df3['Experience (Years)'].max()
max_exp = df3[df3['Experience (Years)'] == max_exp]
max_exp
min_salary = df3['Salary'].min()
df3['Salary_Increase'] = ((df3['Salary'] - min_salary) / min_salary) * 100
df3['Salary_Increase'] = df3['Salary_Increase'].round(2)
df3
dept_counts = df3['Department'].value_counts()

plt.figure(figsize=(8,5))
dept_counts.plot(kind='bar', color='steelblue')

plt.title('distribution by departments')
plt.xlabel('Departments')
plt.ylabel('number of emplpyees')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)
df4['Total_Price'].sum()
df4
most_ordered = df4.groupby('Product')['Quantity'].sum()
most_ordered.idxmax()
avg_ord = df4.groupby('Product')['Quantity'].mean()
avg_ord
sales_per_product = df4.groupby('Product')['Total_Price'].sum()


plt.figure(figsize=(7,7))
sales_per_product.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99','#ffcc99'])

plt.title('Distribution sales by products')
plt.ylabel('') 
plt.show()
