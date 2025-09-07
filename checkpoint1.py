import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/nimrashahab/Desktop/states_edu.csv")
print(df.head())

# Going to focus on Grade 4 Reading!
# How many years of data are logged in our dataset?
# @@@ 1

unique_Years = df['YEAR'].unique()
print(unique_Years)
num_years = len(unique_Years)
print("Number of years in the dataset:", num_years)

# Let's compare Michigan to Ohio. Which state has the higher average across all years in the test you chose?
# @@@2

Compare = df[df['STATE'].isin(['MICHIGAN', 'OHIO'])]
avg_score = Compare.groupby('STATE')['AVG_READING_4_SCORE'].mean()

# Find the average for your chosen test across all states in 2019
# @@@3

info_2019 = df[df['YEAR'] == 2019]
avg_2019 = info_2019['AVG_READING_4_SCORE'].mean()

# For each state, find a maximum value for your chosen test score
# @@@4

max_score = df.groupby('STATE')['AVG_READING_4_SCORE'].max()

# @@@5

df['FED_PCT'] = df['FEDERAL_REVENUE'] / df['TOTAL_REVENUE']
#This feature can help us figure out how much revenue the schools got was federal!

#@@@ 6

# Reading 4 Score vs Total Revenue
plt.scatter(df['TOTAL_REVENUE'], df['AVG_READING_4_SCORE'])
plt.xlabel('Total Revenue')
plt.ylabel('Avg Reading 4 Score')
plt.title('Reading 4 Score vs Total Revenue')
plt.show()

#@@@ 7
# Reading 4 Score vs Math 4 Score
plt.scatter(df['AVG_MATH_4_SCORE'], df['AVG_READING_4_SCORE'])
plt.xlabel('Avg Math 4 Score')
plt.ylabel('Avg Reading 4 Score')
plt.title('Reading 4 Score vs Math 4 Score')
plt.show()

import sklearn
from sklearn.model_selection import train_test_split
import sklearn

# @@@8

X = df[['ENROLL', 'TOTAL_REVENUE', 'FEDERAL_REVENUE', 'AVG_MATH_4_SCORE']]
y = df['AVG_READING_4_SCORE']

# @@@9

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# @@@10

from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer


#@@@11

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)


# @@@13
col_name = 'AVG_MATH_4_SCORE'

f = plt.figure(figsize=(12,6))
plt.scatter(X_train[col_name], y_train, color = "red")
plt.scatter(X_train[col_name], model.predict(X_train), color = "green")

plt.legend(['True Training','Predicted Training'])
plt.xlabel(col_name)
plt.ylabel('AVG_READING_4_SCORE')
plt.title("Model Behavior On Training Set")
plt.show()

# @@@ 14

col_name = 'AVG_MATH_4_SCORE'  

f = plt.figure(figsize=(12,6))
plt.scatter(X_test[col_name], y_test, color="blue")
plt.scatter(X_test[col_name], model.predict(X_test), color="black")

plt.legend(['True testing','Predicted testing'])
plt.xlabel(col_name)
plt.ylabel('AVG_READING_4_SCORE') 
plt.title("Model Behavior on Testing Set")
plt.show()
