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


customers_with_orders=customers_df.merge(orders_df,how="inner",on="CustomerID",suffixes=["_cust","_ordr"])

customers_with_orders=customers_with_orders[customers_with_orders["TotalAmount"]>0]

aggregate_orders=customers_with_orders.groupby(["Name","Email"])["TotalAmount"].sum()

aggregate_orders.sort_values(by="TotalAmount",ascending=False)

print(aggregate_orders)