import pandas as pd
data = pd.read_csv(r"C:\Users\hp\Desktop\python homeworks\рц_17\tackoverflow_qa.csv")
data.head()
df = pd.DataFrame(data)
df
df['creationdate'] = pd.to_datetime(df['creationdate'])
df[df['creationdate'].dt.year > 2014]
df[df['score'] > 50]
df[(df['score'] > 50) & (df['score'] < 100)]
df[df['ans_name'] == 'Scott Boston']
df[df['commentcount'] == 5]
df['creationdate'] = pd.to_datetime(df['creationdate'])
start = '2014-03-01'
end = '2014-10-31'
filtered_df_date = (df['creationdate'] >= start) & (df['creationdate'] <= end)
filtered_unutbu = df['ans_name'] == 'Unutbu'
filtered_score = df['score'] < 5
final_filter = filtered_df_date & filtered_unutbu & filtered_score
df[final_filter]
scoring
scoring = ((df['score'] >=5) & (df['score'] <= 10)) | (df['viewcount'] >10000)
df[scoring]
scot = df['ans_name'] != 'Scott Boston'
df[scot]
homework 3
titanic = pd.read_csv(r"C:\Users\hp\Desktop\python homeworks\рц_17\titanic.csv")
titanic[(titanic['Sex']  == 'female') & (titanic["Age"] >= 20.0) &(titanic['Age'] <= 30.0)]

customers_hundred = titanic[titanic["Fare"] > 100]
customers_hundred
titanic[(titanic['Survived'] == 1) & (titanic['SibSp'] == 0)]

fifty = titanic[(titanic['Fare'] > 50) & (titanic['Embarked'] >= 'C')]
fifty
titanic[(titanic['SibSp'] == 'Sibling') | (titanic['SibSp'] == 'Spouse') & (titanic['SibSp'] == 'Parent') | (titanic['SibSp'] == 'child')]
titanic[(titanic['Age'] == 15) | ((titanic['Age'] < 15) & (titanic['Survived'] == 0))]
titanic[(titanic['Fare'] > 200.0) & (titanic['Cabin'] != 0)]
odd_id = titanic[titanic['PassengerId'] % 2 != 0]
odd_id
unique_tickets = titanic.drop_duplicates(subset='Ticket')
unique_tickets
miss_name = titanic[(titanic['Name'].str.contains('Miss')) & (titanic['Pclass'] == 1)]
miss_name
