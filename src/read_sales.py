import csv

sales_count = 0
total_revenue = 0

with open('c:/Users/bryan/data-engineering-journey/data/raw/sales.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        sales_count = sales_count + 1
        

        quantity = int(row['quantity'])
        price = int(row['price'])

        revenue = quantity * price
        total_revenue = total_revenue + revenue

    print("Total sales count:", sales_count)
    print("Total revenue: ¥", total_revenue)