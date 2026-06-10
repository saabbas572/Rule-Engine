# Transaction Rule Engine

A lightweight Python rule engine for transaction validation and fraud detection.

## Overview

This project implements a basic rule engine that evaluates transactions against one or more rules. Each rule returns a boolean result and a reason when triggered.

## Current Behavior

- `src/model/transactions.py`
  - Defines the `Transaction` model.
- `src/engine/rules.py`
  - Defines `LargeTransactionRule`, which flags transactions above a configurable threshold.
- `src/engine/rule_engine.py`
  - Defines `RuleEngine`, which processes a transaction through all configured rules and returns triggered results.
- `src/main.py`
  - Creates a sample transaction, configures rules, runs the engine, and prints the result.

## Usage

From the repository root:

```bash
python src/main.py
```

## Project Structure

- `src/`
  - `main.py`: example entrypoint
  - `engine/`: rule engine implementation
  - `model/`: transaction data model
- `tests/`: currently empty, intended for unit tests and integration tests
- `data/`: reserved for sample data or configuration files

## Suggested Improvements

The next set of enhancements can include:

- Add more rules:
  - country-based transaction restrictions
  - customer blacklist / whitelist checks
  - transaction velocity / frequency rules
  - merchant category or payment method rules
  - currency-based thresholds and conversion rules
- Improve rule architecture:
  - add a base `Rule` interface or abstract class
  - support rule metadata and severity levels
  - support rule configuration through JSON/YAML
- Add features:
  - CLI or API entrypoint
  - logging and audit trails
  - input data parsing from files or external sources
  - actionable output format (JSON, CSV)
  - unit tests for rules and engine behavior

## Future Work

- Implement a richer rule set and modular rule registration
- Add tests under `tests/`
- Support a configurable rule engine with external rule definitions
- Add better output formatting and error handling
