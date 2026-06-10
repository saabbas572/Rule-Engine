class LargeTransactionRule:
    def __init__(self, threshold=10000, country=['IRAN', 'NORTH KOREA']):
        self.threshold = threshold
        self.country = country

    def evaluate(self, transaction):
        if transaction.country in self.country:
            return transaction.amount > self.threshold
        elif transaction.amount > self.threshold:
            return True
        return False
    
    def reason(self, transaction):
        if transaction.country in self.country and transaction.amount > self.threshold:
            return f"Transaction exceeds {self.threshold} in sanctioned countries"
        else:
            return f"Transaction exceeds {self.threshold}"