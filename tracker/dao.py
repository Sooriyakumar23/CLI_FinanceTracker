import os
import json

def write_transaction(transaction):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "../data/records.json")
    with open(file_path, 'r') as file:
        data = json.load(file)
    dict_transaction = transaction.to_dict()
    data.append(dict_transaction)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
    return

def read_transactions():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "../data/records.json")
    with open(file_path, 'r') as file:
        transactions = json.load(file)
        return transactions