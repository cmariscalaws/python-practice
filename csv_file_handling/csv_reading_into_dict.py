from csv import DictReader

def read_csv_into_dict(file_path):
    data = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = DictReader(csvfile)
        for row in csvreader:
            data[row['id']] = row
    return data

if __name__ == "__main__":
    file_path = 'example.csv'  # Replace with your CSV file path
    data = read_csv_into_dict(file_path)
    for key, row in data.items():
        print(f"key:{key}, {row}")

    print(f"Person in Paris is {data['3']['name']}", f"and he's {  data['3']['age']} old.")  # Accessing specific entry by id
#