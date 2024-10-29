def get_department_name(department_code):
    """Return the department name based on the department code."""
    if department_code == 1:
        return "Marketing"
    elif department_code == 5:
        return "Human Resources"
    elif department_code == 10:
        return "Accounting"
    elif department_code == 12:
        return "Legal"
    elif department_code == 18:
        return "IT"
    elif department_code == 20:
        return "Customer Relations"
    else:
        return "Invalid department code"
def main():
    # List of test department codes
    test_codes = [1, 5, 10, 12, 18, 20, 99]  

    for code in test_codes:
        department_name = get_department_name(code)
        print(f"Department code {code}: {department_name}")