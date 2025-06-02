import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading data

df=pd.read_csv(r"C:\Users\Tirumalaivasan\Documents\Projects\supermarket_sales - Sheet1.csv")

#plot setting

sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] =(10,6)

print("dataset is loaded successfully!")

print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

df['Date'] = pd.to_datetime(df['Date'])

df['Month'] = df['Date'].dt.month_name()

sns.countplot(data=df,x='Gender',hue='Gender',palette='pastel')
plt.title("Customer Gender Distribution")
plt.show()


sns.countplot(data=df,x='Branch',hue='Branch',palette='Set2')
plt.title('Sales by Branch')
plt.show()

#Rating Distribution
sns.histplot(df['Rating'],bins=10,kde=True,color='skyblue')
plt.title('Distribution of Customer Rating')
plt.show()

#Bivariate Analysis(compare 2 variables)
avg_income=df.groupby('Product line')['gross income'].mean()
avg_income.sort_values(ascending=False)
sns.barplot(x=avg_income.values,y=avg_income.index)
plt.title("Average Gross Income by Product Line")
plt.xlabel("Average Gross Income")
plt.ylabel("Product Line")
plt.show()

#Sales by payment Method
payment_sales=df.groupby('Payment')['Total'].sum()
sns.barplot(x=payment_sales.index,y=payment_sales.values)
plt.title("Sales by Payment")
plt.xlabel("Payment method")
plt.ylabel("Total Sales")
plt.show()

#Sales by Gender
sns.boxplot(data=df,x='Gender',y='Total',hue='Gender',palette='Set1')
plt.title("Sales by gender")
plt.xlabel("Gender")
plt.ylabel("Total Sales")
plt.show()

#time series Analysis
daily_sales=df.groupby('Date')['Total'].sum()
daily_sales.plot(kind='line',marker='o')
plt.title("Time series analysis")
plt.show()

#Correlation Heatmap
corr=df[['Unit price','Quantity','Total','Rating','gross income']].corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()