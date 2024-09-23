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
product_sales = last_month_sales.groupby('product_name').agg(
    total_quantity_sold=('quantity_sold', 'sum'),
    avg_order_quantity=('quantity_sold', 'mean')
).reset_index()
top_5_products = product_sales.sort_values(by='total_quantity_sold', ascending=False).head(5)
print(f"Start Date: {start_date}")
print(f"End Date: {end_date}")
print("\nTop 5 Products:")
print(top_5_products)
