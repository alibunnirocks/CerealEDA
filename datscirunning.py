#Exploratory Data Analysis with Cereal

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("C:/Users/alira/.vscode/.vscode/cereal.csv", low_memory=False)

#1. explore data
#print(df.head(10))
#print(df.shape)
#print(df.describe)

#2. Check data for missing values and for duplicates
#print(df.isnull().sum())
#print(df.nunique())

#descriptive statistics
'''
print("The average number of grams of dietary fiber is:",df['fiber'].mean())
low_quantile = df['fiber'].quantile(0.25)
upper_quantile = df['fiber'].quantile(0.75)
print("Interquartile range of grams of dietary fiber:",upper_quantile-low_quantile)
calories_range = df['calories'].max()-df['calories'].min()
print("Range of calories:",calories_range)
'''
#Univariate Analysis (Count of Cereal Fiber)
'''
fiber_counts = df['fiber'].value_counts()

plt.figure(figsize=(8, 6))
plt.bar(fiber_counts.index, fiber_counts, color='deeppink')
plt.title('Count Plot of Dietary Fiber (grams)')
plt.xlabel('Fiber')
plt.ylabel('Count')
plt.show()
'''

#Bivariate Analysis (Correlation between Calories and Ratings with specification of Cereal Manufacturer )
'''
plt.figure(figsize=(12,6))
dataf = pd.DataFrame(df[['rating','calories']])
print(dataf.corr(numeric_only=True))
sns.scatterplot(x='calories', y='rating', data=df, hue='mfr', palette='coolwarm')
plt.xlabel('Calorie Count')
plt.ylabel('Cereal Rating')
plt.title("Relationship between Calories and Cereal Ratings")
plt.show() 
'''
#Multivariate Analysis (Correlation between different measures)
'''
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cbar='inferno')
plt.title('Correlation Between Different Measures')
plt.show()
'''