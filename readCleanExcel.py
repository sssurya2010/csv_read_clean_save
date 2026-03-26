import pandas as pd

Orders_path='/Users/aparya/Downloads/Docs/Orders.csv'
Customers_path='/Users/aparya/Downloads/Docs/Customers.csv'



orders_df=pd.read_csv(Orders_path)
customers_df=pd.read_csv(Customers_path)

# print(df.count())
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# print(df.columns)
# print(df.shape)

pending_orders=orders_df[orders_df['OrderStatus']=='Pending']
# print(pending_orders)

shipped_orders=orders_df[orders_df['OrderStatus']=='Shipped']

pending_shipped_orders = pd.merge(pending_orders,shipped_orders,how='inner', on='CustomerID')
pending_shipped_orders2=pending_orders.join(shipped_orders,on='CustomerID',how='inner',lsuffix="_left",rsuffix='_right')

distinct_order_types=orders_df['OrderStatus'].unique()

# print(pending_shipped_orders.sort_values(by=["CustomerID"]))
# print(pending_shipped_orders['OrderStatus_x'].unique())

# pending_shipped_orders.to_csv("output.csv")
# pending_shipped_orders2.to_csv("output2.csv")

total_pending_orders_amount=pending_orders.groupby("PaymentMethod")["TotalAmount"].sum()
total_count=pending_orders.groupby("PaymentMethod").agg({"TotalAmount":"sum",
                                                         "CustomerID":"nunique"})

# print(customers_df.columns)

customer_and_orders=orders_df.merge(customers_df,how='inner',on="CustomerID")
ordersin2023=customer_and_orders[customer_and_orders["OrderDate"].str.contains('2024')]
print(ordersin2023)