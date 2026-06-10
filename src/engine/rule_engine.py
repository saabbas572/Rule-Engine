class RuleEngine:
    def __init__(self, rules):
        self.rules = rules

    def process(self, transaction):
        results = []

        for rule in self.rules:
            if rule.evaluate(transaction):
                results.append({
                    "flagged": True,
                    "reason": rule.reason(transaction)
                })

        if not results:
            return {
                "flagged": False,
                "reason": "No rules triggered"
            }

        return results