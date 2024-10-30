
def calculate_weekly_gross(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

def calculate_annual_gross(weekly_gross):
    return weekly_gross * 52

def determine_tax_rate(annual_income, filing_status):
    if filing_status.lower() == 'single':
        if annual_income < 12000:
            return 0.05
        elif annual_income < 25000:
            return 0.10
        elif annual_income < 75000:
            return 0.15
        else:
            return 0.20
    elif filing_status.lower() == 'joint':
        if annual_income < 12000:
            return 0.00
        elif annual_income < 25000:
            return 0.06
        elif annual_income < 75000:
            return 0.11
        else:
            return 0.20
    else:
        raise ValueError("Invalid filing status. Please use 'single' or 'joint'.")

def calculate_weekly_tax_withheld(weekly_gross, tax_rate):
    return weekly_gross * tax_rate

def main():
    try:
        hours_worked = float(input("Enter hours worked this period: "))
        hourly_rate = float(input("Enter your hourly rate: $"))
        filing_status = input("Enter your filing status ('single' or 'joint'): ").strip().lower()

        weekly_gross = calculate_weekly_gross(hours_worked, hourly_rate)
        annual_gross = calculate_annual_gross(weekly_gross)
        tax_rate = determine_tax_rate(annual_gross, filing_status)
        weekly_tax_withheld = calculate_weekly_tax_withheld(weekly_gross, tax_rate)
        net_pay = weekly_gross - weekly_tax_withheld

        print(f"\nYou worked {hours_worked} hours this period.")
        print(f"Because you earn ${hourly_rate} per hour, your gross weekly pay is ${weekly_gross:.2f}")
        print(f"Your filing status is '{filing_status}'.")
        print(f"Your tax withholding for the week is ${weekly_tax_withheld:.2f}")
        print(f"Your net pay is ${net_pay:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
