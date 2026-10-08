import csv

sales_count = 0

with open('c:/Users/bryan/data-engineering-journey/data/raw/sales.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    for row in reader:
        sales_count = sales_count + 1

    print("Total sales count:", sales_count)