class LargeTransactionRule:
    def __init__(self, threshold=10000):
        self.threshold = threshold

    def evaluate(self, transaction):
        return transaction.amount > self.threshold
    
    def reason(self):
        return f"Transaction exceeds {self.threshold}"
    