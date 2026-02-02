import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("sales_data.csv")

# Clean data
df.dropna(inplace=True)

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Sales by product
product_sales = df.groupby("Product")["Sales"].sum()

# Sales by region
region_sales = df.groupby("Region")["Sales"].sum()

print("Sales by Product:")
print(product_sales)

print("\nSales by Region:")
print(region_sales)

# Plot sales by product
product_sales.plot(kind="bar", title="Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Plot sales by region
region_sales.plot(kind="bar", title="Sales by Region", color="green")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
