from model.transactions import Transaction
from engine.rules import LargeTransactionRule
from engine.rule_engine import RuleEngine

transaction = Transaction(
    transaction_id=1,
    amount=15000,
    country="IRAN",
    customer_id="C101"
)

rules = [
    LargeTransactionRule(threshold=10000, country=['IRAN', 'NORTH KOREA'])
]

engine = RuleEngine(rules)

result = engine.process(transaction)

print(result)