def generate_report(transactions):
    report = {}
    for transaction in transactions:
        try:
            report[transaction["category"]] += transaction["amount"]
        except:
            report[transaction["category"]] = transaction["amount"]
    return report