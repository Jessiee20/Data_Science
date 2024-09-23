import pandas as pd
data = {
    'product_name': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product D', 'Product C', 'Product E'],
    'order_date': ['2023-08-01', '2023-08-03', '2023-08-05', '2023-08-10', '2023-08-12', '2023-08-15', '2023-08-18', '2023-08-20'],
    'quantity_sold': [10, 5, 12, 8, 7, 6, 15, 3]
}
sales_data = pd.DataFrame(data)
sales_data['order_date'] = pd.to_datetime(sales_data['order_date'])
start_date = '2023-08-01'
end_date = '2023-08-31'
last_month_sales = sales_data[(sales_data['order_date'] >= start_date) & (sales_data['order_date'] <= end_date)]
total_sales_per_product = last_month_sales.groupby('product_name')['quantity_sold'].sum().reset_index()
top_5_products = total_sales_per_product.sort_values(by='quantity_sold', ascending=False).head(5)
print(top_5_products)
