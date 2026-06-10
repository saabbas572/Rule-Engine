class Transaction:
    def __init__(self, transaction_id, amount, country, customer_id=None):
        self.transaction_id = transaction_id
        self.amount = amount
        self.country = country
        self.customer_id = customer_id

    def __str__(self):
        return f"Transaction({self.transaction_id}, {self.amount}, {self.country})"