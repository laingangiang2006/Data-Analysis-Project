import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()

# I. Read CSV
# 1. CUSTOMER ANALYSIS
df1 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/1. CUSTOMER ANALYSIS/1. Top 5 customers by total orders.csv")
df2 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/1. CUSTOMER ANALYSIS/2. Top 5 customers by total spent.csv")
df3 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/1. CUSTOMER ANALYSIS/3. Customer orders summary.csv")

# 2. REVENUE ANALYSIS
df4 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/2. REVENUE ANALYSIS/4. Total order by month.csv")
df5 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/2. REVENUE ANALYSIS/5. Orders count by status.csv")
df6 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/2. REVENUE ANALYSIS/6. Most used payment methods.csv")
df7 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/2. REVENUE ANALYSIS/7. Most used sales channels.csv")

# 3. PRODUCT ANALYSIS
df8 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/3. PRODUCT ANALYSIS/8. Product stats by category.csv")
df9 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/3. PRODUCT ANALYSIS/9. Cheapest product per category.csv")
df10 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/3. PRODUCT ANALYSIS/10. Products count by skin concern.csv")
df11 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/3. PRODUCT ANALYSIS/12. Affordable acne and exfoliation products.csv")

# 4. REVIEW ANALYSIS
df12 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/4. REVIEW ANALYSIS/13. Customer review details.csv")
df13 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/4. REVIEW ANALYSIS/14. Top 5 products by average rating.csv")
df14 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/4. REVIEW ANALYSIS/15. Average rating by category.csv")

# 5. RETURN ANALYSIS
df15 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/5. RETURN ANALYSIS/16. 5 most returned products.csv")
df16 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/5. RETURN ANALYSIS/17. Return rate by product.csv")
df17 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/5. RETURN ANALYSIS/18. Most common return reasons.csv")
df18 = pd.read_csv("/Users/laingangiang/Downloads/CSV File/5. RETURN ANALYSIS/19. Most common refund statuses.csv")

for name, df in [("Top 5 customers by total orders", df1), 
           ("Top 5 customers by total spent", df2), 
           ("Customer orders summary", df3),
           ("Total order by month", df4), 
           ("Orders count by status", df5), 
           ("Most used payment methods", df6),
           ("Most used sales channels", df7),
           ("Product stats by category", df8),
           ("Cheapest product per category", df9),
           ("Products count by skin concern", df10),
           ("Affordable acne and exfoliation products", df11),
           ("Customer review details", df12),
           ("Top 5 products by average rating", df13),
           ("5 most returned products", df15),
           ("Average rating by category", df14),
           ("Return rate by product", df16),
           ("Most common return reasons", df17),
           ("Most common refund statuses", df18)]:
    print(name)
    print(df.describe())
    print(df.head(5))
    print(df.info())
    print(df.value_counts())

# II. Visualization
# 1. Customer orders summary
## Top 5 Customers by Total Orders
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
df1.plot(x="customer_id", y="total_orders", kind="bar", ax=axes[0], color="skyblue")
axes[0].set_title("Top 5 Customers by Total Orders")
axes[0].set_xlabel("Customer ID")
axes[0].set_ylabel("Total Orders")
axes[0].tick_params(axis="x", rotation=45)

## Top 5 Customers by Total Spent
df2.plot(x="customer_id", y="total_spent", kind="bar", ax=axes[1], color="lightcoral")
axes[1].set_title("Top 5 Customers by Total Spent")
axes[1].set_xlabel("Customer ID")
axes[1].set_ylabel("Total Spent")
axes[1].tick_params(axis="x", rotation=45)
plt.tight_layout()
plt.show()

# 2. Top 5 customers by total spent
plt.figure(figsize=(7,7))
plt.pie(df2["total_spent"], labels=df2["customer_id"], autopct="%1.1f%%", startangle=140)
plt.title("Top 5 Customers by Total Spent")
plt.tight_layout()
plt.show()

# 3. Total order by month
df4["date"] = pd.to_datetime(df4["month_year"], format="%m-%Y")
df4["month"] = df4["date"].dt.month
df4["year"] = df4["date"].dt.year

month_labels = {1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun", 7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec"}
df4["month_name"] = df4["month"].map(month_labels)
df4["month_name"] = pd.Categorical(df4["month_name"], categories=list(month_labels.values()), ordered=True)

