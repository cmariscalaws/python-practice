from csv import DictWriter


def write_dict_of_dicts_to_csv(data_dict, csv_filename):

    # The fieldnames list must include the 'id' column plus all the keys from the inner dictionaries.
    # By taking the keys from the first inner dictionary, you assume all inner dictionaries have the same keys.
    fieldnames = ['id'] + list(next(iter(data_dict.values())).keys())

    # A list of dictionaries that the DictWriter can consume.
    rows_for_csv = []
    for record_id, details in data_dict.items():
        # Create a new dictionary for each row.
        row = {'id': record_id}
        # Add all key-value pairs from the inner dictionary.
        row.update(details)
        rows_for_csv.append(row)

    # The name of the CSV file to write to.
    csv_filename = 'employees_with_ids.csv'

    # Write the data to the CSV file.
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row.
        writer.writeheader()

        # Write all the constructed row dictionaries at once.
        writer.writerows(rows_for_csv)

    print(f"Data has been written to {csv_filename}")

if __name__ == '__main__':
    data_dict = {
        'emp_001': {'name': 'Alice', 'department': 'Sales', 'hire_date': '2020-03-15'},
        'emp_002': {'name': 'Bob', 'department': 'Marketing', 'hire_date': '2021-06-20'},
        'emp_003': {'name': 'Charlie', 'department': 'Sales', 'hire_date': '2019-01-10'}
    }
    write_dict_of_dicts_to_csv(data_dict, 'employees_with_ids.csv')
