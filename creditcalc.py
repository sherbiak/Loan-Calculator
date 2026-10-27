import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str)
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)

args = parser.parse_args()

args_list = [args.type, args.principal, args.periods, args.interest, args.payment]

if sum(arg is not None for arg in args_list) < 4:
    print("Incorrect parameters")
    sys.exit()

if args.type not in ("annuity", "diff"):
    print("Incorrect parameters")
    sys.exit()

if args.interest is None or args.interest < 0:
    print("Incorrect parameters")
    sys.exit()

for val in (args.principal, args.periods, args.payment):
    if val is not None and val < 0:
        print("Incorrect parameters")
        sys.exit()

if args.type == "diff":
    if args.payment is not None or args.principal is None or args.periods is None:
        print("Incorrect parameters")
        sys.exit()

if args.type == "annuity":
    annuity_params = [args.principal, args.periods, args.payment]
    if annuity_params.count(None) != 1:
        print("Incorrect parameters")
        sys.exit()

i = args.interest / (12 * 100)

if args.type == "diff":
    total_paid = 0
    p = args.principal
    n = args.periods

    for m in range(1, n + 1):
        d_m = math.ceil((p / n) + i * (p - (p * (m - 1)) / n))
        total_paid += d_m
        print(f"Month {m}: payment is {d_m}")

    overpayment = int(total_paid - p)
    print(f"\nOverpayment = {overpayment}")

elif args.type == "annuity":
    if args.payment is None:
        base = (1 + i) ** args.periods
        payment = math.ceil(args.principal * (i * base) / (base - 1))
        overpayment = int(payment * args.periods - args.principal)

        print(f"Your annuity payment = {payment}!")
        print(f"Overpayment = {overpayment}")

    elif args.principal is None:
        base = (1 + i) ** args.periods
        principal = round(args.payment / ((i * base) / (base - 1)))
        overpayment = int(args.payment * args.periods - principal)

        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {overpayment}")

    elif args.periods is None:
        if args.payment <= i * args.principal:
            print("Incorrect parameters")
            sys.exit()

        n = math.ceil(math.log(args.payment / (args.payment - i * args.principal), 1 + i))
        overpayment = int(args.payment * n - args.principal)

        years = n // 12
        months = n % 12

        year_str = f"{years} year" if years == 1 else f"{years} years"
        month_str = f"{months} month" if months == 1 else f"{months} months"

        if years > 0 and months > 0:
            time_str = f"{year_str} and {month_str}"
        elif years > 0:
            time_str = f"{year_str}"
        else:
            time_str = f"{month_str}"

        print(f"It will take {time_str} to repay this loan!")
        print(f"Overpayment = {overpayment}")