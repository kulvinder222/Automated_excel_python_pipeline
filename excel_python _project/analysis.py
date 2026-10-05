import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("Data_analytics_traning.xlsx")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df["Month"] = pd.to_datetime(df["Order_Date"], errors="coerce").dt.month_name()

# city wise business sale
city_sales = df.groupby("City")["Sales"].sum()
print(city_sales)    

# best sale person
salesperson_sales = df.groupby("Salesperson")["Sales"].sum()
print(salesperson_sales)


# highiest sale month
month_sales = df.groupby("Month")["Sales"].sum()
print(month_sales)


# kaunsa product sale hora hai lekin profit kam de rha hai
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
product_profit = df.groupby("Product")["Profit"].sum()
print(product_profit)



print("Excel data successfully loaded")
print("Total rows:", len(df))



print("\n--- ANALYSIS RESULTS ---")

print("1. Product-wise Sales:")
print(df.groupby("Product")["Sales"].sum())

print("\n2. City-wise Sales:")
print(df.groupby("City")["Sales"].sum())

print("\n3. Salesperson-wise Sales:")
print(df.groupby("Salesperson")["Sales"].sum())

print("\n4. Month-wise Sales:")

print(df.groupby("Month")["Sales"].sum())

print("\n6. Product-wise Profit:")
print(df.groupby("Product")["Profit"].sum())


product_sales = df.groupby("Product")["Sales"].sum()
plt.bar(product_sales.index, product_sales.values)
plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.savefig("Product_Sales.png")
plt.show()


city_sales = df.groupby("City")["Sales"].sum()
plt.bar(city_sales.index, city_sales.values)
plt.title("City-wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.savefig("City_Sales.png")
plt.show()


salesperson_sales = df.groupby("Salesperson")["Sales"].sum()
plt.bar(salesperson_sales.index, salesperson_sales.values)
plt.title("Salesperson-wise Sales")
plt.xlabel("Salesperson")
plt.ylabel("Sales")
plt.savefig("Salesperson_Sales.png")
plt.show()


month_sales = df.groupby("Month")["Sales"].sum()
plt.bar(month_sales.index, month_sales.values)
plt.title("Month-wise Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("Month_Sales.png")
plt.show()

df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
product_profit = df.groupby("Product")["Profit"].sum()
plt.bar(product_profit.index, product_profit.values)
plt.title("Product-wise Profit")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.savefig("Product_Profit.png")
plt.show()