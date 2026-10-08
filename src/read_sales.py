import csv

sales_count = 0
total_revenue = 0
product_revenue = {} 

with open('c:/Users/bryan/data-engineering-journey/data/raw/sales.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        sales_count = sales_count + 1

        product = row['product']
        quantity = int(row['quantity'])
        price = int(row['price'])

        revenue = quantity * price
        total_revenue = total_revenue + revenue

        if product in product_revenue:
            product_revenue[product] = product_revenue[product] + revenue
        else:
            product_revenue[product] = revenue

    print("Total sales count:", sales_count)
    print("Total revenue: ¥", total_revenue)
    print("\nRevenue by product:")
    for product, revenue in product_revenue.items():
        print(product, ": ¥", revenue)

    # Find the product with the highest revenue 
    best_product = max(product_revenue, key=product_revenue.get)
    print("\nBest-performing product:", best_product)
    print("Revenue of best-performing product: ¥", product_revenue[best_product])