#
# Problem Statement: Read customers.csv and orders.csv, clean the data by removing invalid or missing values, 
# and keep only valid customer-order records. Then aggregate orders per customer to calculate total orders, total amount, 
# and average amount. Finally, save top 20 customers as top_customer_order_summary.csv.
#

import pandas as pd

Orders_path='/Users/aparya/Downloads/Docs/Orders.csv'
Customers_path='/Users/aparya/Downloads/Docs/Customers.csv'

orders_df=pd.read_csv(Orders_path)
customers_df=pd.read_csv(Customers_path)

# Join Orders & Customers with CustomerID and get only customers with Orders (inner join with orders)
customer_orders=customers_df.merge(orders_df,how="inner",on="CustomerID",suffixes=["_cust","_ordr"]).copy()

# Check for TotalAmount more than 0 to eliminate invalid rows
customer_agg=customer_orders[customer_orders["TotalAmount"]>0].copy()

# Calculate Total Amount for each customer (Name & email)
customer_final=(customer_orders.groupby(["Name","Email"])["TotalAmount"].sum().to_frame())

# Get top 20 rows by sorting them by Total Amount
top_20_customers=customer_final.sort_values(by="TotalAmount",ascending=False).head(20)

# Save it to CSV
top_20_customers.to_csv("FinalOutput.csv")

