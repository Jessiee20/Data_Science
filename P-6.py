prices = [0.5, 0.3, 1.2, 2.5]  # Example prices: apple, banana, milk, bread
quantities = [4, 6, 2, 1]       # Corresponding quantities
discount_rate = 10              # 10% discount
tax_rate = 5 
subtotal = sum(p * q for p, q in zip(prices, quantities))
discounted_subtotal = subtotal * (1 - discount_rate / 100)
total_cost = discounted_subtotal * (1 + tax_rate / 100)
print(f"The total cost of the purchase is: ${total_cost:.2f}")
