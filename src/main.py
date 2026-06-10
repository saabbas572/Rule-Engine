from model.transactions import Transaction
from engine.rules import LargeTransactionRule
from engine.rule_engine import RuleEngine

transaction = Transaction(
    transaction_id=1,
    amount=9000,
    country="Canada",
    customer_id="C101"
)

rules = [
    LargeTransactionRule(threshold=10000)
]

engine = RuleEngine(rules)

result = engine.process(transaction)

print(result)