# Exploratory-Data-Analysis-EDA-Project
Analyze a dataset to uncover patterns and trends.

Title
Exploratory Data Analysis of Customer Shopping Data

Objective
The objective of this project was to explore customer shopping behavior, identify trends, and discover relationships among different variables.

Tools Used
Python
Pandas
Matplotlib
Seaborn

Dataset Features
Customer Age
Gender
Product Category
Purchase Amount
City
Payment Method

Analysis Performed

Statistical Summary
df.describe()

Checking Correlations
df.corr()

Visualizations

Age Distribution
sns.histplot(df['Age'])

Purchase Amount by Gender
sns.boxplot(x='Gender', y='Purchase_Amount', data=df)

Correlation Heatmap
sns.heatmap(df.corr(), annot=True)

Key Findings
Customers aged between 25 and 35 made the highest number of purchases.
Online payments were the most preferred payment method.
Income and purchase amount showed a positive correlation.
Certain product categories generated significantly higher revenue.

Conclusion
EDA helped me understand the underlying patterns in the dataset and identify important relationships among variables. This project strengthened my analytical thinking and improved my ability to derive meaningful insights from data.
