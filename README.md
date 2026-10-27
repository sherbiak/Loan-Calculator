# Loan Calculator

A command-line financial tool built in Python that calculates annuity and differentiated loan repayments, determines loan principals, computes repayment periods, and assesses total loan overpayment.

## Features

- **Differentiated Payments:** Calculates dynamic monthly payments where principal reduction is constant and interest decreases over time.
- **Annuity Payments:** Calculates fixed monthly payments, total loan principal, or loan duration (in years and months).
- **Overpayment Calculation:** Computes total interest paid over the lifespan of the loan.
- **Command-Line Interface:** Uses Python's built-in `argparse` module with input validation.

## Requirements

- Python 3.8 or higher
* **Operating System:** Configured specifically for **macOS**.

> **Note:** The included virtual environment (`.venv`) is configured for macOS. If running on another operating system, recreate the virtual environment before use.

## Usage

Run the script from your terminal using command-line arguments:

### 1. Activate the Virtual Environment

Before running the program, activate the project's virtual environment:

```bash
source .venv/bin/activate
```

### 2. Differentiated Payments
Calculate month-by-month payments and total overpayment:
```bash
python3 creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
```

### 3. Annuity Monthly Payment
Calculate the fixed monthly payment amount:
```bash
python3 creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
```

### 4. Repayment Duration (Periods)
Calculate the time required to repay the loan:
```bash
python3 creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8
```

### 5. Loan Principal
Calculate the maximum principal loan amount:
```bash
python3 creditcalc.py --type=annuity --payment=8722 --periods=120 --interest=5.6
```