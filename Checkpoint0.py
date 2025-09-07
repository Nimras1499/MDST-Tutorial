# Question 1: Here is a python list, initialize another list called b with the same values as a. a = [1, 2, 3, 4, 5, 6]

b = [1, 2, 3, 4, 5 ,6 ]

# Question 2: get a list containing the last 3 elements of b 

b[-3:]

# Question 3: Create a list of numbers from 1 to 20

Questionthree = list(range(1,21)) # Stop one number after

# Question 4: now get a list with only the even numbers between 1 and 100

even_numbers = [x for x in range(1,101) if x % 2 == 0] # Condition of remainder makes it work!

# Question 5: write a function that takes two numbers as arguments
# and returns the first number divided by the second

def division(x, y):    # similar to C++, just not doing return 0
    return x / y

# Question 6: fizzbuzz
# you will need to use both iteration and control flow 
# go through all numbers from 1 to 30 in order
# if the number is a multiple of 3, print fizz
# if the number is a multiple of 5, print buzz
# if the number is a multiple of 3 and 5, print fizzbuzz and NOTHING ELSE
# if the number is neither a multiple of 3 nor a multiple of 5, print the number


for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)



# @@@ Question 7: create a dictionary that reflects the following menu pricing (taken from Ahmo's)
# Gyro: $9 
# Burger: $9
# Greek Salad: $8
# Philly Steak: $10

ahmoprices = {"Gyro": 9.00, "Burger": 9.00, "Greek Salad": 8.00, "Philly Steak": 10.00}

print(ahmoprices)

# @@@ Question 8: load in the "starbucks.csv" dataset
# refer to how we read the cereal.csv dataset in the tutorial

import pandas as pd
df = pd.read_csv("starbucks.csv")
print(df.head())

# @@@ Question 9: select all rows with more than and including 400 calories
    high_calorie = df[df['calories'] >= 400]

# @@@ Question 10: select all rows whose vitamin c content is higher than the iron content

delicious = df[df['vitamin c'] > df['iron']]

# @@@ Question 11: create a new column containing the caffeine per calories of each drink

df['caffeine_per_calorie'] = df['caffeine'] / df['calories']

# @@@ Question 12: what is the average calorie across all items?
average_Calories = df['calories'].mean()

# @@@ Question 13: how many different categories of beverages are there?
num_categories = df['beverage_category'].nunique()
# @@@ Question 14: what is the average # calories for each beverage category?
avg_category_cals = df.groupby('beverage_category')['calories'].mean()