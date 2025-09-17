import csv

def read_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Skip the header row
        for row in csvreader:
            data.append(row)
    return headers, data

if __name__ == "__main__":
    file_path = 'example.csv'  # Replace with your CSV file path
    headers, data = read_csv(file_path)
    print("Headers:", headers)
    for row in data:
        print(row)