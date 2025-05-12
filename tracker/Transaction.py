class Transaction:
    def __init__(self, amount, type, category):
        self.amount = float(amount)
        self.type = type.lower()
        self.category = category.lower()
    def __str__(self):
        return (f"Transaction Added Successfully: Amount={self.amount}, Type={self.type}, Category={self.category}")
    def to_dict(self):
        return {
            "amount": self.amount,
            "type": self.type,
            "category": self.category
        }