plt.figure(figsize=(12, 5))
sns.barplot(data=df4, x="month_name", y="order_count", hue="year")
plt.title("Total Orders by Month")
plt.xlabel("Month")
plt.ylabel("Total Number  of Order")
plt.tight_layout()
plt.show()

# 4. Orders count by status
sns.barplot(data = df5, x = "order_status", y = "order_count")
plt.title("Orders Count by Status")
plt.xlabel("Order Status")
plt.ylabel("Total Number  of Order")
plt.show()

# 5. Most used payment methods
sns.barplot(data = df6, x = "payment_method", y = "total_orders")
plt.title("Most Used Payment Methods")
plt.xlabel("Payment Method")
plt.ylabel("Total Number  of Order")
plt.show()

# 6. Most used sales channels
sns.barplot(data = df7, x = "sales_channel", y = "order_count")
plt.title("Most Used Sales Channels")
plt.xlabel("Sales Channel")
plt.ylabel("Total Number of Order")
plt.show()

# 7. Product stats by category
fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()

sns.barplot(data=df8, x="category", y="total_products", ax=ax1, color="steelblue", label="Total Products")
sns.lineplot(data=df8, x="category", y="avg_cost_price", ax=ax2, color="tomato", marker="o", label="Avg Cost Price")
ax1.set_xlabel("Category")
ax1.set_ylabel("Total Products", color="steelblue")
ax2.set_ylabel("Average Cost Price", color="tomato")
plt.title("Product Stats by Category")
plt.xticks(rotation=45)
fig.tight_layout()
plt.show()

# 8. Cheapest product per category
sns.barplot(data = df9, x = "category", y = "cost_price")
plt.title("Cheapest Product per Category")
plt.xlabel("Category")
plt.ylabel("Cost Price")
plt.tight_layout()
plt.show()

# 9. Top 5 products by skin concern
df10_filtered = df10[df10["product_count"] > 1]
sns.barplot(data = df10_filtered, x = "concern", y = "product_count")
plt.title("Top 5 Categories by Skin Concern")
plt.xlabel("Concern")
plt.ylabel("Product Count")
plt.tight_layout()
plt.show()

# 10. Affordable acne and exfoliation products
sns.barplot(data = df11, x = "product_id", y = "cost_price")
plt.title("Affordable acne and exfoliation products")
plt.xlabel("Product ID")
plt.ylabel("Total Number")
plt.show()

# 11. Affordable acne and exfoliation products
plt.figure(figsize=(10, 6))
sns.barplot(data=df11, x="product_id", y="cost_price", hue="product_id", palette="Set2")
plt.title("Affordable Acne and Exfoliation Products - Price Comparison")
plt.xlabel("Product ID")
plt.ylabel("Cost Price")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 12. Customer review details
review_counts = df12["rating"].value_counts().sort_index()
sns.barplot(x=review_counts.index, y=review_counts.values)
plt.title("Customer Review Details")
plt.xlabel("Rating")
plt.ylabel("Review Count")
plt.tight_layout()
plt.show()

# 13. Top 5 products by average rating
categories = df13["product_id"]
values = df13["avg_rating"]

plt.barh(categories, values)
plt.title("Top 5 products by average rating")
plt.xlabel("Average Rating")
plt.ylabel("Product ID")
plt.show()

# 14. Average rating by category
categories = df14["category"]
values = df14["avg_rating"]

plt.barh(categories, values)
plt.title("Average rating by category")
plt.xlabel("Average Rating")
plt.ylabel("Category")
plt.show()

# 15. 5 most returned products
sns.barplot(data = df15, x = "product_id", y = "total_orders")
plt.title("5 Most Returned Products")
plt.xlabel("Product ID")
plt.ylabel("Total Number")
plt.show()

# 16. Return rate by product
sns.barplot(data = df16, x = "product_id", y = "product_count")
plt.title("Return Rate by Product")
plt.xlabel("Product ID")
plt.ylabel("Total Number")
plt.show()

# 17. Most common return reasons
category = df17["return_reason"]
value = df17["order_count"]
plt.barh(category, value)
plt.title("Most Common Return Reasons")
plt.xlabel("Total Number of Order")
plt.ylabel("Return Reason")
plt.show()

# 18. Most common refund statuses
category = df18["refund_status"]
value = df18["order_count"]
plt.barh(category, value)
plt.title("Most Common Refund Statuses")
plt.xlabel("Total Number of Order")
plt.ylabel("Refund Status")
plt.show()
