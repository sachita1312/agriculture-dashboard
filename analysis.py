#Upload csv file
import pandas as pd
df=pd.read_csv("plant_disease.csv")

print(df.head())

#Data cleaning 
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print("Shape:", df.shape)

#Add extra columns
import numpy as np
df['severity'] = np.random.randint(1, 5, size=len(df))# Add severity (fake but needed)
df['date'] = pd.date_range(start="2023-01-01", periods=len(df), freq='D') # Add date for time-series

#Visualizations

import matplotlib.pyplot as plt #disease distribution

df['disease'].value_counts().plot(kind='bar')
plt.title("Disease Distribution")
plt.show()

df['disease'].value_counts().plot(kind='pie', autopct='%1.1f%%') #pie chart
plt.title("Disease Percentage")
plt.show()

import seaborn as sns #crop vs disease count

sns.countplot(data=df, x='crop', hue='disease')
plt.title("Disease by Crop")
plt.show()

corr = df[['severity']].corr() # Heatmap

sns.heatmap(corr, annot=True)
plt.title("Heatmap")
plt.show()

df.groupby('date')['severity'].mean().plot() #Time trend
plt.title("Disease Trend Over Time")
plt.show()

#Final csv file
df.to_csv("final_dataset.csv", index=False)