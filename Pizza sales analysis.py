import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv(r"C:\Users\Tirumalaivasan\Documents\Projects\pizza_sales.csv")

# Convert order_date to datetime
df['order_date'] = pd.to_datetime(df['order_date'], dayfirst=True, errors='coerce')

# Total Revenue
print("Total Revenue:", df['total_price'].sum())

# Top Selling Products
print("\nTop Selling Products:")
print(df.groupby('pizza_name')['quantity'].sum().sort_values(ascending=False).head())

# Monthly Sales Trend
df['Month'] = df['order_date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['total_price'].sum()

print("\nMonthly Sales Trend:")
print(monthly_sales.head())

# Plot Monthly Sales Trend
monthly_sales.plot(kind='line', marker='o', title="Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# Sales by Category (corrected)
category_sales = df.groupby('pizza_category')['total_price'].sum()
category_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales by Category')
plt.ylabel('')
plt.tight_layout()
plt.show()
