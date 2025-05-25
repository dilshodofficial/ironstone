import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} 
df = pd.DataFrame(data)

df.rename(columns={"First Name" : "first name", "Age": "age"}, inplace=True)

top3 = df.head(3)
top3

mean = df["age"].mean()
mean

name_city = df[['first name', 'City']]
print(name_city)

df['Salary'] = [2000, 3000, 4000, 1200]

print(df.describe())

second_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

df = pd.DataFrame(second_data)

df

print(df['Sales'].max())
print(df['Expenses'].max())
print(df['Sales'].min())
print(df['Expenses'].min())
print(df['Sales'].mean())
print(df['Expenses'].mean())

third_data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

df = pd.DataFrame(third_data)
df

df.set_index('Category', inplace=True)

print(df.iloc[0:4, 1:5].max())
print('-'*16)
print(df.iloc[0:4, 1:5].min())
print('-'*18)
print(df.iloc[0:4, 1:5].mean())
