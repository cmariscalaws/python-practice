import csv

def gen_single_product_into_csv(filename, product_data):
    # The list of field names, defining the column order
    fieldnames = ['product_id', 'name', 'price']

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the single product dictionary as a row
        writer.writerow(product_data)

if __name__ == '__main__':
    # The data for a single row
    product = {
        'product_id': 'P101',
        'name': 'Laptop',
        'price': 1200.00
    }
    gen_single_product_into_csv('single_product.csv', product)